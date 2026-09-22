# Manual mastering chain — boom bap, hybrid hardware capture

Pro Tools **Studio** is the only DAW. Stock plugins: Pro Multiband Dynamics, Pro Compressor,
Pro Limiter, Reel Tape Saturation. Third-party: **FabFilter Pro-Q 4** and the **Waves SSL
E-Channel**. Routing in [CLAUDE.md](CLAUDE.md), the compressor in
[dbx266xl-reference.md](dbx266xl-reference.md), session layout in
[protools_mastering_session.md](protools_mastering_session.md).

**Chain:** Pro-Q 4 → Pro Multiband Dynamics → SSL E-Channel → Reel Tape Saturation →
Pro Compressor → Pro Limiter. That is the full version; "the short chain" at the end is the
three-plugin one that is usually enough.

**Where it runs:** its own mastering session, on an aux, fed by the imported pass-1 stereo
capture — never on the master fader of the MPC-recording template.

---

## What actually needs mastering here

By the time audio reaches the computer the analog EQ, the SPL transient shaping, the parallel
DBX weight and the XT:C tails are all printed. The master's job is only: kill sub-sonic junk,
control the kick/bass collision, add tape-style glue, and get it loud without flattening the
drums. Everything else was already done on the desk.

**This is a mastering chain, not a mixing one.** Mixing has its own stage and its own session —
[manual_mixing_tascam_protools.md](manual_mixing_tascam_protools.md) — where the balance, the
per-channel surgical work and the delay bus live. By the time a stereo file reaches this chain,
both the tone (printed on the desk) and the balance (rebuilt in the multitrack session) are
settled. Anything fixed here that should have been fixed there gets applied to the whole record
at once, which is why it rarely works.

Same reason the chain lives in its own session: a master chain running while a mix is being
built means every balance decision gets made through a limiter.

### Capture map

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

### What the multitrack holds — post-FX, pre-fader

The per-channel USB sends are **post-EQ, post-insert, pre-fader** (confirmed by riding a fader
against both Pro Tools meters). That splits the capture cleanly in two:

- **Printed on the multitrack:** the Tascam channel EQ, the SPL transient shaping on ch 1–3 and
  10, the XT:C return EQ on 17/18. Committal — there is no undo on a printed EQ curve.
- **Not on the multitrack:** the balance. Fader positions, and anything ridden during the take.

So every channel is tracked at a uniform **≈ −10 dBFS** and the multitrack is a
*level-normalised archive, not a mix*. The leveling is recreated at the mixing step. The only
file that holds the balance you actually heard is the **pass-1 stereo master**.

Three consequences worth remembering at the desk:

1. **A fader cannot fix a hot multitrack channel.** Pulling it down changes the stereo mix and
   does nothing to the recorded track — the trim is the only control that moves the multitrack
   level, and it moves the mix along with it. Set trim for the converter, balance with the fader.
2. **Channels mixed out still land on the multitrack at full level.** A fader at −∞ because that
   layer was not wanted still records. Good as archive, confusing later.
3. **The parallel drum blend is re-creatable, not recallable.** Ch 1–3 dry and ch 19/20 crushed
   arrive as separate files, so a blend can be built later — but not *the* blend, because the
   ratio lived in the faders. The stereo master and a photo of the desk are the only record of it.

**Watch the double-dip.** The drums arrive already parallel-compressed, and band 1 of the
multiband compresses the low end again. If the kick sounds soft rather than tight, pull the
ch 19/20 blend down at mixdown rather than adding master compression.

### Gain staging

| Capture | Target | Why |
|---|---|---|
| Multitrack, per channel | **≈ −10 dBFS**, uniform | Pre-fader, so this is a converter level, not a balance. Uniform keeps the rebuild honest |
| Stereo master (pass 1) | peaks **−10 to −6 dBFS** | Boom bap kicks are short and peaky; a mix already reading −3 dBFS forces the limiter into the transients on the first dB |

---

## Slot 1 — FabFilter Pro-Q 4 (corrective + mid/side)

Surgical only — the Tascam already did the musical EQ.

**Processing mode: Natural Phase.** Linear-phase EQ pre-rings, and pre-ringing smears exactly
what this record is built on — the kick and snare transients. Linear phase is for repairing
broken masters.

| Band | Setting | Why |
|---|---|---|
| 1 | **High-pass 30 Hz, 24 dB/oct**, stereo | Sub-sonic rumble from the samplers and the turntable path. 24 dB/oct is the sweet spot — steeper slopes ring in the low end |
| 2 | **Bell 250 Hz, −1.0 dB, Q 0.7**, stereo | The mud where the XT:C tail and the parallel drum glue pile up. Move to 300–350 Hz if the boxiness sits higher |
| 3 | **Bell 55 Hz, Q 1.2, Dynamic, range −2.5 dB** | Ducks the kick's fundamental only when it hits, leaving the bass alone in between |
| 4 | **Side channel: high-pass 120 Hz, 12 dB/oct** | Keeps the low end mono. The MPC outs are already mono, so this mostly catches low content in the XT:C tail |
| 5 | *Optional* — **Side channel: high shelf 8 kHz, +1.0 dB** | Widens the reverb air without touching the mono drums. The only genuine width move on a mono-source record |
| 6 | *Optional* — **Bell 3 kHz, Q 2.0, Dynamic, range −1.5 dB** | Catches the snare crack only when it spikes harsh. Off unless the snare is actually stabbing |

If a sub-heavy kick is part of the sound, move band 1 to **28 Hz** so the deliberate sub-60 Hz
layer from the MPC survives. Sweep it while soloing the kick.

### Masking vs cancellation — band 3 only fixes one of them

Both sound like a weak low end. They need opposite responses.

**Masking** is two sounds sharing a band at the same moment. The louder one hides the quieter
one. Both are still there. Duck one and the other comes through. That is band 3's whole job.

**Cancellation** is two sounds at the same frequency arriving out of phase. They subtract. The
energy is gone, not hidden. Duck one and even less is left.

**Telling them apart here is hard, and that is the point.** The master is one summed stereo
file — the kick and the bass cannot be separated any more. Two signs point to cancellation: the
low end reads loud on the meter but thin on the speakers, and it gets *weaker* at the moments
the bass and the kick land together. Masking sounds the opposite — plenty of energy, the kick
just buried in it.

**Cancellation is not a mastering problem.** Do not reach for band 3. Go back to the multitrack
session, where the kick and the bass are still separate files, and run the polarity test in
[manual_mixing_tascam_protools.md](manual_mixing_tascam_protools.md). The real fixes live
upstream: polarity, timing, or tuning the sub-60 Hz layer to the key of the track. A re-track is
cheap and honest; a dynamic band on a cancelling low end is neither.

This is a live risk on this record specifically. Every MPC out is mono and lands dead centre,
so the kick and the bass are two near-sine sources in the same place, with nothing but their
phase relationship keeping them apart.

**Why the multiband still exists after this.** Pro-Q's dynamic bands are program-dependent —
threshold and range are yours, attack and release are automatic and not exposed. Pro Multiband
Dynamics gives actual attack and release numbers, which is what the tempo-locked sub band
depends on. Pro-Q for anything surgical or mid/side; the multiband for anything needing timing
set by hand.

---

## Slot 2 — Pro Multiband Dynamics (the exact values)

Four bands. The principle behind every attack number: **an attack faster than one cycle of the
band's lowest frequency distorts rather than compresses.** One cycle at 30 Hz is 33 ms, at
90 Hz 11 ms, at 350 Hz 2.9 ms — which is why the sub band gets a *slow* attack.

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
| Threshold | for **1.5–2.5 dB GR on the loudest kicks only** — typically −18 to −14 dBFS | Meter rests at 0 between hits |
| Band gain | 0, then +0.5 dB if the low end thinned out | |

### Band 2 — Warmth / low-mids (90–350 Hz)

Where the samples' body and the DBX grit live. Barely touch it.

| Param | Value |
|---|---|
| Ratio | **2:1** |
| Knee | **10 dB** (soft) |
| Attack | **30 ms** |
| Release | **250 ms** |
| Threshold | for **0.5–1.5 dB GR**, moving only on the densest bars |
| Band gain | **−0.3 to −0.5 dB** if congested; otherwise 0 |

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

Tames 12-bit aliasing hash, hat spit and the bright edge of the XT:C tail — effectively a
gentle de-esser for a record with no voices yet.

| Param | Value |
|---|---|
| Ratio | **3:1** |
| Knee | **6 dB** |
| Attack | **3 ms** (one cycle at 6 kHz = 0.17 ms, so still slow by comparison) |
| Release | **80 ms** |
| Threshold | for **1–2 dB GR on hat/cymbal peaks**, nothing between them |
| Band gain | 0, or +0.5 dB after gain reduction to keep the sparkle |

**Optional expander on band 4.** Old samplers hiss and the XT:C has a noise floor. Threshold
**−55 dBFS**, ratio **1.5:1**, attack **5 ms**, release **250 ms**. If the XT:C decay starts
chattering, raise the release to 400 ms or switch it off — noise is more forgivable than a
breathing tail.

**Reading the whole plugin:** total GR across all four bands around **2–3 dB on the loudest
bars, near zero in the gaps.** If every band moves all the time, the mix needs fixing on the
Tascam.

---

## Slot 3 — Waves SSL E-Channel (console colour)

The Tascam is a clean desk by design; the colour was always meant to come from outboard. The
E-Channel adds back the 4000-series character in the box, at the last stage where it is still
safe to add it.

**Use the EQ. Leave the DYN section out** (`DYN IN` off) — Pro Compressor in slot 5 does the
glue, and two bus compressors stacked is how a master turns into cardboard. If you prefer the
SSL comp, use it *instead of* slot 5.

**EQ type — start on BROWN.** Brown knob (02) is the smoother, broader curve; black (242) the
more aggressive one. For moves of a dB or less brown fits better; switch to black when a band
needs to bite. Either way the mid bands are **proportional-Q** — bandwidth narrows as you boost
harder, so small moves come out wide and flattering, big moves surgical and aggressive. That is
why this EQ works at ≤1 dB and turns ugly fast past 3 dB.

| Control | Setting | Why |
|---|---|---|
| HF | **Shelf, 10 kHz, +0.5 to +1.0 dB** | Air. Skip if Pro-Q band 5 already added it on the sides |
| HMF | **2.8 kHz, Q 1.0, +0.5 dB** | Snare presence — the crack, not the sizzle |
| LMF | **350 Hz, Q 0.7, −0.5 dB** | Only if still boxy after Pro-Q. Usually skip — one plugin should own the mud |
| LF | **Shelf, 70 Hz, +0.5 to +1.0 dB** | Weight under the kick |
| HPF / LPF | **Out** | Pro-Q already high-passed; two high-passes stack into a steeper slope than either displays |
| SPLIT | **Off** | Only relevant when the filters feed the dynamics sidechain, and the dynamics are off |
| ANALOG | **Off** | A1/A2 add hum and harmonics; the 12-bit sources supply plenty of their own |
| Input trim / Output | Level-matched to bypass | |

**Nothing above 1 dB.** If a band wants +3 dB, the fix belongs on the Tascam at mixdown.

**If using the SSL compressor instead of slot 5:** Ratio **2:1**, threshold for **1 dB GR**,
release **0.3 s**, **F.ATT out** — fast attack is roughly 1 ms and will flatten every MPC
transient. Gate/Expander threshold fully down. Then bypass slot 5 entirely.

---

## Slot 4 — Reel Tape Saturation

The glue for 20+ channels of separately-captured hardware.

| Param | Value |
|---|---|
| Tape speed | **15 IPS** — the low-end head bump and gentle high roll-off are the point; 30 IPS is flatter and more "modern" |
| Tape type | **Opus / 250** for a fuller low end; the darker formulation if the record wants to be dusty |
| Calibration / Input | Push until the meter ticks **1–2 dB into the red on the loudest hits only** |
| Noise | **Off** — the sources supply plenty already |
| Output | Trim back so bypass A/B is level-matched |

Level-matched A/B is not optional. Saturation always sounds better when it is louder; if it
still sounds better at matched level, keep it.

---

## Slot 5 — Pro Compressor (bus glue)

Skip entirely if you used the SSL E-Channel's compressor. One glue compressor, not two.

| Param | Value | Why |
|---|---|---|
| Ratio | **1.5:1** (2:1 max) | Glue, not control |
| Knee | **12 dB** soft | |
| Attack | **30 ms** | Kick and snare transients pass untouched |
| Release | **Auto**, or **300 ms** manual | Auto tracks the tempo well on drum-led material |
| Threshold | for **1–1.5 dB GR maximum** | More and the drums start breathing |
| **Sidechain HPF** | **100 Hz** | The most important setting here — stops the kick ducking the entire record |
| Makeup | Level-matched to bypass | |

---

## Slot 6 — Pro Limiter

| Param | Value |
|---|---|
| Ceiling | **−1.0 dBTP** (true-peak on). Lossy codecs overshoot; this is the safe margin |
| Knee / character | Soft, the more forgiving setting — hard-knee limiting hollows out MPC kicks |
| Release | **Auto**, or **200 ms** if the sustain pumps |
| Threshold | Lower gradually into the loudest bar |
| Dither | **POW-r 2** *only* when rendering to 16-bit. Bouncing 24-bit → no dither |

| Deliverable | Integrated LUFS | Notes |
|---|---|---|
| **Release master** | **−11 LUFS**, −1.0 dBTP | Streaming normalises to ≈ −14 anyway, so pushing past this only buys distortion that gets turned down |
| **Rapper reference bounce** | **−9 LUFS** | Only if someone insists on loud. Same chain, limiter threshold ~2 dB lower |

Watch **PLR (peak-to-loudness): 8–10 dB.** Under 7 and the boom bap punch is gone, whatever the
LUFS number says.

---

## Two directions

**Clean and punchy (90s East Coast):** tape drive to a bare flicker, multiband band 4 gain
+0.5 dB, SSL HF shelf +1.0 dB, Pro-Q side-channel air band in, limiter to −11 LUFS. Let the
transients live.

**Dusty, dark, saturated (underground / lo-fi):** tape drive 3–4 dB into the red, Pro-Q low-pass
around 15–16 kHz, skip the SSL HF shelf and the Pro-Q air band, multiband band 2 gain at 0
(keep the mud), push to −9 LUFS. The S950's 12-bit grit already does half of this — check how
far it has gone before adding more.

---

## The short chain

Six plugins on a master is a lot and most beats do not need them:

**Pro-Q 4 → SSL E-Channel → Pro Limiter**

High-pass and the mid/side low-cut, a dB of console colour, then loudness. Add Reel Tape when
the mix feels like separate boxes rather than one record. Add the multiband only when kick and
bass are actually fighting. Add Pro Compressor only when the whole thing needs knitting and the
SSL's own comp is not doing it.

Full six-stage chain for a finished master; the short chain is the whole job for a reference
bounce.

---

## Bounce checklist

1. Level-matched bypass A/B of the whole chain — better, or just louder? Then the same A/B
   against the reference track in the session.
2. Check mono. The MPC individual outs are mono into the desk, so the low end is already
   mono-compatible; the risk is the XT:C return thinning on the fold-down.
3. Listen to the last bar's reverb tail — where over-compression shows first.
4. Render 24-bit WAV as the archive master; 16-bit + POW-r 2 only if something demands it.
5. Save the MPC project and its samples. The mix is unrecallable, the beat is not.
6. Sleep on it. Reopening the mastering session costs nothing — the file is still sitting there.
