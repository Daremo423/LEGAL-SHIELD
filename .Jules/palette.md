## 2024-02-15 - Lost Focus on Form Hiding

**Learning:** When hiding the subscription form upon success, the keyboard focus is lost (reverting to body), forcing screen reader users to navigate from the top. `aria-live` announces the message but doesn't fix the navigation context.
**Action:** Always pair `display: none` of the active region with an explicit `.focus()` call to the replacement content (ensuring it has `tabindex="-1"`).

## 2025-05-22 - Accessible Form Validation

**Learning:** Browser-native validation can be inconsistent across devices and screen readers. Implementing custom validation using `novalidate`, `aria-invalid`, and `aria-describedby` ensures errors are programmatically associated with inputs and announced reliably.
**Action:** Prefer custom accessible validation over native browser tooltips for critical user flows to guarantee consistent feedback.

## 2026-02-20 - Visual Confirmation for Success States

**Learning:** Text-only feedback can be slow to process. Adding a recognizable icon (like an animated checkmark) to success messages creates immediate cognitive recognition and adds a moment of delight, confirming the action visually as well as textually.
**Action:** Pair status messages with meaningful iconography to enhance scanability and user confidence.
