# daw-less sample based workflow

i can't enjoy working with a DAW like ableton unless i really have to.
sound design, EQing, mixing, sequencing should all be done using hardware.

mastering is done in ableton using plugins.

## Decision

**Mixer + interface in one box: Tascam Model 2400.** It is the hub, does all the EQ and
summing, and its built-in USB multitrack interface **replaces the Scarlett** for the
mixdown. Character comes from my existing outboard, not the desk (see mixer decision below).

A standalone hardware recorder was rejected: it can only capture a stereo master, so it can
never re-capture the 8 multitrack channels, which is exactly the recall I care about (see
below). The Tascam captures the stereo mix *and* the per-channel stems over one USB cable.

## Core principle: the mixer is the hub AND the split point

Everything routes through the Tascam. The MPC's individual outs are wired into channels
1–8 **once** and never re-patched. The console then hands out two things at the same time,
and the split happens *inside the box* over USB — no external splitter, no second interface:

- the **analog stereo bus** = the finished, EQ'd, DAW-less mix
- the **per-channel USB multitrack** (channels 1–8) = dry stems

Both arrive in Ableton over the single USB cable. Switching between "record the mix" and
"record the stems" is just arming different tracks — no rewiring, ever. (This dissolves the
original problem of feeding both a mixer *and* a separate interface from the 8 MPC outs:
with the interface built into the console, there is only one destination.)

## Recall principle: the MPC project is the archive, not the mixer

The thing that lets me revisit a beat for a more professional production later is **not**
the mixer settings — it's the saved **MPC project** (sequence, samples, program,
individual-out routing). That is deterministic: reload it any time and the 8 outs produce
the exact same audio. So dry stems are always re-recordable on demand.

The one thing that is *not* recallable is the analog summing/EQ pass. That's acceptable,
because a pro mix engineer almost always wants **dry stems** and redoes the balance
anyway. My heavy sound design isn't on the summing mixer regardless — it's already baked
into the samples (Nuo2 EQ at sampling time, MPC filters, outboard band-split re-sampling).

Mitigations for the lost analog balance, if ever wanted:
- snap a **phone photo of the console** + one-line note, saved with the project
- set direct outs to **pre-EQ** so stems are dry and remix-ready

**Non-negotiable habit:** save every MPC project + its samples religiously. That is now
the master archive.

## Signal flow

```
SOURCES
  Technics MK7 ───────────────────────► Ecler Nuo2 (phono 2)
  TE KOII ────────────────────────────► Ecler Nuo2 (line 1)
  Ecler Nuo2 main out L/R ────────────► Tascam stereo channel (e.g. 21/22)
  MPC2500 individual outs 1-8 ────────► Tascam channels 1-8      (line in — NO DI box)
  outboard (SPL TD, DBX, Vermona, Lexicon, Alesis) ─► inserts + drum subgroup + aux (see below)

TASCAM MODEL 2400   (mixer + USB interface — replaces the Scarlett)
  analog stereo bus ──────────► USB ──► Ableton : Pass 1 = the mix
  per-channel multitrack 1-8 ─► USB ──► Ableton : Pass 2 = dry stems
  monitor out L/R ────────────────────► active monitors L/R
  aux / subgroup outs ────────────────► MPC record-ins (2500/2000/3000) for re-sampling

  USB ────────────────────────────────► Apple Studio M4  (Ableton = mastering only)
```

**No DI box:** the Palmer Pan existed to balance the MPC's unbalanced outs for the long run
to the Scarlett. The Tascam sits right next to the MPC and its channel line inputs take the
MPC outs directly over short cables — so the **Palmer Pan is redundant** and comes out of
the chain (free to reuse or retire).

When the MPC2000 is the beat machine instead, its individual outs take channels 1–8 (or
9–16), same routing.

## Two-pass capture

Nothing is rewired between passes — only the armed tracks in Ableton change, and both
passes come down the one USB cable. They can even run in a single take.

- **Pass 1 — the mix (every beat):** arm the Tascam **stereo master** in Ableton. MPC outs
  → Tascam → EQ / balance / (optional outboard on insert or aux) → stereo bus → record
  2-track → master in Ableton.
- **Pass 2 — dry stems (only when a beat gets picked up):** arm the **per-channel
  multitrack** (channels 1-8), record the 8 dry channels. Because the MPC project recalls
  the beat perfectly, this can be done any later date, not up front.

## The 8 individual outs are built in

With the Tascam the individual outs aren't a cabling problem — the console **streams every
channel over USB** as its own track. The stems come for free alongside the analog mix.

One thing to verify on the unit: the **per-channel USB tap point**. For truly dry,
remix-ready stems I want each channel recorded **pre-EQ / pre-fader**. If the Tascam's USB
send is post-EQ and I want dry, the **channel inserts (1–12)** give a pre-EQ analog tap via
a half-inserted TRS cable — but for most purposes the built-in USB multitrack is enough.

## Outboard routing (inserts vs aux)

Rule: in-line tone/dynamics go on **inserts** (100% of the signal passes through); ambience
goes on **AUX send/return** (blend a wet amount into the dry).

- **Inserts (series):** SPL Transient Designer (4 ch), DBX 266xl (2 ch), Vermona Lancet (1 ch)
- **AUX (parallel):** Lexicon MPX100 (stereo reverb), Alesis XT:C (reverb)

Gotcha: each channel has **one insert point**. To run two boxes on one channel, wire them
in series externally (box A out → box B in) and patch the whole chain into that single
insert.

My fixed pad layout: kick 1, snare 2, hats 3, bass 4, samples 5–8.

```
Ch1 Kick   ─ insert ─► SPL TD 1  ┐
Ch2 Snare  ─ insert ─► SPL TD 2  │  transient shaping per drum
Ch3 Hats   ─ insert ─► SPL TD 3  │
Ch4 Bass   ─ insert ─► SPL TD 4  ┘
Ch1-4 (+perc) ─► drum SUBGROUP (stereo) ─ insert ─► DBX 266xl L/R   ← kit glue (option B)
Ch5-8 samples ─ no fixed insert; fed by aux FX; Vermona on insert when filtering a layer

AUX 1 ─► Lexicon MPX100 (stereo) ─► return to a stereo channel (e.g. 21/22)
AUX 2 ─► Alesis XT:C ─────────────► return to a stereo channel
```

**Why the subgroup (option B, recommended):** transient-shape each drum individually with
the SPL TD, then bus-compress the *summed* kit with the DBX on a stereo subgroup — the
cohesive, pumping boombap drum glue. Stronger than compressing two drums in isolation, and
it keeps the DBX off the individual channels.

**DBX must run STEREO-LINKED (Stereo Couple ON):** the subgroup carries a stereo drum mix
(panned hats, wide samples). Two independent mono compressors would each duck their own
side on a one-sided transient, lurching the image toward the quieter side every hit. The
266xl's **Stereo Couple** button makes ch1 the master and ch2 follow it exactly, so both
sides duck by the same amount from a summed detector — image stays centered, width intact.
Patch: subgroup insert send **L → DBX in 1, R → DBX in 2**, returns back to the insert;
set threshold/ratio on **ch1 only** (ch2 knobs are ignored while coupled). Glue settings:
~2:1, OverEasy knee, 2–4 dB reduction on hits.
Verify on the 2400: a stereo subgroup insert needs **two insert points (L+R)**. If the
subgroup only exposes a mono insert, fall back to the kick/snare-insert variant below.
*Alternative in the back pocket:* DBX ch1/ch2 as inserts on kick/snare instead of on the
subgroup (kick insert chain becomes `TD1 → DBX1`, snare `TD2 → DBX2`).

**Stems land cleanly with this topology:** the per-channel USB stems tap channels 1–8
*before* the subgroup summing, so the **DBX glue does not print on the stems** — only on the
stereo mix (Pass 1). The **SPL TD is on the individual channels, so it does print** on the
stems. Either way it's fine: the MPC project recalls truly-dry outs any time, so committing
the per-channel transient shaping costs no recall.

## Mixer shortlist

Requirement for every candidate: ≥ 8 mono channels, each exposed **individually** (direct
outs or usable inserts), plus at least one aux send for the outboard chain. Verify
direct-out / insert pre-post behavior against the current manual before buying, and check
the used market first.

The per-piece < 1000 CHF studio rule is **deliberately relaxed for this one box** — the
mixer touches every sound and does all the EQ, so it's the place where spending more
actually changes the record. What the extra money buys, in order of impact: **EQ
character** (British / Trident / Midas curves flatter dusty samples and drums; transparent
A&H / Mackie EQ does not), then **preamp / summing coloration**, then build and channels.

### Budget tier (< 1000 CHF)

- **Allen & Heath ZED-24** — *solid default.* 16 mono channels, balanced **direct out on
  every channel**, 4 aux sends, good preamps. Pre/post-EQ on the direct outs is internally
  selectable — set once to pre. Spare channels for the MPC2000 or a Nuo2 sub-mix.
  ~750–850 CHF new.
- **Mackie 1604-VLZ4** — 16 mono channels, direct out per channel, Onyx preamps. Direct
  outs are post-EQ, so use the **insert half-plug trick** for dry pre-EQ stems.
  ~800–900 CHF.
- **Mackie 1642-VLZ4** — cheapest. Direct outs on channels 1–8 exactly cover the 8 MPC
  outs. Fewer aux sends. ~550–650 CHF.

### Step-up tier (~1,200–1,800 CHF)

- **Allen & Heath GL2400-16** — the ZED-24's bigger sibling. 16 mono, **direct out per
  channel**, 4-band EQ with **two sweepable mids** (ZED sweeps only one), 6 aux, road-grade
  build. Best value increment — same clean A&H voice, much more EQ control.

### Mixer decision — reconciled with 2026 reality (cap < 5k CHF, must be buyable)

Verdict (checked July 2026): **under 5k, buyable new, a *colored* console with per-channel
EQ + individual outs + 8 channels does not exist.** The market is split cheap-and-clean vs
expensive-and-colored — the colored current desks (Audient ASP4816 ~6–10k, Trident 68
~13–14k, SSL Origin / Neve 8424 ~20k+) all blow the budget, and the SSL BiG SiX has only 4
mono channels (too few for the 8 MPC outs). Chasing a new colored desk under 5k is a dead
end.

**Resolution: buy a clean, current, buyable hub and let my existing outboard be the colour.**
My sonic signature doesn't need to live in the desk — I already own the Vermona Lancet, SPL
Transient Designer, DBX 266xl and Lexicon MPX100. On inserts / an aux, *those* are my sound,
and more distinctive than any stock console EQ.

**The hub — Tascam Model 2400** *(recommended, ~1,700–2,000 CHF, in production):*

- 22 input channels, 3-band EQ on all (plenty for the 8 MPC outs + turntable/KOII)
- inserts on channels 1–12 → half-plug dry-stem trick works on 12 channels
- **built-in 24×22 USB interface** — every channel streams individually to the DAW: the
  "individual outs" are built in, and it **can replace the Scarlett** for the mixdown
- one-knob comps on 12 channels + master bus EQ/comp
- fits the two-pass flow in a single take: analog stereo bus = Pass 1 mix; per-channel USB
  multitrack = Pass 2 dry stems (verify the USB tap is pre-EQ for truly dry stems)
- honest catch: the Tascam's own colour is *mild* — the character comes from my outboard

Architecture note: **decided — the Tascam is both mixer and interface and replaces the
Scarlett** for the mixdown. The Scarlett comes out of the mixdown chain (keep it only as a
spare converter). Consequences: the Palmer Pan DI is also redundant, and the wider-studio
jobs the Scarlett used to do — monitoring, the Nuo2 input, and the MPC record-in feeds —
move onto the Tascam's monitor out, a stereo channel, and its aux / subgroup outs.

**Fallback if I ever want a genuinely colored desk (used, patience required):**

- **Toft ATB-16** — the sound I reacted to; Trident-lineage EQ, direct outs. Hard to find.
  ~2,500–4,000 CHF used.
- **Midas Venice / Venice F16** — Midas pres + swept-mid EQ, direct outs; more findable than
  the Toft. Ignore any FireWire, use the direct outs. ~1,500–3,000 CHF used.
- **Allen & Heath GL2400** — cheapest colored-ish route, two swept mids. ~1,000–2,000 CHF.
- Any used console: budget ~200–500 CHF for a tech check / recap.

### Trap to skip

Pure **summing mixers** (Neve 5060, SSL SiX, Heritage) get hyped but have **no per-channel
EQ and no direct outs** — they sum a mix built elsewhere, the opposite of doing EQ and
balance on the desk. The SiX is also only 2 mono channels, too few for the 8 MPC outs.
Wrong tool for this workflow.

## Open items

- decide: keep stems **dry (pre-EQ)** — recommended — or **post-EQ** (carrying my mix moves);
  verify the Tascam's per-channel USB tap point accordingly
- decide whether the outboard chain (Vermona → SPL → DBX → Lexicon) sits on **channel
  inserts / an aux send-return** during the mixdown, or stays purely a sampling-stage tool
- confirm the **Tascam channel map** (MPC 1-8 → ch 1-8; Nuo2 → a stereo channel; spare
  channels for MPC2000 / monitoring)
- work out how the **MPC record-in feeds** for re-sampling come off the Tascam (which aux /
  subgroup outs) now that the Scarlett is gone
- update **CLAUDE.md** signal chain: remove the Scarlett + Palmer Pan from the studio, move
  monitoring + Nuo2 input + MPC record-in feeds onto the Tascam
