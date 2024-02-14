from playwright.sync_api import sync_playwright

def run_playwright():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Navigate to a website
        page.goto('https://iwebnext.com')

        # Perform some actions
        page.click('a')
        page.type('input', 'Hello, Aniket!')

        # Take a screenshot
        page.screenshot(path='test.png')

        # Close the browser
        browser.close()

if __name__ == "__main__":
    run_playwright()
