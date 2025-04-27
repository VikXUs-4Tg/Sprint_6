from selenium.webdriver.common.by import By


class MakeOrderPageLocators:
    BUTTON_NEXT_AND_PLACE_ORDER =       (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    BUTTON_YES =                        (By.XPATH, "//button[contains(text(), 'Да') and @class='Button_Button__ra12g Button_Middle__1CSJM']")
    FIELD_FOR_ENTRY_NAME =              (By.XPATH, "//input[@placeholder='* Имя']")
    FIELD_FOR_ENTRY_LAST_NAME =         (By.XPATH, "//input[@placeholder='* Фамилия']")
    FIELD_FOR_ENTRY_ADDRESS =           (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    FIELD_FOR_ENTRY_TELEPHONE =         (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    FIELD_FOR_ENTRY_METRO_STATION =     (By.XPATH, "//input[@placeholder='* Станция метро']")
    FIELD_FOR_ENTRY_DATE =              (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    FIELD_FOR_ENTRY_RENTAL_PERIOD =     (By.XPATH, "//div[@class='Dropdown-root']")
    FIELD_FOR_ENTRY_COLOR =             (By.XPATH, "//input[contains(text(), 'Цвет самоката')]")
    FIELD_FOR_ENTRY_RENTAL_COMMENT =    (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    TITLE_OF_ORDER_WINDOW =             (By.XPATH, "//div[contains(text(), 'Заказ оформлен') and @class='Order_ModalHeader__3FDaJ']")
    BILLET_FOR_DAY_AT_WEEK =            (By.XPATH, "//div[contains(@class, 'react-datepicker__day--0%billet%and contains(@class, 'outside-month')]")
    BILLET_FOR_RENT_TIME =              (By.XPATH, "//div[contains(text(), '%billet%') and contains(@class, 'Dropdown-option')]")
    BILLET_FOR_COLOR =                  (By.XPATH, "//label[contains(text(), '%billet%')]")
    BILLET_FOR_METRO_STATION =          (By.XPATH, "//li[@data-index='%billet%']")
