import pytest
import allure
from selenium import webdriver
from shop_page import MainShopPage
from shop_page import CartPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Оформление заказа в интернет‑магазине: проверка итоговой суммы")
@allure.description(
    "Тест проверяет сценарий оформления заказа: авторизация, "
    "добавление товаров в корзину, "
    "переход к оформлению, заполнение формы и проверку итоговой суммы."
)
@allure.feature("Оформление заказа")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop(driver):
    shop_page = MainShopPage(driver, "https://www.saucedemo.com/")
    with allure.step("Открыть главную страницу магазина"):
        shop_page.open()
    with allure.step("Авторизоваться под стандартным пользователем"):
        shop_page.authorization()
    with allure.step("Добавить товары в корзину"):
        shop_page.get_add_product()
    shop_page = CartPage(driver, "https://www.saucedemo.com/cart.html")
    with allure.step("Перейти в корзину и начать оформление заказа"):
        shop_page.get_shopping_card()
        shop_page.get_checkout()
    with allure.step("Заполнить данные покупателя"):
        shop_page.get_form()
    with allure.step("Продолжить оформление заказа"):
        shop_page.get_continue()
    with allure.step("Дождаться отображения итоговой суммы"):
        shop_page.get_total()
    with allure.step("Получить и проверить итоговую сумму"):
        result = shop_page.get_result()
        assert result == "Total: $58.29"
