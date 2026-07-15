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

## Manual stem-splitting via tascam EQ and Vermona Filter Lancet

To stay away from the computer and avoid digital stem separation, samples can be band-split using the tascam EQs and the vermona filter and re-sampled into the MPC2500 or MPC3000. The MPC2000 plays back the source sample, its stereo out goes into a tascam stereo channel with its EQs. the filter lancet is routed over a aux send return.


Three-pass band isolation (Premier-style):
- Pass 1: Vermona HP around 250 Hz -> re-sample into MPC2500/3000 pad A (highs, hats, perc)
- Pass 2: Vermona LP around 250 Hz -> pad B (bass, kick body)
- Pass 3: Vermona BP around 1 kHz with high resonance -> pad C (mid focus)

Each pass produces an independently mute-able, layer-able "stem" on its own pad, with analog filter character that digital stem separation cannot replicate.

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

## Gear and signal chain

- Apple Studio M4

- Tascam Model 2400 — 24-channel analog mixing console with built-in 24x22 USB interface and SD multitrack recorder. This is the studio hub: all mixing, EQ and summing happen here, and it is also the audio interface. Replaces the Focusrite Scarlett. Chosen as a clean, current, buyable hub — under 5k CHF no colored console with per-channel EQ + 8 individual outs exists, so the colour comes from the outboard, not the desk. (Fallback colored desk if ever wanted, used market: Toft ATB-16, Midas Venice, A&H GL2400.)
  - usb -> Apple Studio M4 (per-channel multitrack = dry stems, stereo master = the mix)
  - monitor out L/R -> speakers/monitors L,R
  - subgroup outs -> MPC record-ins for re-sampling: sub 1 -> MPC2500, sub 2 -> MPC3000, sub 3 -> MPC2000 (sub 4 = drum-glue bus for the DBX, not a record send)

- MPC2000 
  - can be used as first sampler, to record from turntable and do some light chopping, will then be sent through outboard gear and resampled by 2500 or 3000
  - stereo out L/R -> Tascam stereo channel 19/20
  - record in from tascam - subgroup 3
  - will be resampled by either 2500 or 3000

- MPC2500
  - individual outputs 1-8 -> Palmer Pan 16 -> Tascam channels 1-8
  - stereo out L/R ->  Tascam stereo channel 15/16
  - record in from tascam - subgroup 1

- MPC3000
  - individual outputs 1-8 -> Palmer Pan 16 -> Tascam channels 1-8
  - stereo out L/R -> Tascam stereo channel 17/18
  - record in from tascam - subgroup 2


- Ecler Nuo2
  - main out L/R -> Tascam stereo channel 13/14
  - Technics MK7 -> Ecler Nuo2 phono input 2
  - Teenage Engineering KOII -> Ecler Nuo2 line input 1

- Outboard FX — routed by type: dynamics on channel inserts, ambience and the filter on aux. Each channel has one insert point — chain two boxes externally to share it. Pad/channel layout: kick 1, snare 2, hats 3, bass 4, samples 5-8.
  - SPL Transient Designer (4 ch) — inserts on kick/snare/hats/bass (ch 1-4), transient shaping per drum (prints on the stems). Kept per-channel (not on the drum subgroup) so each drum gets its own attack/sustain — kick and snare want opposite settings, which a single bus insert can't do — and because channel inserts print on the dry stems while a subgroup insert would not. Ch 4 (bass) barely uses transient shaping, so route a perc/sample sound there from the MPC when bass isn't needed.
  - DBX 266xs (2 ch) — insert across the drum subgroup 4 (ch 1-4 summed, stereo) for kit glue. Run **Stereo Couple ON** (ch1 master, ch2 follows) so both sides duck together and the image stays centered; ~2:1 OverEasy, 2-4 dB. Glue prints on the mix only, not the ch 1-8 stems (they tap pre-subgroup). Verify the 2400 subgroup exposes L+R insert points.
  - Vermona Filter Lancet (1 ch) — AUX send/return
  - Lexicon MPX100 (stereo reverb) — AUX send/return
  - Alesis XT:C (reverb) — AUX send/return

- Palmer Pan 16 passive DI-box
  merges the 8 individual outs of both MPC2500 and MPC3000

## currently not in use

- Focusrite Scarlett 18i20 + Focusrite Scarlett OctoPre
  - replaced by the Tascam as hub/interface; kept as a spare converter, currently not in the main chain

- Neutrik patchbay (half-normalled, SPP L1)
  - currently not in use
