# Novatelle

**Let Knowledge Speak for Itself.**

An HTML lesson that presents itself: browser narration, animated SVG, bilingual chapters, and a player you can interrupt. The demo, **This Is Not a Video.**, tells its own story in six scenes over roughly 90 seconds. A dark canvas, cyan diagrams, visible captions, and a persistent playback footer keep the ideas in view.

[Open the demo](https://luisanthoniealkins.github.io/Novatelle/) · [Download the Codex skill](downloads/novatelle-skill.zip) · [Read the skill](.agents/skills/novatelle/SKILL.md)

## Try it

Open the demo above or open `index.html` locally, then press **Play**. Use **EN/ID** to switch languages and **CC** to toggle subtitles. On phones, the gear button opens CC, language, voice, and speed settings. Keep the `downloads/` folder beside the HTML if you want the local skill download link to work.

## How it works

One standalone HTML file contains the lesson, animated SVG visuals, and playback controls. Your browser narrates the text while visual cues follow each segment. There is no build step, API key, or bundled audio or video. The layout adapts to desktop and phone screens.

Voices and pause/resume behavior depend on your browser and operating system. On Android, Resume repeats the current narration segment to avoid native speech-resume failures. Some voices need an internet connection. If narration is unavailable, the lesson continues with paced captions.

The presentation is **43,254 bytes (43.3 KB)**, rounded to **43 KB** in the demo. This excludes browser and voice resources. Its comparison with a roughly **600 MB**, ten-minute Windows Snipping Tool recording is an illustrative observation, not an equivalent-content benchmark.

## Install the reusable skill

1. Download and extract [novatelle-skill.zip](downloads/novatelle-skill.zip). It contains exactly one `novatelle/` directory.
2. For project-local use, put that directory at `.agents/skills/novatelle/` in your project. This repository already includes it there. Avoid accidentally nesting `novatelle/novatelle/`.
3. For personal installation, copy the extracted folder into the skills directory documented for your Codex environment. Consult [OpenAI's skill documentation](https://learn.chatgpt.com/docs/build-skills); installations and supported scopes can differ. Reopen the session if needed, then invoke `$novatelle`.

Choose the **default layout** with a header, chapter bar, content area, subtitles, and compact playback footer, or describe a **custom layout**. You can also reuse individual parts. See [layout options](.agents/skills/novatelle/references/layout-options.md).

Example generation prompt:

> Use $novatelle with the default layout to create a five-minute self-presenting HTML lesson about HTTP requests for new web developers. Use English and natural Bahasa Indonesia, demonstrate a request and response with SVG, and include one practical example. Deliver a standalone http-lesson.html and verify playback, fallback, and phone layout. Do not publish.

Example custom layout prompt:

> Use $novatelle to create an HTTP lesson with a new template: a light paper background, a chapter rail on the left, a large central diagram, and compact playback controls below. Make the chapter rail usable on phones. Keep synchronized narration and bilingual content; do not copy the default dark split layout. Deliver one standalone HTML file and test it. Do not publish.

Example targeted modification prompt:

> Use $novatelle to edit http-lesson.html. Change only scene 2: explain a 404 response and update its diagram and both narrations. Preserve every other scene and the player. Compare the unchanged scenes, test scene 2 and adjacent transitions, and report the diff. Do not publish.

## Contribute

MIT licensed; see [LICENSE](LICENSE). Preserve both languages and follow the [QA checklist](.agents/skills/novatelle/references/qa-checklist.md). For shared player fixes, update `index.html` and `.agents/skills/novatelle/assets/template.html`. For lesson changes, edit the lesson data.
