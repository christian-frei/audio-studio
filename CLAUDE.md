# Boombap Sampling Home Studio

This is my home studio where i make boombap hiphop beats.

## Description

I use a Technics MK7 turntable that goes into a Nuo2 mixer.
Sampling happens usually directly into one of my Akai MPCs 3000, 2000 or 2500.
To reduce screentime in the evening I try to use hardware as much as possible without turning into a complete gear nerd. Hardware should not cost more than 1000CHF (the central mixing console is the deliberate exception — see dawless-setup.md).
Usually, I create one beat at a time on one of my MPCs, I don't switch during a project.
When the beat sounds good enough, basically a few loops, then i record through the 8 individual outs of the MPC into the Tascam Model 2400 console. Mixing, EQ and summing happen on the Tascam (hardware, daw-less); the stereo mix — and optionally the 8 dry stems — are captured over USB. I only switch to ableton for mastering. See dawless-setup.md for the full daw-less workflow and the two-pass (mix + stems) capture.

Medium fidelity:
after watching the masterclass from The Alchemist on aulart.com i try to copy his workflow. he samples everything from the turntable through the dj mixer where heavy EQ is applied to sample the sounds/sonics as close as possible to the end result. the turntable is used like an instrument, the pitch shifter is used to find sonics that are not always hearable at normal speeds. also he uses scratch techniques to sample new kinds of sounds. i m studying the basics of turntableism to achieve these effects.
once sampled he used the LP, BP and HP filters on the MPC2500 to combine different frequency layers so that the beat has some sonics in all hearable frequencies. often a sub-bass below 60 Hz is applied to the kick drum to make it work in a club or big speaker setting.
The goal is to have a complete beat on the MPC2500 which is medium fidelity: enough for rappers to listen to it and get inspired.
Once a track is chosen, only then it is tracked through the eight outs into the Tascam, mixed on the console (daw-less), and the stereo master goes into ableton for mastering only (e.g. Landr).

## Manual stem-splitting via outboard FX chain

To stay away from the computer and avoid digital stem separation, samples can be band-split using the outboard FX chain and re-sampled into the MPC2500. The MPC2000 plays back the source sample, its stereo out goes through the FX chain, and the result is sampled back into the MPC2500.

Chain order: Vermona Lancet -> SPL Transient Designer -> DBX 266xl -> Lexicon MPX100
- Vermona Lancet first: filter to isolate a frequency band (HP, BP, or LP)
- SPL Transient Designer: shape attack/sustain on the isolated band
- DBX 266xl: compress and gate the shaped result
- Lexicon MPX100: add space last so reverb tails are not filtered or compressed

Three-pass band isolation (Premier-style):
- Pass 1: Vermona HP around 250 Hz -> re-sample into MPC2500 pad A (highs, hats, perc)
- Pass 2: Vermona LP around 250 Hz -> pad B (bass, kick body)
- Pass 3: Vermona BP around 1 kHz with high resonance -> pad C (mid focus)

Each pass produces an independently mute-able, layer-able "stem" on its own pad, with analog filter character that digital stem separation cannot replicate.

## Gear and signal chain

- Apple Studio M4

- Tascam Model 2400 — 24-channel analog mixing console with built-in 24x22 USB interface and SD multitrack recorder. This is the studio hub: all mixing, EQ and summing happen here, and it is also the audio interface. Replaces the Focusrite Scarlett.
  - usb -> Apple Studio M4 (per-channel multitrack = dry stems, stereo master = the mix)
  - monitor out L/R -> speakers/monitors L,R
  - aux / subgroup outs -> MPC record-ins (2500/2000/3000) for re-sampling  [exact bus assignment TBD]

- MPC2500 (primary beat machine)
  - individual outputs 1-8 -> Tascam channels 1-8   (line in, no DI)
  - stereo out L/R -> spare Tascam stereo channel (optional)

- MPC3000
  - individual outputs 1-8 -> Tascam channels channels 9-16
  - stereo out L/R -> outboard FX chain -> MPC2500 record in (manual stem-splitting, see above)

- Technics MK7 -> Ecler Nuo2 phono input 2
- Teenage Engineering KOII -> Ecler Nuo2 line input 1
- Ecler Nuo2 main out L/R -> Tascam stereo channel (e.g. 21/22)

- Outboard FX — routed by type: in-line dynamics/tone on channel inserts, ambience on aux. Full patch in dawless-setup.md. Also doubles as the manual stem-splitting re-sampling chain (see that section).
  - SPL Transient Designer (4 ch) — inserts on kick/snare/hats/bass (ch 1-4), transient shaping per drum
  - DBX 266xl (2 ch) — insert across the drum subgroup (stereo) for kit glue
  - Vermona Filter Lancet (1 ch) — insert on a sample channel when filtering a layer; also the re-sampling chain
  - Lexicon MPX100 (stereo reverb) — AUX send/return
  - Alesis XT:C (reverb) — AUX send/return

- Focusrite Scarlett 18i20 + Focusrite Scarlett OctoPre
  - replaced by the Tascam as hub/interface; kept as a spare converter, currently not in the main chain

- Palmer Pan 16 passive DI-box
  - no longer needed — it only balanced the MPC outs for the long run to the Scarlett; the Tascam takes the MPC line outs directly. Free to reuse or retire.

- Neutrik patchbay (half-normalled, SPP L1)
  - currently not in use
