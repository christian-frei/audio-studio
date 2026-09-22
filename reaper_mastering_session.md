# The mastering project — separate from the tracking template

**The mastering chain does not live in the MPC-recording template.** It lives in its own Reaper
project holding one imported stereo file and nothing else. The tracking template stays a
capture template.

Chain settings are in [manual_mastering_reaper.md](manual_mastering_reaper.md); this file is
only about *where* the chain runs. Routing is in [CLAUDE.md](CLAUDE.md).

---

## Why separate

**Because otherwise you stop hearing the mix.** With the chain on the tracking template's
master track, every balance decision made on the Tascam is auditioned through 2–3 dB of
multiband, a tape stage and a limiter pulling everything to −11 LUFS. The compensation happens
without noticing — the kick gets mixed softer because the limiter already makes it feel big,
the top stays dull because the SSL shelf is adding air. Bypass the chain later and the mix
underneath is thin and wrong.

One stage, one project, one job. The tone belongs to the desk, the balance to the multitrack
project, the master to a project whose only job is the master — and none of the three should be
auditioned through the next one's processing.

**Being a beatmaker rather than a mastering engineer argues for the split, not against it.** One
stereo track, one chain, one meter, one reference is the simpler thing to learn — and with the
multitrack open in its own project, the temptation to "fix it at the master" has somewhere
better to go.

It is also the clean handoff: when a beat gets picked up, the deliverable already exists as a
discrete stereo file at a known level with no chain baked in.

---

## The file comes for free

No extra bounce step — **pass 1 of the two-pass capture already is the render.** That 24-bit
Tascam stereo master is what this project imports for a quick master; when the beat went
through the multitrack mix, it is that project's stereo render instead. Either way a single
stereo file arrives here — the pass-2 multitrack never enters this project.

Match the project's sample rate and bit depth to the capture; no sample-rate conversion on the
way in. Any conversion happens once, at the final render.

---

## Session layout

```
[ beat.wav ]  ──send──>  [ CHAIN track ]  ──>  master  ──>  [ MASTER: meter only ]
                                                   ^
[ reference.wav ] ─────────────────────────────────┘   (straight to master, bypasses the chain)
```

| Element | Setting | Why |
|---|---|---|
| Track — the beat | Fader at **unity**, no FX. **Master/parent send OFF**, one send → the CHAIN track | All level work happens in the chain, so the −10 to −6 dBFS render stays the reference point |
| Track — **the chain** | Receives the beat. Plugins in slot order in its FX chain | Bypasses and level-matches as a unit, and leaves the master clean for the reference |
| Track — **a commercial reference** | Straight to the master, never through the chain | One fader flip A/Bs against a record that works |
| Master track | **Metering only** — Pro-L 2's meters, or Youlean until then. No processing | LUFS / true peak / PLR on whatever is playing |

**Turning the beat track's master send off is the step that matters.** Leave it on and the beat
reaches the master twice — once dry, once through the chain — which sounds like a phasey,
slightly louder version of the right answer and is easy to miss.

**The reference track is the highest-value thing in the project**, and it is what this routing
exists to protect: anything on the master processes everything on the path, reference included,
which makes the comparison meaningless. Gain-match the reference before trusting it — louder
always wins otherwise.

---

## Working order

1. Import the pass-1 stereo capture, fader at unity.
2. Import and gain-match a reference that sounds like the target.
3. Set the monitor level on the Tascam and **leave it there**. A fixed, moderate listening level
   decides more than any plugin in the chain.
4. Start with the short chain (Pro-Q 4 → SSL E-Channel → Pro-L 2); add stages only when a
   specific problem asks for one.
5. Level-matched bypass A/B of the whole chain track, repeatedly.
6. Render. 24-bit WAV is the archive master.

**Do it on a different day from the mixdown if possible.** Fresh ears are the only mastering
gear that cannot be bought, and the separate session is what makes coming back tomorrow cheap.

**Monitoring:** mastering playback returns on **ch 21/22** like everything else out of the Mac.
That is fine here — nothing is being captured, so the feedback-loop trap does not apply. It
applies to pass 1 and pass 2, where 21/22 must be muted. Do not leave them muted while trying
to hear the master.

---

## What does not belong here

- **The multitrack.** It has its own project — see
  [manual_mixing_tascam_reaper.md](manual_mixing_tascam_reaper.md).
- **Moves bigger than about a dB.** Those are mix moves. A balance problem goes to the
  multitrack project; a tonal one goes back to the desk, which means re-tracking — cheap,
  because the MPC project reloads to identical 8-out audio.
- **The parallel drum blend.** Rebuilt in the multitrack project, not here.

---

## The one legitimate hybrid — the limiter spot-check

A **single limiter at the target loudness, bypassed by default**, may live on the tracking
template — ReaLimit is fine for this, it is not a mastering decision — answering only *"will this survive being made loud?"* — flip it in, listen ten
seconds, flip it out.

One plugin, never the full chain. Bypassed by default. Never render through it. If it reveals a
problem, the fix goes on the Tascam. If it starts getting left on while mixing, take it out of
the template — the point of the split is that the desk gets heard as it is.
