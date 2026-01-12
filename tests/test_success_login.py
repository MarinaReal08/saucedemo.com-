import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@allure.feature("Login")
@allure.story("Успешный логин standard_user")
def test_success_login(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    with allure.step("Открыть страницу логина"):
        login_page.open_login()
        login_page.should_be_loaded()

    with allure.step("Авторизоваться стандартным пользователем"):
        login_page.login("standard_user", "secret_sauce")

    with allure.step("Проверить, что открылась страница товаров"):
        inventory_page.should_be_opened()
