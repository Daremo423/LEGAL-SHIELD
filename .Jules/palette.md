## 2026-01-20 - Inline Validation and Accessibility Animation
**Learning:** Animated visibility transitions using `opacity` (instead of `display: none`) can cause Playwright's `.toBeVisible()` to pass even when the element is visually hidden (opacity 0).
**Action:** When testing animated visibility states, explicitly check for the toggling class (e.g., `.visible`) or use `.toHaveCSS('opacity', '1')` to ensure true visual presence. Also, ensure `aria-invalid` and `aria-describedby` are correctly managed alongside the visual state for accessibility.
