# Mastering — the easy chain

**Three plugins and a meter.** Everything tonal was printed on the desk and the balance was
settled in the mixing project, so this stage only has to clean the bottom, add a little width
and glue, and hit a loudness target.

**Chain:** Pro-Q 4 → TAIP → ReaLimit. **Youlean Loudness Meter 2** sits on the master track,
metering only.

| Plugin | Job | Cost |
|---|---|---|
| **FabFilter Pro-Q 4** | Rumble out of the bottom, width on the sides | Owned |
| **BABY Audio TAIP** | Subtle glue | Owned |
| **ReaLimit** | Loudness to −12 LUFS | Stock |
| **Youlean Loudness Meter 2** | Reading the result | Free |

**Nothing to buy.** Routing is in [CLAUDE.md](CLAUDE.md), the project layout in
[reaper_mastering_session.md](reaper_mastering_session.md), and whether an automatic service
should do this stage at all is being evaluated in
[mastering_evaluation_landr.md](mastering_evaluation_landr.md).

---

## What arrives here

One stereo file, peaking **−10 to −6 dBFS**, rendered from the mixing project — or the pass-1
Tascam capture for a quick master. Capture rules and gain staging are in
[manual_mixing_tascam_reaper.md](manual_mixing_tascam_reaper.md) and are not repeated here.

By the time it arrives, the Tascam EQ, the SPL transient shaping, the parallel DBX weight and
the XT:C tails are all printed, and the balance is rebuilt. **Anything still wrong is a mix
problem or a desk problem**, and fixing it here applies it to the whole record at once — which
is why it rarely works. A re-track is cheap: the MPC project reloads to identical 8-out audio.

---

## Slot 1 — FabFilter Pro-Q 4

**Processing mode: Natural Phase.** Linear phase pre-rings, and pre-ringing smears exactly what
this record is built on — the kick and snare transients.

| Band | Setting | Why |
|---|---|---|
| 1 | **High-pass 30 Hz, 24 dB/oct**, stereo | Sub-sonic junk from the samplers and the turntable path. It is inaudible, it eats limiter headroom, and it makes the low end feel loose. 24 dB/oct is the sweet spot — steeper slopes ring |
| 2 | **Side channel: high-pass 120 Hz, 12 dB/oct** | Keeps the low end mono. This is what makes the widening below safe rather than a mono-compatibility problem |
| 3 | **Side channel: high shelf 8 kHz, +1.0 dB** | The widening. It lifts air in the sides only, so the drums stay centred and solid while the reverb tails and the delay repeats open up |

**Why widening works this way here.** Every MPC out is mono and lands dead centre, so there is
almost nothing in the sides except the XT:C tail, the delay bus and the reverb bus. Lifting the
side channel at the top therefore widens exactly the things that *should* be wide, and touches
the drums not at all. Pushing the shelf past +1.5 dB starts to sound like an effect — and
**check mono before trusting it**, because anything that vanishes on fold-down was only ever in
the sides.

If a beat needs more than these three bands, that is the mix asking for attention, not the
master.

---

## Slot 2 — TAIP (glue)

**This stage owns the tape**, and now also the glue — there is no bus compressor in the chain,
so TAIP's GLUE control is the only dynamics processing on the master.

| Control | Setting | Why |
|---|---|---|
| MODEL | **DUAL** | Two emulations chained, each applying half the DRIVE — slightly more weight for the same colour, and gentler per stage |
| INPUT | **NORMAL** | HOT is the more distorted input stage. The record already carries 12-bit distortion from the source |
| DRIVE | **15–25 %** | Audible on bypass, invisible otherwise |
| AUTO GAIN | **On** | The level-matched A/B below depends on it. Without it, louder wins every time |
| **GLUE** | **20–35 %** | Tape's compression artefact, and the only glue in the chain. Enough to make 20+ separately-captured channels read as one record, not enough to breathe |
| NOISE | **0** | The S950, the MPC converters and the turntable supply plenty of real noise |
| WEAR | **0** | Wow and flutter smear the timing the record is built on. If tape warble is wanted it belongs upstream, printed into a sample before it reaches the MPC |
| PRESENCE | **30–40 %** | Keeps most of tape's high-end attenuation, which also dulls 12-bit hash in the top octaves. Raise it if the hats lose air |
| LO-SHAPE | **Low** | Saturating the low end muddies the kick and refills the space the high-pass just cleared |
| HI-SHAPE | **Neutral to slightly up** | Puts what saturation there is into the mids — the sample and the snare body — rather than the sub or the hash |
| MIX | **100 %** | Nothing to run parallel around at this drive |

**GLUE is the setting that changed** when the chain got simplified. It used to sit near zero
because a bus compressor followed it; now nothing else does that job, so it carries it. If the
record still sounds like separate boxes, this is the control — not the drive.

**Where the weight comes from.** TAIP does not model a tape head bump, so if the low end feels
thin the answer is the desk or the mix, not LO-SHAPE. Adding low-end saturation here is how a
kick turns to mush.

**Level-matched A/B is not optional.** Saturation always sounds better when it is louder; if it
still sounds better at matched level, keep it.

---

## Slot 3 — ReaLimit

| Param | Value |
|---|---|
| Ceiling | **−1.0 dBTP**, true peak limiting **on**. Lossy codecs overshoot on encode; this is the margin that protects against it |
| Target | **−12 LUFS integrated** |
| Release | **~200 ms**, longer if the sustain pumps |
| Gain | Raise gradually into the loudest bar. **1–2 dB of gain reduction is the whole job** |
| Dither | **Off in the plugin.** Reaper's render dialog does it — 16-bit only |

**−12 LUFS against YouTube's −14.** Shorts normalises with a plain gain change at playback, so a
−12 master simply plays about 2 dB down — no re-limiting, no damage. It is a deliberate 2 dB in
hand for everywhere that does *not* normalise, and it costs nothing where it does. Pushing well
past this buys distortion that gets turned down anyway; the full reasoning is in
[mastering_evaluation_landr.md](mastering_evaluation_landr.md).

**Watch PLR (peak-to-loudness): 8–10 dB.** Under 7 and the boom bap punch is gone, whatever the
LUFS number says.

**Render an unlimited 24-bit version too**, every time. A professional mastering engineer wants
headroom, not a finished master to undo — and that file cannot be reconstructed later.

---

## The meter — Youlean Loudness Meter 2

Free, on the **master track**, after everything, processing nothing. It is not part of the
chain; it is how the chain gets checked.

| Read | For |
|---|---|
| **LUFS Integrated** | The −12 target. Measure over the whole beat, not a bar |
| **True peak** | Confirms the −1.0 dBTP ceiling actually held |
| **LUFS Short-term** | The balance check — watch it across sections. A chorus 3 dB above the verse is a *mix* imbalance, and it belongs back in the mixing project |
| **PLR / dynamics readout** | The 8–10 dB punch window |

**Short-term is the one worth learning.** Integrated tells you whether the file is loud enough;
short-term tells you whether the beat is *even*, which is the thing a beginner cannot hear yet
and a meter shows instantly.

---

## What is deliberately not in this chain

Recorded so it does not creep back in:

- **No multiband.** ReaXComp was in an earlier version of this chain. A multiband fixes
  frequency-specific dynamics problems, and those come from the mix — where kick and bass are
  still separate files and can actually be fixed. See the masking-vs-cancellation section in
  [manual_mixing_tascam_reaper.md](manual_mixing_tascam_reaper.md).
- **No bus compressor.** The drums were already glued in hardware, in parallel, by the DBX, and
  TAIP's GLUE covers the rest. Two more dB of bus compression is how a master turns to cardboard.
- **No SSL E-Channel here.** It still earns its place on the ch 19/20 drum return in the mixing
  project. On a master it was adding a dB of colour to a record that gets its colour from a
  12-bit sampler and a turntable.
- **No Pro-L 2, no Pro-C 3.** At −12 LUFS the limiter does 1–2 dB of work, which ReaLimit does
  perfectly well. The FabFilter question is in [reaper_evaluation.md](reaper_evaluation.md), and
  the answer is not "for loudness".

**Adding a plugin here should feel like an admission**, not an improvement — it means something
upstream was left unfinished.

---

## Two directions

**Clean and punchy (90s East Coast):** TAIP drive at the bottom of its range, PRESENCE up around
50 %, the side air band in at +1.0 dB. Let the transients live.

**Dusty and dark (underground / lo-fi):** TAIP drive toward 25 %, PRESENCE down to 20–30 %, skip
the side air band entirely. The S950's 12-bit grit already does half of this — check how far it
has gone before adding more.

---

## Render checklist

1. Level-matched bypass A/B of the whole chain — better, or just louder? Then the same A/B
   against the reference track in the project.
2. Check mono. The MPC outs are mono into the desk, so the low end is already mono-compatible;
   the risk is the side air band, the XT:C return and the delay thinning on fold-down.
3. Low-end sanity check. If the kick loses weight exactly where the bass lands, that is
   cancellation and it is not a mastering job — back to the mixing project.
4. Listen to the last bar's reverb tail — where over-compression shows first.
5. Youlean reads **−12 LUFS integrated, −1.0 dBTP, PLR 8–10**.
6. Render **24-bit WAV** as the archive master, plus an **unlimited 24-bit** version for a
   professional. For 16-bit, tick **Dither master mix** and **Noise shaping** in the render
   dialog — at 24-bit, neither.
7. Save the MPC project and its samples. The mix is unrecallable, the beat is not.
8. Sleep on it. Reopening the mastering project costs nothing — the file is still sitting there.
