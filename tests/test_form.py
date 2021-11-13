"""
These tests cover Tools QA home page tests.

"""
import time
from selenium.webdriver.common.by import By
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

  form_page.type_first_name('Hilsa')
  form_page.type_last_name('Fish')
  form_page.type_user_email(form_page.get_random_email())
  form_page.select_gender('male')
  form_page.type_user_number('1785452564')
  form_page.close_ads()
  form_page.type_date_of_birth("10-10-2021")
  form_page.type_subject('Hilsa Project')
  form_page.select_hobby("sports","music")
  form_page.select_file_for_picture_upload("fish.jpg")
  form_page.select_state_from_state_dropdown("Rajasthan")
  form_page.select_city_from_city_dropdown("Jaipur")
  form_page.submit_form()
  form_page.close_modal()


  
  