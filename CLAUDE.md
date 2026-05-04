# Boombap Sampling Home Studio

This is my home studio where i make boombap hiphop beats.

## Description

I use a Technics MK7 turntable that goes into a Nuo2 mixer.
Sampling happens usually directly into one of my Akai MPCs 3000, 2000 or 2500.
To reduce screentime in the evening I try to use hardware as much as possible without turning into a complete gear nerd. Hardware should not cost more than 1000CHF.
Usually, I create one beat at a time on one of my MPCs, I don't switch during a project.
When the beat sounds good enough, basically a few loops then i record through the 8 individual outs of the MPC into a Focusrite scarlett 18i20 and arm 8 tracks in ableton. Afterwards i switch fully to ableton where i do a simple mixdown.

Medium fidelity:
after watching the masterclass from The Alchemist on aulart.com i try to copy his workflow. he samples everything from the turntable through the dj mixer where heavy EQ is applied to sample the sounds/sonics as close as possible to the end result. the turntable is used like an instrument, the pitch shifter is used to find sonics that are not always hearable at normal speeds. also he uses scratch techniques to sample new kinds of sounds. i m studying the basics of turntableism to achieve these effects.
once sampled he used the LP, BP and HP filters on the MPC2500 to combine different frequency layers so that the beat has some sonics in all hearable frequencies. often a sub-bass below 60 Hz is applied to the kick drum to make it work in a club or big speaker setting.
The goal is to have a complete beat on the MPC2500 which is medium fidelity: enough for rappers to listen to it and get inspired.
Once a track is chosen, only then it will be tracked through the eight outs into ableton where some final polishing happens (SmartEq:4, NI transient master, and Landr mastering plugin).

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

- Focusrite Scarlett 18i20 with Focusrite Scarlett OctoPre, resulting in 16 line ins
  - usb -> Apple Studio M4
  - out 1,2 -> speakers/monitors L,R
  - out 7,8 -> MPC3000 record in L,R
  - out 9,10 -> MPC2000 record in L,R

- Technics MK7 -> Ecler Nuo2 phono input 2

- Ecler Nuo2 main out L/R -> Focusrite Scarlett in 15,16

- Palmer Pan 16 passive DI-box, merge link is active on all channels
  - xlr balanced outs 1-8 into scarlett 1-8

- MPC2500
  - individual outputs 1-8 -> Palmer Pan 1-8
  - stereo out L/R -> scarlett 9/10
  
- MPC2000
  - individual outputs 1-8 -> Palmer Pan 1-8
  - stereo out L/R -> scarlett 11/12

- Teenage Engineering KOII -> Ecler Nuo2 line input 1

- DBX 266xl
- SPL Transient Designer
- Lexicon MPX100
- Vermona Filter Lancet
- Alesis XT:C
  - currently not in use

- Neutrik patchbay (half-normalled, SPP L1)
  - currently not in use
