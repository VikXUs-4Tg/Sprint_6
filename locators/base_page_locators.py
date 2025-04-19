from selenium.webdriver.common.by import By


class BasePageLocators:
    BUTTON_SCOOTER = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']")
    BUTTON_YANDEX = (By.XPATH, "//a[@class ='Header_LogoYandex__3TSOI']")
    BUTTON_PLACE_AN_ORDER = (By.XPATH, "//button[@class ='Button_Button__ra12g']")
    #accept_cookie_button = (By.XPATH, "//button[contains(text(), 'да все привыкли')]")
