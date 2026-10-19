# Presentation contract

## Content schema

`<script type="application/json" id="lesson-data">` contains one object:

```json
{
  "brand": "Lesson name",
  "tagline": {"en": "An idea explained", "id": "Gagasan yang dijelaskan"},
  "scenes": [{
    "kind": "flow",
    "title": {"en": "A question", "id": "Sebuah pertanyaan"},
    "subtitle": {"en": "Follow the idea", "id": "Ikuti gagasannya"},
    "labels": {"en": ["Ask", "Try", "Check"], "id": ["Tanya", "Coba", "Periksa"]},
    "segments": [
      {"en": "Ask a clear question.", "id": "Ajukan pertanyaan yang jelas."},
      {"en": "Try an example.", "id": "Coba sebuah contoh."},
      {"en": "Check the result.", "id": "Periksa hasilnya."}
    ],
    "note": {"en": "", "id": ""}
  }]
}
```

`flow` shows up to three SVG nodes. Each segment highlights the next node; the neutral example has three segments per scene. For more nodes or labels that need wrapping, extend the renderer and test narrow screens. `shown(cue, html)` reveals content from a segment index after playback begins; only the new cue receives `.reveal`. Already revealed content should not animate again on each segment. `.moving` is a pausable motion primitive. Diagrams need meaningful translated labels. Additional languages require matching UI translations, voice language mapping, and content fields.

Optional `speech: {"en": "pronunciation-friendly text", "id": "teks untuk pengucapan"}` inside a segment overrides only its spoken text. Captions continue using the normal `en`/`id` fields. Use this only when needed, and listen to the target voice; no particular phonetic spelling works for every engine. The neutral template has no brand-specific pronunciation substitutions or external CTAs.

The JSON is lesson content. Header, main content placement, captions, and footer are a replaceable visual shell: see [layout options](layout-options.md). A custom shell does not require changing the content schema or speech controller.

## Player invariants

- One shared state holds scene, segment, language, rate, playback status, and generation.
- `cancel()` increments generation before canceling speech. Late callbacks must check that generation and settle at most once.
- No speech until a user activates Play. Navigation before playback previews a scene without speaking.
- A segment completes only after narration ends and its finite entrance cue completes. A short gap separates segments. Continuous decorative motion is not a completion prerequisite.
- Pause freezes the presentation clock and CSS animation. Android cancels unfinished speech and Resume restarts the current segment; desktop requests native speech pause. A voice engine may finish a word or buffered audio before stopping; do not promise sample-accurate pause. Verify native pause/resume on the target browser; if adding a restart fallback, disclose that it repeats only the current segment.
- Voice or speed changes restart only the current segment; when paused, changes apply on Resume. Language changes translate UI and visuals, reset the current scene to its first segment, and preserve paused/playing state.
- `voiceschanged` and delayed retries update the selector. A missing matching voice uses captions with a reading-time clock, never a mismatched-language voice. Speech errors use the same fallback. A generous active-time watchdog recovers when a browser never emits completion; it is an error recovery mechanism, not normal scene timing.
- Timers advance only while playing; no callback can advance a canceled scene. The default does not pause on tab hiding. It accounts for elapsed time when timers are delayed, but browsers/OS may suspend background speech or execution. Never resume a user-paused lesson merely because it becomes visible.
- Captions are available throughout narration, on by default, and toggleable with CC. In the default layout they overlay content without shifting it; custom layouts may place them differently. Native controls have translated labels and unclipped focus rings. Reduced motion disables animations while preserving content and progression.
- Default settings are visible on wide screens and open upward from a gear on compact screens. Preserve Escape dismissal, focus return, outside-click dismissal, and safe handling of viewport changes when adapting this UI. Hidden settings must not remain keyboard-focusable.

## Portability and honesty

Embed CSS, JS, SVG, and lesson data. No required fetches. Browser speech may use local or online voice services; do not guarantee offline narration. File URLs work where browser policy allows; text mode remains available. Static hosting needs no build. Narration duration is approximate. Do not represent scripted examples as live AI execution. Keep external download links optional and source links truthful.
