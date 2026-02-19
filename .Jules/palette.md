## 2025-01-22 - Accessible Async Status

**Learning:** For dynamic updates (like button text changes) on disabled elements, screen readers may not announce the change.
**Action:** Always use a separate `aria-live` region (e.g., `<div role="status" class="sr-only">`) to announce status changes, even if the visible UI updates.
