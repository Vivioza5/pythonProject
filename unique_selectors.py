from selenium import webdriver
import time

link1 = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link1)
    input1 = browser.find_element_by_css_selector("div.first_block input.form-control.first")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector("div.first_block input.form-control.second")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector("div.first_block input.form-control.third")
    input3.send_keys("Petrov@gmail.com")
    input4 = browser.find_element_by_css_selector("div.second_block input.form-control.first")
    input4.send_keys("0986134770")
    input5 = browser.find_element_by_css_selector("div.second_block input.form-control.second")
    input5.send_keys("Smolensk")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(10)
    welcome_text_elt = browser.find_element_by_tag_name("h1")

    assert "Congratulations! You have successfully registered!" == welcome_text_elt.text

finally:
    time.sleep(10)
    browser.quit()



