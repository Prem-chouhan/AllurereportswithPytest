from selenium import webdriver
import pytest


class TestHtml:

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Firefox()
        yield
        self.driver.close()

    def test_homePage(self, setup):
        self.driver.get("https://www.google.com/")
        assert self.driver.title == "Google"


# if __name__ == "__main__":
#     pytest.main()
