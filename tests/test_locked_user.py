import allure
from pages.login_page import LoginPage


@allure.feature("Login")
@allure.story("Логин заблокированного пользователя")
def test_locked_user(page):
    login_page = LoginPage(page)

    with allure.step("Открыть страницу логина"):
        login_page.open_login()
        login_page.should_be_loaded()

    with allure.step("Попробовать войти заблокированным пользователем"):
        login_page.login("locked_out_user", "secret_sauce")

    with allure.step("Проверить сообщение об ошибке"):
        login_page.should_see_error_contains("locked out")
