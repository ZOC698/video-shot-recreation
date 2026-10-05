# Video Shot Recreation

[中文](README.md) | [日本語](README.ja.md) | [English](README.en.md)

A Codex skill with Chinese, Japanese, and English documentation for reference-video analysis, action quantification, character replacement, complete prompts, and generated-video comparison. Respond in the user's language unless a different prompt language is requested.

For requests such as “keep this shot, replace the character” and “why does this version move incorrectly?” Model-independent; no validation case is required before use. This is a Markdown-only method package, without bundled scripts, generation services, or media.

## Capabilities

- Analyze shots or consecutive frames: composition, action, camera movement, effects, and narrative purpose.
- Quantify enemy counts, simultaneous attackers, projectile volleys, intervals, action duration, and displacement.
- Preserve selected shots while replacing characters, costumes, or settings with supplied assets.
- Compare source and generated versions, separating visible differences, missing instructions, and causal hypotheses.
- Produce complete prompts, simple blocking-diagram descriptions, or editing suggestions as requested.

**Use quantification and causality together; preserve the user's goals.** Numbers are useful. Community advice is not a set of mandatory model parameters. Replacing a character does not authorize rewriting the story.

## Example requests

```text
Use $video-shot-recreation to analyze seconds 5–12 of this video.
Inspect takeoff through impact frame by frame, with images and descriptions.
Do not guess sounds you have not heard.
```

```text
Keep the reference's key compositions, shot order, and ending where the impact carries the characters through a portal.
Replace the protagonist with my character reference and write a complete 30-second prompt.
Quantify visible enemies, simultaneous attackers, and pulses per volley separately.
```

```text
Compare the reference, version one, and version two by matching action events.
Focus on why version two became running and why the final impact looks like pushing.
Provide diagnosis and local fixes only; do not rewrite the whole sequence.
```

These demonstrate invocation, not validated successful generations.

## Installation

Place the repository in a `video-shot-recreation` folder under the Codex skills directory. The default is `~/.codex/skills`; with a custom `CODEX_HOME`, use its `skills` subdirectory. For the default configuration:

```sh
git clone https://github.com/ZOC698/video-shot-recreation.git ~/.codex/skills/video-shot-recreation
```

Do not overwrite an existing folder; compare and preserve local changes first. Invoke `$video-shot-recreation` in a new conversation after installation; reopen the conversation if it is not recognized. You can also read the Markdown without installing it.

## Files and languages

| Document | Purpose |
|---|---|
| [SKILL.md](SKILL.md) | Single registered skill entry point, in Chinese |
| [SKILL.en.md](SKILL.en.md) | Complete English translation of the working instructions |
| [SKILL.ja.md](SKILL.ja.md) | Complete Japanese translation |
| [SOURCES.en.md](SOURCES.en.md) | Sources, adopted methods, and evidence boundaries |

Translations do not create additional skills. Read one language version; loading all three is unnecessary.

## Design rationale

Recurring collaboration problems were more specific than missing words such as “spectacular” or “ultrafast”:

- Carrying the previous video's story into a new clip.
- Filling the background with enemies while only one or two attack.
- Requesting “dense pulses” without sources, volleys, or overlap.
- Turning impact into prolonged pushing, or flight into running.
- Keeping an old “no cape” constraint after adopting a new cape reference.
- Treating reflection, refraction, and enormous scale as decoration without geometry.
- Extracting every frame but claiming complete review without inspecting them all.

These become diagnostic methods, not universal numerical or narrative templates. A user reported better results after quantifying enemies and pulses; that is creative feedback, not a controlled experiment or cross-model success-rate measurement.

## Quantification example

> Creative target: three emitters on each side, one pulse per emitter per volley, six pulses total per volley. Start the second volley 0.4 seconds after the first; each pulse remains visible for 0.6 seconds. The protagonist moves sideways during the overlap, and missed pulses terminate on the road behind them.

This specifies sources, counts, and timing. It is not a universal optimum or an official API. Label measurements, estimates, and targets; use ranges or lower bounds when occlusion prevents counting.

## Boundaries and dependencies

- Reading the method requires no FFmpeg. FFmpeg/ffprobe can inspect metadata and extract frames; PySceneDetect is optional for candidate cuts. State inspection limits when tools are unavailable.
- Real-time viewing, consecutive-frame inspection, and listening serve different purposes. Do not claim audio review without hearing it.
- Generation, uploads, and public release of private files are not automatic; they need authorization in the current task.
- Prompts do not guarantee frame-exact execution. Local revision, segmented generation, and editing are options, not prerequisites.
- The repository contains independently written documentation, not private videos, character images, conversation logs, or third-party film frames.

## Sources and validation status

Combines project experience, community fight-prompt methods, shot-list practice, and public tool documentation. See [SOURCES.en.md](SOURCES.en.md) for links and qualifications. No complete third-party skill or example script was copied.

Document structure, links, and skill formatting have been checked. No cross-model generation evaluation or success rate is claimed. Issues describing specific problems are welcome; media submission is optional.
