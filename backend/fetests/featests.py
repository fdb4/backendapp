import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import  Service
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.keys import Keys
import pytest
service=Service()
driver=webdriver.Chrome(service=service)
driver.get("http://localhost:3000")
def test_registration():

    try:
        WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, '//button[text()="SIGN UP"]')))
    except:
        assert True is False
    try:
        driver.find_element(By.XPATH, '//button[text()="SIGN UP"]').click()
        WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, '//button[text()="Sign Up"]')))
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
            WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.CLASS_NAME, "error-message")))
        except:
            assert True is False
        driver.find_element(By.NAME, "password").clear()
        WebDriverWait(driver, 10).until(ec.text_to_be_present_in_element_value((By.NAME, "password"),""))
        driver.find_element(By.NAME, "password").send_keys("Password")
        driver.find_element(By.XPATH, '//button[text()="Login"]').click()
    except:
        assert True is False
    try:
        WebDriverWait(driver,10)
        WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, '//button[text()="Submit Survey"]')))
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
        WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, '//button[text()="Submit Survey"]')))
        driver.find_element(By.XPATH, '//button[text()="Submit Survey"]').click()
    except:
        assert True is False

def test_DLog():
    try:#This Code is just a mess
        WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.LINK_TEXT, 'Daily Log')))
        driver.find_element(By.LINK_TEXT, 'Daily Log').click()
    except:
        assert True is False
    try:
        #water=driver.find_element(By.NAME, "calorie")#Idk why this works but it works
        #water.send_keys("2000")
        #
        try:
            WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.NAME, "mood")))
            driver.find_element(By.NAME, "mood").send_keys(Keys.LEFT)
            WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, '(//input[@name="calorie"])')))
            driver.find_element(By.XPATH, '(//input[@name="calorie"])').send_keys("2000")
        except:
            driver.get("http://localhost:3000/dailylog")
            driver.find_element(By.NAME, "mood").send_keys(Keys.LEFT)
            WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, '(//input[@name="calorie"])')))
            driver.find_element(By.XPATH, '(//input[@name="calorie"])').send_keys("2000")
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.NAME, "water")))
        driver.find_element(By.NAME, "water").send_keys("2000")
        driver.find_element(By.CLASS_NAME,"submit-button").click()

    except:
        assert True is False
def test_workouts():
    try:
        WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.LINK_TEXT, "Workouts")))
        driver.find_element(By.LINK_TEXT, 'Workouts').click()
        WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.CLASS_NAME, 'green')))
        driver.find_element(By.CLASS_NAME, 'green').click()
        WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, '//button[text()="Create Workout"]')))
        driver.find_element(By.XPATH, '//button[text()="Create Workout"]').click()
        WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.NAME, 'planName')))
        driver.find_element(By.NAME, 'planName').send_keys("MyWOPlan")
        driver.find_element(By.XPATH,'//button[text()="Add Exercise"]').click()
        WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, '(//select[@name="workoutID"])[1]')))
        select = Select(driver.find_element(By.XPATH, '(//select[@name="workoutID"])[1]'))
        select.select_by_value("5")
        WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.NAME, 'Sets')))
        driver.find_element(By.NAME, 'Sets').send_keys("20")
        WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.NAME, 'reps')))
        driver.find_element(By.NAME, 'reps').send_keys("20")
        #Second Excersie
        driver.find_element(By.XPATH, '//button[text()="Add Exercise"]').click()
        select = Select(driver.find_element(By.XPATH, '(//select[@name="workoutID"])[2]'))
        select.select_by_value("8")
        WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, '(//input[@name="Sets"])[2]')))
        driver.find_element(By.XPATH, '(//input[@name="Sets"])[2]').send_keys("20")
        WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, '(//input[@name="reps"])[2]')))
        driver.find_element(By.XPATH, '(//input[@name="reps"])[2]').send_keys("20")
        driver.find_element(By.XPATH, '//button[text()="Submit Workout Plan"]').click()

    except:
        assert True is False
def test_VWO():#ViewWorkout
    #Dumbbell Flyes
    #Lat Pulldowns
    try:
        driver.refresh()
        WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.CLASS_NAME,'workout-header')))
        driver.find_element(By.CLASS_NAME,'workout-header').click()
        WebDriverWait(driver,10).until(ec.text_to_be_present_in_element((By.CLASS_NAME,"exercise-list"),"Dumbbell Flyes"))
        WebDriverWait(driver,10).until(ec.text_to_be_present_in_element((By.CLASS_NAME,"exercise-list"),"Lat Pulldowns"))

    except:
        assert True is False

def test_coachreq():
    try:
        WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.LINK_TEXT, "Coaches")))
        driver.find_element(By.LINK_TEXT, 'Coaches').click()
        try:
            driver.find_element(By.XPATH, '(//a[@href="/coaches/1"])[1]').click()#just a selneium problem
        except:
            driver.get("http://localhost:3000/coaches/1")
        WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH,'(//button[@id="view"])[2]')))
        driver.find_element(By.XPATH,'(//button[@id="view"])[2]')

    except:
        assert True is False
def test_sendMessage():
    try:
        driver.refresh()
        WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, '(//button[@id="view"])[1]')))
        driver.find_element(By.XPATH, '(//button[@id="view"])[1]').click()
        WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, '//textarea[@id="message"]')))
        driver.find_element(By.XPATH,'//textarea[@id="message"]').send_keys("This is my message")
        WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, '//button[text()="Send Message"]')))
        driver.find_element(By.XPATH, '(//button[text()="Send Message"])[2]').click()
    except:
        assert True is False
def test_delp():
    try:
        WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, '//img[@alt="User Profile"]')))
        driver.find_element(By.XPATH, '//img[@alt="User Profile"]').click()
        #driver.find_element(By.XPATH, '//img[@alt="User Profile"]').click()#once again no idea why
        driver.find_element(By.XPATH, '//img[@alt="Settings Icon"]').click()
        WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, '//button[text()="Delete"]')))
        driver.find_element(By.XPATH, '//button[text()="Delete"]').click()
        WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, '//button[text()="Yes"]')))
        driver.find_element(By.XPATH, '//button[text()="Yes"]').click()
    except:
        assert True is False
'''
    
def test_login():
    driver.get("http://localhost:3000")
    try:
        WebDriverWait(driver,10).until(ec.element_to_be_clickable((By.XPATH,'//a[text()="LOGIN"]')))
    except:
        assert True is False
    driver.find_element(By.XPATH,'//a[text()="LOGIN"]').click()
    driver.find_element(By.NAME,"email").send_keys("kirt@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("Passwords")
    driver.find_element(By.XPATH, '//button[text()="Login"]').click()
    try:
        WebDriverWait(driver,10).until(ec.presence_of_element_located((By.CLASS_NAME,"error-message")))
    except:
        assert True is False
    driver.find_element(By.NAME, "password").send_keys("Passwords")
    driver.find_element(By.XPATH,'//button[text()="Login"]').click()'''
