# Manual mastering chain — boom bap, hybrid hardware capture

Pro Tools **Studio** is the DAW — the only DAW. Stock plugins used below: Pro Multiband
Dynamics, Pro Compressor, Pro Limiter, Reel Tape Saturation. Third-party: **FabFilter Pro-Q 4**
and the **Waves SSL E-Channel** strip. See [CLAUDE.md](CLAUDE.md) for the live routing and
[dbx266xl-reference.md](dbx266xl-reference.md) for the compressor itself.

**Chain at a glance:** Pro-Q 4 → Pro Multiband Dynamics → SSL E-Channel → Reel Tape Saturation
→ Pro Compressor → Pro Limiter. That is the full version; see "the short chain" at the end for
the three-plugin version that is usually enough.

## The brief (my own words)

I record through the Tascam Model 2400's analog EQ — **post-FX, so the EQ prints** — with the
Alesis XT:C reverb on the snare returning on its own EQ'd stereo channel, and kick/snare/hi-hat
feeding a subgroup that goes through the hardware DBX and comes back as a **parallel** return
to fatten them. That leaves a lot of channels: 10 from the MPC alone (8 individual outs + the
stereo pair), plus the reverb return, plus the glue return.

---

## First: what actually needs mastering here

The premise in the original draft is right, and the post-FX capture makes it more so — by the
time audio reaches the computer, the analog EQ, the SPL transient shaping, the parallel DBX
weight and the XT:C tails are all printed. The master's job is only: kill sub-sonic junk,
control the kick/bass collision, add tape-style glue, and get it loud without flattening the
drums. Everything else is already done upstairs on the desk.

One thing to hold onto before the settings: **this is a mastering chain, not a licence to
re-mix.** Capturing 20+ channels into Pro Tools is useful as an archive and a safety, but the
mix stays on the Tascam — that is the whole daw-less point. If the DAW multitrack starts
getting faders ridden, the desk has quietly become a very expensive preamp.

### Capture map (current routing)

The original draft's "channels 1–16 MPC, 17/18 Alesis, 19/20 dbx" was guesswork; it happens to
have landed on 19/20 for the DBX, which is now right for a different reason. Actual:

| Tascam ch | Source |
|---|---|
| 1 / 2 / 3 | Kick / snare / hi-hat — **SPL Transient Designer printed**, also feeding subgroup 1/2 |
| 4–8 | Perc, bass, instrumental samples (MPC individual outs via Palmer Pan 16) |
| 9 | free |
| 10 | Akai S950 — Vermona in-line, SPL 4 on the insert. Re-sampling source, not usually in the mix |
| 11 / 12 | MPC2000 stereo out |
| 13 / 14 | MPC2500 stereo out |
| 15 / 16 | Ecler Nuo2 (turntable + KOII) |
| 17 / 18 | **Alesis XT:C return — the snare reverb, EQ'd and printed** |
| 19 / 20 | **DBX 266XL parallel drum-glue return** |
| 21 / 22 | Mac / Pro Tools returns — mute during capture |

Everything is captured **post-FX**, so the multitrack is not a set of dry stems: ch 1–3 carry
the SPL and the EQ, ch 17/18 carry the EQ'd reverb. That is deliberate and committal.

The one thing that stays adjustable after the fact is the **parallel drum blend**. Because the
DBX returns on its own pair instead of being inserted on the subgroup, the dry drums (ch 1–3)
and the crushed copy (ch 19/20) land in Pro Tools as separate tracks — so the dry/crushed ratio
can still be moved later even though the EQ cannot. Worth capturing both every time for that
reason alone.

**Watch the double-dip.** The drums now arrive already parallel-compressed, and band 1 of the
multiband below compresses the low end again. If the kick starts sounding soft rather than
tight, the fix is usually pulling the ch 19/20 blend down at mixdown, not adding more master
compression.

### Gain staging into the box

Track the stereo master so peaks land around **−10 to −6 dBFS**. Boom bap kicks are short and
peaky; a mix that already reads −3 dBFS leaves the limiter nothing to work with and forces it
into the transients on the very first dB.

---

## Slot 1 — FabFilter Pro-Q 4 (corrective + mid/side)

Pro-Q 4 replaces EQ3 here outright: steeper filters, per-band mid/side, dynamic bands and a
usable analyzer. Surgical only — the Tascam already did the musical EQ.

**Processing mode: Natural Phase.** Not Linear Phase. Linear-phase EQ pre-rings, and pre-ringing
smears exactly the thing this record is built on — the kick and snare transients. Linear phase
is for repairing broken masters, not for boom bap.

| Band | Setting | Why |
|---|---|---|
| 1 | **High-pass 30 Hz, 24 dB/oct**, stereo | Sub-sonic rumble from the samplers and the turntable path. 24 dB/oct is the sweet spot — Pro-Q will go to 96, but steeper slopes ring in the low end |
| 2 | **Bell 250 Hz, −1.0 dB, Q 0.7**, stereo | The mud where the XT:C tail and the parallel drum glue pile up. Move to 300–350 Hz if the boxiness sits higher |
| 3 | **Bell 55 Hz, Q 1.2, Dynamic, range −2.5 dB** | Ducks the kick's fundamental only when it hits, leaving the bass alone in between. More surgical than a full multiband band |
| 4 | **Side channel: high-pass 120 Hz, 12 dB/oct** | Keeps the low end mono and centered. The MPC outs are already mono, so this mostly catches low content in the XT:C reverb tail |
| 5 | *Optional* — **Side channel: high shelf 8 kHz, +1.0 dB** | Widens the reverb air without touching the mono drums. The only genuine width move available on a mono-source record |
| 6 | *Optional* — **Bell 3 kHz, Q 2.0, Dynamic, range −1.5 dB** | Catches the snare crack only when it spikes harsh. Leave it off unless the snare is actually stabbing |

If a sub-heavy kick is part of the sound, move band 1 to **28 Hz** so the deliberate sub-60 Hz
layer from the MPC survives intact. Sweep it while soloing the kick.

**Why the multiband still exists after this.** Pro-Q's dynamic bands are program-dependent —
you set threshold and range, but attack and release are automatic and not exposed. Pro
Multiband Dynamics gives you the actual attack and release numbers, which is what the
tempo-locked sub band in slot 2 depends on. Use Pro-Q for anything surgical or mid/side, and
the multiband for anything that needs timing you can set by hand.

---

## Slot 2 — Pro Multiband Dynamics (the exact values)

Four bands. The principle behind every attack number below: **an attack faster than one cycle
of the band's lowest frequency distorts rather than compresses.** One cycle at 30 Hz is 33 ms,
at 90 Hz it is 11 ms, at 350 Hz 2.9 ms. That is why the sub band gets a *slow* attack — the
original draft's "fast attack" on 20–90 Hz would turn the kick's fundamental into a buzz.

Release is tied to the tempo so the band recovers before the next hit:

| BPM | 1 beat | 8th | 16th |
|---|---|---|---|
| 82 | 732 ms | 366 ms | 183 ms |
| 86 | 698 ms | 349 ms | 174 ms |
| 90 | 667 ms | 333 ms | 167 ms |
| 93 | 645 ms | 323 ms | 161 ms |

Rule: **band release ≈ 8th-note value × 0.6.** At 90 BPM that is 200 ms. Recompute per beat.

**Crossovers: 90 Hz / 350 Hz / 6 kHz.**

### Band 1 — Sub & kick body (20–90 Hz)

| Param | Value | Why |
|---|---|---|
| Ratio | **2.5:1** | Control, not limiting |
| Knee | **6 dB** | Slightly soft, keeps the onset natural |
| Attack | **25 ms** | ≥ one cycle at 40 Hz; anything faster distorts the fundamental |
| Release | **200 ms** @ 90 BPM (use the formula) | Recovered before the next 8th |
| Threshold | Set for **1.5–2.5 dB GR on the loudest kicks only** — typically −18 to −14 dBFS | The meter should rest at 0 between hits |
| Band gain | 0, then +0.5 dB if the low end thinned out | |

### Band 2 — Warmth / low-mids (90–350 Hz)

This is where the samples' body and the DBX grit live. Barely touch it.

| Param | Value |
|---|---|
| Ratio | **2:1** |
| Knee | **10 dB** (soft) |
| Attack | **30 ms** |
| Release | **250 ms** |
| Threshold | for **0.5–1.5 dB GR**, moving only on the densest bars |
| Band gain | **−0.3 to −0.5 dB** if the mix is congested; otherwise 0 |

If in doubt, bypass the compressor here and use band gain alone. A static −0.5 dB beats a
compressor chewing on the warmest part of the record.

### Band 3 — Mids, snare crack, reverb bloom (350 Hz – 6 kHz)

The snare transient is roughly 5–15 ms. A 45 ms attack lets the whole crack through and only
catches what follows — including the XT:C tail, which is exactly what should *not* get pumped.

| Param | Value |
|---|---|
| Ratio | **1.5:1** |
| Knee | **12 dB** (softest musical setting) |
| Attack | **45 ms** |
| Release | **300 ms** |
| Threshold | for **≤ 1 dB GR** |
| Band gain | 0 |

### Band 4 — Top (6 kHz and up)

Fast and short here: this band tames 12-bit aliasing hash, hat spit and the bright edge of the
XT:C tail. It is effectively a gentle de-esser for a record with no voices yet.

| Param | Value |
|---|---|
| Ratio | **3:1** |
| Knee | **6 dB** |
| Attack | **3 ms** (one cycle at 6 kHz = 0.17 ms, so this is still slow by comparison) |
| Release | **80 ms** |
| Threshold | for **1–2 dB GR on hat/cymbal peaks**, nothing between them |
| Band gain | 0, or +0.5 dB after gain reduction to keep the sparkle |

### Optional — the expander section on band 4

Old samplers hiss and the XT:C has a noise floor. A gentle downward expansion on the top band
pushes it under between hits:

- Expander threshold **−55 dBFS**, ratio **1.5:1**, attack **5 ms**, release **250 ms**

Watch reverb tails — if the XT:C decay starts chattering or ducking, raise the release to
400 ms or switch it off. Noise is more forgivable than a breathing tail.

### Reading the whole plugin

Total gain reduction across all four bands should sit around **2–3 dB on the loudest bars and
near zero in the gaps.** If every band is moving all the time, the mix needs fixing on the
Tascam, not here.

---

## Slot 3 — Waves SSL E-Channel (console colour)

The Tascam is a clean desk by design — the studio's colour was always meant to come from
outboard. The E-Channel is where the 4000-series console character that the Tascam
deliberately does not supply gets added back, in the box, at the last stage where it is still
safe to add it.

**Use the EQ. Leave the DYN section out** (`DYN IN` off) — Pro Compressor in slot 5 is doing
the glue, and two bus compressors stacked is how a master turns into cardboard. If you prefer
the SSL comp, use it *instead of* slot 5; settings below.

**EQ type — start on BROWN.** The Waves plugin toggles between the two E-series revisions:
brown knob (02) is the smoother, broader curve, black knob (242) the more aggressive one. For
master-bus moves of a dB or less, brown is the better fit; switch to black when a band needs
to bite. A/B them — it is a taste call, not a rule.

Either way the mid bands are **proportional-Q**: bandwidth narrows automatically as you boost
harder. Small moves come out wide and flattering, big moves come out surgical and aggressive.
That is exactly why this EQ works on a master at ≤1 dB and turns ugly fast past 3 dB.

| Control | Setting | Why |
|---|---|---|
| HF | **Shelf, 10 kHz, +0.5 to +1.0 dB** | Air. Skip if Pro-Q band 5 already added it on the sides |
| HMF | **2.8 kHz, Q 1.0, +0.5 dB** | Snare presence — the crack, not the sizzle |
| LMF | **350 Hz, Q 0.7, −0.5 dB** | Only if still boxy after Pro-Q. Usually skip — one plugin should own the mud |
| LF | **Shelf, 70 Hz, +0.5 to +1.0 dB** | Weight under the kick |
| HPF / LPF | **Out** | Pro-Q already high-passed. Two high-passes stack into a steeper slope than either one displays |
| SPLIT | **Off** | Only relevant when the filters feed the dynamics sidechain, and the dynamics are off |
| ANALOG | **Off** | A1/A2 add hum and harmonic content; the 12-bit sources supply plenty of their own |
| Input trim / Output | Level-matched to bypass | |

**Nothing above 1 dB.** If a band wants +3 dB, the fix belongs on the Tascam at mixdown, not
here.

**If using the SSL compressor instead of slot 5:** Ratio **2:1**, Threshold for **1 dB gain
reduction**, Release **0.3 s**, **F.ATT out**. Fast attack on the E-Channel is roughly 1 ms and
will flatten every MPC transient; the normal (slow) setting is the one that lets drums through.
Leave the Gate/Expander threshold fully down — there is nothing on a finished master worth
gating. Then bypass slot 5 entirely.

---

## Slot 4 — Reel Tape Saturation

The glue for 20+ channels of separately-captured hardware.

| Param | Value |
|---|---|
| Tape speed | **15 IPS** — the low-end head bump and the gentle high roll-off are the point; 30 IPS is flatter and more "modern" |
| Tape type | **Opus / 250** for a fuller low end; the darker formulation if the record wants to be dusty |
| Calibration / Input | Push until the meter ticks **1–2 dB into the red on the loudest hits only** |
| Noise | **Off** — the sources supply plenty already |
| Output | Trim back so bypass A/B is level-matched |

Level-matched A/B is not optional. Saturation always sounds "better" when it is louder; if it
still sounds better at matched level, keep it.

---

## Slot 5 — Pro Compressor (bus glue)

Skip this entirely if you used the SSL E-Channel's compressor in slot 3. One glue compressor,
not two.

| Param | Value | Why |
|---|---|---|
| Ratio | **1.5:1** (2:1 max) | Glue, not control |
| Knee | **12 dB** soft | |
| Attack | **30 ms** | Kick and snare transients pass untouched |
| Release | **Auto**, or **300 ms** manual | Auto tracks the tempo well on drum-led material |
| Threshold | for **1 to 1.5 dB GR maximum** | More than that and the drums start breathing |
| **Sidechain HPF** | **100 Hz** | The single most important setting here — stops the kick from ducking the entire record. Pro Compressor's sidechain EQ does this natively |
| Makeup | Level-matched to bypass | |

---

## Slot 6 — Pro Limiter

| Param | Value |
|---|---|
| Ceiling | **−1.0 dBTP** (true-peak on). Lossy codecs overshoot; this is the safe margin |
| Knee / character | Soft, the more forgiving "character" setting — hard-knee limiting hollows out MPC kicks |
| Release | **Auto**, or **200 ms** if the sustain pumps |
| Threshold | Lower gradually into the loudest bar |
| Dither | **POW-r 2** *only* when rendering to 16-bit. Bouncing 24-bit → no dither |

### Loudness targets

| Deliverable | Integrated LUFS | Notes |
|---|---|---|
| **Release master** | **−11 LUFS**, −1.0 dBTP | Spotify/Apple normalize to ≈ −14 anyway, so pushing past this only buys distortion that gets turned down |
| **Rapper reference bounce** | **−9 LUFS** | Only if someone insists on loud. Same chain, limiter threshold ~2 dB lower |

Keep an eye on **PLR (peak-to-loudness): 8–10 dB.** Under 7 and the boom bap punch is gone,
whatever the LUFS number says. Pro Tools' master-fader meter has loudness modes built in.

---

## Two decisions that change the settings

The original draft ended by asking these. Both answers are already covered above — here are
the deltas rather than the question:

**Clean and punchy (90s East Coast):** tape drive to a bare flicker, multiband band 4 gain
+0.5 dB, SSL HF shelf +1.0 dB, Pro-Q side-channel air band (5) in, limiter to −11 LUFS. Let
the transients live.

**Dusty, dark, saturated (underground / lo-fi):** tape drive 3–4 dB into the red, add a Pro-Q
low-pass around 15–16 kHz, skip the SSL HF shelf and the Pro-Q air band, multiband band 2 gain
at 0 (keep the mud), push to −9 LUFS. The S950's 12-bit grit is already doing half of this —
check how far it has gone before adding more.

---

## The short chain

Six plugins on a master is a lot, and most beats do not need them. The version that is usually
enough:

**Pro-Q 4 → SSL E-Channel → Pro Limiter**

High-pass and the mid/side low-cut, a dB of console colour, then loudness. Add Reel Tape when
the mix feels like separate boxes rather than one record. Add the multiband only when the
kick and bass are actually fighting. Add Pro Compressor only when the whole thing needs
knitting and the SSL's own comp is not doing it.

Reach for the full six-stage chain when a beat is going out as a finished master. For a
reference bounce to send a rapper, the short chain is the whole job.

---

## The one legitimate mixing move in the DAW

Everything else is mixed on the Tascam, but the **parallel drum blend is re-adjustable by
design** (ch 1–3 dry, ch 19/20 crushed, captured separately). If that blend needs work after
the fact, the Waves SSL E-Channel on the ch 19/20 return is the right tool — carving the
parallel copy rather than re-mixing the drums. Black knob here, not brown; this is a channel,
and it is meant to bite:

| Move | Setting | Why |
|---|---|---|
| Filters | **HPF 100 Hz** | Stops the crushed copy from doubling the kick's low end into mush. The dry kick keeps the weight |
| HF | **Shelf, 8 kHz, +2 dB** | Brings up room and snare tail — the part worth blending in |
| LMF | **400 Hz, Q 1.0, −2 dB** | The parallel copy is where boxiness accumulates first |
| Dynamics | **Off** | The DBX already compressed this. Twice is mud |

Bigger moves are fine here than on the master — this is a parallel channel, and it is meant to
be carved, not flattered.

---

## Bounce checklist

1. Level-matched bypass A/B of the whole chain — is it actually better, or just louder?
2. Check mono. The MPC individual outs are mono into the desk, so the low end is already
   mono-compatible; the risk is the XT:C and Lexicon returns thinning on the fold-down.
3. Listen to the last bar's reverb tail — that is where over-compression shows first.
4. Render 24-bit WAV as the archive master; 16-bit + POW-r 2 only if something demands it.
5. Save the MPC project and its samples. The mix is unrecallable, the beat is not — that rule
   does not change just because there is a DAW in the room.
