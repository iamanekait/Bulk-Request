# Playwright Automation

This Python script demonstrates how to use Playwright to automate browser interactions. Playwright is a Python library for automating browsers. It provides a high-level API to control web browsers such as Chromium, Firefox, and WebKit.

## Installation

You need to install Playwright and its dependencies:

```bash
pip install playwright
```

## Usage

```python
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
```

### Explanation

- This script opens a Chromium browser using Playwright.
- It navigates to the website https://iwebnext.com.
- It clicks on the first anchor (`<a>`) element it finds on the page.
- It types "Hello, Aniket!" into the first input (`<input>`) element it finds on the page.
- It takes a screenshot of the current page and saves it as `test.png`.
- Finally, it closes the browser.

## Notes

- This is a synchronous version of Playwright. Playwright also supports an asynchronous API for advanced use cases.
- You can customize the browser type (e.g., `p.firefox.launch()`, `p.webkit.launch()`) according to your preference.
- Playwright offers powerful capabilities for browser automation, including page interactions, element manipulation, and testing.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
