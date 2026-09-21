import re, sys, html as H
import xml.etree.ElementTree as ET

def parse_style(s):
    d={}
    for part in (s or '').split(';'):
        if not part: continue
        if '=' in part:
            k,v=part.split('=',1); d[k]=v
        else: d[part]=True
    return d

def num(d,k,default=None):
    try: return float(d[k])
    except Exception: return default

class Cell:
    pass

def load(path):
    root=ET.parse(path).getroot()
    pages=[]
    for dia in root.findall('diagram'):
        model=dia.find('mxGraphModel')
        cells={}
        order=[]
        for c in model.find('root').findall('mxCell'):
            o=Cell()
            o.id=c.get('id'); o.value=c.get('value') or ''
            o.style=parse_style(c.get('style'))
            o.edge=c.get('edge')=='1'; o.vertex=c.get('vertex')=='1'
            o.source=c.get('source'); o.target=c.get('target')
            g=c.find('mxGeometry')
            o.x=o.y=o.w=o.h=0; o.points=[]
            if g is not None:
                o.x=float(g.get('x') or 0); o.y=float(g.get('y') or 0)
                o.w=float(g.get('width') or 0); o.h=float(g.get('height') or 0)
                arr=g.find('Array')
                if arr is not None:
                    o.points=[(float(p.get('x')), float(p.get('y'))) for p in arr.findall('mxPoint')]
            cells[o.id]=o; order.append(o)
        pages.append((dia.get('name'), cells, order))
    return pages

def bbox(order):
    xs=[];ys=[]
    for o in order:
        if o.vertex:
            xs += [o.x, o.x+o.w]; ys += [o.y, o.y+o.h]
        for px,py in o.points:
            xs.append(px); ys.append(py)
    return min(xs), min(ys), max(xs), max(ys)

def anchor(o, style, kind):
    """connection point on box o, from exitX/exitY or entryX/entryY"""
    px=num(style, kind+'X'); py=num(style, kind+'Y')
    if px is None or py is None: return None
    return (o.x + px*o.w, o.y + py*o.h)

def side_point(o, toward):
    """point on o's perimeter on the side facing `toward`"""
    cx,cy=o.x+o.w/2, o.y+o.h/2
    dx,dy=toward[0]-cx, toward[1]-cy
    if o.w==0 or o.h==0: return (cx,cy)
    if abs(dx)/max(o.w,1) > abs(dy)/max(o.h,1):
        return (o.x + (o.w if dx>0 else 0), cy)
    return (cx, o.y + (o.h if dy>0 else 0))

def ortho(points, start_horiz):
    """expand a point list into an orthogonal polyline"""
    out=[points[0]]
    horiz=start_horiz
    for q in points[1:]:
        p=out[-1]
        if abs(q[0]-p[0])<0.5 or abs(q[1]-p[1])<0.5:
            out.append(q)
        else:
            if horiz: out.append((q[0], p[1]))
            else:     out.append((p[0], q[1]))
            out.append(q)
        if len(out)>=2:
            a,b=out[-2],out[-1]
            if abs(b[0]-a[0])>0.5: horiz=False
            elif abs(b[1]-a[1])>0.5: horiz=True
    # collapse duplicates
    ded=[out[0]]
    for p in out[1:]:
        if abs(p[0]-ded[-1][0])>0.5 or abs(p[1]-ded[-1][1])>0.5: ded.append(p)
    return ded

def render_page(name, cells, order, ox, oy):
    verts=[o for o in order if o.vertex]
    edges=[o for o in order if o.edge]
    svg=[]; divs=[]; labels=[]
    for e in edges:
        s=cells.get(e.source); t=cells.get(e.target)
        if not s or not t: continue
        st=anchor(s, e.style, 'exit'); en=anchor(t, e.style, 'entry')
        first_wp = e.points[0] if e.points else (t.x+t.w/2, t.y+t.h/2)
        last_wp  = e.points[-1] if e.points else (s.x+s.w/2, s.y+s.h/2)
        if st is None: st=side_point(s, first_wp)
        if en is None: en=side_point(t, last_wp)
        pts=[st]+e.points+[en]
        # start direction: horizontal if the exit sits on a vertical edge of the box
        start_horiz = abs(st[0]-s.x)<1 or abs(st[0]-(s.x+s.w))<1
        poly=ortho(pts, start_horiz)
        d='M '+' L '.join(f'{p[0]-ox:.1f} {p[1]-oy:.1f}' for p in poly)
        col=e.style.get('strokeColor','#333333')
        sw=e.style.get('strokeWidth','1.4')
        dash=' stroke-dasharray="6 4"' if e.style.get('dashed')=='1' else ''
        marker=' marker-end="url(#ah)"' if col=='#333333' else f' marker-end="url(#ah{abs(hash(col))%9999})"'
        svg.append(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="{sw}"{dash}{marker}/>')
        if e.style.get('startArrow'): 
            svg.append(f'<path d="M {poly[0][0]-ox:.1f} {poly[0][1]-oy:.1f} L {poly[1][0]-ox:.1f} {poly[1][1]-oy:.1f}" fill="none" stroke="{col}" stroke-width="{sw}" marker-start="url(#ahs)"/>')
        if e.value:
            # label at the middle of the polyline by arc length
            total=sum(((poly[i+1][0]-poly[i][0])**2+(poly[i+1][1]-poly[i][1])**2)**.5 for i in range(len(poly)-1))
            half=total/2; acc=0; lp=poly[0]
            for i in range(len(poly)-1):
                seg=((poly[i+1][0]-poly[i][0])**2+(poly[i+1][1]-poly[i][1])**2)**.5
                if acc+seg>=half:
                    r=(half-acc)/seg if seg else 0
                    lp=(poly[i][0]+(poly[i+1][0]-poly[i][0])*r, poly[i][1]+(poly[i+1][1]-poly[i][1])*r); break
                acc+=seg
            fc=e.style.get('fontColor','#222')
            labels.append(f'<div class="elabel" style="left:{lp[0]-ox:.1f}px;top:{lp[1]-oy:.1f}px;color:{fc}">{e.value}</div>')
    for o in verts:
        st=o.style
        is_text = 'text' in st and st.get('html')=='1' and 'rounded' not in st
        css=[f'left:{o.x-ox:.1f}px', f'top:{o.y-oy:.1f}px', f'width:{o.w:.1f}px', f'height:{o.h:.1f}px']
        css.append(f"font-size:{st.get('fontSize','13')}px")
        if 'fontColor' in st: css.append(f"color:{st['fontColor']}")
        if not is_text:
            css.append(f"background:{st.get('fillColor','#ffffff')}")
            border='dashed' if st.get('dashed')=='1' else 'solid'
            css.append(f"border:1.3px {border} {st.get('strokeColor','#666')}")
            arc=num(st,'arcSize',10) or 10
            if st.get('rounded')=='1': css.append(f"border-radius:{min(arc,12)}px")
            if st.get('shadow')=='1': css.append("box-shadow:2px 2px 3px rgba(0,0,0,.18)")
        css.append('justify-content:'+('flex-start' if st.get('verticalAlign')=='top' else 'center'))
        css.append('align-items:'+('flex-start' if st.get('align')=='left' else 'center'))
        css.append('text-align:'+('left' if st.get('align')=='left' else 'center'))
        pl=num(st,'spacingLeft',0) or 0; pt=num(st,'spacingTop',0) or 0
        css.append(f'padding:{pt+3:.0f}px 6px 3px {pl+6:.0f}px')
        divs.append(f'<div class="v" style="{";".join(css)}"><div class="lbl">{o.value}</div></div>')
    return svg, divs+labels

def main(src, out):
    pages=load(src)
    blocks=[]; maxw=0; totalh=0
    for name, cells, order in pages:
        x0,y0,x1,y1=bbox(order)
        pad=14
        w=x1-x0+pad*2; h=y1-y0+pad*2
        svg,divs=render_page(name, cells, order, x0-pad, y0-pad)
        maxw=max(maxw,w); totalh+=h+52
        blocks.append((name,w,h,svg,divs))
    parts=[]
    for name,w,h,svg,divs in blocks:
        parts.append(f'''<div class="page" style="width:{w:.0f}px">
  <div class="ptitle">{H.escape(name)}</div>
  <div class="canvas" style="width:{w:.0f}px;height:{h:.0f}px">
    <svg width="{w:.0f}" height="{h:.0f}">{''.join(svg)}</svg>
    {''.join(divs)}
  </div>
</div>''')
    doc=f'''<!doctype html><meta charset="utf-8">
<style>
@page {{ size: A3 portrait; margin: 7mm; }}
html,body {{ margin:0; padding:0; }}
body {{ font-family:-apple-system,"Helvetica Neue",Helvetica,Arial,sans-serif; color:#111;
        width:{maxw:.0f}px; }}
h1 {{ font-size:22px; margin:0 0 2px 0; }}
.sub {{ font-size:12.5px; color:#444; margin:0 0 14px 0; }}
.page {{ margin:0 0 26px 0; }}
.ptitle {{ font-size:14px; font-weight:700; letter-spacing:.06em; text-transform:uppercase;
           color:#555; border-bottom:1.5px solid #bbb; padding-bottom:3px; margin-bottom:9px; }}
.canvas {{ position:relative; }}
.canvas svg {{ position:absolute; left:0; top:0; }}
.v {{ position:absolute; box-sizing:border-box; display:flex; flex-direction:column;
      line-height:1.28; overflow:hidden; }}
.lbl {{ width:100%; }}
.elabel {{ position:absolute; transform:translate(-50%,-50%); background:#fff;
           font-size:10.5px; line-height:1.2; padding:1px 3px; text-align:center;
           white-space:nowrap; }}
</style>
<h1>Boombap Sampling Home Studio — signal chain</h1>
<p class="sub">Analog gear does the sound modeling, printed and unchangeable. The DAW does the mixing. Mastering is a third stage in its own session.</p>
{''.join(parts)}
<svg width="0" height="0"><defs>
<marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#333333"/></marker>
<marker id="ahs" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M 10 0 L 0 5 L 10 10 z" fill="#333333"/></marker>
</defs></svg>
'''
    # per-colour arrowheads
    cols=set(re.findall(r'marker-end="url\(#ah(\d+)\)"', doc))
    extra=''
    for name,w,h,svg,divs in blocks:
        for p in svg:
            m=re.search(r'stroke="(#[0-9a-fA-F]{6})".*?marker-end="url\(#ah(\d+)\)"', p)
            if m: extra+=f'<marker id="ah{m.group(2)}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="{m.group(1)}"/></marker>'
    doc=doc.replace('</defs>', extra+'</defs>')
    open(out,'w').write(doc)
    print(f'wrote {out}  ({maxw:.0f} x {totalh:.0f} px)')

main(sys.argv[1], sys.argv[2])
