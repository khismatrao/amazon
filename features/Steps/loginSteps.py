import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@given('browser is open')
def launchBrowser(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.maximize_window()


@when('user is on login page')
def loginpage(context):
    context.driver.get(r"https://www.amazon.in/gp/css/homepage.html?ref_=nav_youraccount_btn")
    time.sleep(5)
    #context.driver.implicit_wait(5)
    context.driver.find_element_by_id("nav-link-accountList").click()
    time.sleep(5)




@when('user enter username')
def enterUsername(context):
    username = context.driver.find_element_by_id("ap_email")
    #username = context.driver.find_element(By.XPATH, value="//input[@id='ap_email']")
    username.send_keys("ishwarikhismatrao31@gmail.com")


@when('Click on the continue button')
def clickBtn(context):
    continueBtn = context.driver.find_element(By.XPATH, value="//input[@id='continue']")
    continueBtn.click()



@then('user enter password')
def enterPassword(context):
    password = context.driver.find_element(By.XPATH, value="//input[@id='ap_password']")
    password.send_keys("Sonali@123")
    time.sleep(5)


@then('Click on the submit button')
def clickSubmitBtn(context):
    #actualText = ""
    context.driver.find_element_by_id("signInSubmit").click()
    #submitbtn = context.driver.find_element(By.XPATH, value="//input[@id='signInSubmit']")
    #submitbtn.click()
    # expectedText = "sign-in"
    time.sleep(7)
    # try:
    #     actualText = context.driver.find_element_by_id("//h1[@class='a-spacing-small']").text
    # except:
    #     context.driver.close()
    #     assert True, "Test case pass"
    #
    # #if actualText == expectedText:
    #     context.driver.close()
    #     assert False,"Test case fail"

    # actualText = context.driver.find_element_by_xpath("//h1[@class='a-spacing-small']").text
    # assert context.actualText == "sign-in" ,"Test case passed"
    # print("hello")
    # context.driver.close()
    #
@then('user navigated to home page')
def homePage(context):
    #try:
    actualText = context.driver.find_element(By.XPATH,value="//span[@id='nav-link-accountList-nav-line-1']").text
    assert actualText == "Hello, Ishwari", "Test case passed"
    print("hello")
    context.driver.close()

    # except:
    #      print("Test case failed")
    #      context.driver.close()

@then('close browser')
def closeBrowser(context):
    context.driver.close()
