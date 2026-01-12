import allure
from pages.login_page import LoginPage


@allure.feature("Login")
@allure.story("Логин с неверным паролем")
def test_wrong_password(page):
    login_page = LoginPage(page)

    with allure.step("Открыть страницу логина"):
        login_page.open_login()
        login_page.should_be_loaded()

    with allure.step("Попробовать войти с неверным паролем"):
        login_page.login("standard_user", "wrong_password")

    with allure.step("Проверить сообщение об ошибке"):
        login_page.should_see_error_contains("do not match")
