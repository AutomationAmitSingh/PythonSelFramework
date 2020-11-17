
from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self,getData):
        log = self.getLogger()
        homepage= HomePage(self.driver)
        log.info("first name is "+getData["First Name"])
        homepage.getName().send_keys(getData["First Name"])
        homepage.getEmail().send_keys(getData["Last Name"])
        homepage.getCheckBox().click()
        self.selectOptionByText(homepage.getGender(), getData["Gender"])

        homepage.submitForm().click()

        alertText = homepage.getSuccessMessage().text

        assert ("Success" in alertText)
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData("TC1"))
    def getData(self, request):
        return request.param

