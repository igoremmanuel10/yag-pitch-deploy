from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    # iPhone 14 viewport
    context = browser.new_context(
        viewport={"width": 390, "height": 844},
        device_scale_factor=3,
        is_mobile=True,
        user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X)"
    )
    page = context.new_page()
    page.goto('https://yag-pitch-deploy.vercel.app', wait_until='networkidle')
    page.wait_for_timeout(2000)

    # Take full page screenshot
    page.screenshot(path='/tmp/pitch-mobile-full.png', full_page=True)
    print("Full page screenshot saved")

    # Take individual slide screenshots
    for i in range(1, 16):
        slide = page.locator(f'#slide-{i}')
        if slide.count() > 0:
            slide.scroll_into_view_if_needed()
            page.wait_for_timeout(500)
            page.screenshot(path=f'/tmp/pitch-mobile-slide{i}.png')
            print(f"Slide {i} captured")

    browser.close()
    print("Done!")
