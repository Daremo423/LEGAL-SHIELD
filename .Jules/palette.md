## 2025-02-27 - Async Button Accessibility
**Learning:** Using `disabled` attribute on buttons removes them from the tab order, causing focus loss for keyboard users when the state changes.
**Action:** Use `aria-disabled="true"` instead of `disabled` for async actions, combined with CSS to visually indicate the disabled state. This keeps the element focusable and allows screen readers to announce updates.
