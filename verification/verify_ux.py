from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the file
        filepath = os.path.abspath("index.html")
        page.goto(f"file://{filepath}")

        # Take initial screenshot
        page.screenshot(path="verification/1_initial.png")
        print("Initial screenshot taken.")

        # Click the button
        # Use ID to locate button as text changes
        btn = page.locator("#notify-btn")
        btn.click()

        # Verify loading state
        # Need to be quick or use waitFor function if state changes fast
        # But here it stays for 2 seconds.
        page.wait_for_timeout(500) # Wait a bit for the text to change
        page.screenshot(path="verification/2_loading.png")
        print("Loading screenshot taken.")

        # Verify loading text
        if "Subscribing..." in btn.inner_text():
            print("Loading text verified.")
        else:
            print(f"Loading text mismatch: {btn.inner_text()}")

        # Verify disabled state
        if btn.get_attribute("aria-disabled") == "true":
             print("Aria-disabled verified.")
        else:
             print("Aria-disabled missing.")

        # Wait for success state
        page.wait_for_timeout(2000)

        # Verify success state
        page.screenshot(path="verification/3_success.png")
        print("Success screenshot taken.")

        if "Subscribed!" in btn.inner_text():
             print("Success text verified.")
        else:
             print(f"Success text mismatch: {btn.inner_text()}")

        if "success" in btn.get_attribute("class"):
             print("Success class verified.")
        else:
             print("Success class missing.")

        browser.close()

if __name__ == "__main__":
    run()
