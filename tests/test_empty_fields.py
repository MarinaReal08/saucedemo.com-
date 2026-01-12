import allure
from pages.login_page import LoginPage


@allure.feature("Login")
@allure.story("Логин с пустыми полями")
def test_empty_fields(page):
    login_page = LoginPage(page)

    with allure.step("Открыть страницу логина"):
        login_page.open_login()
        login_page.should_be_loaded()

    with allure.step("Попытка логина с пустыми полями"):
        login_page.login("", "")

    with allure.step("Проверить сообщение о необходимости имени пользователя"):
        login_page.should_see_error_contains("Username is required")
