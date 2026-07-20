import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def __init__(self, driver, url):
    self.driver = driver
    self.url = url
    self.wait = WebDriverWait(self.driver, 10)


class MainShopPage:
    # Поле ввода логина
    LOGIN_INPUT = (By.CSS_SELECTOR, "#user-name")
    # Поле ввода пароля
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#password")
    # Кнопка входа в систему
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login-button")
    # Кнопка добавления рюкзака в корзину
    ADD_sauce_labs_backpack_BUTTON = (
        By.NAME, 'add-to-cart-sauce-labs-backpack')
    # Кнопка добавления футболки в корзину
    ADD_sauce_labs_bolt_t_shirt_BUTTON = (
            By.NAME, "add-to-cart-sauce-labs-bolt-t-shirt")
    # Кнопка добавления детского комбинезона в корзину
    ADD_to_cart_sauce_labs_onesie_BUTTON = (
            By.NAME, "add-to-cart-sauce-labs-onesie")

    def __init__(self, driver, url):
        """
        Инициализация MainShopPage.

        :param driver: WebDriver, объект для управления браузером
        :param url: str, URL страницы для открытия
        """
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get(self.url)

# 1. Открываем сайт магазина: https://www.saucedemo.com/ в FireFox.

    @allure.step("Открытие страницы Saucedemo.com")
    def open(self):
        self.driver.get(
            "https://www.saucedemo.com/checkout-step-one.html"
            )

    @allure.step("Авторизация пользователя на сайте")
    def authorization(self):
        """
        Авторизует пользователя на сайте с использованием
        стандартных учётных данных.
        """
        with allure.step("Заполнение поля Username"):
            login_input = self.wait.until(EC.presence_of_element_located(
                self.LOGIN_INPUT
            ))
            login_input.send_keys("standard_user")

        with allure.step("Заполнение поля Password"):
            password_input = self.wait.until(EC.presence_of_element_located(
                self.PASSWORD_INPUT
            ))
            password_input.send_keys("secret_sauce")

        with allure.step("Отклик кнопки Login"):
            login_button = self.wait.until(EC.presence_of_element_located(
                self.LOGIN_BUTTON
            ))
            login_button.click()

    @allure.step("Добавление продуктов в корзину")
    def get_add_product(self):
        """
        Добавляет продукты в корзину на странице магазина.
        """
        with allure.step("Отклик кнопки добавления рюкзака в корзину"):
            self.wait.until(
                EC.presence_of_element_located(
                    self.ADD_sauce_labs_backpack_BUTTON)
            ).click()
        with allure.step("Отклик кнопки добавления футболки в корзину"):
            self.wait.until(
                EC.presence_of_element_located(
                    self.ADD_sauce_labs_bolt_t_shirt_BUTTON)
            ).click()
        with allure.step(
            "Отклик кнопки добавления "
            "детского комбинезона в корзину"
        ):
            self.wait.until(
                EC.presence_of_element_located(
                    self.ADD_to_cart_sauce_labs_onesie_BUTTON)
            ).click()


class CartPage:
    """
    Страница корзины, содержащая элементы управления и данные.
    """
    # Кнопка корзины
    SHOPPING_CART_BUTTON = (By.ID, "shopping_cart_container")
    # Кнопка оформления заказа
    CHECKOUT_BUTTON = (By.ID, "checkout")
    # Поле ввода имени
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "#first-name")
    # Поле ввода фамилии
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "#last-name")
    # Поле ввода почтового кода
    POSTAL_CODE_INPUT = (By.CSS_SELECTOR, "#postal-code")
    # Кнопка продолжения
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "#continue")
    # Общая сумма
    TOTAL_VALUE = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver, url):
        """
        Инициализация MainShopPage.
        :param driver: объект WebDriver
        :param url: str, URL страницы
        """
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get(self.url)

    @allure.step("Открытие страницы корзины")
    def get_shopping_card(self):
        """
        Открывает корзину, используя кнопку на странице.
        """
        with allure.step("Отклик кнопки корзины"):
            self.wait.until(
                EC.presence_of_element_located(self.SHOPPING_CART_BUTTON)
            ).click()

    @allure.step("Оформление заказа в корзине")
    def get_checkout(self):
        """
        Инициирует процесс оформления заказа, нажав соответствующую кнопку.
        """
        with allure.step("Отклик кнопки оформления заказа"):
            self.wait.until(
                EC.presence_of_element_located(self.CHECKOUT_BUTTON)
            ).click()

    @allure.step("Заполнение форм данных: имя, фамилия и почтовый индекс")
    def get_form(self):
        """
        Заполняет форму данными: имя, фамилия и почтовый индекс.

        :return: None
        """
        with allure.step("Заполнение поля First Name"):
            fist_name_input = self.wait.until(EC.presence_of_element_located(
                self.FIRST_NAME_INPUT
            ))
            fist_name_input.send_keys("Kirill")
        with allure.step("Заполнение поля Last Name"):
            last_name_input = self.wait.until(EC.presence_of_element_located(
                self.LAST_NAME_INPUT
            ))
            last_name_input.send_keys("Stanin")
        with allure.step("Заполнение поля Zip/Postal Code"):
            postal_code_input = self.wait.until(EC.presence_of_element_located(
                self.POSTAL_CODE_INPUT
            ))
            postal_code_input.send_keys("456537")

    @allure.step("Процесс оформления заказа")
    def get_continue(self):
        """
        Продолжает процесс оформления, нажав соответствующую кнопку.
        """
        with allure.step("Отклик кнопки Continue"):
            self.wait.until(
                EC.presence_of_element_located(self.CONTINUE_BUTTON)
            ).click()

    @allure.step("Ожидание появления итогой суммы")
    def get_total(self):
        """
        Ожидает появления общей суммы на странице.

        :return: None
        """
        self.wait.until(EC.presence_of_element_located(
            self.TOTAL_VALUE
        ))

    def get_result(self):
        """
        Возвращает текст общей суммы из элемента на странице.

        :return: str, текст общей суммы
        """
        with allure.step("Получение итоговой суммы"):
            self.wait.until(EC.text_to_be_present_in_element(
                self.TOTAL_VALUE, "Total: $58.29"))
            result_element = self.driver.find_element(*self.TOTAL_VALUE)
            return result_element.text

    def log_total(self):
        result = self.get_result()
        with allure.step(f"Итоговая сумма: {result}"):
            return result
