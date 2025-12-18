from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # IMPORTANT
    page = browser.new_page()

    page.goto("https://example.com")
    time.sleep(5)  # keep browser open

    browser.close()
