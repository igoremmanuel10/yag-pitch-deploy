from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1440, "height": 900})
    page.goto('https://yag-pitch-deploy.vercel.app', wait_until='networkidle')
    page.wait_for_timeout(2000)

    for i in range(1, 16):
        slide = page.locator(f'#slide-{i}')
        if slide.count() > 0:
            slide.scroll_into_view_if_needed()
            page.wait_for_timeout(400)
            page.screenshot(path=f'/tmp/pitch-desktop-slide{i}.png')
            print(f"Slide {i} captured")

    browser.close()
