import os
import urllib.parse
from playwright.sync_api import sync_playwright, expect

def test_page_title():
    cesta = os.path.abspath("index.html")
    cesta = urllib.parse.quote(cesta)

   
    

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(f"file://{cesta}")
        nadpis_1=page.locator("h1").first()
        expect(nadpis_1).to_be_visible()
        browser.close()