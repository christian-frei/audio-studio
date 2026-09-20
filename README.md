# Boombap Sampling Home Studio

Hardware-first home studio for making boombap hip-hop beats. Vinyl sampling through Akai MPCs,
mixed daw-less on a Tascam Model 2400, mastered in Pro Tools Studio.

## Workflow

1. Sample from vinyl (Technics MK7 → Ecler Nuo2 → Tascam), into the MPC directly or via the Akai S950
2. Build the beat on one MPC per project (MPC2500 or MPC2000 — never both)
3. Track the 8 individual MPC outs through the Palmer Pan 16 into Tascam ch 1-8
4. Mix on the Tascam — **daw-less**: EQ, balance and summing all on the desk
5. Capture over USB **post-FX**, so the desk EQ prints: stereo master every time, multitrack when a beat gets picked up
6. Master in Pro Tools Studio

## Signal Chain

```mermaid
graph TD
    TT[Technics MK7] -->|phono 2| ECL[Ecler Nuo2]
    KOII[TE KOII] -->|line 1| ECL
    ECL -->|ch 15/16| T[Tascam Model 2400]

    MPC2500 -->|outs 1-8| PAL[Palmer Pan 16]
    MPC2000 -->|outs 1-8| PAL
    PAL -->|ch 1-8| T
    MPC2000 -->|stereo · ch 11/12| T
    MPC2500 -->|stereo · ch 13/14| T

    S950[Akai S950] --> VER[Vermona Filter Lancet]
    VER -->|ch 10| T

    T -->|ch 1-3 + ch 10 inserts| SPL[SPL Transient Designer 4]
    SPL --> T
    T -->|subgroup 1/2| DBX[DBX 266XL]
    DBX -->|ch 19/20 · parallel glue| T
    T -->|aux 4| XTC[Alesis XT:C]
    XTC -->|ch 17/18| T

    T -->|aux 1 · mono| S950
    T -->|subgroup 3/4| MPC2000
    T -->|subgroup 5/6| MPC2500

    T -->|USB · post-FX| MAC[Apple Studio M4 · Pro Tools Studio]
    MAC -->|ch 21/22| T
    T -->|monitor out| MON[Monitors]
```

## Key routing decisions

- **Drums are glued in parallel, not inserted.** Ch 1-3 feed subgroup 1/2 → DBX 266XL → back
  in on ch 19/20, blended under the dry channels. The compressed copy can be crushed hard
  because the dry channels keep the transients.
- **Sample-sends are subgroups, not auxes.** Subgroup 3/4 → MPC2000 and 5/6 → MPC2500 give a
  stereo, post-fader feed with its own level control, and leave three auxes free.
- **Capture is post-FX.** The desk EQ and the SPL transient shaping print on the recording.
  The multitrack is deliberately not a set of dry stems.

## Docs

- [CLAUDE.md](CLAUDE.md) — full routing, gear list, rack layout, capture and recall
- [manual_mastering_protools_studio.md](manual_mastering_protools_studio.md) — the mastering chain with exact values
- [dbx266xl-reference.md](dbx266xl-reference.md) — DBX 266XL settings for parallel drum glue
