# ========== 新增：可视化浏览器配置（直接加在conftest.py最开头） ==========
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        # 关键配置：headless=False（显示浏览器）、slow_mo=500（步骤延迟500ms）
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()
        yield page  # 提供page对象给其他夹具（如login_page）
        page.close()
        context.close()
        browser.close()
# ========== 新增结束 ==========

# 以下是你原来的conftest.py代码（无需修改）
# ===================== 必须添加！conftest.py 要用 =====================
REPORT_DIR = "allure-results"    # 测试报告目录
SCREENSHOT_DIR = "screenshots"   # 失败截图目录
PACT_DIR = "pacts"               # 契约测试文件目录
import pytest
import os
from config.settings import Config

def pytest_configure(config):
    os.makedirs(Config.REPORT_DIR, exist_ok=True)
    os.makedirs(Config.SCREENSHOT_DIR, exist_ok=True)
    os.makedirs(Config.PACT_DIR, exist_ok=True)

@pytest.fixture(scope="function")
def login_page(page):
    from pages.login_page import LoginPage
    return LoginPage(page)

@pytest.fixture(scope="function")
def product_page(page):
    from pages.product_page import ProductPage
    return ProductPage(page)

@pytest.fixture(scope="function")
def checkout_page(page):
    from pages.checkout_page import CheckoutPage
    return CheckoutPage(page)

@pytest.fixture(scope="function")
def redis_helper():
    from utils.redis_helper import RedisHelper
    return RedisHelper()

@pytest.fixture(scope="function")
def db_helper():
    from utils.db_helper import DBHelper
    return DBHelper()

@pytest.fixture(scope="session")
def pact_consumer():
    from pact import Consumer, Provider
    pact = Consumer("EcommerceConsumer").has_pact_with(
        Provider("UserService"),
        pact_dir=Config.PACT_DIR
    )
    pact.start_service()
    yield pact
    pact.stop_service()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            from pages.base_page import BasePage
            base_page = BasePage(page)
            base_page.take_screenshot(f"failed_{item.name}")
