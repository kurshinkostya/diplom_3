import allure
import time

from locators.locators import MainPageLocators, OrdersPageLocators
from pages.base_page import BasePage

class CreateOrderPage(BasePage): 

    @allure.step('Проверить отображение структуры заказа')
    def check_order_structure(self):
        return self.check_presense(OrdersPageLocators.ORDER_STRUCTURE).is_displayed()

    @allure.step('Кликнуть на заказ в ленте')
    def click_order(self):
        self.wait_for_element_to_be_clickable(OrdersPageLocators.ORDER_LINK)
        self.click_on_element(OrdersPageLocators.ORDER_LINK)

    @allure.step('Найти номер заказа в истории заказов')
    def is_order_id_found_at_history(self, order_number):
        orders = self.find_until_all_elements_located(OrdersPageLocators.ALL_ORDERS_AT_HISTORY)
        order_numbers = [order.text for order in orders]
        return order_number in order_numbers

    @allure.step('Найти номер заказа в ленте заказов')
    def is_order_id_found_at_feed(self, order_number):
        orders = self.find_until_all_elements_located(OrdersPageLocators.ALL_ORDERS_AT_FEED)
        order_numbers = [order.text for order in orders]
        return order_number in order_numbers

    @allure.step('Получить счетчик заказов')
    def get_total_order_count_daily(self, counter_locator):
        count_text = self.get_actually_text(counter_locator)
        return int(count_text)

    @allure.step('Получить номер заказа пользователя')
    def get_user_order(self, order_number):
        return order_number.replace('#', '').strip()

    @allure.step('Получить номер заказа в работе')
    def get_user_order_in_progress(self):
        self.wait_until_element_visibility(OrdersPageLocators.NUMBER_IN_PROGRESS)
        order_element = self.driver.find_element(*OrdersPageLocators.NUMBER_IN_PROGRESS)
        return order_element.text