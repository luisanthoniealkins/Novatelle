# Acceptance checklist

Keep screenshots, test scripts, logs, snapshots, generated examples, and reports in a Git-ignored location. Record commands and actual results; distinguish deterministic simulated speech from audible voice checks.

- Open the HTML via `file://` and a plain static server. Verify no console errors, remote runtime requests, or missing assets. Play must require a user gesture.
- Run every scene through the end and Replay. Check all segments, chapter buttons, Previous/Next, and page count. Estimate duration from word count; manually time live speech on the intended device.
- Use a deterministic speech mock that can finish, error, stall, and emit late callbacks. Rapidly jump three scenes and fire canceled callbacks. They must not change the current segment. Duplicate end/error callbacks must not double-advance.
- Pause speech and motion; wait; resume. Also pause during the transition gap. Test repeated Play/Pause, switching language while speaking or paused, and voice/speed changes. Nothing should advance while paused.
- Check empty voices, delayed `voiceschanged`, missing selected language, speech exceptions/errors, and absent Web Speech API. Text fallback must complete; no hanging timeline.
- Inspect all visible and accessible labels in both languages, including diagram text, captions, source panel, fallback messages, and end state.
- Inspect desktop, 390px phone, 320px narrow phone, and short landscape screens. All controls must be reachable without document-level horizontal overflow. Test keyboard focus, native select operation, 200% zoom, and reduced motion.
- Confirm the chosen layout matches the user's preference. Default and custom shells must both keep usable controls; neither is exempt from playback checks. On the default shell, test gear open/close, Escape and outside dismissal, focus return, resizing across the 1000px breakpoint, CC on/off without layout shift, and horizontally scrolling the playback controls on narrow phones. No document-level horizontal overflow or clipped focus rings.
- Verify visible labels and button sizes do not jump between playback states. Newly introduced cues may animate; previously revealed cues should stay still. Before Play, narration-only reveals stay hidden.
- Simulate hidden/visible events: playback is not automatically paused by the default template, and an explicit user pause remains paused. Listen on actual devices before claiming uninterrupted background speech.
- Confirm every download and source link. When packaging a skill, verify one root folder, metadata, and that template edits remain reusable.
- For targeted edits, compare the unmodified scene objects and player to the before snapshot. Open and play the edited output.
- Exercise layout choice with a request using the default and one requesting a different shell. A custom request must not silently inherit the dark default layout. An existing-lesson edit must not trigger an unnecessary template-selection question or redesign.
- Manual audio: listen for pronunciation, overlapping utterances, pause/resume behavior, voice switches, and reasonable pacing in both languages. Browser automation cannot certify audible quality. Record browser/OS/voice and any failed behavior.
