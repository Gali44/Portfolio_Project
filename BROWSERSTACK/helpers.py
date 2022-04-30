import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import WebDriverException as WDE

# main_url
url = "https://qasvus.wixsite.com/ca-marketing"


# main_email
main_email = "mailto:qasv.us@gmail.com"


# assert page title
def assert_title(smt, driver):
    assert smt in driver.title
    print("The title of the page is:", driver.title)


# assert title for back page
def assert_back_title(driver):
    assert "California Marcketing" in driver.title
    print("Back to the main page")


# assert title with different attribute
def check_title(a, driver):
    assert a in driver.title
    print(f'The title of the {a} is:', driver.title)


# icons XPATH
facebook = "//img[@alt='Facebook']"
twitter = "//img[@alt='Twitter']"
vk = "//img[@alt='VK Share']"
youtube = "//img[@alt='YouTube']"
linkedin = "//img[@alt='LinkedIn']"


# set up random delay
def delay_1_5():
    time.sleep(random.randint(1, 5))


# function for switching windows
def switching_windows(driver):
    wait = WebDriverWait(driver, 3)
    original_window = driver.current_window_handle
    wait.until(EC.number_of_windows_to_be(2))
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break


# function to check the logo
def logo_check(smt, path, driver):
    wait = WebDriverWait(driver, 3)
    try:
        wait.until(
            EC.visibility_of_element_located((By.XPATH, path)))
        print(f'We have {smt} logo')
    except WDE:
        print(f'Smt is wrong with {smt} logo')
        driver.get_screenshot_as_file(f'{smt}_logo_loading_error.png')
        driver.save_screenshot(f'{smt}_logo_loading_error.png')


# function to check the specific element on the page
def specific_element_check(smt, path, driver):
    wait = WebDriverWait(driver, 3)
    try:
        wait.until(
            EC.visibility_of_element_located((By.XPATH, path)))
        print(f'The right {smt} page')
    except WDE:
        print(f'Check {smt} page')
        driver.get_screenshot_as_file(f'{smt} _link_error.png')
        driver.save_screenshot(f'{smt} _link_error.png')


# function product color
def product_color(path, colorr, driver):
    color = driver.find_element(By.XPATH, path).text
    if colorr in color:
        print("Correct color")
    else:
        print("Wrong color")


# compare text
def comparison_xpath(path, argument, text, driver):
    if driver.find_element(By.XPATH, path).text == argument:
        print(f'Correct {text}')
    else:
        print(f'Incorrect {text}')


# compare text
def comparison_class(path, argument, text, driver):
    if driver.find_element(By.CLASS_NAME, path).text == argument:
        print(f'Correct {text}')
    else:
        print(f'Incorrect {text}')
