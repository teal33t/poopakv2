import unittest

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import *
from actions import log, random_useragent


class Spider(unittest.TestCase):
    options = None
    profile = None
    capabilities = None

    # Setup options for webdriver
    def setUpOptions(self):
        self.options = webdriver.FirefoxOptions()
        self.options.headless = HEADLESS

    # Setup profile
    def setUpProfile(self):
        self.profile = webdriver.FirefoxProfile()

        if DISABLE_IMAGE_LOAD:
            self.profile.set_preference('permissions.default.image', 2)
            self.profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')

        if USER_AGENT_ROTATE:
            self.profile.set_preference("general.useragent.override", random_useragent())

        self.profile.update_preferences()

    # Enable Marionette, An automation driver for Mozilla's Gecko engine
    def setUpCapabilities(self):
        self.capabilities = webdriver.DesiredCapabilities.FIREFOX
        self.capabilities['marionette'] = True

    # Setup settings
    def setUp(self):
        self.setUpProfile()
        self.setUpOptions()
        self.setUpCapabilities()

        if USE_PROXY:
            self.setUpProxy()

        self.driver = webdriver.Firefox(options=self.options, capabilities=self.capabilities,
                                        firefox_profile=self.profile, executable_path=executable_path)

    # Main function

    def test_run(self):
        driver = self.driver

        log("Start get")
        driver.get(START_URL)
        log("End get")

    def tearDown(self):
        log("Good bye")
        self.driver.close()


if __name__ == "__main__":
    unittest.main()