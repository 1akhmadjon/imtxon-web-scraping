from playwright.sync_api import sync_playwright


url = 'https://www.youtube.com/@pdpuz/videos'


with sync_playwright() as p:
    browser = p.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(url)
    video_datas = page.query_selector_all('#video-title')[:5]
    arr = {}
    for date in video_datas:
        title = date.text_content().strip()
        description = date.get_attribute('aria-label').strip()
        arr = {
            'title': title,
            'description': description
        }
        print(arr)

    page.wait_for_timeout(10000)
