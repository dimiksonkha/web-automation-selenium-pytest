"""
These tests cover Tools QA home page tests.

"""

import pytest
from pages.form import FormPage
from pages.home import HomePage



def test_form_submission(driver):
  home_page = HomePage(driver)

  assert driver.current_url == "https://demoqa.com/"
  
  home_page.visit_form_page()

  assert driver.current_url == "https://demoqa.com/forms"
  
  form_page = FormPage(driver)
  
  assert driver.current_url == "https://demoqa.com/automation-practice-form"

  
  
  