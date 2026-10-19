# Optional default layout and custom designs

The template is a working reference, not a visual acceptance mandate. A user can keep it, modify part of it, or define a new layout. Do not enforce this project's pixel values, palette, or control grouping on another design.

## Default shell

| Region | Default behavior | Adaptation examples |
|---|---|---|
| Header | Lesson name at left, short translated tagline at right; consistent font sizes and vertical padding across widths | Centered title, logo, course identity, or no tagline |
| Chapter navigation | Clickable segments immediately below the header; active glow belongs to the thin visible bar, not its larger hit area | Named tabs, chapter list, accessible step selector |
| Content area | Fluid width; text and SVG side by side on desktop, stacked on phones; content can scroll independently | Full-width diagram, cards, code walkthrough, quiz, custom scene grid |
| Captions | On by default after Play; positioned over the bottom of the stage above the footer; CC does not shift the content | Dedicated caption row, transcript panel, different subtitle placement |
| Footer | Stable height; Play/Pause/Resume share a width; separators group playback, navigation, and CC | Different icon style, compact player, alternative accessible arrangement |
| Settings | Language, voice, speed visible when roomy; gear opens an upward panel on narrow screens; Escape/outside click closes it | Side panel, dialog, persistent labeled settings |

The default preserves button sizes on small screens. The left playback group can scroll horizontally while the gear stays visible; padding prevents focus-ring clipping. A custom layout can use another accessible overflow solution. Test the actual text in both languages rather than assuming one breakpoint fits every lesson.

Default CSS has two main width thresholds (1000px for settings, 740px for content) and a short-landscape rule. These are implementation choices, not device requirements. There is no separate launch button or fullscreen control. Browser playback starts from the footer's Play button.

## Custom layout workflow

Use the user's provided design as the source of visual decisions. If they ask for a new template without details, ask for the intended look and any reference, then fill in routine choices. A custom template is authored HTML/CSS; a theme field alone does not create a different layout.

Start from the bundled controller when practical. In the default file, the controller binds to:

- Identity/content: `brand`, `tagline`, `chapterNav`, `title`, `subtitle`, `eyebrow`, `visual`.
- Transport: `play`, `prev`, `page`, `next`, `captions`.
- Captions: `subtitleOverlay`, `caption`.
- Settings: `settingsToggle`, `settingsPanel`, `language`, `voiceLabel`, `voiceTitle`, `voice`, `speedTitle`, `speed`.

If removing or replacing a region, adapt its JS references, labels, focus handling, and responsive behavior together. Do not hide broken controls with CSS. Keep scene data separate from shell/controller code so future targeted content edits do not become redesigns.

## Example choices

- “Use the default layout for a five-minute HTTP lesson.” → Copy the shell, replace neutral lesson data and visuals.
- “Use the default footer, but a light header and full-width diagram.” → Retain control behavior; customize those regions only.
- “Use a new template: warm paper colors, left chapter rail, centered content, bottom playback.” → Build that design and reconnect navigation/settings responsively. The dark split layout is not required.
- “Change only scene 2 in this existing lesson.” → Keep its existing layout and unrelated scenes; do not ask for a new template choice.
