## 2025-02-27 - Async Button Accessibility
**Learning:** Using `disabled` attribute on buttons removes them from the tab order, causing focus loss for keyboard users when the state changes.
**Action:** Use `aria-disabled="true"` instead of `disabled` for async actions, combined with CSS to visually indicate the disabled state. This keeps the element focusable and allows screen readers to announce updates.

## 2025-03-02 - Status Region for Screen Readers
**Learning:** Depending solely on button text changes (`btn.innerHTML`) for async action feedback is insufficient for accessibility, especially when the button possesses an explicit `aria-label`. The `aria-label` masks the inner text changes from screen readers.
**Action:** Implemented a separate visually hidden `div` with `role="status"` and `aria-live="polite"` to reliably announce state changes (e.g. loading, success). Additionally, updated the button's `aria-label` upon success to ensure it remains accurate when focused.
