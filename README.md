# Novatelle

**Let Knowledge Speak for Itself.**

An HTML lesson that presents itself: browser narration, animated SVG, bilingual chapters, and a player you can interrupt. The demo, **This Is Not a Video.**, tells its own story in six scenes over roughly 90 seconds. A dark canvas, cyan diagrams, visible captions, and a persistent playback footer keep the ideas in view.

[Open the demo](index.html) · [Download the Codex skill](downloads/novatelle-skill.zip) · [Read the skill](.agents/skills/novatelle/SKILL.md)

The [demo link](index.html) works from the published GitHub Pages site. Enable Pages using the steps below, then share the URL shown in your repository's Pages settings.
Repository: [luisanthoniealkins/Novatelle](https://github.com/luisanthoniealkins/Novatelle). This address is configured in the demo; publication and GitHub Pages availability still need to be verified.

## Try it

Open `index.html` in a modern browser and press **Play** in the footer. Keep the `downloads/` folder beside it for the ZIP link. The lesson itself is self-contained and has no build step, API key, CDN, external font, or required network request.

Alternatively, from this directory:

```sh
python -m http.server 8000
```

Open `http://localhost:8000`. Use Play/Pause, Previous/Next, chapter bars, EN/ID, voice selection, and 0.75×–1.5× speed. Keyboard Tab reaches all controls. The CC button toggles video-style subtitles overlaid above the compact controls without shifting the content. On narrower screens, the gear button opens language, voice, and speed settings above the single-row footer; Escape or a click outside closes it. The end-screen View source on GitHub link opens the repository alongside the skill download.

## How it works

The `lesson-data` JSON separates content from the embedded renderer and player. Short narration segments trigger explicit visual cues. Speech completion and finite visual completion drive progression; normal scenes do not advance on a fixed duration. A cancellation generation rejects stale speech callbacks after navigation. Pause freezes narration and animation. Switching tabs does not automatically pause playback. The player accounts for delayed background timers; browsers or mobile operating systems may still suspend speech or the page. The layout adapts to desktop, portrait phones, and short landscape windows.

Changing language restarts the current scene while keeping the paused/playing state. Changing voice or speed restarts only the current segment, immediately if playing or on Resume if paused. No speech starts on page load. A final Replay returns to the beginning.

Voice availability, pronunciation, and pause/resume support vary by OS and browser. Some voices require a network connection; fully offline speech is not guaranteed. No audio is bundled. Missing matching voices or speech errors fall back to readable, paced captions. A timeout recovers from a stalled speech engine. Test audible playback on your intended device, particularly mobile browsers. HTML size excludes the browser, system TTS engine, installed/downloaded voice assets, and external runtime resources.

The size scene uses the owner's observation: a roughly 10-minute Windows Snipping Tool screen recording using default settings was about **600 MB**, while an **earlier HTML prototype** was about **26 KB**. These are different artifacts from one example, **not a controlled apples-to-apples benchmark**. The 26 KB excludes browser/system TTS, voice assets, external runtime costs, and resources outside the file. It is not the size promised for this demo.

## Install the reusable skill

1. Download and extract [novatelle-skill.zip](downloads/novatelle-skill.zip). It contains exactly one `novatelle/` directory.
2. For project-local use, put that directory at `.agents/skills/novatelle/` in your project. This repository already includes it there. Avoid accidentally nesting `novatelle/novatelle/`.
3. For personal installation, copy the extracted folder into the skills directory documented for your Codex environment. Consult [OpenAI's skill documentation](https://learn.chatgpt.com/docs/build-skills); installations and supported scopes can differ. Reopen the session if needed, then invoke `$novatelle`.

The skill offers an **optional default layout**: header, chapter bar, content area, CC subtitles, and a compact footer with responsive settings. For a new lesson, it asks whether to use this default or define a custom layout when you have not already specified one. You can also keep just part of the default, such as its footer. Existing lessons keep their layout unless you request a redesign. Autonomous requests use the default when no preference is given.

The template is topic-neutral and includes the current player behavior. Its visual design is a starting point, not a requirement. See [layout options](.agents/skills/novatelle/references/layout-options.md). Example generation prompt:

> Use $novatelle with the default layout to create a five-minute self-presenting HTML lesson about HTTP requests for new web developers. Use English and natural Bahasa Indonesia, demonstrate a request and response with SVG, and include one practical example. Deliver a standalone http-lesson.html and verify playback, fallback, and phone layout. Do not publish.

Example custom layout prompt:

> Use $novatelle to create an HTTP lesson with a new template: a light paper background, a chapter rail on the left, a large central diagram, and compact playback controls below. Make the chapter rail usable on phones. Keep synchronized narration and bilingual content; do not copy the default dark split layout. Deliver one standalone HTML file and test it. Do not publish.

Example targeted modification prompt:

> Use $novatelle to edit http-lesson.html. Change only scene 2: explain a 404 response and update its diagram and both narrations. Preserve every other scene and the player. Compare the unchanged scenes, test scene 2 and adjacent transitions, and report the diff. Do not publish.

## Public files

```text
index.html                              Standalone demo / Pages entry point
README.md, LICENSE, .gitignore, .nojekyll
.agents/skills/novatelle/SKILL.md         Reusable skill instructions
.agents/skills/novatelle/assets/template.html
.agents/skills/novatelle/references/      Player contract and QA checklist
downloads/novatelle-skill.zip             Installable public skill
scripts/package-skill.py                 Reproducible standard-library packager
```

`private/`, test outputs, and local experiments are ignored and must stay out of commits. The source skill and its ZIP are public and should be included in your commit. Rebuild the ZIP after a skill change:

```sh
python scripts/package-skill.py
```

The packager uses an explicit five-file allowlist, fixed timestamps, and sorted paths. ZIP bytes are repeatable in the same Python/zlib environment.

## Publish manually to GitHub Pages

- Review rights and content, confirm the configured repository URL, and commit only the public files listed here. Do not include launch notes or QA outputs.
- Create or open your GitHub repository and push your reviewed `main` branch yourself.
- Open **Settings → Pages → Build and deployment → Source: Deploy from a branch → Branch: main → / (root) → Save**.
- Wait for GitHub's deployment, then use the exact URL shown in Pages settings; do not guess it.
- Verify the served demo, EN/ID, speech with a user gesture, phone controls, Replay, View source on GitHub, and the relative `downloads/novatelle-skill.zip` link. Extract the downloaded ZIP to check it.

`.nojekyll` enables plain static publishing. Nothing in this project deploys automatically. GitHub Pages publishes repository content: ignored local files are not uploaded by this workflow, but ignored files must never be manually included in a deployment.

## Contribute

MIT licensed; see [LICENSE](LICENSE). Keep changes focused, preserve both languages, and test the behavior in the [QA checklist](.agents/skills/novatelle/references/qa-checklist.md). For player fixes, update both standalone files and rebuild the skill ZIP. For content changes, edit the lesson data without replacing the player. Record browser limitations honestly; a passing simulated speech test does not certify audible quality.
