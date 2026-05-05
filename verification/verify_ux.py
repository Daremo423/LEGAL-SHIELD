import os
import re
from playwright.sync_api import sync_playwright, expect

def verify_ux():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the local index.html
        file_path = os.path.abspath("index.html")
        page.goto(f"file://{file_path}")

        print(f"Loaded {page.title()}")

        # Take initial screenshot
        page.screenshot(path="verification/initial_state.png")
        print("Initial screenshot taken.")

        # Test 1: Submit empty form
        print("Testing empty submission...")
        page.click("button[type='submit']")

        # Expect error message
        error_msg = page.locator("#email-error")
        # Check for visible class because we use opacity for animation
        expect(error_msg).to_have_class(re.compile(r"visible"))
        expect(error_msg).to_have_text("Email address is required.")
        print("PASS: Empty submission showed correct error.")

        page.screenshot(path="verification/empty_submission_error.png")

        # Test 2: Invalid email
        print("Testing invalid email...")
        page.fill("#email", "invalid-email")
        page.click("button[type='submit']")

        expect(error_msg).to_have_class(re.compile(r"visible"))
        expect(error_msg).to_have_text("Please enter a valid email address.")
        print("PASS: Invalid email showed correct error.")

        page.screenshot(path="verification/invalid_email_error.png")

        # Test 3: Valid email (clears error)
        print("Testing valid email...")
        page.fill("#email", "test@example.com")

        # Inputting valid email should clear error (on input event)
        expect(error_msg).not_to_have_class(re.compile(r"visible"))
        print("PASS: Valid input cleared error message.")

        page.click("button[type='submit']")

        # Wait for success message
        success_msg = page.locator(".status-message")
        expect(success_msg).to_be_visible()
        expect(success_msg).to_contain_text("Thanks!")
        print("PASS: Valid submission succeeded.")

        # Take final screenshot
        page.screenshot(path="verification/success_state.png")
        print("Success screenshot taken.")

        browser.close()

if __name__ == "__main__":
    verify_ux()
