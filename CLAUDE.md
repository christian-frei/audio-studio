# Boombap Sampling Home Studio

This is my home studio where i make boombap hiphop beats.

## Description

I use a Technics MK7 turntable that goes into an Ecler Nuo2 mixer.
Sampling happens usually directly into one of my Akai MPCs 2000 or 2500.
To reduce screentime in the evening I try to use hardware as much as possible without turning into a complete gear nerd. Hardware should not cost more than 1000CHF (the central mixing console is the deliberate exception).
Usually, I create one beat at a time on one of my MPCs, I don't switch during a project.
When the beat sounds good enough, basically a few loops, then i record through the 8 individual outs of the MPC into the Tascam Model 2400 console. Mixing, EQ and summing happen on the Tascam (hardware, daw-less); the stereo mix — and the multitrack channels — are captured over USB **post-FX, so the Tascam EQ prints on the recording**. I only switch to Pro Tools for mastering. See "Daw-less mixdown, capture and recall" below for the two-pass workflow.

Medium fidelity:
after watching the masterclass from The Alchemist on aulart.com i try to copy his workflow. he samples everything from the turntable through the dj mixer where heavy EQ is applied to sample the sounds/sonics as close as possible to the end result. the turntable is used like an instrument, the pitch shifter is used to find sonics that are not always hearable at normal speeds. also he uses scratch techniques to sample new kinds of sounds. i m studying the basics of turntableism to achieve these effects.
once sampled he used the LP, BP and HP filters on the MPC2500 to combine different frequency layers so that the beat has some sonics in all hearable frequencies. often a sub-bass below 60 Hz is applied to the kick drum to make it work in a club or big speaker setting.
The goal is to have a complete beat on the MPC2500 which is medium fidelity: enough for rappers to listen to it and get inspired.
Once a track is chosen, only then it is tracked through the eight outs into the Tascam, mixed on the console (daw-less), and the stereo master goes into Pro Tools for mastering only.

## Manual stem-splitting via S950 playback + Vermona Filter Lancet

To stay away from the computer and avoid digital stem separation, a mono sample is band-split
with the Vermona filter (and the Tascam channel EQ) and re-sampled into the MPC. The **Akai
S950 plays back the source sample** (loaded via aux 1 from the turntable or any source) and
returns on **ch 10**, where the Tascam EQ and the in-line Vermona shape it before it goes back
out to a sampler.

Three-pass band isolation (Premier-style) — set the Vermona for each pass and re-sample ch 10
into the target sampler by assigning ch 10 to **subgroup 5/6 -> MPC2500** or
**subgroup 3/4 -> MPC2000**:
- Pass 1: Vermona HP around 250 Hz -> pad A (highs, hats, perc)
- Pass 2: Vermona LP around 250 Hz -> pad B (bass, kick body)
- Pass 3: Vermona BP around 1 kHz with high resonance -> pad C (mid focus)

Each pass produces an independently mute-able, layer-able "stem" on its own pad, with analog
filter character that digital stem separation cannot replicate. Bypass the Vermona for a fourth
pass to get the unfiltered full-range layer.

Since the S950 now uses a single channel instead of the old dry/filtered ch 9 + ch 10 pair,
there is no permanent side-by-side dry vs. filtered comparison — it is one channel, switched
by the filter bypass. Ch 9 is free if the parallel dry/filtered pair is ever wanted back.

## Daw-less mixdown, capture and recall

All mixing, EQ and summing happen on the Tascam; Pro Tools is only for mastering. The Tascam is
mixer and USB interface in one, so the mix and the multitrack come off a single USB cable with
no rewiring — the split happens inside the box.

**Post-FX capture is deliberate.** The per-channel USB sends are set post-FX so the Tascam's
channel EQ prints on the recording — the desk EQ is part of the sound, not something to
re-do later. Consequence: the multitrack is **not** a set of dry stems. Ch 1-3 arrive with the
SPL Transient Designer and the EQ already printed, and ch 17/18 carry the XT:C return EQ'd.
That is committal — there is no undo on a printed EQ curve — which is the trade accepted in
exchange for never mixing in the box.

Two-pass capture (nothing rewired between passes; can be a single take):
- **Pass 1 — the mix (every beat):** arm the Tascam stereo master, EQ/balance on the desk, stereo bus -> 2-track -> master in Pro Tools.
- **Pass 2 — the multitrack (only when a beat gets picked up):** arm the per-channel USB multitrack and record. Can be done any time later.

Because the DBX drum glue returns on its own pair (ch 19/20) rather than being an insert, the
**parallel blend is re-creatable in Pro Tools**: the dry drums on ch 1-3 and the compressed
copy on ch 19/20 are captured as separate tracks, so the dry/crushed ratio can still be moved
after the fact even though everything else is committed.

Recall principle — the **MPC project is the archive, not the mixer**: the saved sequence,
samples, program and out-routing reload to identical 8-out audio, so the multitrack is always
re-recordable; only the analog pass (fader balance, EQ curves, SPL and DBX knob positions) is
unrecallable. **Save every MPC project + its samples religiously**, and if a re-track is ever
likely, photograph the desk and the outboard front panels before tearing the session down —
that photo is the only "session recall" a daw-less setup has.

**Feedback-loop trap:** ch 21/22 carries the Mac's return. If those channels are up while the
stereo master is being captured over USB, the DAW output feeds the master which feeds the DAW.
Keep 21/22 muted (or out of the master) during capture, and input monitoring off in Pro Tools.

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
3U   DBX 266XL                  ← warm; tweaked during mixdown, at hand height
2U   Lexicon MPX100             ← currently not in use, still racked
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

- Apple Studio M4 — runs **Pro Tools Studio**, the only DAW (no Ableton). Returns to the desk
  on ch 21/22 along with everything else coming out of the Mac. Mastering plugins: Pro Tools
  stock (Pro Multiband Dynamics, Pro Compressor, Pro Limiter, Reel Tape Saturation) plus
  **FabFilter Pro-Q 4** and the **Waves SSL E-Channel** strip. Chain and exact settings in
  [manual_mastering_protools_studio.md](manual_mastering_protools_studio.md).

- Tascam Model 2400 — 24-channel analog mixing console with built-in 24x22 USB interface and SD multitrack recorder. This is the studio hub: all mixing, EQ and summing happen here, and it is also the audio interface. Replaces the Focusrite Scarlett. Chosen as a clean, current, buyable hub — under 5k CHF no colored console with per-channel EQ + 8 individual outs exists, so the colour comes from the outboard, not the desk. (Fallback colored desk if ever wanted, used market: Toft ATB-16, Midas Venice, A&H GL2400.)
  - usb -> Apple Studio M4. Per-channel sends are **post-FX** (EQ prints); stereo master = the mix
  - monitor out L/R -> speakers/monitors L,R

  **Channel map**

  | ch | source | insert / notes |
  |----|--------|----------------|
  | 1 | kick (MPC out 1 via Palmer) | insert -> SPL Transient Designer 1; -> subgroup 1/2 |
  | 2 | snare (MPC out 2 via Palmer) | insert -> SPL Transient Designer 2; -> subgroup 1/2 |
  | 3 | hi-hat (MPC out 3 via Palmer) | insert -> SPL Transient Designer 3; -> subgroup 1/2 |
  | 4-8 | perc, bass, instrumental samples (MPC outs 4-8 via Palmer) | no insert |
  | 9 | *free* | |
  | 10 | Akai S950 (mono) | Vermona in-line before the input; insert -> SPL Transient Designer 4 |
  | 11/12 | MPC2000 stereo out | |
  | 13/14 | MPC2500 stereo out | |
  | 15/16 | Ecler Nuo2 (turntable + KOII) | |
  | 17/18 | Alesis XT:C stereo return | EQ'd and recorded post-EQ |
  | 19/20 | DBX 266XL return — **parallel** drum glue | blended under ch 1-3, not an insert |
  | 21/22 | Mac Studio M4 / Pro Tools returns | mute during capture — see feedback-loop trap |

  **Aux sends**
  - aux 1 -> **mono** -> Akai S950 sample-in
  - aux 4 -> Alesis XT:C
  - aux 2, 3, 5 -> free (the MPC sample-sends moved to subgroups; Lexicon out of service)

  **Subgroups**
  - subgroup 1/2 -> DBX 266XL -> back in on ch 19/20 — drum glue, parallel
  - subgroup 3/4 -> **stereo** -> MPC2000 sample-in
  - subgroup 5/6 -> **stereo** -> MPC2500 sample-in

  Using subgroups rather than auxes for the sample-sends buys a stereo, post-fader feed with
  its own level control, and leaves three auxes free.

- Source-sampler role — the Akai S950, fed mono by aux 1, playing back on ch 10 to be
  re-sampled into whichever MPC holds the project (via subgroup 3/4 or 5/6).

- Akai S950 (12-bit mono sampler) — character/source sampler:
  samples from turntable or any Tascam source, adds the 12-bit / ~10 kHz grit, and its selectable
  anti-aliasing low-pass filters clean up down-pitched material. Then resampled into the MPC.
  All mono. Mainly here for re-sampling into the MPC, not as a playback voice in the mix.
  - main out -> Vermona Filter Lancet -> Tascam ch 10; ch 10's insert -> SPL Transient Designer 4
  - record/sample in from tascam - aux 1 (mono)
  - re-sampled into the MPC2500 (subgroup 5/6) or MPC2000 (subgroup 3/4)
  - the full ch 10 chain is therefore: S950 -> Vermona (in-line, before the input) -> channel
    insert -> SPL 4 -> Tascam EQ -> subgroup send. Filter shape, transient shape and EQ are all
    printed into the MPC when re-sampled
  - 8 individual outs unused for now (mono character-box role); available later if wanted
  - **16-keygroup sampling template** — a saved program with 16 short "empty" samples on 16
    keygroups pre-mapped to the 16 Arturia BeatStep pads. Sample fresh chops "into" those
    keygroups and they land already assigned to pads for instant MPC-style play; then re-sample
    the result into the MPC. The BeatStep only plays notes/velocity — filter and tune are
    dialed by hand on the S950 (per keygroup or KGALL).
  - control: no remote CC for filter or tuning — the S950's MIDI only exposes note/velocity,
    pitch bend, program change, CC7 (volume) and CC1 (LFO depth). Filter/tune = hardware, by hand.
    (velocity does drive filter brightness; the BeatStep can't remap an encoder to velocity.)

  Only one MPC is active per project — the Palmer merges whichever one is running, so the
  two never feed ch 1-8 at the same time.

- MPC2500
  - individual outputs 1-8 -> Palmer Pan 16 (merge) -> Tascam channels 1-8
  - stereo out L/R -> Tascam stereo channel 13/14
  - record/re-sample in from tascam - subgroup 5/6 (stereo)

- MPC2000
  - individual outputs 1-8 -> Palmer Pan 16 (merge) -> Tascam channels 1-8
  - stereo out L/R -> Tascam stereo channel 11/12
  - record/re-sample in from tascam - subgroup 3/4 (stereo)

- Ecler Nuo2
  - main out L/R -> Tascam stereo channel 15/16
  - Technics MK7 -> Ecler Nuo2 phono input 2
  - Teenage Engineering KOII -> Ecler Nuo2 line input 1

- Outboard FX — routed by type: transient shaping on channel inserts, bus compression on a subgroup returned in parallel, reverb on aux (send out, return to a channel), filter in-line. Each channel has one insert point — chain two boxes externally to share it. Pad/channel layout: kick 1, snare 2, hi-hat 3, percussion 4, bass 5, instrumental samples 6-8.
  - SPL Transient Designer (4 ch) — inserts on kick/snare/hi-hat (ch 1-3) plus the S950 on ch 10. Ch 1-3 get transient shaping per drum, printed on the recording; kept per-channel rather than on the drum subgroup so each drum gets its own attack/sustain — kick and snare want opposite settings, which a single bus insert can't do. **SPL ch 4 sits on the ch 10 insert** so material is already punchier *before* it is re-sampled into the MPC — the attack is baked into the sample rather than fought with later. Watch the record level into the sampler: an attack boost raises peaks without moving the average much, so a level that looked safe can clip the MPC input once the SPL is engaged. Set the sampler's record level with the SPL in circuit.
  - DBX 266XL (2 ch) — **parallel** drum glue. Ch 1-3 (kick/snare/hi-hat) feed subgroup 1/2 -> DBX -> back in on ch 19/20, blended underneath the dry channels to fatten them. Because it is parallel rather than an insert, it can be compressed far harder than a bus insert would tolerate — heavy gain reduction adds weight and the dry channels keep the transients. Run **Stereo Couple ON** (ch1 master, ch2 follows) so both sides move together and the image stays centered. Settings in [dbx266xl-reference.md](dbx266xl-reference.md). Check polarity on the return: if ch 19/20 up makes the drums thinner instead of fatter, the return is flipped.
  - Vermona Filter Lancet (1 ch) — in-line on the S950's output (S950 -> Vermona -> ch 10), the band-split tool for the manual stem-splitting workflow above.
  - Alesis XT:C (reverb) — aux 4 send, stereo return on ch 17/18, mainly the snare reverb. The return is EQ'd on the desk and recorded post-EQ.
  - Lexicon MPX100 (stereo reverb) — currently not in use.

- Palmer Pan 16 passive DI-box
  merges the 8 individual outs of the MPC2500 and the MPC2000 into Tascam ch 1-8 (merge mode,
  one MPC active per project)

## Open items / to confirm

- **Subgroup count** — this routing uses six subgroup busses (1/2, 3/4, 5/6). Worth confirming
  the Model 2400 exposes that many as independent physical outputs.
- **Ch 9** — the only free channel left.

## currently not in use

- Lexicon MPX100 — out of service, still racked in Rack A (2U). Aux 4 now goes to the XT:C.

- MPC3000 — retired, out of the setup. The Palmer now merges the MPC2500 and the MPC2000.

- Focusrite Scarlett 18i20 + Focusrite Scarlett OctoPre
  - replaced by the Tascam as hub/interface; kept as a spare converter, currently not in the main chain

- Neutrik patchbay (half-normalled, SPP L1)
  - currently not in use
