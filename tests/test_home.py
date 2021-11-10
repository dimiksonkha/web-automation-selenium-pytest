"""
These tests cover Tools QA home page tests.

"""

import pytest
from pages.home import HomePage



def test_form_submission(driver):
  home_page = HomePage(driver)
  home_page.visit_form_page()
  assert driver.current_url == "https://demoqa.com/forms"
  