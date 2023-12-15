import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import  Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.keys import Keys
import pytest
service=Service()
driver=webdriver.Chrome(service=service)
driver.get("http://localhost:3000")
def test_registration():

    try:
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '//button[text()="SIGN UP"]')))
    except:
        assert True is False
    try:
        driver.find_element(By.XPATH, '//button[text()="SIGN UP"]').click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '//button[text()="Sign Up"]')))
        driver.find_element(By.NAME, "firstname").send_keys("feat")
        driver.find_element(By.NAME, "lastname").send_keys("ures")
        driver.find_element(By.NAME, "email").send_keys("ures@gmail.com")
        driver.find_element(By.NAME, "password").send_keys("Password")
        select=Select(driver.find_element(By.NAME,"userType"))
        select.select_by_value("client")
        driver.find_element(By.XPATH, '//button[text()="Sign Up"]').click()
    except:
        assert True is False
def test_clientlogin():
    try:
        driver.find_element(By.XPATH, '//a[text()="LOGIN"]').click()
        driver.find_element(By.NAME, "email").send_keys("ures@gmail.com")
        driver.find_element(By.NAME, "password").send_keys("Passwords")
        driver.find_element(By.XPATH, '//button[text()="Login"]').click()
        try:
            WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "error-message")))
        except:
            assert True is False
        driver.find_element(By.NAME, "password").clear()
        driver.find_element(By.NAME, "password").send_keys("Password")
        driver.find_element(By.XPATH, '//button[text()="Login"]').click()
    except:
        assert True is False
    try:
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '//button[text()="Submit Survey"]')))
        select = Select(driver.find_element(By.NAME, "height"))
        select.select_by_value(r"5'0")
        driver.find_element(By.NAME, "weight").send_keys("150")
        driver.find_element(By.NAME, "age").send_keys("40")
        select = Select(driver.find_element(By.NAME, "gender"))
        select.select_by_value(r"male")
        driver.find_element(By.NAME, "goalweight").send_keys("140")
        select = Select(driver.find_element(By.NAME, "movement"))
        select.select_by_value(r"sedentary")
        select = Select(driver.find_element(By.NAME, "cycling"))
        select.select_by_value(r"yes")
        select = Select(driver.find_element(By.NAME, "strength"))
        select.select_by_value(r"yes")
        select = Select(driver.find_element(By.NAME, "running"))
        select.select_by_value(r"no")
        select = Select(driver.find_element(By.NAME, "sports"))
        select.select_by_value(r"yes")
        select = Select(driver.find_element(By.NAME, "yoga"))
        select.select_by_value(r"no")
        select = Select(driver.find_element(By.NAME, "swimming"))
        select.select_by_value(r"yes")
        select = Select(driver.find_element(By.NAME, "martialarts"))
        select.select_by_value(r"yes")
        driver.find_element(By.NAME, "other").send_keys("Just your average client")
        driver.find_element(By.XPATH, '//button[text()="Submit Survey"]').click()
    except:
        assert True is False

def test_DLog():
    try:
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '//a[text()="Daily Log"]')))
        driver.find_element(By.XPATH, '//a[text()="Daily Log"]').click()
        driver.find_element(By.NAME, "water").send_keys("2000")
        driver.find_element(By.NAME, "calorie").send_keys("2000")
        driver.find_element(By.NAME,"mood").send_keys(Keys.LEFT)
        driver.find_element(By.NAME,"mood").send_keys(Keys.LEFT)
        driver.find_element(By.XPATH, '//button[text()="Submit"]').click()
    except:
        assert True is False
'''def test_login():
    driver.get("http://localhost:3000")
    try:
        WebDriverWait(driver,10).until(expected_conditions.element_to_be_clickable((By.XPATH,'//a[text()="LOGIN"]')))
    except:
        assert True is False
    driver.find_element(By.XPATH,'//a[text()="LOGIN"]').click()
    driver.find_element(By.NAME,"email").send_keys("kirt@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("Passwords")
    driver.find_element(By.XPATH, '//button[text()="Login"]').click()
    try:
        WebDriverWait(driver,10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"error-message")))
    except:
        assert True is False
    driver.find_element(By.NAME, "password").send_keys("Passwords")
    driver.find_element(By.XPATH,'//button[text()="Login"]').click()'''
