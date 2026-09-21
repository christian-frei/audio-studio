# Boombap Sampling Home Studio

Home studio for making boombap hiphop beats.

## Description

A Technics MK7 turntable goes into an Ecler Nuo2 mixer; sampling usually happens directly into
one of the Akai MPCs, 2000 or 2500. Hardware as much as possible to cut evening screentime,
without turning into a complete gear nerd — **hardware stays under 1000 CHF**, the central
mixing console being the deliberate exception. One beat at a time on one MPC; no switching
mid-project.

When a beat is good enough — basically a few loops — it is tracked through the MPC's 8
individual outs into the Tascam Model 2400. Mixing, EQ and summing happen on the Tascam
(hardware, daw-less); Pro Tools is for mastering only. Details in
[Daw-less mixdown, capture and recall](#daw-less-mixdown-capture-and-recall).

### Medium fidelity

Following The Alchemist's masterclass on aulart.com: sample everything from the turntable
through the DJ mixer, with heavy EQ applied on the way in, so the sonics are already as close
to the end result as possible. The turntable is used as an instrument — the pitch shifter finds
sonics that are not audible at normal speed, and scratch techniques produce new kinds of
sounds. I'm studying basic turntablism to get at these.

Once sampled, the MPC2500's LP, BP and HP filters combine frequency layers so the beat has
something in every hearable band. A sub-bass below 60 Hz often goes under the kick so it works
on a club system.

The goal is a complete beat on the MPC2500 at medium fidelity — enough for rappers to listen
and get inspired. Only once a track is chosen does it get tracked, mixed on the console and
mastered.

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

The S950 uses a single channel rather than the old dry/filtered ch 9 + ch 10 pair, so there is
no permanent side-by-side comparison — it is one channel, switched by the filter bypass. Ch 9
is free if the parallel dry/filtered pair is ever wanted back.

## Daw-less mixdown, capture and recall

All mixing, EQ and summing happen on the Tascam; Pro Tools is only for mastering. The Tascam is
mixer and USB interface in one, so the mix and the multitrack come off a single USB cable with
no rewiring — the split happens inside the box.

**Post-FX capture is deliberate.** The per-channel USB sends are post-FX so the Tascam's channel
EQ prints on the recording — the desk EQ is part of the sound, not something to re-do later. So
the multitrack is **not** a set of dry stems: ch 1-3 arrive with the SPL Transient Designer and
the EQ already printed, ch 17/18 carry the XT:C return EQ'd. Committal — there is no undo on a
printed EQ curve — and that is the trade accepted in exchange for never mixing in the box.

**Those sends are also pre-fader** (post-EQ, post-insert, pre-fader — confirmed by riding a
fader against both Pro Tools meters). The EQ and transient shaping print; the **balance does
not**. Every channel is therefore tracked at a uniform **≈ -10 dBFS**, making the multitrack a
level-normalised archive rather than a mix — the leveling is recreated at the mixing step, and
the only file holding the balance actually heard is the pass-1 stereo master. Two consequences
at the desk: a fader cannot fix a hot multitrack channel (only the trim moves the recorded
level, and it moves the mix with it), and channels faded out of the mix still record at full
level.

Two-pass capture (nothing rewired between passes; can be a single take):
- **Pass 1 — the mix (every beat):** arm the Tascam stereo master, EQ/balance on the desk,
  stereo bus -> 2-track -> master in Pro Tools.
- **Pass 2 — the multitrack (only when a beat gets picked up):** arm the per-channel USB
  multitrack and record. Can be done any time later.

Because the DBX drum glue returns on its own pair (ch 19/20) rather than being an insert, the
dry drums on ch 1-3 and the compressed copy land in Pro Tools as separate tracks, so a
dry/crushed ratio can still be built after the fact. **Re-creatable, not recallable** — the
ratio itself lived in the faders, so the stereo master and a photo of the desk are the only
record of the blend that was heard.

Recall principle — the **MPC project is the archive, not the mixer**: the saved sequence,
samples, program and out-routing reload to identical 8-out audio, so the multitrack is always
re-recordable; only the analog pass (fader balance, EQ curves, SPL and DBX knob positions) is
unrecallable, and the fader balance is not even in the multitrack. **Save every MPC project +
its samples religiously**, and if a re-track is ever likely, photograph the desk and the
outboard front panels before tearing the session down — that photo is the only "session recall"
a daw-less setup has.

**Feedback-loop trap:** ch 21/22 carries the Mac's return. If those channels are up while the
stereo master is being captured over USB, the DAW output feeds the master which feeds the DAW.
Keep 21/22 muted (or out of the master) during capture, and input monitoring off in Pro Tools.

## Racks and cooling

Wooden 19" racks, **open at the back** — passive convection is what the outboard relies on,
since none of it has fans worth counting on. Principle: heat rises, so the warmest box goes at
the top with an empty U above it, and passive no-heat boxes go low or outside the rack. Never
clamp a solid panel flat on a unit's lid.

**Rack A — 5 HE** (bottom → top):

```
5U   (empty — SPL vent gap)
4U   SPL Transient Designer 4   ← hottest / vents up, so it sits under the gap
3U   DBX 266XL                  ← warm; tweaked during mixdown, at hand height
2U   Lexicon MPX100             ← out of service, still racked
1U   Alesis XT:C                ← set-and-forget reverb
```

**Rack B — 4 HE** (bottom → top):

```
4U   (empty — S950 vent gap)
3U   ┐
2U   ├ Akai S950 (occupies 3U)
1U   ┘
```

Akai S950 — exactly 3U / 133 mm, 410 mm deep, ~10.8 kg. Runs warm, passively cooled through top
slots, so it sits at the bottom with the gap above it and the top cover stays clear.

The Palmer Pan 16 is deliberately **not** racked — passive, never touched during a mix, just a
merge box in the signal path, so it lives on a shelf or behind the desk.

## Gear and signal chain

- Apple Studio M4 — runs **Pro Tools Studio**, the only DAW (no Ableton). Returns to the desk
  on ch 21/22 along with everything else coming out of the Mac. Mastering plugins: Pro Tools
  stock (Pro Multiband Dynamics, Pro Compressor, Pro Limiter, Reel Tape Saturation) plus
  **FabFilter Pro-Q 4** and the **Waves SSL E-Channel** strip. Chain and settings in
  [manual_mastering_protools_studio.md](manual_mastering_protools_studio.md); session layout in
  [protools_mastering_session.md](protools_mastering_session.md).

- Tascam Model 2400 — 24-channel analog console with built-in 24x22 USB interface and SD
  multitrack recorder. The studio hub: all mixing, EQ and summing happen here, and it is also
  the audio interface. Replaces the Focusrite Scarlett. Chosen as a clean, current, buyable
  hub — under 5k CHF no colored console with per-channel EQ + 8 individual outs exists, so the
  colour comes from the outboard, not the desk. (Fallback colored desk if ever wanted, used
  market: Toft ATB-16, Midas Venice, A&H GL2400.)
  - usb -> Apple Studio M4. Per-channel sends post-FX and pre-fader; stereo master = the mix
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

  Subgroups rather than auxes for the sample-sends buys a stereo, post-fader feed with its own
  level control, and leaves three auxes free.

- Akai S950 (12-bit mono sampler) — the character / source sampler, and the only box in the
  setup whose job is to be re-sampled rather than mixed. Fed mono by aux 1 from the turntable
  or any Tascam source, it adds the 12-bit / ~10 kHz grit, and its selectable anti-aliasing
  low-pass filters clean up down-pitched material. Plays back on ch 10 to be re-sampled into
  whichever MPC holds the project. All mono.
  - main out -> Vermona Filter Lancet -> Tascam ch 10; ch 10's insert -> SPL Transient Designer 4
  - record/sample in from tascam - aux 1 (mono)
  - re-sampled into the MPC2500 (subgroup 5/6) or MPC2000 (subgroup 3/4)
  - the full ch 10 chain: S950 -> Vermona (in-line, before the input) -> channel insert ->
    SPL 4 -> Tascam EQ -> subgroup send. Filter shape, transient shape and EQ all print into
    the MPC when re-sampled
  - 8 individual outs unused for now; available later if wanted
  - **16-keygroup sampling template** — a saved program with 16 short "empty" samples on 16
    keygroups pre-mapped to the 16 Arturia BeatStep pads. Sample fresh chops "into" those
    keygroups and they land already assigned to pads for instant MPC-style play; then re-sample
    the result into the MPC.
  - control: no remote CC for filter or tuning — the S950's MIDI only exposes note/velocity,
    pitch bend, program change, CC7 (volume) and CC1 (LFO depth), so filter and tune are dialed
    by hand (per keygroup or KGALL). Velocity does drive filter brightness, but the BeatStep
    can't remap an encoder to velocity.

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

- Palmer Pan 16 passive DI-box — merges the 8 individual outs of the MPC2500 and the MPC2000
  into Tascam ch 1-8 (merge mode). Only one MPC is active per project, so the two never feed
  ch 1-8 at the same time.

- Outboard FX — routed by type: transient shaping on channel inserts, bus compression on a
  subgroup returned in parallel, reverb on aux, filter in-line. Each channel has one insert
  point — chain two boxes externally to share it. Pad/channel layout: kick 1, snare 2,
  hi-hat 3, percussion 4, bass 5, instrumental samples 6-8.
  - **SPL Transient Designer (4 ch)** — inserts on kick/snare/hi-hat (ch 1-3) plus the S950 on
    ch 10. Per-channel rather than on the drum subgroup so each drum gets its own
    attack/sustain — kick and snare want opposite settings, which a single bus insert can't do.
    **SPL ch 4 sits on the ch 10 insert** so material is already punchier *before* it is
    re-sampled — the attack is baked into the sample rather than fought with later. Watch the
    record level into the sampler: an attack boost raises peaks without moving the average
    much, so a level that looked safe can clip the MPC input once the SPL is engaged. Set the
    sampler's record level with the SPL in circuit.
  - **DBX 266XL (2 ch)** — **parallel** drum glue. Ch 1-3 feed subgroup 1/2 -> DBX -> back in on
    ch 19/20, blended underneath the dry channels to fatten them. Being parallel rather than an
    insert, it can be compressed far harder than a bus insert would tolerate: heavy gain
    reduction adds weight while the dry channels keep the transients. Run **Stereo Couple ON**
    (ch1 master, ch2 follows) so both sides move together and the image stays centered. Settings
    in [dbx266xl-reference.md](dbx266xl-reference.md). Check polarity on the return — if ch
    19/20 up makes the drums thinner instead of fatter, the return is flipped.
  - **Vermona Filter Lancet (1 ch)** — in-line on the S950's output, the band-split tool for the
    manual stem-splitting workflow above.
  - **Alesis XT:C (reverb)** — aux 4 send, stereo return on ch 17/18, mainly the snare reverb.
    The return is EQ'd on the desk and recorded post-EQ.
  - **Lexicon MPX100 (stereo reverb)** — out of service.

## Open items / to confirm

- **Subgroup count** — this routing uses six subgroup busses (1/2, 3/4, 5/6). Worth confirming
  the Model 2400 exposes that many as independent physical outputs.
- **Ch 9** — the only free channel left.

## Currently not in use

- **Lexicon MPX100** — out of service, still racked in Rack A (2U). Aux 4 now goes to the XT:C.
- **MPC3000** — retired. The Palmer now merges the MPC2500 and the MPC2000.
- **Focusrite Scarlett 18i20 + Scarlett OctoPre** — replaced by the Tascam as hub/interface;
  kept as a spare converter, out of the main chain.
- **Neutrik patchbay** (half-normalled, SPP L1) — not currently patched in.
