# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

class TestThe():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_the(self):
    self.driver.get("https://www.thedigitalcraft.com/home")
    self.driver.set_window_size(1382, 744)
    self.driver.find_element(By.ID, "live-events").click()
    self.driver.find_element(By.ID, "first_name").click()
    self.driver.find_element(By.ID, "first_name").send_keys("vidya")
    self.driver.find_element(By.ID, "last_name").click()
    self.driver.find_element(By.ID, "last_name").send_keys("prasad")
    self.driver.find_element(By.ID, "email").click()
    self.driver.find_element(By.ID, "email").send_keys("vidyap2djx@gmail.com")
    self.driver.find_element(By.ID, "question").click()
    self.driver.find_element(By.ID, "question").send_keys("it is just not a question testing with selenium ide thankyou")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
  
