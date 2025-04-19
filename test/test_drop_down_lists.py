import pytest
from data import  TestClass, const, control_words
from page_objects.main_page import MainPage
from locators.main_page_locators import MainPageLocators as MPL


drop_down_lists_test_data =                                                         [
[MPL.IMPORTANT_QUESTIONS_1, control_words['drop_down_lists_1']],
[MPL.IMPORTANT_QUESTIONS_2, control_words['drop_down_lists_2']],
[MPL.IMPORTANT_QUESTIONS_3, control_words['drop_down_lists_3']],
[MPL.IMPORTANT_QUESTIONS_4, control_words['drop_down_lists_4']],
[MPL.IMPORTANT_QUESTIONS_5, control_words['drop_down_lists_5']],
[MPL.IMPORTANT_QUESTIONS_6, control_words['drop_down_lists_6']],
[MPL.IMPORTANT_QUESTIONS_7, control_words['drop_down_lists_7']],
[MPL.IMPORTANT_QUESTIONS_8, control_words['drop_down_lists_8']]
                                                                                    ]

class TestDropDownLists(TestClass):
    driver = None

    @pytest.mark.parametrize('pointer_of_object,result', drop_down_lists_test_data)
    def test_drop_down_lists(self, pointer_of_object,result):
        self.driver.get(const['webpage'])
        main_page = MainPage(self.driver)
        main_page.check_drop_down_lists(target=pointer_of_object, expected_value=result)
