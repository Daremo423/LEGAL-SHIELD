# Palette's Journal - Critical Learnings

## 2024-05-22 - [Accessible Status Updates]
**Learning:** Modifying text content of a focused element (like a button) is not reliably announced by all screen readers.
**Action:** Always use a separate visually hidden live region (`role="status"`) to announce dynamic state changes like "Sending..." or "Subscribed!".
