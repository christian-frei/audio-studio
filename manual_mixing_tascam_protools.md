# Mixing — what the desk commits, what Pro Tools decides

The Tascam commits the **tone**; Pro Tools decides the **balance**. That split is forced by the
capture itself: the per-channel USB sends are post-EQ and **pre-fader**, so the EQ, the SPL
transient shaping, the DBX glue and the XT:C tails all print, and the fader positions do not.
Something has to rebuild the balance afterwards, and that is what the Pro Tools multitrack
template is for.

Mastering is a separate stage again — chain in
[manual_mastering_protools_studio.md](manual_mastering_protools_studio.md), session layout in
[protools_mastering_session.md](protools_mastering_session.md). Routing and channel map in
[CLAUDE.md](CLAUDE.md).

**This is not a daw-less setup, and it is not trying to be.** The Tascam and the analog gear
are there for sound modeling that cannot be changed afterwards — decided in the moment, on
hardware, and printed. The DAW is for mixing. Both halves keep their point: nothing tonal gets
deferred to a plugin, and nothing about the balance gets frozen before it is ready.

---

## Two routes to a mix

| | Route A — desk mix | Route B — multitrack mix |
|---|---|---|
| Source | Pass 1 stereo capture | Pass 2 per-channel multitrack |
| Balance | Tascam faders, printed into the stereo file | Rebuilt in the Pro Tools template |
| When | The quick bounce — sending a rapper something the same evening | **The standard.** Every beat worth keeping |
| Next step | Straight to the mastering session | Bounce a stereo mix, then the mastering session |

**Route B is the default, and the multitrack is captured on every beat** — not only on the ones
that get picked up. The two passes are one take with nothing rewired, so the extra cost is disk
space and nothing else, and having all the stems on hand pays twice over:

- **A quick master stays quick.** The template opens with the balance to rebuild and nothing
  else to decide — the tone is already printed on the stems.
- **Anything later starts from stems.** An in-depth master, a remix, a version prepared for
  distribution — all of it begins with the parts, instead of with a re-track.

The MPC project is still the archive and a re-track is still cheap, but a re-track only
reproduces the *tone* if the desk and the outboard are still set the way they were — which
depends on a photograph and a careful rebuild. The multitrack is the only thing that freezes
the analog pass outright. Route A stays for the fast reference bounce; it is no longer where
most beats end.

---

## Capture and gain staging

Two-pass capture, nothing rewired between passes — it can be a single take:

- **Pass 1 — the mix (every beat):** arm the Tascam stereo master. EQ and balance on the desk,
  stereo bus → 2-track → Pro Tools.
- **Pass 2 — the multitrack (every beat):** arm the per-channel USB multitrack and record it in
  the same take. It can be done later from a reloaded MPC project, but doing it now costs
  nothing and keeps the analog tone that was actually heard.

**Post-FX capture is deliberate.** The channel EQ prints — the desk EQ is part of the sound,
not something to re-do later. So the multitrack is **not** a set of dry stems: ch 1-3 arrive
with the SPL Transient Designer and the EQ already on them, ch 17/18 carry the XT:C return
EQ'd. Committal, and that is the trade.

**Pre-fader is the other half.** The balance does not print. Every channel is therefore tracked
at a uniform **≈ −10 dBFS** — a converter level, not a mix — and the multitrack arrives as a
level-normalised archive. Three things follow at the desk:

1. **A fader cannot fix a hot multitrack channel.** Only the trim moves the recorded level, and
   it moves the desk mix with it. Set trim for the converter, balance with the fader.
2. **Channels faded out of the mix still record at full level.** Good as archive, confusing
   later when the multitrack holds parts that are not in the record.
3. **The parallel drum blend is re-creatable, not recallable.** Ch 1-3 dry and ch 19/20 crushed
   are separate files, so a ratio can be built later — but not *the* ratio, which lived in the
   faders. Rebuilding it is a job for the template; see below.

**Feedback-loop trap.** Ch 21/22 carries the Mac's return. If those channels are up while the
stereo master is being captured over USB, the DAW output feeds the master which feeds the DAW.
Keep 21/22 muted (or out of the master) during both passes, and input monitoring off in
Pro Tools.

---

## The Pro Tools multitrack template

A channel per Tascam channel, each with a **FabFilter Pro-Q 4**, plus a submix, a delay bus,
and a **Waves SSL E-Channel** on the ch 19/20 drum-glue return.

**Processing mode: Natural Phase**, same reasoning as the master — linear phase pre-rings, and
pre-ringing smears the kick and snare transients this record is built on.

**Surgical only.** The musical EQ already happened on the desk and is printed. A Pro-Q instance
here is for a specific collision, not for tone. If a channel wants a broad +3 dB shelf, that is
a sign the desk pass was wrong and the honest fix is a re-track — which is cheap, because the
MPC project reloads to identical 8-out audio.

**Most channels should end up with the plugin doing nothing.** An instance on every channel is
fine as a template — it is there when needed — but a template is not a to-do list.

### Analog coloring — off by default

Leave it off on every channel. The reasoning is the same as the SSL's ANALOG switch on the
master: the 12-bit S950, the MPC converters, the turntable and the Ecler already supply more
harmonic content than any model adds, and the whole architecture exists to get colour from
hardware rather than plugins.

Per instance it is inaudible. Across 22 instances it compounds — mostly as low-level harmonic
hash in the top octaves, which is exactly where 12-bit aliasing already lives. It also costs
CPU 22 times over for an effect that does not survive a fair comparison.

If it is ever worth testing, test it honestly: **all instances on vs. all instances off, on the
full mix, level-matched.** One channel soloed proves nothing. And if the flavour is wanted, put
a single instance on the submix — one audible decision rather than 22 invisible ones.

### The kick / bass collision

The most useful thing in the whole template, and the one that justifies per-channel Pro-Q.

**First, work out which problem it actually is.** Masking and cancellation look the same on the
meter and need opposite fixes:

- **Polarity test.** Flip polarity on the bass channel and listen to the low end. If it gets
  *louder*, the two were cancelling — ducking will not fix that, and the real fix is timing or
  tuning. If it gets thinner, they were summing fine and the problem is masking, which is what
  the duck is for.
- **Tuning.** Cancellation is a live risk here specifically because every MPC out is mono and
  lands dead centre — two near-sine low sources at close frequencies will beat. If the kick
  carries a deliberate sub-60 Hz layer, that layer has a pitch: tune it to the key of the track
  rather than leaving it wherever the sample fell.

**Then the duck**, on the bass channel's Pro-Q 4, keyed from the kick via the external
sidechain:

| Param | Value | Why |
|---|---|---|
| Band type | **Dynamic bell**, external sidechain from ch 1 | Only moves when the kick hits; bass is untouched in between |
| Frequency | **The kick's fundamental** — sweep 45–70 Hz with the kick soloed | Guessing wastes the move. It is wherever that kick sample actually sits |
| Q | **1.0–1.5** | Wide enough to catch the fundamental, narrow enough to leave the rest of the bass |
| Range | **−2 to −4 dB** | Past −6 dB it stops being invisible and starts pumping |
| Second band | *Often needed* — **90–140 Hz, static −1 dB** | Where the bass's body masks the kick's punch. Static beats dynamic here |

**Known limitation:** Pro-Q's dynamic bands are program-dependent — threshold and range are
yours, attack and release are automatic and not exposed. If the duck sounds late or smeared,
that is the plugin, not the settings, and a dedicated sidechain compressor is the tool.

### The parallel drum blend

Ch 1-3 dry and ch 19/20 crushed arrive as separate files, so the blend is rebuilt here — from
scratch, since the ratio was in the faders and the faders were not recorded. **Start by
matching the pass-1 stereo master by ear**; that file is the only surviving record of the
blend that was actually heard.

The **Waves SSL E-Channel** on the ch 19/20 return is the better tool than Pro-Q for this —
carve the parallel copy rather than re-mix the drums. Black knob, not brown: this is a channel,
and it is meant to bite.

| Move | Setting | Why |
|---|---|---|
| Filters | **HPF 100 Hz** | Stops the crushed copy doubling the kick's low end into mush. The dry kick keeps the weight |
| HF | **Shelf, 8 kHz, +2 dB** | Brings up room and snare tail — the part worth blending in |
| LMF | **400 Hz, Q 1.0, −2 dB** | Where boxiness accumulates first in a parallel copy |
| Dynamics | **Off** | The DBX already compressed this. Twice is mud |

Bigger moves are fine here than anywhere else in the template — a parallel copy is meant to be
carved, not flattered. If ch 19/20 up makes the drums *thinner* rather than fatter, the return
is polarity-flipped; fix that at the desk before trying to EQ around it.

### The submix

One Pro-Q instance owning a collective problem — the place for the frequency that is wrong
across a whole group rather than on one channel.

The rule that keeps it useful: **one plugin owns each problem.** If 300 Hz is being cut on four
channels *and* on the submix, one of those decisions is wrong. Fix it where the problem is —
per-channel if one source causes it, on the submix if it only exists once things are summed.

Gentle moves. Anything past a dB or two here is a mix problem wearing an EQ costume.

**Nothing else belongs here.** Not bus compression — that already happened, in hardware, as the
DBX on subgroup 1/2 returning parallel on ch 19/20, and doing it again in the box is
compressing twice. Not saturation — the analog-coloring section rules it out, with the single
level-matched instance above as the only exception. And not a safety limiter; see
[Monitor protection](#monitor-protection) for why that one has to stay out of the signal path
entirely.

The submix's other job is not an effect at all: it is the **level checkpoint**. The bounce has
to leave the mix peaking **−10 to −6 dBFS** for the mastering session. That is a fader, not a
plugin.

### The delay bus

For the chopped samples, to fill space that a mono, mostly-dry record leaves open.

| Param | Setting | Why |
|---|---|---|
| Time | **1/8 dotted**, or **1/4 triplet** against the swing | The dotted eighth is the classic; triplets sit better under heavy swing |
| Short option | **80–140 ms slap**, no tempo sync | For snare and one-shot chops — depth without a rhythmic figure |
| Return HPF | **300–500 Hz** | Keeps repeats out of the kick and bass. The single most important setting here |
| Return LPF | **3–6 kHz** | Dulls the repeats so they sit behind the dry — and hides 12-bit hash in the tails |
| Feedback | **15–25 %** | Enough for two or three audible repeats |
| Send | **Post-fader** | So the delay follows the balance being rebuilt, rather than drifting off it |

**Duck the delay under the dry.** A dynamic band or a compressor on the return, keyed from the
send, keeps the repeats out of the way while the chop is playing and lets them bloom in the
gaps. Without it the delay is just mud with a rhythm.

**This is the width.** Every MPC out is mono and lands centre, so a stereo or ping-pong delay
return is one of the very few genuine width tools on the record — the same argument as the
side-channel air band on the master. Keep the low end out of it (that is what the HPF is for)
and the mono fold-down stays safe.

---

## Monitor protection

A safety limiter is worth having, and **the one place it must not go is the signal path.**

- **Not on the submix.** It would print into the bounce, and it only sees what is routed
  through it. A limiter there is a mix decision wearing protection's clothes.
- **Not on the master fader.** Master FX are included in a render — in Reaper by default, and
  in Pro Tools a master fader insert is in the bounce path too. That ships a limited mix into
  the mastering session invisibly, which is exactly the "fix it at the master" move the
  separate-session rule exists to prevent.
- **On Reaper's Monitoring FX chain** (View → Monitoring FX). It sits after the master, feeds
  the hardware output only, and is not part of an offline render. This is what it is for, and
  Pro Tools has no equivalent — so it is a genuine point in Reaper's favour, listed as test 10
  in [reaper_evaluation.md](reaper_evaluation.md) rather than assumed.

| Slot | Setting | Why |
|---|---|---|
| 1 — subsonic filter | **HPF 20 Hz** | DC offset and subsonic thumps kill woofers more reliably than loud music does. Ahead of the limiter, so it is not what the limiter is reacting to |
| 2 — limiter | **ReaLimit** or Pro-L 2, ceiling **−6 dBFS**, no gain | Mixes bounce at −10 to −6 dBFS peak, so this never engages during normal work — but the full-scale accident is ~10 dB louder, and it catches that |

**If it shows gain reduction while you are just mixing, the ceiling is wrong**, not the mix.
The meter resting at 0 is the whole point; a safety limiter that works every day is a
compressor nobody decided to use.

### What this does not cover

The loudest events in this room never pass through the DAW, so the monitoring chain does
nothing for any of them:

- the **ch 21/22 feedback loop** — the most dangerous thing in the setup, and it is analog, at
  the desk master
- needle drops and cueing the Technics into the Ecler
- patching a jack with a channel up, an MPC pad at full, an S950 glitch

Protection for those lives after the Tascam monitor out. Before buying anything for it, check
the two things that may already handle it: whether the monitors have their own protection
limiter, and whether the Tascam's monitor section gives a mute that can be hit by reflex. The
DBX 266XL's PeakStopPlus would do the job well, but it is committed to drum glue on subgroup
1/2 and moving it there costs the parallel blend.

---

## Recall

The **MPC project is the archive, not the mixer.** The saved sequence, samples, program and
out-routing reload to identical 8-out audio, so the multitrack is always re-recordable. Only
the analog pass is unrecallable — fader balance, EQ curves, SPL and DBX knob positions — and
the fader balance is not even in the multitrack.

So: **save every MPC project and its samples religiously.** If a re-track is ever likely,
photograph the desk and the outboard front panels before tearing the session down. That photo
is the only session recall a hardware mix has.

The Pro Tools session recalls itself, but only for the half of the mix that happened in the
box. That is the case for capturing the multitrack every time: the stems carry the analog tone
in a form that needs no photograph and no rebuild, and the fader balance — the one thing
neither the stems nor the MPC project hold — is the thing the Pro Tools session is for.

---

## Checklist

1. Trim set for ≈ −10 dBFS per channel **before** balancing with faders.
2. Both passes armed — stereo master **and** multitrack — with ch 21/22 muted for both.
3. Polarity test on the bass before reaching for the duck.
4. Sub-60 Hz kick layer tuned to the key of the track.
5. Analog coloring off, unless a level-matched all-on/all-off test on the full mix says otherwise.
6. Parallel drum blend rebuilt against the pass-1 stereo master, and the ch 19/20 return
   checked for polarity.
7. Delay return high-passed and ducked.
8. One plugin owns each problem — no frequency fixed twice.
9. Safety limiter in the monitoring chain, not on the submix or the master — and showing no
   gain reduction during normal work.
10. Mono check before bouncing. Everything is mono at source; the delay return and the XT:C are
   the only things that can thin out on fold-down.
