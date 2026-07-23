# Boombap Sampling Home Studio

This is my home studio where i make boombap hiphop beats.

## Description

I use a Technics MK7 turntable that goes into an Ecler Nuo2 mixer.
Sampling happens usually directly into one of my Akai MPCs 3000, 2000 or 2500.
To reduce screentime in the evening I try to use hardware as much as possible without turning into a complete gear nerd. Hardware should not cost more than 1000CHF (the central mixing console is the deliberate exception).
Usually, I create one beat at a time on one of my MPCs, I don't switch during a project.
When the beat sounds good enough, basically a few loops, then i record through the 8 individual outs of the MPC into the Tascam Model 2400 console. Mixing, EQ and summing happen on the Tascam (hardware, daw-less); the stereo mix — and optionally the 8 dry stems — are captured over USB. I only switch to ableton for mastering. See "Daw-less mixdown, capture and recall" below for the two-pass (mix + stems) workflow.

Medium fidelity:
after watching the masterclass from The Alchemist on aulart.com i try to copy his workflow. he samples everything from the turntable through the dj mixer where heavy EQ is applied to sample the sounds/sonics as close as possible to the end result. the turntable is used like an instrument, the pitch shifter is used to find sonics that are not always hearable at normal speeds. also he uses scratch techniques to sample new kinds of sounds. i m studying the basics of turntableism to achieve these effects.
once sampled he used the LP, BP and HP filters on the MPC2500 to combine different frequency layers so that the beat has some sonics in all hearable frequencies. often a sub-bass below 60 Hz is applied to the kick drum to make it work in a club or big speaker setting.
The goal is to have a complete beat on the MPC2500 which is medium fidelity: enough for rappers to listen to it and get inspired.
Once a track is chosen, only then it is tracked through the eight outs into the Tascam, mixed on the console (daw-less), and the stereo master goes into ableton for mastering only (e.g. Landr).

## Manual stem-splitting via S950 playback + Vermona Filter Lancet

To stay away from the computer and avoid digital stem separation, a mono sample is band-split
with the Vermona filter (and the Tascam channel EQ) and re-sampled into the MPC2500 or MPC3000.
The **Akai S950 plays back the source sample** (loaded via aux 1 from the turntable or any
source); its output lands on the desk as a dry/filtered pair — L on ch 9 (dry), R through the
in-line Vermona on ch 10 (filtered) — so the same signal sits on the desk clean and
analog-filtered side by side. The Tascam EQ on ch 9/10 can shape either further.

Three-pass band isolation (Premier-style) — set the Vermona for each pass and re-sample ch 10
into the target sampler (raise ch 10's aux 2 send -> MPC2500, or aux 3 -> MPC3000):
- Pass 1: Vermona HP around 250 Hz -> pad A (highs, hats, perc)
- Pass 2: Vermona LP around 250 Hz -> pad B (bass, kick body)
- Pass 3: Vermona BP around 1 kHz with high resonance -> pad C (mid focus)

Each pass produces an independently mute-able, layer-able "stem" on its own pad, with analog
filter character that digital stem separation cannot replicate. The dry ch 9 stays available as
a full-range reference, or re-sample it onto a fourth pad as the unfiltered layer.

## Daw-less mixdown, capture and recall

All mixing, EQ and summing happen on the Tascam; Ableton is only for mastering. The Tascam is
mixer and USB interface in one, so the mix and the stems come off a single USB cable with no
rewiring — the split happens inside the box.

Two-pass capture (nothing rewired between passes; can be a single take):
- **Pass 1 — the mix (every beat):** arm the Tascam stereo master, EQ/balance on the desk, stereo bus -> 2-track -> master in Ableton.
- **Pass 2 — dry stems (only when a beat gets picked up):** arm the per-channel USB multitrack (ch 1-8) and record the 8 dry channels. Can be done any time later.

Recall principle — the **MPC project is the archive, not the mixer**: the saved sequence,
samples, program and out-routing reload to identical 8-out audio, so dry stems are always
re-recordable; only the analog summing/EQ pass is unrecallable (fine — a pro mix wants dry
stems anyway). **Save every MPC project + its samples religiously.** For truly dry stems,
verify the Tascam's per-channel USB tap is pre-EQ; if post-EQ, use the ch 1-12 insert
half-plug (TRS to first detent) for a pre-EQ analog tap.

## Racks and cooling

Wooden 19" racks, **open at the back** — good for passive convection cooling, which is what
the outboard relies on (none of it has fans worth counting on). Cooling principle: heat rises,
so the warmest / most vent-dependent box goes at the top with an empty U above it; passive,
no-heat boxes go low or outside the rack. Keep top vent slots unobstructed — never clamp a
solid panel flat on a unit's lid.

**Rack A — 5 HE** (bottom → top):

```
5U   (empty — SPL vent gap)
4U   SPL Transient Designer 4   ← hottest / vents up, so it sits under the gap
3U   DBX 266xs                  ← warm; tweaked during mixdown, at hand height
2U   Lexicon MPX100             ← set-and-forget reverb
1U   Alesis XT:C                ← set-and-forget reverb
```

The Palmer Pan 16 is deliberately **not** in a rack — it's passive (no heat) and never touched
during a mix, just a merge box in the signal path, so it lives on a shelf / behind the desk.

**Rack B — 4 HE** (bottom → top):

```
4U   (empty — S950 vent gap)
3U   ┐
2U   ├ Akai S950 (occupies 3U)
1U   ┘
```

Akai S950 — exactly 3U / 133 mm, 410 mm deep, ~10.8 kg. Runs warm, passively cooled through
top slots, so it sits at the bottom with the 1U gap above it; keep the top cover clear (no
solid board flush on the lid). Open back does the rest.

## Gear and signal chain

- Apple Studio M4

- Tascam Model 2400 — 24-channel analog mixing console with built-in 24x22 USB interface and SD multitrack recorder. This is the studio hub: all mixing, EQ and summing happen here, and it is also the audio interface. Replaces the Focusrite Scarlett. Chosen as a clean, current, buyable hub — under 5k CHF no colored console with per-channel EQ + 8 individual outs exists, so the colour comes from the outboard, not the desk. (Fallback colored desk if ever wanted, used market: Toft ATB-16, Midas Venice, A&H GL2400.)
  - usb -> Apple Studio M4 (per-channel multitrack = dry stems, stereo master = the mix)
  - monitor out L/R -> speakers/monitors L,R
  - aux sends (5 total) -> re-sampling record-ins + reverb sends: aux 1 -> S950, aux 2 -> MPC2500, aux 3 -> MPC3000, aux 4 -> Lexicon MPX100, aux 5 -> Alesis XT:C
  - outboard returns to channels: S950 L -> ch 9, S950 R (via Vermona) -> ch 10, Lexicon -> ch 11, Alesis XT:C -> ch 12
  - subgroup 1 = drum bus: kick/snare/hi-hat/perc (ch 1-4) summed, out to the DBX 266xs and back (glue return); not a record send

- Source-sampler role — a box fed by aux 1 (sample-in) that plays back into the desk to be
  re-sampled by the 2500/3000. Currently the Akai S950 (out on ch 9 dry / ch 10 via the Vermona).
  The retired MPC2000 (out on ch 19/20) shares the aux 1 sample-send when it's active — one
  samples at a time.

- Akai S950 (12-bit mono sampler) — character/source sampler holding the source-sampler slot (took over from the now-retired MPC2000):
  samples from turntable or any Tascam source, adds the 12-bit / ~10 kHz grit, and its selectable
  anti-aliasing low-pass filters clean up down-pitched material. Then resampled by the 2500 or 3000.
  All mono.
  - main out L -> Tascam ch 9 (dry); main out R -> Vermona Filter Lancet -> Tascam ch 10 (filtered) — parallel dry + analog-filtered blend of the same mono signal
  - record/sample in from tascam - aux 1
  - will be resampled by either 2500 or 3000
  - 8 individual outs unused for now (mono character-box role); available later if wanted

- MPC2500
  - individual outputs 1-8 -> Palmer Pan 16 -> Tascam channels 1-8
  - stereo out L/R ->  Tascam stereo channel 15/16
  - record/re-sample in from tascam - aux 2

- MPC3000
  - individual outputs 1-8 -> Palmer Pan 16 -> Tascam channels 1-8
  - stereo out L/R -> Tascam stereo channel 17/18
  - record/re-sample in from tascam - aux 3


- Ecler Nuo2
  - main out L/R -> Tascam stereo channel 13/14
  - Technics MK7 -> Ecler Nuo2 phono input 2
  - Teenage Engineering KOII -> Ecler Nuo2 line input 1

- Outboard FX — routed by type: dynamics on channel inserts, reverbs on aux (send out, return to a channel); the Vermona filter is patched in-line on the S950's R output rather than on an aux. Each channel has one insert point — chain two boxes externally to share it. Pad/channel layout: kick 1, snare 2, hi-hat 3, percussion 4, bass 5, instrumental samples 6-8.
  - SPL Transient Designer (4 ch) — inserts on kick/snare/hi-hat/percussion (ch 1-4), transient shaping per drum (prints on the stems). Kept per-channel (not on the drum subgroup) so each drum gets its own attack/sustain — kick and snare want opposite settings, which a single bus insert can't do — and because channel inserts print on the dry stems while a subgroup insert would not. All four inserted channels are percussive, exactly what transient shaping wants; bass now sits on ch 5, outside the SPL (it barely benefits from transient shaping anyway).
  - DBX 266xs (2 ch) — on the drum subgroup 1 (ch 1-4 = kick/snare/hi-hat/perc summed, stereo; bass on ch 5 stays out of the glue): bus out to the DBX and back as the glue return. Run **Stereo Couple ON** (ch1 master, ch2 follows) so both sides duck together and the image stays centered; ~2:1 OverEasy, 2-4 dB. Glue prints on the mix only, not the ch 1-8 stems (they tap pre-subgroup). Verify the 2400 subgroup 1 exposes L+R insert/return points.
  - Vermona Filter Lancet (1 ch) — patched in-line on the S950's right output (S950 R -> Vermona -> ch 10), so ch 9 carries the dry S950 and ch 10 the filtered copy. No longer on an aux.
  - Lexicon MPX100 (stereo reverb) — aux 4 send, return to ch 11
  - Alesis XT:C (reverb) — aux 5 send, return to ch 12

- Palmer Pan 16 passive DI-box
  merges the 8 individual outs of both MPC2500 and MPC3000

## currently not in use

- MPC2000 — retired for now (inactive), off the desk for space. Returns as the source-sampler
  (stereo out -> ch 19/20, sample-in <- aux 1) once there's desktop room again; the S950 holds
  that role meanwhile.

- Focusrite Scarlett 18i20 + Focusrite Scarlett OctoPre
  - replaced by the Tascam as hub/interface; kept as a spare converter, currently not in the main chain

- Neutrik patchbay (half-normalled, SPP L1)
  - currently not in use
