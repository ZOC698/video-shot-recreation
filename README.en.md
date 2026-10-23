# Video Shot Recreation (v3.0 Fused Edition)

[中文](README.md) | [日本語](README.ja.md) | [English](README.en.md)

An industrial-grade cinematic analysis and storyboard transplantation Skill: seamlessly fusing **Director's 5 Core Iron Rules**, **Codex contact sheets (adaptive 10 to 100+ frames)**, **6-dimension audiovisual deconstruction**, and the **[PromptDirector](https://github.com/wchao6891/PromptDirector) Local-First MCP Cockpit**.

---

## What's New in v3.0 (Fused Edition)

### 1. Deep Integration with PromptDirector MCP Protocols
- **Timeline Synchronization (`timeNotes`)**: Exports millisecond-level timeline notes (`{assetId, startMs, endMs, text}`) directly viewable in browser video review timelines.
- **Visual Set System Deconstruction (`visualSetAnalyses`)**: Structured analysis for multi-frame contact sheets (`sharedVisualSystem`, `differences`, `continuity`, `compositionRules`, `reusablePrompt`).
- **One-Click Native Persistence (`save_material`)**: Packages contact sheets, 6D reports, and recreated prompt matrices for local library storage and Agent Skill distribution (`save_skill`).
- **Data Integrity Guarantee**: Strict segregation between objective visual facts and AI reverse engineering (`ai-suggestion`).

### 2. Director's 5 Core Iron Rules
1. **Shot Awareness & Dynamic Framing**: No flat static shots. Seamless progression across EWS, Dutch tilts, Crash Zooms, and Tracking.
2. **Codex Contact Sheets & 6D Framework**: Structured grid contact sheets with millisecond badges and 6-dimension synthesis.
3. **Strict Zero-Hallucination & Dense Sampling**: Sub-second sampling without speculative storytelling.
4. **One Shot, One Group & Multi-Stage VFX Evolution**: Track complex shockwaves and plasma vortexes through all evolutionary phases; audit exact character positions without assuming motion.
5. **Information-Density Adaptive Sampling (No Upper Bound)**: Scale from a dozen frames up to 100+ frames to capture every impact frame and kinetic transition.

---

## Directory Structure

```text
video-shot-recreation/
├── SKILL.md            # Primary skill entry point (Fused Edition)
├── README.md           # Documentation (Chinese)
├── README.en.md        # Documentation (English)
├── SOURCES.md          # References & sources
└── scripts/
    ├── generate_shot_sheets.py      # Adaptive contact sheet generation & PromptDirector exporter
    └── example_shot_config.json    # Example shot breakdown configuration
```

---

## Quick Start

```bash
# Generate contact sheets and export PromptDirector MCP JSON payload
python scripts/generate_shot_sheets.py \
  --video "reference_video/clip.mp4" \
  --config "scripts/example_shot_config.json" \
  --outdir "output/" \
  --export_pd
```
