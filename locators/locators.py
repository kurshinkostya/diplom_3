from selenium.webdriver.common.by import By


class MainPageLocators:
    PROFILE_BUTTON = By.XPATH, ".//p[text()='Личный Кабинет']"
    LOGIN_PROFILE_BUTTON = By.XPATH, ".//button[text()='Войти в аккаунт']"
    CONSTRUCTOR_BUTTON = By.XPATH, '//p[text()="Конструктор"]/parent::a'
    MAIN_LIST_TITLE = By.XPATH, "//h1[text()='Соберите бургер']"
    ORDERS_LIST_BUTTON = By.XPATH, '//p[text()="Лента Заказов"]/parent::a'
    
    # ингредиент "Флюоресцентная булка R2-D3"
    BUN_INGREDIENT = (By.XPATH, '//p[text()="Флюоресцентная булка R2-D3"]')  
    
    # детали ингредиента
    INGREDIENT_DETAILS_POPUP = (By.XPATH, '//h2[text()="Детали ингредиента"]')  
    
    # закрытие всплывающего окна
    CROSS_BUTTON = By.XPATH, '//button[contains(@class,"close")]'  
    
    # счетчик
    INGREDIENT_COUNTER = (By.XPATH, '//ul[1]/a[1]//p[contains(@class, "num")]')  
    ORDER_BASKET = (By.XPATH, "//span[@class='constructor-element__text' and text()='Перетяните булочку сюда (низ)']")
    
    # кнопка "Оформить заказ"
    CREATE_ORDER_BUTTON = By.XPATH, '//button[text()="Оформить заказ"]'  
    
    # идентификатор заказа
    ORDER_IDENTIFICATE = (By.XPATH, '//p[text()="идентификатор заказа"]')  
    ORDER_ID = (By.CLASS_NAME, "Modal_modal__title_shadow__3ikwq")
    LOADING_CHECK_BOX = (By.XPATH, ".//img[@alt='tick animation']")
    
    # попап - Ваш заказ начали готовить 
    ORDER_STATUS_TEXT = By.XPATH, '//p[text()="Ваш заказ начали готовить"]'  
    CLOSE_MODAL_ORDER = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')][1]")
    MAIN_ORDER_H1 = By.XPATH, ".//p[text()='Соберите бургер']"


class AuthLoginLocators:
    # /login
    EMAIL_FIELD = (By.XPATH, ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']")
    PASSWORD_FIELD = (By.XPATH, ".//input[@type='password' and @name='Пароль']")
    LOGIN_BUTTON_ANY_FORMS = (By.XPATH, ".//button[text()='Войти']")
    
    # "Восстановить пароль"
    FORGOT_PASSWORD = (By.XPATH, '//a[contains(@href, "/forgot-password")]')    
    LOGIN_TEXT = (By.XPATH, ".//h2[text()='Вход']")


class AuthRegistreLocators:
    pass


class AuthForgotPasswordlocators:
    
    INPUT_EMAIL = By.XPATH, '//label[text()="Email"]/following-sibling::input'  # поле ввода почты
    RESET_BUTTON = By.XPATH, '//button[text()="Восстановить"]'  # кнопка "Восстановить"

    INPUT_ACTIVE = By.CSS_SELECTOR, '.input.input_status_active'  # поле пароль активно
    SHOW_PASSWORD_BUTTON = By.XPATH, '//div[contains(@class,"icon-action")]'  # кнопка "Показать пароль"
    SAVE_BUTTON = By.XPATH, '//button[text()="Сохранить"]'  # кнопка "Сохранить"


class UserProfileLocators:
    # кнопка "Профиль"
    PROFILE_BUTTON = (By.LINK_TEXT, 'Профиль')  
    
    # кнопка "История заказов"
    ORDER_HISTORY_BUTTON = (By.LINK_TEXT, 'История заказов')  
    # нажатая кнопка "История заказов"
    ENABLED_ORDER_HISTORY_BUTTON = (By.XPATH, '//ul/li[2]/a[contains(@class, "Account_link_active")]')  
    LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выход']")
    LK_INFO_MESSAGE = (By.XPATH, ".//p[contains(text(),'персональные данные')]")


class OrdersPageLocators:
    
    # заголовок "Лента заказов"
    ORDERS_LIST_TITLE = (By.XPATH, '//h1[text()="Лента заказов"]') 
    
     # состав
    ORDER_STRUCTURE = By.XPATH, '//p[text()="Cостав"]' 
    
    # ссылка на заказ в Ленте заказов
    ORDER_LINK = By.XPATH, '//*[contains(@class, "OrderHistory_link")]'  
    ALL_ORDERS_AT_HISTORY = (By.XPATH, "//div[contains(@class, 'OrderHistory_textBox__3lgbs')]/p[contains(@class, "
                                       "'text_type_digits-default')]")
    ALL_ORDERS_AT_FEED = (By.XPATH, ".//div[@class='OrderHistory_textBox__3lgbs mb-6']//p[@class='text "
                                    "text_type_digits-default']")

    TOTAL_ORDER_COUNT = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    DAILY_ORDER_COUNT = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    
    # номер в разделе "В работе"
    NUMBER_IN_PROGRESS_2 = (By.CSS_SELECTOR, 'ul.OrderFeed_orderListReady__1YFem li')  
    NUMBER_IN_PROGRESS = (By.XPATH, ".//ul[@class='OrderFeed_orderListReady__1YFem "
                                         "OrderFeed_orderList__cBvyi']/li[@class='text text_type_digits-default mb-2']")