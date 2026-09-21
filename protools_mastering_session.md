# The mastering session — separate from the tracking template

**The mastering chain does not live in the MPC-recording template.** It lives in its own Pro
Tools session holding one imported stereo file and nothing else. The tracking template stays a
capture template.

Chain settings are in
[manual_mastering_protools_studio.md](manual_mastering_protools_studio.md); this file is only
about *where* the chain runs. Routing is in [CLAUDE.md](CLAUDE.md).

---

## Why separate

**Because otherwise you stop hearing the mix.** With the chain on the tracking template's
master fader, every balance decision made on the Tascam is auditioned through 2–3 dB of
multiband, a tape stage and a limiter pulling everything to −11 LUFS. The compensation happens
without noticing — the kick gets mixed softer because the limiter already makes it feel big,
the top stays dull because the SSL shelf is adding air. Bypass the chain later and the mix
underneath is thin and wrong.

Same rule as the daw-less one, a floor up: the mix belongs to the Tascam, the master belongs to
a session whose only job is the master.

**Being a beatmaker rather than a mastering engineer argues for the split, not against it.** One
stereo track, one chain, one meter, one reference is the simpler thing to learn. Staring at 20
channels of multitrack, the temptation to "fix it at the master" is constant — and that is the
one thing mastering cannot do.

It is also the clean handoff: when a beat gets picked up, the deliverable already exists as a
discrete stereo file at a known level with no chain baked in.

---

## The file comes for free

No extra bounce step — **pass 1 of the two-pass capture already is the render.** That 24-bit
Tascam stereo master is what this session imports. The pass-2 multitrack never enters it.

Match the session's sample rate and bit depth to the capture; no sample-rate conversion on the
way in. Any conversion happens once, at the final render.

---

## Session layout

```
[ beat.wav ]  ──bus──>  [ AUX: the chain ]  ──>  output  ──>  [ MASTER FADER: meter only ]
                                                    ^
[ reference.wav ] ──────────────────────────────────┘   (straight out, bypasses the chain)
```

| Element | Setting | Why |
|---|---|---|
| Stereo track — the beat | Fader at **unity**, no plugins. Output → a stereo bus | All level work happens in the chain, so the −10 to −6 dBFS capture stays the reference point |
| Stereo aux — **the chain** | Input = that bus. Plugins in slot order | Bypasses and level-matches as a unit, and leaves the output path clean for the reference |
| Stereo track — **a commercial reference** | Straight to the **output path**, bypassing the chain | One fader flip A/Bs against a record that works |
| Master fader | **Metering only** — loudness meter, no processing | LUFS / true peak / PLR on whatever is playing |

**The reference track is the highest-value thing in the session**, and it is what the aux
routing exists to protect: a master fader processes everything on the path, reference included,
which makes the comparison meaningless. Gain-match the reference before trusting it — louder
always wins otherwise.

---

## Working order

1. Import the pass-1 stereo capture, fader at unity.
2. Import and gain-match a reference that sounds like the target.
3. Set the monitor level on the Tascam and **leave it there**. A fixed, moderate listening level
   decides more than any plugin in the chain.
4. Start with the short chain (Pro-Q 4 → SSL E-Channel → Pro Limiter); add stages only when a
   specific problem asks for one.
5. Level-matched bypass A/B of the whole aux, repeatedly.
6. Render. 24-bit WAV is the archive master.

**Do it on a different day from the mixdown if possible.** Fresh ears are the only mastering
gear that cannot be bought, and the separate session is what makes coming back tomorrow cheap.

**Monitoring:** mastering playback returns on **ch 21/22** like everything else out of the Mac.
That is fine here — nothing is being captured, so the feedback-loop trap does not apply. It
applies to pass 1 and pass 2, where 21/22 must be muted. Do not leave them muted while trying
to hear the master.

---

## What does not belong here

- **The multitrack.** It is pre-fader, level-normalised and holds no balance — an archive, not
  a mixing environment. It stays with the tracking template.
- **Moves bigger than about a dB.** Those are mix moves; they belong on the Tascam, which means
  re-tracking — cheap, because the MPC project reloads to identical 8-out audio.
- **The parallel drum blend.** Adjustable after the fact, but in the multitrack session.

---

## The one legitimate hybrid — the limiter spot-check

A **single Pro Limiter at the target loudness, bypassed by default**, may live on the tracking
template, answering only *"will this survive being made loud?"* — flip it in, listen ten
seconds, flip it out.

One plugin, never the full chain. Bypassed by default. Never render through it. If it reveals a
problem, the fix goes on the Tascam. If it starts getting left on while mixing, take it out of
the template — the point of the split is that the desk gets heard as it is.
