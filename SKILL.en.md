---
name: video-shot-recreation
description: Industrial-grade shot-by-shot film analysis, action & VFX morphology quantification, Codex-style contact sheet generation, and storyboard transplantation workflow.
---

# Video Shot Recreation (v2.0)

[中文](SKILL.md) | [日本語](SKILL.ja.md) | [English](SKILL.en.md)

This file is the primary entry point for the skill. Deliver in the user's language.

Transform raw reference video into auditable shot breakdowns and executable generative prompts.

---

## 0. Director Directives & 5 Core Iron Rules (User Verbatim Records)

> ### 🛑 Rule 1: Shot Awareness & Scale Transition
> **"And the camera is completely static—don't you know how to cut shots? Don't you know how to use medium, wide, and close-ups? Is the director skill I gave you just air?"**  
> * **Standard**: Strictly prohibit monotonous flat eye-level static shots. Master spatial progression: EWS establishing → high/low angle tension → Crash Zoom emotional peaks → lateral tracking speed.

> ### 🛑 Rule 2: Codex Contact Sheet & 6-Dimension Framework
> **"Why is the Codex film analysis in contact sheets while yours is one-by-one? I want contact sheets with descriptions under each frame, and a group summary covering lens choice, visual effects, narrative function, character action & mechanics, behavioral logic & psychology, and cinematographic techniques. Give me a professional breakdown of every frame, followed by a final synthesis report."**  
> * **Standard**: No scattered single images. Group frames into dark-themed contact sheets with millisecond badges. Every group must provide the 6-dimension synthesis.

> ### 🛑 Rule 3: Prohibit Sparse Sampling & Visual Hallucination
> **"Frame-by-frame analysis! Your sampling is way too sparse, missing critical information and causing ridiculous errors. Still too sparse—analyze the first thirty seconds first."**  
> * **Standard**: No sparse multi-second jumps. Lock onto core action windows with ultra-dense sub-second frame sampling. Never hallucinate unrecorded motion.

> ### 🛑 Rule 4: One Shot, One Group & Full VFX Morphology Tracking
> **"Even cut down to 30 seconds you did it so sloppily. Take this for example: Hulk never rushed out of the fire fog! You missed several frames and hallucinated this info. Second, the golden shockwave is the core VFX of this clip; its morphological evolution is the key technique for its impact, yet you only took one frame! Analyze frame-by-frame, one shot per group, don't be lazy."**  
> * **Standard**:
>   1. **One Shot, One Group**: Each physical cut is an independent group.
>   2. **Full Morphology Tracking**: Complex VFX (shockwaves, explosions) must be tracked across all evolutionary phases (e.g., core collapse → vertical arch → rotating vortex → hemispherical dome).
>   3. **Audit Real Subject Position**: Never hallucinate movement. If the character stays inside the blast core, record it as inside.

> ### 🛑 Rule 5: Information-Density Adaptive Sampling (No Upper Limit)
> **"The grid is not limited to a fixed number of frames. If information density is high, 100 frames is fine; if information density is low and screen changes are few, a dozen frames is fine. The key is to preserve the original information so that the analysis has zero omissions and zero mistakes."**  
> * **Standard**:
>   1. **Break Rigid Frame Limits**: Frame count is strictly proportional to visual change rate.
>   2. **High-Density Explosive Beats**: Sample 24, 48, or 100+ frames to capture every micro-step, impact frame, and fluid bifurcation.
>   3. **Low-Density Establishing Beats**: Sample 8-16 frames.
>   4. **Ultimate Metric**: Total information preservation without omission.

---

## I. Four-Step Industrial Pipeline

1. **Precision Cut Detection**: Automatic frame differencing / histogram correlation to isolate physical cuts.
2. **Adaptive Contact Sheet Synthesis**: Using `scripts/generate_shot_sheets.py` to produce dark-themed grid images with badges.
3. **Micro-Frame Analysis & 6-Dimension Summary**: Lens, VFX, narrative, mechanics, psychology, cinematography.
4. **Storyboard Transplantation Report**: Character mapping, scale contrast mechanics, and generative prompt matrix (Seedance 2.5 / Midjourney).
