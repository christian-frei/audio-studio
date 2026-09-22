# Manual mastering chain — boom bap, hybrid hardware capture

**Reaper** is the only DAW. Stock: **ReaXComp** for the multiband. Owned third-party:
**FabFilter Pro-Q 4**, the **Waves SSL E-Channel**, **BABY Audio TAIP**. On the way in:
**FabFilter Pro-C 2** and **Pro-L 2** — until they land, ReaComp and **ReaLimit** hold those
two slots. Routing in [CLAUDE.md](CLAUDE.md), the compressor in
[dbx266xl-reference.md](dbx266xl-reference.md), project layout in
[reaper_mastering_session.md](reaper_mastering_session.md).

**Chain:** Pro-Q 4 → ReaXComp → SSL E-Channel → TAIP → Pro-C 2 → Pro-L 2. That is the full
version; "the short chain" at the end is the three-plugin one that is usually enough.

**Where it runs:** its own mastering project, on a chain track, fed by the imported stereo
file — never on the master track of the capture template.

---

## What actually needs mastering here

By the time audio reaches the computer the analog EQ, the SPL transient shaping, the parallel
DBX weight and the XT:C tails are all printed. The master's job is only: kill sub-sonic junk,
control the kick/bass collision, add tape-style glue, and get it loud without flattening the
drums. Everything else was already done on the desk.

**This is a mastering chain, not a mixing one.** Mixing has its own stage and its own project —
[manual_mixing_tascam_reaper.md](manual_mixing_tascam_reaper.md) — where the balance, the
per-channel surgical work and the delay bus live. By the time a stereo file reaches this chain,
both the tone (printed on the desk) and the balance (rebuilt in the multitrack project) are
settled. Anything fixed here that should have been fixed there gets applied to the whole record
at once, which is why it rarely works.

Same reason the chain lives in its own project: a master chain running while a mix is being
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
| 21 / 22 | Mac / Reaper returns — mute during capture |

### What the multitrack holds — post-FX, pre-fader

The per-channel USB sends are **post-EQ, post-insert, pre-fader** (confirmed by riding a fader
against the desk and the Reaper meters together). That splits the capture cleanly in two:

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

**Band 3 only fixes masking.** If the low end is weak because the kick and the bass are
*cancelling*, ducking one of them leaves even less. The signs from a summed master: the low end
reads loud on the meter but thin on the speakers, and it gets weaker at the moments the bass
and the kick land together. That is not a mastering problem — go back to the multitrack project
where the two are still separate files. Explanation and the polarity test in
[manual_mixing_tascam_reaper.md](manual_mixing_tascam_reaper.md).

**Why the multiband still exists after this.** Pro-Q's dynamic bands are program-dependent —
threshold and range are yours, attack and release are automatic and not exposed. ReaXComp
Dynamics gives actual attack and release numbers, which is what the tempo-locked sub band
depends on. Pro-Q for anything surgical or mid/side; the multiband for anything needing timing
set by hand.

---

## Slot 2 — ReaXComp (the exact values)

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

**Crossovers: 90 Hz / 350 Hz / 6 kHz.** In ReaXComp these are the band *bottom frequencies* —
four bands starting at 20 Hz, 90 Hz, 350 Hz and 6 kHz. Per band it gives numeric threshold,
ratio, knee, attack, release and output gain, which is exactly what the values below assume.

**ReaXComp compresses but does not expand.** The optional downward expander on band 4 has no
equivalent here. Skip it: the doc already marked it optional, and the trade was always "noise
is more forgivable than a breathing tail". A ReaGate on a split band would do it, but that is a
lot of routing for a problem this record does not really have.

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

**The band-4 expander is gone.** Old samplers hiss and the XT:C has a noise floor, and the
old chain had an optional downward expander here for it. ReaXComp only compresses, so there is
nothing to set. Leave it: the trade was always "noise is more forgivable than a breathing
tail", and this record has enough deliberate noise in it that a gate on the top band was never
going to be the thing that saved it.

**Reading the whole plugin:** total GR across all four bands around **2–3 dB on the loudest
bars, near zero in the gaps.** If every band moves all the time, the mix needs fixing on the
Tascam.

---

## Slot 3 — Waves SSL E-Channel (console colour)

The Tascam is a clean desk by design; the colour was always meant to come from outboard. The
E-Channel adds back the 4000-series character in the box, at the last stage where it is still
safe to add it.

**Use the EQ. Leave the DYN section out** (`DYN IN` off) — Pro-C 2 in slot 5 does the
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

## Slot 4 — TAIP (tape)

The glue for 20+ channels of separately-captured hardware.

**This stage owns the tape.** Nothing upstream saturates — no tape or console colour on the
mixing submix, by decision, so this slot is the only pass at the effect and can be set without
accounting for a second one.

**TAIP has no IPS switch**, and the old spec here was written around 15 IPS for two specific
reasons. Both survive the move, from different controls: the gentle high roll-off is what
PRESENCE does, and the low-end head bump is not modelled at all — slot 3's LF shelf at 70 Hz is
already doing that job, which is the honest answer rather than forcing LO-SHAPE into the role.

| Control | Setting | Why |
|---|---|---|
| MODEL | **DUAL** | Two emulations chained, each applying half the DRIVE — slightly more weight for the same amount of colour, and gentler per stage. This slot is glue for 20+ separately-captured channels, which is what weight means here |
| INPUT | **NORMAL** | HOT is the more distorted input stage. Wrong on a master; the record already carries 12-bit distortion from the source |
| DRIVE | **15–25 %** | The master bus wants less than a mix bus would. Audible on bypass, invisible otherwise — the old Reel Tape spec called this "1–2 dB into the red on the loudest hits only" |
| AUTO GAIN | **On** | The level-matched A/B above depends on it. Without it, louder wins every time |
| GLUE | **0–10 %** | Tape's compression artefact, and slot 5 is already a bus compressor set for ~1 dB GR. Two serial glues on a master is how a record ends up flat |
| NOISE | **0** | The S950, the MPC converters and the turntable supply plenty of real noise |
| WEAR | **0** | Wow and flutter on a finished master smear the timing the whole record is built on. If tape warble is wanted it belongs upstream, printed into a sample before it reaches the MPC |
| PRESENCE | **30–40 %** | Keeps most of tape's high-end attenuation — this is the 15 IPS roll-off, arrived at from the other direction. It also dulls 12-bit hash in the top octaves. Raise it if the hats lose air |
| LO-SHAPE | **Low** | Saturating the low end refills the band that band 3 and the multiband's sub band just cleared, with harmonics. The head bump comes from slot 3, not from here |
| HI-SHAPE | **Neutral to slightly up** | Puts what saturation there is into the mids and upper mids — the sample and the snare body — rather than into the sub or the hash |
| MIX | **100 %** | Nothing to run parallel around at this drive. Pull back to 70–85 % only if DRIVE is pushed for a deliberately crunchy record |

**If the head bump turns out to matter**, ChowTape is free and has a real IPS control. Worth a
level-matched comparison before assuming slot 3's shelf covers it.

Level-matched A/B is not optional. Saturation always sounds better when it is louder; if it
still sounds better at matched level, keep it.

---

## Slot 5 — FabFilter Pro-C 2 (bus glue)

Skip entirely if you used the SSL E-Channel's compressor. One glue compressor, not two.

| Param | Value | Why |
|---|---|---|
| Style | **Bus** | Program-dependent and gentle by design. Mastering style is the alternative; Punch and Pumping are the wrong end of the plugin for this |
| Ratio | **1.5:1** (2:1 max) | Glue, not control |
| Knee | **12 dB** soft | |
| Attack | **30 ms** | Kick and snare transients pass untouched |
| Release | **Auto**, or **300 ms** manual | Auto tracks the tempo well on drum-led material |
| Threshold | for **1–1.5 dB GR maximum** | More and the drums start breathing |
| **Sidechain HPF** | **100 Hz** | The most important setting here — stops the kick ducking the entire record. Pro-C 2's sidechain filter section, not an external key |
| Dry/Wet | **100 % wet** | Parallel belongs on the drum bus at the desk, and it already happened there in hardware |
| Output | Level-matched to bypass | |

**Until Pro-C 2 arrives:** ReaComp in the same slot, same numbers, with its detector high-pass
set to 100 Hz. It does the job — Pro-C 2 is bought for the interface and the metering, not
because the slot was empty.

---

## Slot 6 — FabFilter Pro-L 2

| Param | Value |
|---|---|
| Style | **Punchy** — it is built to let short transients through, which is the whole argument for an MPC kick. Allround if Punchy sounds too crisp |
| Ceiling | **−1.0 dBTP**, true peak limiting **on**. Lossy codecs overshoot; this is the safe margin |
| Oversampling | **4x** | 
| Release | **~200 ms**, or Auto if the sustain pumps |
| Channel linking | **High** — the sources are mono and centred, so unlinked limiting only moves the image around |
| Gain | Raise gradually into the loudest bar |
| Dither | **Off in the plugin.** Reaper's render dialog does the dither — see the render checklist |

**Pro-L 2 replaces the metering too**, which is the real reason it is the first of the two to
buy: LUFS-I/S/M, true peak and the dynamic-range readout are built into it, so nothing else has
to supply the numbers the targets below are written in.

**Until it arrives:** **ReaLimit** holds the slot for ceiling and release, with **Youlean
Loudness Meter 2** (free) on the master track for LUFS, true peak and PLR. Reaper's own
loudness calculation can confirm an integrated figure on a finished render, but a live meter is
what a limiter threshold actually gets set against.

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

**Pro-Q 4 → SSL E-Channel → Pro-L 2**

High-pass and the mid/side low-cut, a dB of console colour, then loudness. Add TAIP when the
mix feels like separate boxes rather than one record. Add ReaXComp only when kick and bass are
actually fighting. Add Pro-C 2 only when the whole thing needs knitting and the SSL's own comp
is not doing it.

Full six-stage chain for a finished master; the short chain is the whole job for a reference
render.

---

## Render checklist

1. Level-matched bypass A/B of the whole chain — better, or just louder? Then the same A/B
   against the reference track in the project.
2. Check mono. The MPC individual outs are mono into the desk, so the low end is already
   mono-compatible; the risk is the XT:C return thinning on the fold-down.
3. Low-end sanity check. If the kick loses weight exactly where the bass lands, that is
   cancellation, not a mastering job — back to the multitrack project, and no band 3.
4. Listen to the last bar's reverb tail — where over-compression shows first.
5. Render 24-bit WAV as the archive master. For 16-bit, tick **Dither master mix** and
   **Noise shaping** in the render dialog — at 24-bit, neither.
6. Save the MPC project and its samples. The mix is unrecallable, the beat is not.
7. Sleep on it. Reopening the mastering project costs nothing — the file is still sitting there.
