from driver.driver import driver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from faker import Faker
import unittest

faker = Faker()
full_name = faker.name()
first_name = full_name.split()[0]
last_name = full_name.split()[1]
domain = "@gmail.com"
password = "very_secret_password"


def fill_details():
    driver.find_element_by_name('firstname').send_keys(first_name)
    driver.find_element_by_name('lastname').send_keys(last_name)
    driver.find_element_by_name('reg_email__').send_keys(first_name + '.' + last_name + domain)
    driver.find_element_by_name('reg_email_confirmation__').send_keys(first_name + '.' + last_name + domain)
    driver.find_element_by_name('reg_passwd__').send_keys(password)


def set_birthday():
    month = Select(driver.find_element_by_id('month'))
    month.select_by_value("7")
    day = Select(driver.find_element_by_id('day'))
    day.select_by_value("15")
    year = Select(driver.find_element_by_id('year'))
    year.select_by_value("1990")

class TestFB(unittest.TestCase):

    def test_sign_up_to_fb(self):
        driver.get('https://www.facebook.com/')
        self.assertTrue('Facebook' in driver.title)
        fill_details()
        set_birthday()
        sign_up_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "websubmit"))
        )
        sign_up_button.click()

        error_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "_5633"))
        )

        assert error_message.text in 'Please choose a gender. You can change who can see this later.'

    def tearDown(self):
        driver.close()


if __name__ == '__main__':
    unittest.main()
