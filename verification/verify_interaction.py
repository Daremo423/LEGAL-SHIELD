from playwright.sync_api import sync_playwright, expect
import re

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("file:///app/index.html")

        button = page.locator("#notify-btn")

        # Verify initial state
        button.screenshot(path="verification/1_initial.png")

        # Click button
        button.click()

        # Verify loading state
        # The spinner class should be present
        expect(button.locator(".spinner")).to_be_visible()
        expect(button).to_have_attribute("aria-disabled", "true")
        button.screenshot(path="verification/2_loading.png")

        # Verify success state
        # Wait for the text to change (timeout is 2000ms in JS)
        expect(button).to_have_text("You're in!", timeout=5000)

        # Check if success class is applied.
        # to_have_class checks the entire class attribute string or list of classes.
        # Since we have "success", and possibly others if we had any,
        # but here we just added 'success' to the class list.
        # The button likely has no class initially, so it will be just "success"
        # or it might have other classes.
        # Let's use a regex to be safe if there were other classes.
        expect(button).to_have_class(re.compile(r"success"))

        button.screenshot(path="verification/3_success.png")

        browser.close()

if __name__ == "__main__":
    run()
