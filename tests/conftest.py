import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            slow_mo=300
        )
        yield browser
        browser.close()


@pytest.fixture
def context(browser):
    context = browser.new_context(
        record_video_dir="artifacts/videos/",
        record_video_size={"width": 1280, "height": 720}
    )
    yield context
    context.close()


@pytest.fixture
def page(context):
    page = context.new_page()
    yield page