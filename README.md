# Boombap Sampling Home Studio

Hardware-first home studio for making boombap hip-hop beats. Vinyl sampling through Akai MPCs, multitrack recording into Ableton for mixdown.

## Workflow

1. Sample from vinyl (Technics MK7 → Ecler Nuo2 → MPC)
2. Build the beat on one MPC per project (MPC3000, MPC2000, or MPC2500)
3. Record 8 individual MPC outs through the patchbay into a Focusrite Scarlett 18i20
4. Mixdown in Ableton Live

## Signal Chain

```mermaid
graph TD
    TT[Technics MK7] -->|channel 2| MIX[Ecler Nuo2]
    MIX -->|main out L/R · bay 7/8| PB[Neutrik Patchbay]

    MPC3000 -->|outs 1-8 · bay 1-6, 9, 10| PB
    MPC2000 -->|outs 1-8 · bay 11-18| PB

    PB -->|bay outs 1/2| DBX[DBX 266xl]
    DBX -->|scarlett in 1/2| SC[Focusrite Scarlett 18i20]
    PB -->|bay outs 3-8| SC

    SC -->|USB| MAC[Apple Studio M4 · Ableton Live]
    SC -->|out 1/2| MON[Monitors]
    SC -->|out 7/8| MPC3000
    SC -->|out 9/10| MPC2000
```

## Patchbay Routing

Patchbay outs 1-8 feed Scarlett ins 1-8. The DBX 266xl is inserted on channels 1 and 2 between the patchbay and the Scarlett.
