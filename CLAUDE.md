# Boombap Sampling Home Studio

Home studio for making boombap hiphop beats.

## Description

A Technics MK7 turntable goes into an Ecler Nuo2 mixer; sampling usually happens directly into
one of the Akai MPCs, 2000 or 2500. Hardware as much as possible to cut evening screentime,
without turning into a complete gear nerd — **hardware stays under 1000 CHF**, the central
mixing console being the deliberate exception. One beat at a time on one MPC; no switching
mid-project.

When a beat is good enough — basically a few loops — it is tracked through the MPC's 8
individual outs into the Tascam Model 2400.

**The division of labour:** the Tascam and the analog gear do the sound modeling — EQ,
transient shaping, glue, reverb — and that is printed on the way in and cannot be changed
afterwards. **The DAW is for mixing**: balance, surgical corrections and time-based effects.
Mastering is a third stage again, in its own project. See
[manual_mixing_tascam_reaper.md](manual_mixing_tascam_reaper.md).

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

## Sampling from the computer

Drum breaks that live on the hard disk are chopped in **Serato Sample** on the Mac, then sent
out for grit rather than used directly: Serato Sample -> Mac out -> **ch 21/22** -> **aux 1**
-> Akai S950 -> Vermona -> ch 10 -> subgroup 3/4 or 5/6 -> MPC.

**The instrumental VSTs are never used directly.** Serato Sample and **Subfactory** (sub-bass)
live in one **tone-shaping template**, opened only at the very start of a project to play
material out to the S950 or an MPC over the path above, then closed. **Those projects are never
saved.** The DAW here is just a vehicle for holding an instrumental VST and playing it — nothing
it makes stays in the DAW, everything it makes ends up as a sample on hardware, which is what
the archive rule assumes. The sub-60 Hz layer is generated this way and sampled into the MPC, so
it is part of the beat; it is never a channel in a mixing session, where it would be a tonal
decision made at the wrong stage.

Note the conflict with the capture rule: this path needs ch 21/22 **up**, while a USB capture
needs them **muted** (feedback-loop trap). Same channels, two opposite states — be deliberate
about which one the desk is in.

## Capture and mixing

Full workflow in [manual_mixing_tascam_reaper.md](manual_mixing_tascam_reaper.md). The
parts that constrain the routing:

- **Post-FX, pre-fader.** The per-channel USB sends carry the Tascam EQ and the SPL shaping;
  they do not carry the fader positions. Tone prints, balance does not.
- **Uniform ≈ -10 dBFS.** Every channel is tracked at a converter level, not a mix level. The
  trim sets what is recorded, the fader does not — so a fader cannot fix a hot multitrack
  channel, and channels faded out of the desk mix still record at full level.
- **Two passes, nothing rewired — both on every beat.** Pass 1 = the Tascam stereo master,
  Pass 2 = the per-channel multitrack, recorded in the same take. The multitrack is the
  standard, not a contingency: post-FX, pre-fader stems make a quick master quick and let a
  later in-depth master, remix or distribution version start from the parts. The MPC project
  reloads identically, but only the stems freeze the analog tone without a photograph and a
  rebuild.
- **Feedback-loop trap.** Ch 21/22 carries the Mac's return. With those channels up during a
  USB capture the DAW output feeds the master which feeds the DAW. Mute 21/22 for both passes
  and keep record monitoring off in Reaper.
- **Recall.** The MPC project is the archive, not the mixer — it reloads to identical 8-out
  audio, so the multitrack is always re-recordable. The analog pass is not recallable: **save
  every MPC project + its samples**, and photograph the desk and outboard front panels before
  tearing down a session that might need a re-track.

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

- Apple Studio M4 — runs **Reaper** (licence bought, $60 one-time), the only DAW — no Ableton,
  no Pro Tools, and no DAW subscription. Returns to the
  desk on ch 21/22 along with everything else coming out of the Mac. Plugins: Reaper stock
  (ReaDelay, ReaVerbate, ReaComp, ReaLimit) plus **FabFilter Pro-Q 4**, the **Waves SSL
  E-Channel** strip, **BABY Audio TAIP** and the free **Youlean Loudness Meter 2**. The
  mastering chain is three plugins — Pro-Q 4 → TAIP → ReaLimit to −12 LUFS — and nothing is on
  the shopping list. Mixing template in
  [manual_mixing_tascam_reaper.md](manual_mixing_tascam_reaper.md); mastering chain in
  [manual_mastering_reaper.md](manual_mastering_reaper.md) and its project
  layout in [reaper_mastering_session.md](reaper_mastering_session.md).

- Tascam Model 2400 — 24-channel analog console with built-in 24x22 USB interface and SD
  multitrack recorder. The studio hub: every tonal decision is made and printed here, and it is
  also the audio interface. Replaces the Focusrite Scarlett. Chosen as a clean, current, buyable
  hub — under 5k CHF no colored console with per-channel EQ + 8 individual outs exists, so the
  colour comes from the outboard, not the desk. (Fallback colored desk if ever wanted, used
  market: Toft ATB-16, Midas Venice, A&H GL2400.)
  - usb -> Apple Studio M4. Per-channel sends post-FX and pre-fader; stereo master = the mix
  - monitor out L/R -> **ADAM Audio A7V** nearfields. DSP driver-protection limiters built in
    (peak and voice-coil thermal), not defeatable — front LED flashing with the music = program
    peaks, lit for longer = overheating. So no hardware limiter is needed in the monitor path;
    see [manual_mixing_tascam_reaper.md](manual_mixing_tascam_reaper.md) under Monitor
    protection

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
  | 21/22 | Mac Studio M4 / Reaper returns | mute during capture — see feedback-loop trap |

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
