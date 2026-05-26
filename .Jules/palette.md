## 2026-01-20 - Inline Validation and Accessibility Animation
**Learning:** Animated visibility transitions using `opacity` (instead of `display: none`) can cause Playwright's `.toBeVisible()` to pass even when the element is visually hidden (opacity 0).
**Action:** When testing animated visibility states, explicitly check for the toggling class (e.g., `.visible`) or use `.toHaveCSS('opacity', '1')` to ensure true visual presence. Also, ensure `aria-invalid` and `aria-describedby` are correctly managed alongside the visual state for accessibility.

## 2026-02-23 - Visual Success Feedback with Dynamic SVGs
**Learning:** When generating visual success indicators (like SVG icons) dynamically in JavaScript, creating elements without the proper XML namespace will cause them not to render.
**Action:** Always use `document.createElementNS('http://www.w3.org/2000/svg', tag)` when building SVG elements in JavaScript to ensure they are correctly parsed by the browser.
