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

        # Locate the button
        btn = page.get_by_role("button", name="Subscribe for updates")

        # Click the button
        print("Clicking button...")
        btn.click()

        # Wait for success state (button has class success)
        print("Waiting for success state...")
        page.wait_for_selector("button.success", timeout=5000)

        # Verify button text
        success_btn = page.locator("button.success")
        text = success_btn.inner_text()
        print(f"Button text: {text}")
        if "✅ Subscribed!" not in text:
            print("FAILED: Button text incorrect")
            exit(1)

        # Verify live region
        status = page.locator("#status-message")
        status_text = status.inner_text()
        print(f"Status message: {status_text}")
        if "Successfully subscribed!" not in status_text:
             print("FAILED: Status message incorrect")
             exit(1)

        # Check background color of button
        # Evaluate valid css
        bg_color = success_btn.evaluate("element => window.getComputedStyle(element).backgroundColor")
        print(f"Background color: {bg_color}")
        # #15803d is rgb(21, 128, 61)
        if "rgb(21, 128, 61)" not in bg_color:
             print("FAILED: Background color incorrect")
             exit(1)

        # Screenshot
        page.screenshot(path="verification/success_state.png")
        print("Screenshot saved to verification/success_state.png")

        browser.close()

if __name__ == "__main__":
    run()
