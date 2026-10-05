# Sources, Adaptation, and Evidence Boundaries

[中文](SOURCES.md) | [日本語](SOURCES.ja.md) | [English](SOURCES.en.md)

Reviewed: 2026-10-05. Linked content may change. This document records what was borrowed, not endorsement of every third-party conclusion or affiliation with the projects.

## Community action-direction methods

[liyue-aigc/seedance-2-5-fight-director](https://github.com/liyue-aigc/seedance-2-5-fight-director)

Reviewed its SKILL.md and the core-engine, grammar-library, diagnose, fight-camera-library, seedance-adaptation, and examples references.

Adopted: pair actions with opponent responses; follow contact with force consequences; maintain group participation at different depths; preserve position and momentum across cuts; distinguish asset roles from output failures.

Not adopted as universal rules: fixed action-frequency ceilings, default equal opponents, ever-increasing crowd density, terrain-changing endings for every crowd fight, or mandatory segmentation at a fixed duration. The requested reference story, camera positions, extraordinary speed, and portals take priority.

Its [examples.md](https://github.com/liyue-aigc/seedance-2-5-fight-director/blob/main/references/examples.md) states that examples have not undergone actual generation or success-rate testing. This project treats them as community choreography methods, not proven model limits. The documentation independently summarizes methods rather than copying complete scripts.

## Shot lists and visual planning

[StudioBinder: How to Make a Shot List](https://www.studiobinder.com/blog/how-to-make-a-shot-list/)

Adopted the practice of organizing visual information into shot lists and using images to communicate intent. This project adds observation/estimate/target evidence labels. A shot list is an organizational tool, not a model parameter; the commercial software is not required.

## Media timing and frame data

[FFmpeg: ffprobe Documentation](https://ffmpeg.org/ffprobe.html)

Stream, format, frame, and timestamp inspection provide metadata evidence. Read actual frame rates, durations, and counts; variable-rate timing cannot be derived solely by dividing frame number by nominal rate. Metadata tools do not replace visual interpretation.

## Limits of automatic cut detection

[PySceneDetect: Detectors](https://www.scenedetect.com/docs/latest/api/detectors.html)

ContentDetector uses inter-frame color/intensity changes; AdaptiveDetector compares changes over a rolling window and can mitigate false detections during fast camera motion. Use these for candidates and review the cuts. Default thresholds are not recommendations for every film.

## Project collaboration experience

Drawn from collaboration preceding this project: reference analysis, character replacement, rhythm comparisons, optical-geometry corrections, and local editing. Only general methods are shared, not attachments, identifying information, or local paths.

- Separate source observations, author hypotheses, and new creative targets.
- Counts of active enemies and pulses can be more useful than abstract density words; positive user feedback exists, but no controlled validation was conducted.
- Extremely brief source bursts should not inherit rigid realistic-action timing.
- New capes, eyes, and other design changes must replace stale constraints.
- Reflections, refracted backgrounds, and immense scale need camera/geometry relationships.
- Preserve original local media and verify analysis and editing completion separately.

These are revisable working hypotheses and agreements, not official platform conclusions. Report only checks actually performed. Documentation checks are not generation-quality validation.
