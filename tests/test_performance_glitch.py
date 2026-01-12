import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from playwright.sync_api import expect


@allure.feature("Login")
@allure.story("Логин performance_glitch_user при возможных задержках")
def test_performance_glitch_user(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    with allure.step("Открыть страницу логина"):
        login_page.open_login()
        login_page.should_be_loaded()

    with allure.step("Авторизоваться пользователем performance_glitch_user"):
        login_page.login("performance_glitch_user", "secret_sauce")

    with allure.step("Ожидать загрузки страницы товаров несмотря на задержку"):
        # Явно увеличим ожидание для надёжности
        page.set_default_timeout(15000)
        inventory_page.should_be_opened()
