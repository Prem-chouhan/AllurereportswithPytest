from allure_commons.types import AttachmentType
from selenium import webdriver
import pytest
import allure


@allure.severity(allure.severity_level.NORMAL)
class TestAllure:

    @allure.severity(allure.severity_level.MINOR)
    def test_Site(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.google.com/")
        status = self.driver.find_element_by_xpath("//*[@id='hplogo']").is_displayed()
        if status:
            assert True
        else:
            assert False
        self.driver.close()

    def test_skip(self):
        pytest.skip("I am Skipping to test method")

    @allure.severity(allure.severity_level.CRITICAL)
    def test_title(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.google.com/")
        present_title = self.driver.title
        if present_title == "Google123":
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Testlogin", attachment_type=AttachmentType.PNG)
            assert False
        self.driver.close()
