# Reaper evaluation — can it replace Pro Tools Studio?

**Status: evaluating.** Nothing decided, nothing migrated. This file is the test plan and the
inventory; the verdict goes at the bottom once the tests are run.

Current stack: Pro Tools Studio, ~200 CHF/year. See
[manual_mixing_tascam_protools.md](manual_mixing_tascam_protools.md) and
[manual_mastering_protools_studio.md](manual_mastering_protools_studio.md) for what the DAW
actually has to do.

---

## Why this is on the table

Pro Tools **Artist** is not an option: it caps at 16 simultaneous inputs, and the capture is
17-19 channels (8 MPC outs, ch 10 S950, the active MPC's stereo pair, 15/16 Ecler, 17/18 XT:C,
19/20 DBX). All six subgroups are already committed — 1/2 to the DBX, 3/4 and 5/6 to the MPC
sample-sends — so there is no spare bus to fold channels into, and folding would commit a
balance, which is exactly what the pre-fader capture exists to avoid.

So the real choice is **Studio at 200 CHF/year, forever** versus a DAW without a track-count
tier. Input count gated by price is a Pro Tools peculiarity, not an industry norm.

### The cost picture

Reaper is **$60 (~54 CHF)**, one-time, non-subscription. A licence covers the current major
version *and the next one* — buy during v7 and it runs through 8.99. Majors land roughly every
four years, so that is realistically ~5 years before being asked again, and nothing stops
working when a newer major arrives. The $60 personal tier is legitimate under $20k/year gross.

| | 5-year cost | Own it after? |
|---|---|---|
| Pro Tools Studio | **~1000 CHF** | No — sessions stop opening |
| Reaper, free plugins only | **~54 CHF** | Yes |
| Reaper + Pro-L 2 + Pro-C 2 | **~350 CHF** | Yes, and DAW-agnostic |

*Verify current Reaper version and FabFilter prices before committing — FabFilter gives credit
for owned licences when buying a bundle, so owning Pro-Q 4 should reduce the other two.*

---

## Plugin inventory — what maps to what

Everything below is cross-format (VST3/AU), so none of it is tied to Pro Tools. **No AAX-only
plugins are in use**, which is the thing that would otherwise block a move outright.

### The tone-shaping template — the stage that is easy to forget

| Tool | Role | Reaper |
|---|---|---|
| **Serato Sample** | Chopping drum breaks that live on the hard disk | VST3/AU — hosts fine, *verify* |
| **Subfactory** | Sub-bass generation — played and sampled, never mixed | VST3/AU — *verify* |

Neither of these is ever used directly in a mix. They live in one **tone-shaping template** that
is opened at the very start of a project, used to play material out to the S950 or an MPC, and
then closed. **Those projects are never saved.** The DAW is only a vehicle for holding an
instrumental VST and playing it — nothing it makes stays in the DAW, everything it makes ends up
as a sample on hardware, which is what the archive rule already assumes.

That narrows what Reaper has to prove here to two things: the plugins load and authorise, and
the output reaches ch 21/22. No session recall, no automation, no mix state, no plugin delay
compensation — there is no session to lose. Rebuilding a template that is never saved is a
one-time cost, so this stage is the cheapest part of a DAW switch rather than the riskiest.

**Routing note.** The chopped output reaches the S950 the long way round: Serato Sample → Mac
out → **Tascam ch 21/22** → **aux 1** → S950 → Vermona → ch 10 → subgroup 3/4 or 5/6 → MPC.
Ch 21/22 must be **up** for this, which is the opposite of the capture rule — during a USB
capture those channels are muted to avoid the feedback loop. Two different states for the same
channels, so it is worth being deliberate about which one the desk is in.

### Mixing template

| Slot | Plugin | Status |
|---|---|---|
| Per-channel surgical EQ | **FabFilter Pro-Q 4** | Owned |
| Kick/bass dynamic duck | **Pro-Q 4**, dynamic band + external sidechain | Owned — *routing is the known friction, see tests* |
| ch 19/20 parallel drum blend | **Waves SSL E-Channel** | Owned |
| Submix | **Pro-Q 4** | Owned |
| Delay bus | **ReaDelay** (stock) — tempo-sync, feedback, per-tap HP/LP | Free — *verify the filters* |
| Delay ducking | ReaComp sidechained from the send | Free — same routing friction |

One owned plugin needs a decision rather than a slot:

- **NI transient shaper** — duplicates the SPL Transient Designer, which is already printed on
  ch 1-3 and ch 10 on the way in. Using it again in the box means shaping transients twice.
  Keep it for the parallel drum return or a sample that needs rescuing, not as a default.

**Subfactory is not in this template.** It belongs to the tone-shaping stage above: the
sub-60 Hz layer is played there, sampled into the MPC, and from then on it is part of the beat
and part of the archive. It never appears as a channel in a mixing session — a sub generated at
mix time would be a *tonal* decision made in the mixing stage, which is exactly what the
division of labour rules out.

### Mastering chain

| Slot | Pro Tools | Replacement | Cost |
|---|---|---|---|
| 1 — corrective EQ | Pro-Q 4 | **Pro-Q 4** | Owned |
| 2 — multiband | Pro Multiband Dynamics | **ReaXComp** — numeric per-band attack/release, adjustable crossovers | Free |
| 3 — console colour | SSL E-Channel | **SSL E-Channel** | Owned |
| 4 — tape | Reel Tape Saturation | **TAIP** | Owned |
| 5 — bus glue | Pro Compressor | **Pro-C 2**, or **TDR Kotelnikov** free | ~140 CHF / 0 |
| 6 — limiter | Pro Limiter | **Pro-L 2**, or **ReaLimit** free | ~160 CHF / 0 |

Three caveats on the substitutions:

**ReaXComp compresses but does not expand.** The optional band-4 downward expander (−55 dBFS,
1.5:1) has no direct equivalent — it would need ReaGate on a split band, or simply skipping it.
The doc already marks it optional and the trade was always "noise is more forgivable than a
breathing tail", so skipping is fine.

**TAIP has no IPS switch.** The slot-4 spec is written in Reel Tape's language — 15 IPS, tape
formulation, calibration into the red. TAIP's controls are different, so that section would
need rewriting in TAIP's terms after a level-matched A/B. No reason to buy another tape plugin
for this; **ChowTape is free** and does have a real IPS control if the head-bump behaviour turns
out to matter.

**Pro-L 2 would replace the metering too** — it has LUFS, true peak and PLR built in, which is
what the Pro Tools master fader was providing. That is the strongest argument for buying it
over ReaLimit.

### Metering

Losing the Pro Tools master fader's loudness modes is a real gap — the targets (−11 LUFS,
−1.0 dBTP, PLR 8-10) are unusable without a meter.

- **Youlean Loudness Meter 2** (free) — LUFS-M/S/I, true peak, history. The default pick.
- **Voxengo SPAN** (free) — spectrum, separate job from loudness. Worth having alongside.
- **Reaper's own loudness tools** — the master meter can display LUFS and there is a loudness
  calculation action. *Verify whether this is enough on its own.*
- **Pro-L 2** — makes all of the above optional if bought.

---

## What actually has to be bought: nothing

Every slot has a free or owned answer. Pro-L 2 and Pro-C 2 are quality-of-life, not gaps — and
Pro-L 2 is the better of the two to buy first, because it covers the limiter *and* the
metering. Pro-C 2 is the weakest case: Kotelnikov is free and has the sidechain high-pass that
slot 5 calls the most important setting.

So the honest minimum to evaluate properly is **$60**, using free plugins everywhere, and
decide on FabFilter afterwards from experience rather than in advance.

---

## What Reaper must prove

Run these against a real project, not a toy one. Reaper's trial is fully functional and does
not expire, so all of this can happen before paying.

| # | Test | Pass criteria |
|---|---|---|
| 1 | **Arm and record 20+ Tascam inputs** | All channels arm, input numbers match the channel map, a 3-minute take records with no dropouts on the M4 |
| 2 | **Kick → bass sidechain into Pro-Q 4** | The duck works. Reaper routes sidechain via channels 3/4 and the plugin pin matrix, which is genuinely fiddlier than Pro Tools — the test is whether it can be *saved into a template* so it is set up once, not per project |
| 3 | **Project template reload** | Save the 22-channel template, close, reopen: inputs, plugins, folder/bus routing and sidechain all return intact |
| 4 | **Plugin formats** | Pro-Q 4, SSL E-Channel, TAIP, NI transient shaper, **Serato Sample**, **Subfactory** all load and authorise |
| 5 | **Tone-shaping template → S950 path** | Chop a break (or play a sub), route out to ch 21/22, into aux 1, sampled by the S950 or an MPC — the sampling loop still closes. Session recall is irrelevant here; the project is thrown away |
| 6 | **Mastering topology** | Beat → chain bus → master, reference track → master *directly*, master metering only. The reference must audibly bypass the chain |
| 7 | **Input monitoring off** | Confirmable and default-off, so the ch 21/22 feedback trap stays avoidable |
| 8 | **CPU under load** | 22 tracks each with Pro-Q 4, plus the SSL and the delay bus, on the Mac Studio M4 |
| 9 | **Export** | 24-bit WAV archive master; 16-bit with dither when needed |

### Known friction, expected

**Sidechain routing is the one thing that is clearly worse than Pro Tools.** No dropdown — you
raise the destination track to 4 channels, send the kick to channels 3/4, then map them in the
plugin's pin connector. It works and it is stable, but it is several steps. Test 2 exists
because the whole question is whether it survives being saved into a template.

Everything else is learning curve rather than capability.

---

## What would send me back to Pro Tools

Decide these *before* running the tests, so the result is not rationalised afterwards:

- Test 1 or 5 fails — the capture or the sampling loop does not work. **Blocker.**
- Test 2 works but cannot be templated, so the duck has to be rebuilt every project. **Blocker**
  — that is a per-beat tax on the one move the mixing template exists for.
- Tests 3, 6, 7, 9 fail. **Blockers**, though all are unlikely.
- Test 8 struggles. **Not a blocker** — thin the per-channel Pro-Q instances, since the doc
  already says most channels should end up doing nothing.
- "It feels unfamiliar." **Not a blocker.** That is the price of the switch, and it is worth
  roughly 950 CHF over five years.

## What is lost either way

- Pro Tools muscle memory, and sessions that will not convert. There is no clean AAF path into
  Reaper — a migration means consolidating audio and rebuilding, not converting.
- Interchange with a studio that expects a Pro Tools session. Low risk here: the deliverables
  are a mastered stereo WAV or a WAV multitrack, both format-agnostic.
- **Nothing from the archive.** The MPC project plus its samples is the archive, and the
  multitrack is always re-recordable from it. That principle is what makes this switch low-risk
  at all — the thing a DAW change would endanger is exactly the thing that does not live in
  the DAW.

One point in Reaper's favour on the same principle: an `.RPP` project file is **plain text**,
readable and diffable in twenty years without the software that made it.

---

## Verdict

*To be filled in after the tests. Record the date, which tests failed, and the decision.*
