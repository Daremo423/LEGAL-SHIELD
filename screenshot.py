import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        filepath = f"file://{os.path.abspath('index.html')}"
        await page.goto(filepath)

        os.makedirs("verification", exist_ok=True)

        btn = page.locator("#notify-btn")
        await page.screenshot(path="verification/screenshot-initial.png")

        await btn.click()
        await page.screenshot(path="verification/screenshot-loading.png")

        await page.wait_for_timeout(2500)
        await page.screenshot(path="verification/screenshot-success.png")

        print("Screenshots taken.")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
