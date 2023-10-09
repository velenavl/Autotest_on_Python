from testpage_1 import OperationsHelper
import logging
import time


def test_step1(browser):
    logging.info('Test Starting')
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login('KiraZ2')
    testpage.enter_pass('gi89mjb90f')
    testpage.click_login_button()
    testpage.click_contact_button()
    time.sleep(4)
    testpage.enter_name('Kira Andreeva')
    testpage.enter_email('velernavl@inbox.ru')
    testpage.enter_content('Test Text')
    time.sleep(4)
    testpage.click_contact_us_button()
    time.sleep(4)
    assert testpage.alert() == 'Form successfully submitted'
