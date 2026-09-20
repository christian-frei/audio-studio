# DBX 266XL Reference — parallel drum glue

Quick reference for the DBX 266XL compressor/gate in its current role: **parallel drum bus
compression**. Kick, snare and hi-hat (Tascam ch 1-3) feed subgroup 1/2, the subgroup feeds the
266XL, and the compressor returns to the desk on **ch 19/20**, blended underneath the dry
channels to fatten them.

```
Tascam ch 1 (kick)   ┐
Tascam ch 2 (snare)  ├─> subgroup 1/2 ─> DBX 266XL ─> Tascam ch 19/20 ─> stereo master
Tascam ch 3 (hi-hat) ┘        (dry channels 1-3 also go straight to the master)
```

**The dry drums are never replaced — the compressed copy is added underneath.** That single
fact inverts most of the usual compressor advice, see below.


## Compressor Controls

| Knob | What it does | Range |
|------|-------------|-------|
| **Threshold** | Level above which compression starts | -40dB to +20dB |
| **Ratio** | How much signal gets squashed above threshold | 1:1 (off) to ∞:1 (limiter) |
| **Attack** | How fast compressor clamps down after threshold is crossed | Fast to Slow |
| **Release** | How fast compressor lets go after signal drops below threshold | Fast to Slow |
| **Output Gain** | Make-up gain to restore volume lost to compression | -20dB to +20dB |
| **OverEasy** | Soft knee (on) vs hard knee (off) | Button |
| **Auto** | Overrides attack/release with program-dependent auto values | Button |
| **Stereo Couple** | Ch 1 controls both channels, ch 2 follows | Button |


## Compressor — How the Knobs Interact

Think of it as a sequence:

1. Signal comes in and hits the **threshold** — everything above this line gets compressed
2. **Ratio** determines how hard it gets compressed (4:1 means 4dB over threshold becomes 1dB over)
3. **Attack** controls how fast that compression kicks in — slow attack lets the initial hit punch through
4. **Release** controls how fast compression stops after the signal drops back down
5. **Output gain** brings the overall level back up since compression made things quieter

The gain reduction meter on the front panel shows you how many dB are being removed in real time. Watch it while you tweak.


## Starting Settings — parallel drum bus (current setup)

Goal: a crushed, dense copy of the drums sitting under the dry ones — weight and room, not punch.

| Control | Setting | Why |
|---------|---------|-----|
| **Stereo Couple** | **ON** (ch 1 master, ch 2 follows) | Both sides duck together; the drum image stays centered instead of wandering |
| OverEasy | **OFF** | Hard knee — in parallel you want it to grab decisively |
| Auto | **OFF** | Manual control |
| Threshold | Low — **10 to 20 dB gain reduction** on hits | This is meant to be obviously squashed. Watch the meter, not the knob |
| Ratio | **8:1** (up to ∞:1) | Heavy. The dry channels are carrying the dynamics |
| Attack | **FAST** | The inversion: clamp the transient, let the *body and tail* come up. The dry channels already supply the attack |
| Release | **Fast to medium** — recovered before the next 8th note | The pump-back-up between hits *is* the effect. Too slow and the drums stay flat |
| Output Gain | Enough that ch 19/20 faders sit in a usable range | |

**Blending it in:** start with ch 19/20 all the way down. Raise until the drums thicken, then
pull back about 2 dB — the point where you notice it disappearing when muted, not the point
where you notice it when unmuted. Typically the return sits well below the dry channels.

**Check polarity first.** If raising ch 19/20 makes the drums thinner or hollower instead of
fatter, the return is out of phase with the dry channels. Nothing else here matters until that
is right.


## Why fast attack now, when slow attack was right before

When the 266XL was inserted directly on a kick channel, a **slow** attack was correct: the
transient had to survive, because the compressed signal was the only signal.

In parallel it is the opposite. The dry ch 1-3 already deliver every transient at full
strength. The compressed copy's job is to supply what the dry signal lacks — sustain, body,
the tail of the snare, the space between hits. A fast attack flattens the peaks and lifts
everything underneath them, which is exactly the material worth blending in.

If the parallel return sounds clicky or brittle, the attack has gone too slow, not too fast.


## Ratio Cheat Sheet

- **1:1** — No compression (bypassed)
- **2:1** — Gentle, subtle leveling
- **3:1** — Moderate, good for snares on an insert
- **4:1** — Solid all-around drum compression on an insert
- **8:1** — Heavy, noticeable squash — the parallel zone
- **∞:1** — Limiter, nothing gets above the threshold


## Attack Cheat Sheet

- **Slow attack** = transient passes through uncompressed, then the body gets compressed.
  Result: PUNCH. Right for an **insert** on a single drum.
- **Medium attack** = some transient gets compressed. Balanced, slightly rounder.
- **Fast attack** = compressor clamps down immediately on the transient. The punch softens but
  the sound gets thicker and more even. Right for **parallel**, which is the current setup.


## If you ever insert it on a single drum again

Kept for reference — the old per-channel settings:

| Control | Kick | Snare |
|---------|------|-------|
| OverEasy | OFF | OFF |
| Auto | OFF | OFF |
| Threshold | for 3-6 dB GR | for 3-6 dB GR |
| Ratio | 4:1 | 3:1 to 4:1 |
| Attack | Slow | Medium-slow (snare transients are shorter) |
| Release | Medium-fast | Medium |
| Output Gain | match bypassed level | match bypassed level |


## Gate/Expander Section

### Why It's Called "Expansion" and Not Just "Gating"

**Compression** reduces dynamic range — it makes loud and quiet closer together by pushing loud things down.

**Expansion** is the opposite — it increases dynamic range by pushing quiet things further down. When a signal drops below the threshold, the expander makes it even quieter than it already was. It "expands" the gap between your wanted signal (the drum hit) and the unwanted quiet stuff (noise, bleed, hum).

A **gate** is just extreme expansion. When the expansion ratio is cranked high enough, quiet signals don't just get turned down a bit — they get slammed to silence.

So on the 266XL:

- **Low gate ratio** = gentle downward expansion (quiet stuff gets a bit quieter)
- **High gate ratio** = hard gate (quiet stuff gets silenced)

### Gate/Expander Controls

| Knob | What it does |
|------|-------------|
| **Threshold** | Level below which expansion/gating kicks in. Fully counterclockwise = OFF (bypassed) |
| **Ratio** | How aggressively quiet signals get attenuated. Low = expansion, High = gate |

### Do You Need the Gate?

Normally no — the MPC individual outs are clean, with no mic bleed to clean up. But in the
**parallel** role it has one genuine use: heavy compression lifts the noise floor between hits
along with everything else. If the blended return brings up audible hiss or sampler noise in
the gaps, a gentle downward expansion (low ratio, threshold just under the quietest hit you
want to keep) pushes it back down.

Raise the threshold slowly and stop the moment drum tails start getting clipped. If the
expander is audibly chattering, it is doing more harm than the noise was.


## Learning Exercises

### Exercise 1: Hear what parallel actually does

Play a drum loop from the MPC with ch 19/20 down.

1. Solo ch 19/20 alone — it should sound crushed, flat, ugly, and *loud in the tails*. That's correct
2. Unsolo, then raise ch 19/20 slowly under the dry drums
3. Mute and unmute the return repeatedly — the drums should get smaller when muted

### Exercise 2: Hear what attack does in parallel

Same loop, return blended in.

1. Set attack to **slowest** — listen for the clicky, brittle edge
2. Turn toward **fastest** — the body and tails come up, the clicks go away
3. This is the opposite of what the insert version taught. Hear it once and it sticks

### Exercise 3: Hear what release does

Set attack fast, ratio 8:1, threshold for heavy gain reduction.

1. Release **slowest** — the drums stay flat and lifeless, no recovery between hits
2. Turn toward **fastest** — hear the level breathing back up between hits
3. Find the point where it recovers just before the next hit lands. That's tempo-dependent — recheck it on every beat

### Exercise 4: Find the blend point

1. Raise ch 19/20 until it is clearly audible as a separate thing — too far
2. Back off until it stops being separately audible
3. Back off 2 dB more
4. Mute/unmute. If nothing is lost on mute, you went too far

### Exercise 5: Understand the gate

1. Turn gate ratio **low**
2. Slowly raise gate threshold from OFF
3. Listen to the noise between hits drop away
4. Keep going and drum tails start getting cut — back off before that point
