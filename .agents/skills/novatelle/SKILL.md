---
name: novatelle
description: Create or edit standalone HTML lessons with browser narration, animated visuals, bilingual scenes, and playback controls, using an optional default layout or a custom design. Use for self-presenting training, interactive tutorials, or targeted changes to an existing HTML lesson.
---

# Novatelle

Deliver an actual standalone HTML lesson. Keep user content separate from the playback implementation. No runtime packages, remote fonts, audio files, or API keys are required.

## Choose the layout

The bundled layout is a **soft template: a starting point, not a required design**. For a new lesson without a layout preference, ask once: “Use the default Novatelle layout (header, chapter bar, content area, subtitles, and compact footer), or define a custom layout?” Continue outlining content while awaiting the choice. If the user requests autonomous work or offers no preference, state that you will use the default and proceed.

If a reference, design, or template choice is already provided, use it without asking again. For edits, preserve the existing layout unless redesign is requested. “Define a custom layout” can mean a written description, reference file, or changes to the default; do not require a formal specification. Resolve routine details yourself and ask only about material omissions.

Read [layout options](references/layout-options.md) when choosing or changing the presentation shell. Header/footer placement, colors, typography, spacing, and breakpoints are flexible. The playback invariants in the presentation contract remain applicable to either layout. Do not add a runtime template picker unless requested.

## Create a lesson

1. Establish the audience, topic, outcome, approximate duration, and languages from the request. Use sensible stated assumptions when unspecified; the template provides English and Bahasa Indonesia.
2. Read [the presentation contract](references/presentation-contract.md). For the default layout, copy [the working template](assets/template.html). For a custom layout, adapt its shell or reuse its controller in the requested design. Read the content JSON and player before editing; preserve controller-to-DOM bindings or update them together.
3. Replace `lesson-data` with a topic-specific narrative: question, explanation, concrete example, application, recap. For a five-minute lesson, aim around 650–750 English words; speech rate and voice change duration. Segment speech into short coherent thoughts, each with a visual cue. Do not pad with the Novatelle promotional story.
4. Set `brand`, translated `tagline`, and all scene titles, subtitles, labels, notes, and narration. Keep a stable scene order. Use `flow` for a generic SVG diagram or add a focused renderer for the topic. Extend animation primitives only when the lesson benefits. User content is data, not executable code: escape inserted text, and serialize JSON safely (escape `<` as `\u003c` when necessary).
5. Preserve generation cancellation, segmented completion, fallback, accessible playback controls, and reduced-motion behavior. Their visual arrangement may change. The neutral template has no promotional links; add a download or repository CTA only if useful and supplied by the user. Do not copy the Novatelle demo's brand, anecdotes, pronunciation substitutions, or repository into unrelated lessons.
6. Run [the QA checklist](references/qa-checklist.md), including a real browser. Deliver the HTML with actual size, verified behavior, and remaining manual audio checks. Do not publish unless asked.

## Edit an existing lesson

Read the requested scene and its dependencies, then change only its content and necessary renderer/style hooks. For “change only scene N and narration,” preserve other scene objects and the player byte-for-byte where possible. Save a before snapshot in an ignored test location and compare unchanged scene objects after editing. Update both languages together. Do not replace a working player to make a content edit.

Run the edited scene, adjacent transitions, pause/resume, language switch, and rapid navigation. Rerun broader player checks if player code changed. Report exactly which content changed and any effects on duration.
