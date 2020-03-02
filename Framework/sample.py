from selenium import webdriver
import pytest


class Test:
    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Firefox()

    def test_check(self, setup):
        self.driver.get("https://github.com/mozilla/geckodriver/releases")
