import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

@given(u'I launch browser is open')
def step_impl(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.maximize_window()


@when(u'user is on login page url')
def step_impl(context):
    context.driver.get(r"https://www.amazon.in/gp/css/homepage.html?ref_=nav_youraccount_btn")
    time.sleep(5)
    # context.driver.implicit_wait(5)
    context.driver.find_element_by_id("nav-link-accountList").click()
    time.sleep(5)


@when(u'user enter "{user}"')
def step_impl(context , user):
    username = context.driver.find_element_by_id("ap_email")
    # username = context.driver.find_element(By.XPATH, value="//input[@id='ap_email']")
    username.send_keys(user)


@when(u'Click on the continue btn')
def step_impl(context):
    continueBtn = context.driver.find_element(By.XPATH, value="//input[@id='continue']")
    continueBtn.click()


@then(u'user enter "{pwd}"')
def step_impl(context, pwd):
    password = context.driver.find_element(By.XPATH, value="//input[@id='ap_password']")
    password.send_keys(pwd)
    time.sleep(5)


@then(u'Click on the submit btn')
def step_impl(context):
    context.driver.find_element_by_id("signInSubmit").click()
    # submitbtn = context.driver.find_element(By.XPATH, value="//input[@id='signInSubmit']")
    # submitbtn.click()
    time.sleep(7)


@then(u'close chrome browser')
def step_impl(context):
    context.driver.close()
