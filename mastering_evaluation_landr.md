# Mastering evaluation — LANDR Standard, LANDR Pro, or the manual Reaper chain?

**Status: evaluating.** Nothing decided, nothing subscribed. This file is the test plan; the
verdict goes at the bottom once the tests are run.

The chain being compared against is in [manual_mastering_reaper.md](manual_mastering_reaper.md),
running in the project layout from [reaper_mastering_session.md](reaper_mastering_session.md).

**Two things frame the whole question, and they are not what they look like:**

1. These beats do not need a perfect master. A professional masters the real release. What is
   needed is a deliverable that survives YouTube Shorts and impresses a rapper.
2. There is no mastering experience here yet, which is a real constraint and should be treated
   as one rather than wished away.

---

## First: there is no YouTube limiter

This is the premise worth correcting before spending anything, because it changes what the
evaluation is even for.

**YouTube normalises with a gain change, not a limiter.** Upload something at −7 LUFS and the
player turns it down by about 7 dB at playback. Nothing is re-limited, nothing is re-compressed,
no processing is applied to the audio. Upload something at −20 LUFS and it is *not* turned up —
it just plays quiet.

**The target is ≈ −14 LUFS integrated, and Shorts uses the same target as the rest of YouTube.**

So the loudness war is unwinnable by design:

| Upload at | What plays | What survives |
|---|---|---|
| −14 LUFS | −14 LUFS | Everything |
| **−12 LUFS** *(the target here)* | −14 LUFS (turned down 2 dB) | Everything. 2 dB of limiting, which is about what the chain does anyway |
| −11 LUFS | −14 LUFS (turned down 3 dB) | Everything, 3 dB of limiting included |
| −7 LUFS | −14 LUFS (turned down 7 dB) | The distortion. Nothing sounds louder, the transients are just gone |

**The damage people blame on the platform is almost always their own limiter**, baked in before
upload, permanent, and then turned down anyway. The one thing the platform genuinely does to the
audio is transcode it to a lossy codec, and that is what **−1.0 dBTP** protects against —
overshoot on encode is real, and it is the only true-peak risk here.

**What this means for the money question:** at a −12 LUFS target a limiter on this material is
doing roughly **1–2 dB of work**. That is not a hard job for any limiter. Buying Pro-L 2 to be loud on
Shorts is buying the wrong tool for a problem that does not exist. If FabFilter money gets spent
later it should go to **Pro-MB** instead — it expands as well as compresses, which nothing in the
setup currently does — and it should be argued on that capability, not on loudness.

### What the targets become

| Deliverable | Integrated | True peak | Why |
|---|---|---|---|
| **YouTube Shorts** | **−12 LUFS** | **−1.0 dBTP** | Two dB above the normalisation target, so it plays ~2 dB down — deliberate headroom in hand for everywhere that does *not* normalise, at no cost where it does |
| Rapper reference | −12 LUFS | −1.0 dBTP | Loud enough to feel finished on a phone. Past this is vanity |
| **Archive / handoff to the pro** | **No limiting.** 24-bit WAV | — | The mastering engineer wants headroom, not a finished master to undo |

**Keep the archive separate from the Shorts version.** Rendering one loud file and sending that
to a professional later is the single most expensive mistake available here, and it costs
nothing to avoid: render twice from the same project.

---

## The three options

| | LANDR Standard | LANDR Pro | Manual Reaper chain |
|---|---|---|---|
| Cost | ~$144/yr *(confirm)* | up to ~$190/yr *(confirm)* | **$0** — already owned |
| Model | Subscription | Subscription | One-time, already paid |
| WAV masters | Limited allowance (~36/yr) | Unlimited | Unlimited |
| MP3 masters | Unlimited | Unlimited | n/a |
| Experience needed | None | None | Some — but the doc supplies most of it |
| Time per beat | Minutes | Minutes | 30–60 min at first, less later |
| Recallable | No | No | Yes — it is an `.RPP` |
| Consistent across beats | Very | Very | Only once there is a template and a habit |

*LANDR's pricing pages render in the browser and could not be read directly — confirm the
current numbers and the WAV allowance before committing to a tier.*

**Standard vs Pro is mostly a WAV-count question**, and that is the axis that matters least
here. If the professional masters everything that gets released, the LANDR output is a
disposable deliverable for Shorts and for sending a rapper something — and an MP3 is arguably
enough for both. **On the stated use case, Pro is hard to justify over Standard.**

---

## What each one is actually good at

### LANDR — good at consistency, bad at this record specifically

**The real argument for it:** no experience required, every beat comes back sounding
approximately the same, and it takes minutes. With no mastering experience, an automatic master
is very likely to beat a first manual attempt — and for a Shorts deliverable that nobody will
master-quality-check, "reliably fine" is worth more than "occasionally better."

**The real argument against it:** this record is *deliberately* dusty, dark and 12-bit, and
automatic mastering is built to normalise material toward a conventional target. It brightens,
it evens out, it de-emphasises the things that read as flaws. The whole architecture here exists
to commit character on the way in — an AI master is the one stage that can quietly undo it,
because it cannot tell a deliberate roll-off from a mistake.

**The subscription is also the thing just deliberately escaped.** Pro Tools was dropped partly
to stop renting the studio. A mastering subscription re-introduces exactly that, for a stage the
docs already describe as the least important of the three.

### The manual chain — good at this record, slower to trust

**The chain already exists**, with exact values, written around this material. Most of it is
already owned, and the chain has since been cut to exactly that: **Pro-Q 4 → TAIP → ReaLimit**,
with Youlean on the master. Three plugins and maybe eight decisions between them.

**The inexperience problem is real but already addressed.** The things that substitute for
experience are all in [reaper_mastering_session.md](reaper_mastering_session.md): a gain-matched
commercial reference in the project, a fixed monitor level, level-matched bypass A/B, moves
under a dB, and sleeping on it. Those are not advanced techniques — they are the discipline that
makes a beginner's master come out fine.

**The honest risk:** with no experience, an unfamiliar chain can make things worse, and the
feedback loop is slow because the mistakes are subtle. This is the one place where an automatic
master has a genuine advantage.

---

## The third option nobody asks for: use LANDR without paying

**LANDR's free tier masters to MP3 at no cost.** That is not good enough to be the deliverable,
but it is an excellent **reference** — run a beat through it, then A/B the free LANDR master
against the manual one, gain-matched, and the gap is visible immediately.

This is worth doing regardless of which way the decision goes. A reference is the thing
inexperience is actually short of, and this one is free and made from the exact same source
file.

---

## The test

One beat, three masters, blind, level-matched. Do it on a beat that is finished and familiar.

| # | Test | Pass criteria |
|---|---|---|
| 1 | **Render the source** | One 24-bit stereo mix at −10 to −6 dBFS peak, no limiting. This same file feeds all three |
| 2 | **LANDR free MP3 master** | Costs nothing. Note which style/intensity was used |
| 3 | **Manual chain** | Pro-Q 4 → TAIP → ReaLimit to −12 LUFS / −1.0 dBTP |
| 4 | **Normalise all three to −14 LUFS** | Non-negotiable. Louder always wins an unmatched comparison, which is how people talk themselves into subscriptions |
| 5 | **Blind A/B on a phone speaker** | This is Shorts. A phone is the honest monitor, not the A7Vs |
| 6 | **Then A/B on the A7Vs** | Where the character question shows up — is the dust still there, or did something tidy it away? |
| 7 | **Upload one Short of each** | The only way to see what the platform actually does. Check YouTube's "stats for nerds" content-loudness readout |
| 8 | **Repeat on a second, different beat** | One beat proves nothing. A dark beat and a bright one behave differently through an automatic master |

### Decide these before listening

So the result is not rationalised afterwards:

- **If the manual master is indistinguishable from LANDR on a phone** — the subscription buys
  nothing for the stated use case. Manual wins by cost, by recall, and by not renting anything.
- **If LANDR is clearly better and the manual one sounds amateur** — subscribe to **Standard**,
  and keep the manual chain for the 24-bit archive that goes to the professional. Revisit after
  ten beats, when there is more experience to compare against.
- **If LANDR sounds louder but thinner, or brighter than intended** — that is the architecture
  being undone, and it is a no regardless of convenience.
- **If the manual chain takes so long that beats stop getting finished** — that is a real failure
  and it beats any audio argument. The point is to make beats, not to master them.
- **Pro over Standard only if** the WAV allowance is actually hit in practice. It will not be,
  early on.

---

## Interim recommendation, before any of this is run

**Do not buy Pro-L 2 for this.** At a −12 LUFS target the limiter is doing 1–2 dB of work, which
ReaLimit does fine. That question is independent of the LANDR one and the answer is already no.

**Start manual, with the three-plugin chain, and use free LANDR as the reference.** It costs nothing,
it builds the experience that is currently missing, and it keeps the deliverable recallable. If
after ten beats the manual masters still sound wrong next to the free LANDR MP3, that is real
evidence for subscribing — and it will be evidence, not a guess.

**Whatever happens, render the 24-bit unlimited archive every time.** The professional master
later depends on it, and it is the one decision here that cannot be undone.

---

## Verdict

*To be filled in after the tests. Record the date, which beats were tested, and the decision.*
