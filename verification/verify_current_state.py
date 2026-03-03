from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        # Load local file
        page.goto("file:///app/index.html")

        button = page.get_by_label("Subscribe for updates")
        button.screenshot(path="verification/button_before.png")
        page.screenshot(path="verification/page_before.png")

        browser.close()

if __name__ == "__main__":
    run()
