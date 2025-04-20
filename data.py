from selenium import webdriver
from locators.main_page_locators import MainPageLocators as MPL

firefox_options = webdriver.FirefoxOptions()
#firefox_options.add_argument('--headless')
firefox_options.add_argument('--window-size=1024,768')

const = {
'webpage' : 'https://qa-scooter.praktikum-services.ru/',
'wait_timer' : 10
}

control_words = {
'drop_down_lists_1' : 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.',
'drop_down_lists_2' : 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.',
'drop_down_lists_3' : 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.',
'drop_down_lists_4' : 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.',
'drop_down_lists_5' : 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.',
'drop_down_lists_6' : 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.',
'drop_down_lists_7' : 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.',
'drop_down_lists_8' : 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
}

drop_down_lists_test_data =                                        [
[MPL.IMPORTANT_QUESTIONS_1, control_words['drop_down_lists_1']],
[MPL.IMPORTANT_QUESTIONS_2, control_words['drop_down_lists_2']],
[MPL.IMPORTANT_QUESTIONS_3, control_words['drop_down_lists_3']],
[MPL.IMPORTANT_QUESTIONS_4, control_words['drop_down_lists_4']],
[MPL.IMPORTANT_QUESTIONS_5, control_words['drop_down_lists_5']],
[MPL.IMPORTANT_QUESTIONS_6, control_words['drop_down_lists_6']],
[MPL.IMPORTANT_QUESTIONS_7, control_words['drop_down_lists_7']],
[MPL.IMPORTANT_QUESTIONS_8, control_words['drop_down_lists_8']]
                                                                    ]