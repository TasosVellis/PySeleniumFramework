from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.HomePage import HomePage
from PageObjects.CheckOutPage import CheckOutPage
from Utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkOutPage = homePage.shopItems()
        log.info("Getting all the card titles")
        cards = checkOutPage.getCardTitles()
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkOutPage.getCardFooter()[i].click()
        self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
        confirmpage = checkOutPage.checkOutItems()
        log.info("Entering country name")
        self.driver.find_element_by_id("country").send_keys("gre")
        self.verifyLinkPresense("Greece")
        self.driver.find_element_by_link_text("Greece").click()
        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element_by_css_selector("[value='Purchase']").click()
        successText = self.driver.find_element_by_class_name("alert-success").text
        log.info("Text received from application is "+successText)

        assert "Success! Thankasdasdg you!" in successText

        self.driver.get_screenshot_as_file("screen.png")
