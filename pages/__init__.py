from pages.auth_user_page import AuthUserPage
from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.recovery_password_page import PasswordRecoveryPage
from pages.create_order_page import CreateOrderPage 
from pages.user_profile_page import UserProfilePage

class UIWorkerWeb(MainPage, AuthUserPage, PasswordRecoveryPage, UserProfilePage, CreateOrderPage):
    """Класс объединяет все классы по работе со страницами используя множественно наследование"""
    def __init__(self, driver, locators):
        super().__init__(driver)
        self.locators = locators