from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Get absolute path to index.html
        cwd = os.getcwd()
        file_path = f"file://{cwd}/index.html"

        print(f"Navigating to {file_path}")
        page.goto(file_path)

        # Locate the email input and submit button
        email_input = page.locator("#email")
        submit_btn = page.locator("#submit-btn")
        form = page.locator("#notify-form")
        status_message = page.locator("#status-message")

        # Type valid email
        email = "test@example.com"
        print(f"Typing email: {email}")
        email_input.fill(email)

        # Click the button
        print("Clicking submit button...")
        submit_btn.click()

        # Wait for success state (status message visible)
        print("Waiting for status message to be visible...")
        status_message.wait_for(state="visible", timeout=5000)

        # Verify form is hidden
        if form.is_visible():
            print("FAILED: Form should be hidden after success")
            exit(1)

        # Verify status message content
        text = status_message.inner_text()
        print(f"Status message text: {text}")
        expected_text = f"Thanks! We've added {email} to our list."

        # Verify text content (checking partial match because icon text might be separate if implemented differently, but inner_text usually combines them)
        if expected_text not in text:
            print(f"FAILED: Status message text incorrect. Expected '{expected_text}', found '{text}'")
            exit(1)

        # Verify success icon presence
        print("Verifying success icon...")
        icon = status_message.locator(".success-icon")
        if icon.count() == 0:
            print("FAILED: Success icon (.success-icon) not found")
            exit(1)

        # Verify icon is SVG
        tag_name = icon.evaluate("el => el.tagName")
        if tag_name.lower() != "svg":
             print(f"FAILED: Success icon is not an SVG, it is {tag_name}")
             exit(1)

        # Take screenshot
        page.screenshot(path="verification/success_state_verified.png")
        print("Screenshot saved to verification/success_state_verified.png")

        print("SUCCESS: Verified success message, form visibility, and success icon.")
        browser.close()

if __name__ == "__main__":
    run()
