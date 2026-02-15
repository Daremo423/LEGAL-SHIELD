## 2024-02-15 - Lost Focus on Form Hiding
**Learning:** When hiding the subscription form upon success, the keyboard focus is lost (reverting to body), forcing screen reader users to navigate from the top. `aria-live` announces the message but doesn't fix the navigation context.
**Action:** Always pair `display: none` of the active region with an explicit `.focus()` call to the replacement content (ensuring it has `tabindex="-1"`).
