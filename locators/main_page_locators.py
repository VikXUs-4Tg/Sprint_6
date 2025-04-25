from selenium.webdriver.common.by import By


class MainPageLocators:
    EMPTY_LOCATOR_BY_ID =       (By.ID, "")
    FIELD_HOW_IT_WORKS =        (By.XPATH, "//div[@class='Home_RoadMap__2tal_']")
    BUTTON_PLACE_AN_ORDER =     (By.XPATH, "//button[contains(text(), 'Заказать') and @class='Button_Button__ra12g Button_Middle__1CSJM']")
    IMPORTANT_QUESTIONS_1 =     (By.XPATH, "//div[contains(text(), 'Сколько это стоит? И как оплатить?')]")
    IMPORTANT_QUESTIONS_2 =     (By.XPATH, "//div[contains(text(), 'Хочу сразу несколько самокатов! Так можно?')]")
    IMPORTANT_QUESTIONS_3 =     (By.XPATH, "//div[contains(text(), 'Как рассчитывается время аренды?')]")
    IMPORTANT_QUESTIONS_4 =     (By.XPATH, "//div[contains(text(), 'Можно ли заказать самокат прямо на сегодня?')]")
    IMPORTANT_QUESTIONS_5 =     (By.XPATH, "//div[contains(text(), 'Можно ли продлить заказ или вернуть самокат раньше?')]")
    IMPORTANT_QUESTIONS_6 =     (By.XPATH, "//div[contains(text(), 'Вы привозите зарядку вместе с самокатом?')]")
    IMPORTANT_QUESTIONS_7 =     (By.XPATH, "//div[contains(text(), 'Можно ли отменить заказ?')]")
    IMPORTANT_QUESTIONS_8 =     (By.XPATH, "//div[contains(text(), 'Я жизу за МКАДом, привезёте?')]")
    TEXT_FIELD_OF_ELEMENT =     (By.XPATH, "./p")
