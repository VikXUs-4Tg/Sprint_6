from selenium import webdriver
from locators.main_page_locators import MainPageLocators as MPL

firefox_options = webdriver.FirefoxOptions()
#firefox_options.add_argument('--headless')

const = {
'WEBPAGE' : 'https://qa-scooter.praktikum-services.ru/',
'WAIT_TIMER' : 10,
'DROP_DOWN_LISTS_1' : 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.',
'DROP_DOWN_LISTS_2' : 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.',
'DROP_DOWN_LISTS_3' : 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.',
'DROP_DOWN_LISTS_4' : 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.',
'DROP_DOWN_LISTS_5' : 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.',
'DROP_DOWN_LISTS_6' : 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.',
'DROP_DOWN_LISTS_7' : 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.',
'DROP_DOWN_LISTS_8' : 'Да, обязательно. Всем самокатов! И Москве, и Московской области.',
'MADE_ORDER_TITLE_WINDOW' : 'Заказ оформлен',
'DZEN_URL': 'https://dzen.ru/?yredirect=true'
}

drop_down_lists_test_data =                                        [
[MPL.IMPORTANT_QUESTIONS_1, const['DROP_DOWN_LISTS_1']],
[MPL.IMPORTANT_QUESTIONS_2, const['DROP_DOWN_LISTS_2']],
[MPL.IMPORTANT_QUESTIONS_3, const['DROP_DOWN_LISTS_3']],
[MPL.IMPORTANT_QUESTIONS_4, const['DROP_DOWN_LISTS_4']],
[MPL.IMPORTANT_QUESTIONS_5, const['DROP_DOWN_LISTS_5']],
[MPL.IMPORTANT_QUESTIONS_6, const['DROP_DOWN_LISTS_6']],
[MPL.IMPORTANT_QUESTIONS_7, const['DROP_DOWN_LISTS_7']],
[MPL.IMPORTANT_QUESTIONS_8, const['DROP_DOWN_LISTS_8']]
                                                                    ]
