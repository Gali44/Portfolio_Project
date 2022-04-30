import time
import unittest
from faker import Faker
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import WebDriverException as WDE
import helpers as HP
import my_key_browserstack as KEY


class windows_10_1920_1080_chrome(unittest.TestCase):

    def setUp(self):
        desired_cap = {
            'os_version': '10',
            'resolution': '1920x1080',
            'browser': 'Chrome',
            'browser_version': 'latest',
            'os': 'Windows',
            'name': 'BStack-[Python] Sample Test',  # test name
            'build': 'BStack Build Number 1' # CI/CD job or build name
        }
        url = KEY.my_key
        desired_cap['acceptSslCerts'] = True
        self.driver = webdriver.Remote(command_executor=url, desired_capabilities=desired_cap)

    # check if social media icons are clickable
    def test_icons_clickability(self):
        driver = self.driver
        driver.get(HP.url)
        self.driver.maximize_window()

        # random delay function, helper
        HP.delay_1_5()

        # check the title is right, helper
        HP.assert_title("California Marcketing", driver)

        # set up wait time
        wait = WebDriverWait(driver, 3)

        # verify icons are clickable, helpers
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.facebook)))
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.twitter)))
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.vk)))
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.youtube)))
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.linkedin)))
            print("Icons are clickable")
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "All icons are clickable"}}')
        except WDE:
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Some icons are not clickable"}}')
            raise Exception("Check icons clickability")
        driver.quit()

    # validate all social network links lead to right pages
    def test_social_network_links(self):
        driver = self.driver
        driver.get(HP.url)
        self.driver.maximize_window()

        # random delay function, helper
        HP.delay_1_5()

        # check the title is right, helper
        HP.assert_title("California Marcketing", driver)

        # find Facebook icon and click
        driver.find_element(By.XPATH, HP.facebook).click()

        # original window set up
        original_window = driver.current_window_handle

        # switch windows if more than one, helper
        HP.switching_windows(driver)

        # random delay, helper
        HP.delay_1_5()

        # verify you are on the right page, helper
        HP.assert_title("Facebook", driver)

        # verify logo, try/except, plus screenshots, helper
        HP.logo_check("Facebook", "//div[@class='l9j0dhe7 buofh1pr j83agx80 bp9cbjyn']", driver)

        # verify the specific element, try/except, plus screenshots, helper
        HP.specific_element_check("Facebook", "//a[contains(text(), 'QA at Silicon Valley California')]", driver)

        # close and switch back
        driver.close()
        driver.switch_to.window(original_window)

        # verify the title of the page when back, helper
        HP.assert_back_title(driver)

        # find TW icon and click
        driver.find_element(By.XPATH, HP.twitter).click()

        # switch windows if more than one, helper
        HP.switching_windows(driver)

        HP.delay_1_5()

        # verify you are on the right page
        HP.assert_title("Твиттер", driver)

        # verify logo, try/except, plus screenshots, helper
        HP.logo_check("TW", "//*[@role='heading']", driver)

        # verify the specific element, try/except, plus screenshots, helper
        HP.specific_element_check("TW", "//a[@dir='ltr'][contains(.,'http://QASV.US')]", driver)

        # close and switch back
        driver.close()
        driver.switch_to.window(original_window)

        # verify the title of the page when back, helper
        HP.assert_back_title(driver)

        # find VK icon and click
        driver.find_element(By.XPATH, HP.vk).click()

        # switch windows if more than one, helper
        HP.switching_windows(driver)

        HP.delay_1_5()

        # verify you are on the right page
        HP.assert_title("QA at Silicon Valley", driver)

        # verify logo, try/except, plus screenshots, helper
        HP.logo_check("VK", "//*[@class='HeaderNav__item HeaderNav__item--logo']", driver)

        # verify the specific element, try/except, plus screenshots, helper
        HP.specific_element_check("VK", "//*[@href='/away.php?to=https%3A%2F%2Fbit.ly%2F2Q8bBhW&cc_key=']", driver)

        # close and switch back
        driver.close()
        driver.switch_to.window(original_window)

        # verify the title of the page when back, helper
        HP.assert_back_title(driver)

        # find TouTube icon and click
        driver.find_element(By.XPATH, HP.youtube).click()

        # switch windows if more than one, helper
        HP.switching_windows(driver)

        HP.delay_1_5()

        # verify you are on the right page
        HP.assert_title("Sergey Efremov", driver)

        # verify logo, try/except, plus screenshots, helper
        HP.logo_check("YouTube", "//*[@id='logo-icon']", driver)

        # verify the specific element, try/except, plus screenshots, helper
        HP.specific_element_check("YouTube", "//*[contains(text(), 'Sergey Efremov_USA')]", driver)

        # close and switch back
        driver.close()
        driver.switch_to.window(original_window)

        # verify the title of the page when back, helper
        HP.assert_back_title(driver)

        # find LinkedIn icon and click
        driver.find_element(By.XPATH, HP.linkedin).click()

        # switch windows if more than one, helper
        HP.switching_windows(driver)

        HP.delay_1_5()

        # verify you are on the right page
        HP.assert_title("LinkedIn", driver)

        # verify logo, try/except, plus screenshots, helper
        HP.logo_check("LinkedIn", "//*[@id='ember16']", driver)

        # verify the specific element, try/except, plus screenshots, helper
        HP.specific_element_check("LinkedIn", "//*[@alt='QA at Silicon Valley California logo']", driver)

        # close and switch back
        driver.close()
        driver.switch_to.window(original_window)

        # verify the title of the page when back, helper
        HP.assert_back_title(driver)
        driver.quit()

    # check "Get in touch"
    def test_get_in_touch(self):
        driver = self.driver
        driver.get(HP.url)
        self.driver.maximize_window()

        # check the title is right, helper
        HP.assert_title("California Marcketing", driver)

        # set wait time
        wait = WebDriverWait(driver, 3)

        # check 'Get in touch' clickability
        try:
            wait.until(EC.element_to_be_clickable(
                (By.CLASS_NAME, "wQYUw")))
            print("'Get in touch' clickable")
        except WDE:
            print("Check 'Get in touch' clickability")

        # check the button text is correct
        button_text = driver.find_element(By.CLASS_NAME, "wQYUw").text
        if button_text == "Get In Touch":
            print("Right 'Get in Touch' button text")
        else:
            print("Incorrect button text")

        # compare on site email with the correct one
        email = driver.find_element(By.LINK_TEXT, "Get In Touch").get_attribute("href")

        # print on page email and supposed email
        print(email)
        print(HP.main_email)

        # assert on page email
        if email == HP.main_email:
            print("The email is correct")
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "The email is correctt!"}}')
        else:
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "The email is not correct"}}')
            raise Exception("The email is not correct")
        driver.quit()

    # check header menu links (except "More")
    def test_header_menu_links(self):
        driver = self.driver
        driver.get(HP.url)
        self.driver.maximize_window()

        # check the title is right, helper
        HP.assert_title("California Marcketing", driver)

        # set wait time
        wait = WebDriverWait(driver, 5)

        # list for final assertion
        wrong_list = []

        # click 'Blog'
        wait.until(EC.element_to_be_clickable((By.XPATH, "//p[@class='_1zyfI'][contains(.,'Blog')]"))).click()
        WebDriverWait(driver, 3)

        # assert 'Blog' title, hepler
        HP.check_title('Blog', driver)

        # check specific element on the page
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'All Posts')]")))
            print("The right 'Blog' page")
        except WDE:
            wrong_blog = "Smt is wrong with 'Blog' page"
            print(wrong_blog)
            wrong_list.append(wrong_blog)

        # back in the browser
        driver.back()

        # click 'Shop'
        wait.until(EC.element_to_be_clickable((By.XPATH, "//p[@class ='_1zyfI'][contains(., 'Shop')]"))).click()
        WebDriverWait(driver, 3)

        # assert 'Shop' title, hepler
        HP.check_title('Shop', driver)

        # check specific element on the page
        try:
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//h3[contains(.,'Product 1')]")))
            print("The right 'Shop' page")
        except WDE:
            wrong_shop = "Smt is wrong with 'Shop' page"
            print(wrong_shop)
            wrong_list.append(wrong_shop)

        # back in the browser
        driver.back()

        # click 'Servises'
        wait.until(EC.element_to_be_clickable((By.XPATH, "//p[@class ='_1zyfI'][contains(., 'Servises')]"))).click()
        WebDriverWait(driver, 3)

        # assert 'Servises' title, hepler
        HP.check_title('Servises', driver)

        # check specific element on the page
        try:
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//h1[contains(.,'Our Services')]")))
            print("The right 'Servises' page")
        except WDE:
            wrong_servises = "Smt is wrong with 'Servises' page"
            print(wrong_servises)
            wrong_list.append(wrong_servises)

        # back in the browser
        driver.back()

        # click 'Home'
        wait.until(EC.element_to_be_clickable((By.XPATH, "//p[@class='_1zyfI'][contains(.,'Home')]"))).click()
        WebDriverWait(driver, 3)

        # assert 'Home' title, hepler
        HP.check_title('Home', driver)

        # check specific element on the page
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "(// span[contains(., 'LET CALIFORNIA MARKETING "
                                                                   "GROW YOUR BUSINECS')])[2]")))
            print("The right 'Home' page")
        except WDE:
            wrong_home = "Smt is wrong with 'Home' page"
            print(wrong_home)
            wrong_list.append(wrong_home)

        # assert the assertion list is empty
        print(len(wrong_list))
        if len(wrong_list) == 0:
            print("All header links work correctly")
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "All header links are correct!"}}')
        else:
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Not all header links are corrrect"}}')
            raise Exception("Check header links")
        driver.quit()

    # localization test of first screen
    def test_first_screen_text(self):
        driver = self.driver
        driver.get(HP.url)
        self.driver.maximize_window()

        # check the title is right, helper
        HP.assert_title("California Marcketing", driver)

        # get the text
        first_line = driver.find_element(By.XPATH, "//a[contains(.,'CALIFORNIA MARCKETING')]").text
        second_line = driver.find_element(By.XPATH,
                                          "(//a[@href='https://qasvus.wixsite.com/ca-marketing/blog'])[2]").text
        third_line = driver.find_element(By.XPATH,
                                         "(//span[contains(.,'LET CALIFORNIA MARKETING GROW YOUR BUSINECS')])[2]").text
        print(first_line, second_line, third_line)

        # compare on site text with correct one, first line
        if first_line == "CALIFORNIA MARKETING":
            print("First line is fine")
        else:
            print("Incorrect first line")

        # compare on site text with correct one, second line
        if second_line == "A Full-Stack Creative Agency in CA":
            print("Second line is fine")
        else:
            print("Incorrect second line")

        # compare on site text with correct one, third line
        if third_line == "LET CALIFORNIA MARKETING GROW YOUR BUSINESS":
            print("Third line is fine")
        else:
            print("Incorrect third line")

        # assert full text
        if [first_line, second_line, third_line] == ["CALIFORNIA MARKETING", "A Full-Stack Creative "
                                                                                         "Agency in CA",
                                                                 'LET CALIFORNIA MARKETING GROW YOUR BUSINESS']:
            print("First screen text is correct")
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "First screen text is correct"}}')
        else:
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "First screen text is not correct""}}')
            raise Exception("Check the first screen text")
        driver.quit()

    # wix chat functionality
    def test_lets_chat(self):
        driver = self.driver
        driver.get(HP.url)
        self.driver.maximize_window()

        # check the title is right, helper
        HP.assert_title("California Marcketing", driver)

        # set up faker
        f = Faker()

        # assertion list
        list_for_assertion = []

        time.sleep(3)

        # find and switch to chat iframe
        iframe = driver.find_element(By.XPATH, "//iframe [@title='Wix Chat']")
        driver.switch_to.frame(iframe)

        # find and open the chat
        try:
            driver.find_element(
                locate_with(By.CLASS_NAME, "_28JNc").below({By.XPATH: "//*[@charset='utf-8']"})).click()
            ok_result = "Chat is on the page"
            print(ok_result)
            list_for_assertion.append(ok_result)
        except WDE:
            fail_result = "Smt is wrong with chat"
            print(fail_result)
            list_for_assertion.append(fail_result)

        time.sleep(3)

        # send fake text
        try:
            driver.find_element(By.TAG_NAME, "textarea").send_keys(f.text() + Keys.ENTER)
            ok_result = "The message was sent in the chat"
            print(ok_result)
            list_for_assertion.append(ok_result)
        except WDE:
            fail_result = "Smt is wrong with messages"
            print(fail_result)
            list_for_assertion.append(fail_result)

        # check if except prints in the list for final assertion
        list_for_assertion = ' '.join(list_for_assertion).split()
        if "wrong" not in list_for_assertion:
            print("The chat works correctly")
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Online chat works correctly!"}}')
        else:
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Smt is wrong with chat"}}')
            raise Exception("Check the chat")
        driver.quit()

    # video search bar functionality
    def test_video_selection(self):
        driver = self.driver
        driver.get(HP.url)
        self.driver.maximize_window()

        # check the title is right, helper
        HP.assert_title("California Marcketing", driver)

        time.sleep(2)

        # find video search bar and send "Big Sur"
        try:
            driver.find_element(
                locate_with(By.CLASS_NAME, "VVhXp").below({By.XPATH: "//*[@title='All Videos']"})).send_keys(
                "Big Sur" + Keys.ENTER)
            print("Search bar works")
        except WDE:
            print("Check the search bar")

        time.sleep(2)

        # assert video with "Big Sur" in the title is displayed
        if driver.find_element(By.XPATH, "//*[@src='https://i.ytimg.com/vi/X-HxnNAaioM/mqdefault.jpg']").is_displayed():
            print("The right video is displayed")
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "The right video is displayed!"}}')
        else:
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Сье is wrong with video search bar"}}')
            raise Exception("Check video search bar")
        driver.quit()

    # cart smoke testing
    def test_cart_shopping(self):
        driver = self.driver
        driver.get(HP.url)
        self.driver.maximize_window()

        # check the title is right, helper
        HP.assert_title("California Marcketing", driver)

        # set up wait time
        wait = WebDriverWait(driver, 3)

        # click 'Shop'
        shop = wait.until(EC.element_to_be_clickable((By.XPATH, "//p[@class ='_1zyfI'][contains(., 'Shop')]")))
        shop.click()

        time.sleep(5)

        # assert 'Shop' title, helper
        HP.check_title('Shop', driver)

        # check specific element on the page, helper
        HP.specific_element_check('Shop', "//h3[contains(.,'Product 1')]", driver)

        # find 'product1', get text and click
        product = driver.find_element(By.XPATH, "// h3[contains(.,'Product 1')]")
        product_text = product.text
        product.click()
        print("Successfully clicked on", product_text)

        time.sleep(5)

        # assert the title
        assert product_text in driver.title
        print("The right product page")

        # assert the product name on the page match the one was chosen
        on_page_product_text = driver.find_element(By.XPATH, "//h1[contains(@class,'2yxAN')]").text
        if product_text == on_page_product_text:
            print("Match:", product_text, "and", on_page_product_text)
        else:
            print("Not a match")

        # find price for one piece, turn into integer
        price = driver.find_element(By.XPATH, "//span[@data-hook='formatted-primary-price']").text
        price = int(price.replace("$", "").replace(".00", ""))
        print("The price for 1 piece is:", price)

        # set color and quantity
        try:
            driver.find_element(By.XPATH, "(//div[contains(@class,'ColorPickerItem2201735070__radioInner')])[1]").click()
            driver.find_element(By.XPATH, "//span[contains(@data-hook, 'number-input-spinner-up-arrow')]").click()
            print("The color and quantity were set")
        except WDE:
            print("Smt is wrong with color/quantity")

        # click on "Add to cart" button
        try:
            driver.find_element(By.XPATH,
                            "//span[@class ='buttonnext1002411228__content'][contains(., 'Add to Card')]").click()
            print("The product was added to cart")
        except WDE:
            print("Smt is wrong with adding to cart")

        time.sleep(5)

        # find curtain frame and switch
        try:
            driver.switch_to.frame(driver.find_element(By.CLASS_NAME, "_2DJg7"))
            print("Switched to frame")
        except WDE:
            print("Check the frame")

        # click on "View cart" button
        wait.until(EC.element_to_be_clickable((By.ID, "widget-view-cart-button"))).click()

        time.sleep(5)

        # assert title
        assert "Cart" in driver.title

        # assert specific element on the page
        my_cart = driver.find_element(By.CLASS_NAME, "_2NsyK").text
        if my_cart == "My cart":
            print("We are on the cart page")
        else:
            print("Check the cart page")

        # assert product name
        product_name = driver.find_element(By.CLASS_NAME, "_1dkgR").text
        if product_name == product_text:
            print("Right product in the cart")
        else:
            print("Wrong product in the cart")

        # check the quantity is correct
        howMany = driver.find_element(By.XPATH, "//input[@aria-label='Choose quantity']").get_attribute("value")
        if howMany == "2":
            print("Correct quantity")
        else:
            print("Wrong quantity")

        # check the price is correct
        total_price = driver.find_element(By.CLASS_NAME, "_32Pyj").text
        total_price = int(total_price.replace("$", "").replace(".00", ""))
        if total_price == int(howMany) * price:
            print("Correct total price")
        else:
            print("Wrong total price")

        # check the color is correct, helper
        HP.product_color("(//li[contains(.,'Color: Black')])[2]", "Black", driver)

        # find and click on 'CheckOut' button
        try:
            driver.find_element(By.CLASS_NAME, "_34QVp").click()
            print("Click on 'CheckOut' button")
        except WDE:
            print("Smt is wrong with 'CheckOut' button")

        time.sleep(5)

        # find iframe and switch
        try:
            driver.switch_to.frame(driver.find_element(By. CLASS_NAME, "MUsGO"))
            print("Switched to frame")
        except WDE:
            print("No frame")

        # assert the frame doesn't include "We can't accept online orders right now"
        fr2text = driver.find_element(By. CLASS_NAME, "maaPx").text
        print(fr2text)
        if "We can't accept online orders right now" not in fr2text:
            print("Checkout without 'cant accept online orders'")
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Checkout without: cant accept online orders"}}')
        else:
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Wrong checkout process"}}')
            raise Exception("Check checkout")
        driver.quit()

    # event reservation smoke testing
    def test_event_reservation(self):
        driver = self.driver
        driver.get(HP.url)
        self.driver.maximize_window()

        # set up faker library
        f = Faker()

        # set up wait time
        wait = WebDriverWait(driver, 3)

        # check the title is right, helper
        HP.assert_title("California Marcketing", driver)

        time.sleep(4)

        try:
            event = driver.find_element(By.XPATH, "(//a[@data-hook='ev-rsvp-button'][contains(.,'RSVP')])[1]")
            print("Event section")
        except WDE:
            print("Cant find event section")

        # name, date and place of the first event
        event_name = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "DTbMp"))).text
        print(event_name)
        event_date = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "VFsgs"))).text
        print(event_date)
        event_place = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "lNymU"))).text
        print(event_place)

        # click on "RSVP" button
        event.click()
        print("'RSVP' button was clicked")

        # assert title
        assert event_name in driver.title
        print("Its the middle event page")

        # check if event name, date and place are correct, helpers
        HP.comparison_xpath("//h1[@data-hook='event-title']", event_name, "event name", driver)
        HP.comparison_class("_6vtCb", event_date, "event date", driver)
        HP.comparison_class("-OEip", event_place, "event place", driver)

        # click on 'RSVP' button
        time.sleep(3)
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@data-hook='rsvp-button'][contains(.,'RSVP')])[2]"))).send_keys('\n')
        time.sleep(3)

        # assert driver title
        assert event_name in driver.title
        print("It`s the final event page")

        # check event name and place, helpers
        HP.comparison_xpath("//*[@data-hook='event-title']", event_name, "event name", driver)
        HP.comparison_xpath("//*[@data-hook='event-location']", event_place, "event place", driver)

        # fill the form
        driver.find_element(By.ID, "firstName").send_keys(f.first_name())
        driver.find_element(By.ID, "lastName").send_keys(f.last_name())
        driver.find_element(By.ID, "email").send_keys(f.email())

        # find and click on 'Submit' page
        try:
            driver.find_element(By.XPATH, "//button[@data-hook='form-button']").click()
            print("Submit button was clicked")
        except WDE:
            print("Check the 'Submit' button")

        time.sleep(5)

        # assert 'thank you' page
        if driver.find_element(By.XPATH, "//h2[@data-hook='thank-you-message-title']").text == "Thank you! See you soon":
            print("The form was submitted")
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Event form was submitted!"}}')
        else:
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Smt is wrong with event form submition"}}')
            raise Exception("Check event form")
        driver.quit()

    # subscription form functionality
    def test_subscribe_form(self):
        driver = self.driver
        driver.get(HP.url)
        self.driver.maximize_window()

        # set up Faker library
        f = Faker()

        # set up wait time
        wait = WebDriverWait(driver, 3)

        # check the title is right, helper
        HP.assert_title("California Marcketing", driver)

        # find 'Subscription form'
        form = wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(@class,'color_15')])[14]"))).text
        if form == "Subscribe Form":
            print("'Subscription form' was found")
        else:
            print("Cant find 'Subscription form'")

        # put email
        try:
            driver.find_element(By.XPATH, "//input[@id='input_comp-ksocylga1']").send_keys(f.email())
            print("The email was sent")
        except WDE:
            print("The email wasn't sent")

        # wait and click on 'Submit' button
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-disabled='false'][contains(., 'Submit')]"))).click()
        print("Submit button was clicked")

        time.sleep(4)

        # assert the form was sent
        if driver.find_element(By.XPATH, "//span[@class='color_15'][contains(.,'Thanks for submitting!')]").is_displayed():
            print("The form was sent")
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "The form was sent!"}}')
        else:
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "The form was not sent"}}')
            raise Exception("Check subscription form")
        driver.quit()

class windows_10_1920_1080_firefox(unittest.TestCase):

    def setUp(self):
        desired_cap = {
            'os_version': '10',
            'resolution': '1920x1080',
            'browser': 'Firefox',
            'browser_version': 'latest',
            'os': 'Windows',
            'name': 'BStack-[Python] Sample Test',  # test name
            'build': 'BStack Build Number 1'  # CI/CD job or build name
        }
        url = KEY.my_key
        desired_cap['acceptSslCerts'] = True
        self.driver = webdriver.Remote(command_executor=url, desired_capabilities=desired_cap)

    # check if social media icons are clickable
    def test_icons_clickability(self):
        driver = self.driver
        driver.get(HP.url)
        self.driver.maximize_window()

        # random delay function, helper
        HP.delay_1_5()

        # check the title is right, helper
        HP.assert_title("California Marcketing", driver)

        # set up wait time
        wait = WebDriverWait(driver, 3)

        # verify icons are clickable, helpers
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.facebook)))
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.twitter)))
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.vk)))
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.youtube)))
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.linkedin)))
            print("Icons are clickable")
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "All icons are clickable"}}')
        except WDE:
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Some icons are not clickable"}}')
            raise Exception("Check icons clickability")
        driver.quit()

    # validate all social network links lead to right pages
    def test_social_network_links(self):
        driver = self.driver
        driver.get(HP.url)
        self.driver.maximize_window()

        # random delay function, helper
        HP.delay_1_5()

        # check the title is right, helper
        HP.assert_title("California Marcketing", driver)

        # find Facebook icon and click
        driver.find_element(By.XPATH, HP.facebook).click()

        # original window set up
        original_window = driver.current_window_handle

        # switch windows if more than one, helper
        HP.switching_windows(driver)

        # random delay, helper
        HP.delay_1_5()

        # verify you are on the right page, helper
        HP.assert_title("Facebook", driver)

        # verify logo, try/except, plus screenshots, helper
        HP.logo_check("Facebook", "//div[@class='l9j0dhe7 buofh1pr j83agx80 bp9cbjyn']", driver)

        # verify the specific element, try/except, plus screenshots, helper
        HP.specific_element_check("Facebook", "//a[contains(text(), 'QA at Silicon Valley California')]", driver)

        # close and switch back
        driver.close()
        driver.switch_to.window(original_window)

        # verify the title of the page when back, helper
        HP.assert_back_title(driver)

        # find TW icon and click
        driver.find_element(By.XPATH, HP.twitter).click()

        # switch windows if more than one, helper
        HP.switching_windows(driver)

        HP.delay_1_5()

        # verify you are on the right page
        time.sleep(3)
        HP.assert_title("Twitter", driver)

        # verify logo, try/except, plus screenshots, helper
        HP.logo_check("TW", "//*[@role='heading']", driver)

        # verify the specific element, try/except, plus screenshots, helper
        HP.specific_element_check("TW", "//a[@dir='ltr'][contains(.,'http://QASV.US')]", driver)

        # close and switch back
        driver.close()
        driver.switch_to.window(original_window)

        # verify the title of the page when back, helper
        HP.assert_back_title(driver)

        # find VK icon and click
        driver.find_element(By.XPATH, HP.vk).click()

        # switch windows if more than one, helper
        HP.switching_windows(driver)

        HP.delay_1_5()

        # verify you are on the right page
        time.sleep(3)
        HP.assert_title("QA at Silicon Valley", driver)

        # verify logo, try/except, plus screenshots, helper
        HP.logo_check("VK", "//*[@class='HeaderNav__item HeaderNav__item--logo']", driver)

        # verify the specific element, try/except, plus screenshots, helper
        HP.specific_element_check("VK", "//*[@href='/away.php?to=https%3A%2F%2Fbit.ly%2F2Q8bBhW&cc_key=']", driver)

        # close and switch back
        driver.close()
        driver.switch_to.window(original_window)

        # verify the title of the page when back, helper
        HP.assert_back_title(driver)

        # find TouTube icon and click
        driver.find_element(By.XPATH, HP.youtube).click()

        # switch windows if more than one, helper
        HP.switching_windows(driver)

        HP.delay_1_5()

        # verify you are on the right page
        time.sleep(5)
        HP.assert_title("Sergey Efremov_USA", driver)

        # verify logo, try/except, plus screenshots, helper
        HP.logo_check("YouTube", "//*[@id='logo-icon']", driver)

        # verify the specific element, try/except, plus screenshots, helper
        HP.specific_element_check("YouTube", "//*[contains(text(), 'Sergey Efremov_USA')]", driver)

        # close and switch back
        driver.close()
        driver.switch_to.window(original_window)

        # verify the title of the page when back, helper
        HP.assert_back_title(driver)

        # find LinkedIn icon and click
        driver.find_element(By.XPATH, HP.linkedin).click()

        # switch windows if more than one, helper
        HP.switching_windows(driver)

        HP.delay_1_5()

        # verify you are on the right page
        time.sleep(3)
        HP.assert_title("LinkedIn", driver)

        # verify logo, try/except, plus screenshots, helper
        HP.logo_check("LinkedIn", "//*[@id='ember16']", driver)

        # verify the specific element, try/except, plus screenshots, helper
        HP.specific_element_check("LinkedIn", "//*[@alt='QA at Silicon Valley California logo']", driver)

        # close and switch back
        driver.close()
        driver.switch_to.window(original_window)

        # verify the title of the page when back, helper
        HP.assert_back_title(driver)
        driver.quit()

    # check "Get in touch"
    def test_get_in_touch(self):
        driver = self.driver
        driver.get(HP.url)
        self.driver.maximize_window()

        # check the title is right, helper
        HP.assert_title("California Marcketing", driver)

        # set wait time
        wait = WebDriverWait(driver, 3)

        # check 'Get in touch' clickability
        try:
            wait.until(EC.element_to_be_clickable(
                (By.CLASS_NAME, "wQYUw")))
            print("'Get in touch' clickable")
        except WDE:
            print("Check 'Get in touch' clickability")

        # check the button text is correct
        button_text = driver.find_element(By.CLASS_NAME, "wQYUw").text
        if button_text == "Get In Touch":
            print("Right 'Get in Touch' button text")
        else:
            print("Incorrect button text")

        # compare on site email with the correct one
        email = driver.find_element(By.LINK_TEXT, "Get In Touch").get_attribute("href")

        # print on page email and supposed email
        print(email)
        print(HP.main_email)

        # assert on page email
        if email == HP.main_email:
            print("The email is correct")
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "The email is correctt!"}}')
        else:
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "The email is not correct"}}')
            raise Exception("The email is not correct")
        driver.quit()

    # check header menu links (except "More")
    def test_header_menu_links(self):
        driver = self.driver
        driver.get(HP.url)
        self.driver.maximize_window()

        # check the title is right, helper
        HP.assert_title("California Marcketing", driver)

        # set wait time
        wait = WebDriverWait(driver, 5)

        # list for final assertion
        wrong_list = []

        # click 'Blog'
        wait.until(EC.element_to_be_clickable((By.XPATH, "//p[@class='_1zyfI'][contains(.,'Blog')]"))).click()
        WebDriverWait(driver, 5)

        # assert 'Blog' title, hepler
        HP.check_title('Blog', driver)

        # check specific element on the page
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'All Posts')]")))
            print("The right 'Blog' page")
        except WDE:
            wrong_blog = "Smt is wrong with 'Blog' page"
            print(wrong_blog)
            wrong_list.append(wrong_blog)

        # back in the browser
        driver.back()

        # click 'Shop'
        wait.until(EC.element_to_be_clickable((By.XPATH, "//p[@class ='_1zyfI'][contains(., 'Shop')]"))).click()
        WebDriverWait(driver, 3)

        # assert 'Shop' title, hepler
        HP.check_title('Shop', driver)

        # check specific element on the page
        try:
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//h3[contains(.,'Product 1')]")))
            print("The right 'Shop' page")
        except WDE:
            wrong_shop = "Smt is wrong with 'Shop' page"
            print(wrong_shop)
            wrong_list.append(wrong_shop)

        # back in the browser
        driver.back()

        # click 'Servises'
        wait.until(EC.element_to_be_clickable((By.XPATH, "//p[@class ='_1zyfI'][contains(., 'Servises')]"))).click()
        WebDriverWait(driver, 3)

        # assert 'Servises' title, hepler
        HP.check_title('Servises', driver)

        # check specific element on the page
        try:
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//h1[contains(.,'Our Services')]")))
            print("The right 'Servises' page")
        except WDE:
            wrong_servises = "Smt is wrong with 'Servises' page"
            print(wrong_servises)
            wrong_list.append(wrong_servises)

        # back in the browser
        driver.back()

        # click 'Home'
        wait.until(EC.element_to_be_clickable((By.XPATH, "//p[@class='_1zyfI'][contains(.,'Home')]"))).click()
        WebDriverWait(driver, 3)

        # assert 'Home' title, hepler
        HP.check_title('Home', driver)

        # check specific element on the page
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "(// span[contains(., 'LET CALIFORNIA MARKETING "
                                                                   "GROW YOUR BUSINECS')])[2]")))
            print("The right 'Home' page")
        except WDE:
            wrong_home = "Smt is wrong with 'Home' page"
            print(wrong_home)
            wrong_list.append(wrong_home)

        # assert the assertion list is empty
        print(len(wrong_list))
        if len(wrong_list) == 0:
            print("All header links work correctly")
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "All header links are correct!"}}')
        else:
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Not all header links are corrrect"}}')
            raise Exception("Check header links")
        driver.quit()

    # localization test of first screen
    def test_first_screen_text(self):
        driver = self.driver
        driver.get(HP.url)
        self.driver.maximize_window()

        # check the title is right, helper
        HP.assert_title("California Marcketing", driver)

        # get the text
        first_line = driver.find_element(By.XPATH, "//a[contains(.,'CALIFORNIA MARCKETING')]").text
        second_line = driver.find_element(By.XPATH,
                                          "(//a[@href='https://qasvus.wixsite.com/ca-marketing/blog'])[2]").text
        third_line = driver.find_element(By.XPATH,
                                         "(//span[contains(.,'LET CALIFORNIA MARKETING GROW YOUR BUSINECS')])[2]").text
        print(first_line, second_line, third_line)

        # compare on site text with correct one, first line
        if first_line == "CALIFORNIA MARKETING":
            print("First line is fine")
        else:
            print("Incorrect first line")

        # compare on site text with correct one, second line
        if second_line == "A Full-Stack Creative Agency in CA":
            print("Second line is fine")
        else:
            print("Incorrect second line")

        # compare on site text with correct one, third line
        if third_line == "LET CALIFORNIA MARKETING GROW YOUR BUSINESS":
            print("Third line is fine")
        else:
            print("Incorrect third line")

        # assert full text
        if [first_line, second_line, third_line] == ["CALIFORNIA MARKETING", "A Full-Stack Creative "
                                                                                         "Agency in CA",
                                                                 'LET CALIFORNIA MARKETING GROW YOUR BUSINESS']:
            print("First screen text is correct")
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "First screen text is correct"}}')
        else:
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "First screen text is not correct""}}')
            raise Exception("Check the first screen text")
        driver.quit()

    # wix chat functionality
    def test_lets_chat(self):
        driver = self.driver
        driver.get(HP.url)
        self.driver.maximize_window()

        # check the title is right, helper
        HP.assert_title("California Marcketing", driver)

        # set up faker
        f = Faker()

        # assertion list
        list_for_assertion = []

        time.sleep(7)

        # find and switch to chat iframe
        iframe = driver.find_element(By.XPATH, "//iframe [@title='Wix Chat']")
        driver.switch_to.frame(iframe)

        # find and open the chat
        try:
            driver.find_element(
                locate_with(By.CLASS_NAME, "_28JNc").below({By.XPATH: "//*[@charset='utf-8']"})).click()
            ok_result = "Chat is on the page"
            print(ok_result)
            list_for_assertion.append(ok_result)
        except WDE:
            fail_result = "Smt is wrong with chat"
            print(fail_result)
            list_for_assertion.append(fail_result)

        time.sleep(3)

        # send fake text
        try:
            driver.find_element(By.TAG_NAME, "textarea").send_keys(f.text() + Keys.ENTER)
            ok_result = "The message was sent in the chat"
            print(ok_result)
            list_for_assertion.append(ok_result)
        except WDE:
            fail_result = "Smt is wrong with messages"
            print(fail_result)
            list_for_assertion.append(fail_result)

        # check if except prints in the list for final assertion
        list_for_assertion = ' '.join(list_for_assertion).split()
        if "wrong" not in list_for_assertion:
            print("The chat works correctly")
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Online chat works correctly!"}}')
        else:
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Smt is wrong with chat"}}')
            raise Exception("Check the chat")
        driver.quit()

    # video search bar functionality
    def test_video_selection(self):
        driver = self.driver
        driver.get(HP.url)
        self.driver.maximize_window()

        # check the title is right, helper
        HP.assert_title("California Marcketing", driver)

        time.sleep(2)

        # find video search bar and send "Big Sur"
        try:
            driver.find_element(
                locate_with(By.CLASS_NAME, "VVhXp").below({By.XPATH: "//*[@title='All Videos']"})).send_keys(
                "Big Sur" + Keys.ENTER)
            print("Search bar works")
        except WDE:
            print("Check the search bar")

        time.sleep(2)

        # assert video with "Big Sur" in the title is displayed
        if driver.find_element(By.XPATH, "//*[@src='https://i.ytimg.com/vi/X-HxnNAaioM/mqdefault.jpg']").is_displayed():
            print("The right video is displayed")
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "The right video is displayed!"}}')
        else:
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Сье is wrong with video search bar"}}')
            raise Exception("Check video search bar")
        driver.quit()

    # cart smoke testing
    def test_cart_shopping(self):
        driver = self.driver
        driver.get(HP.url)
        self.driver.maximize_window()

        # check the title is right, helper
        HP.assert_title("California Marcketing", driver)

        # set up wait time
        wait = WebDriverWait(driver, 3)

        # click 'Shop'
        shop = wait.until(EC.element_to_be_clickable((By.XPATH, "//p[@class ='_1zyfI'][contains(., 'Shop')]")))
        shop.click()

        time.sleep(5)

        # assert 'Shop' title, helper
        HP.check_title('Shop', driver)

        # check specific element on the page, helper
        HP.specific_element_check('Shop', "//h3[contains(.,'Product 1')]", driver)

        # find 'product1', get text and click
        product = driver.find_element(By.XPATH, "// h3[contains(.,'Product 1')]")
        product_text = product.text
        product.click()
        print("Successfully clicked on", product_text)

        time.sleep(5)

        # assert the title
        assert product_text in driver.title
        print("The right product page")

        # assert the product name on the page match the one was chosen
        on_page_product_text = driver.find_element(By.XPATH, "//h1[contains(@class,'2yxAN')]").text
        if product_text == on_page_product_text:
            print("Match:", product_text, "and", on_page_product_text)
        else:
            print("Not a match")

        # find price for one piece, turn into integer
        price = driver.find_element(By.XPATH, "//span[@data-hook='formatted-primary-price']").text
        price = int(price.replace("$", "").replace(".00", ""))
        print("The price for 1 piece is:", price)

        # set color and quantity
        try:
            driver.find_element(By.XPATH,
                                "(//div[contains(@class,'ColorPickerItem2201735070__radioInner')])[1]").click()
            driver.find_element(By.XPATH, "//span[contains(@data-hook, 'number-input-spinner-up-arrow')]").click()
            print("The color and quantity were set")
        except WDE:
            print("Smt is wrong with color/quantity")

        # click on "Add to cart" button
        try:
            driver.find_element(By.XPATH,
                                "//span[@class ='buttonnext1002411228__content'][contains(., 'Add to Card')]").click()
            print("The product was added to cart")
        except WDE:
            print("Smt is wrong with adding to cart")

        time.sleep(7)

        # find curtain frame and switch
        try:
            driver.switch_to.frame(driver.find_element(By.CLASS_NAME, "_2DJg7"))
            print("Switched to frame")
        except WDE:
            print("Check the frame")

        # click on "View cart" button
        wait.until(EC.element_to_be_clickable((By.ID, "widget-view-cart-button"))).click()

        time.sleep(5)

        # switch back
        driver.switch_to.default_content()

        # assert title
        assert "Cart" in driver.title

        # assert specific element on the page

        my_cart = driver.find_element(By.CLASS_NAME, "_2NsyK").text
        if my_cart == "My cart":
            print("We are on the cart page")
        else:
            print("Check the cart page")

        # assert product name
        product_name = driver.find_element(By.CLASS_NAME, "_1dkgR").text
        if product_name == product_text:
            print("Right product in the cart")
        else:
            print("Wrong product in the cart")

        # check the quantity is correct
        howMany = driver.find_element(By.XPATH, "//input[@aria-label='Choose quantity']").get_attribute("value")
        if howMany == "2":
            print("Correct quantity")
        else:
            print("Wrong quantity")

        # check the price is correct
        total_price = driver.find_element(By.CLASS_NAME, "_32Pyj").text
        total_price = int(total_price.replace("$", "").replace(".00", ""))
        if total_price == int(howMany) * price:
            print("Correct total price")
        else:
            print("Wrong total price")

        # check the color is correct, helper
        HP.product_color("(//li[contains(.,'Color: Black')])[2]", "Black", driver)

        # find and click on 'CheckOut' button
        try:
            driver.find_element(By.CLASS_NAME, "_34QVp").click()
            print("Click on 'CheckOut' button")
        except WDE:
            print("Smt is wrong with 'CheckOut' button")

        time.sleep(5)

        # find iframe and switch
        try:
            driver.switch_to.frame(driver.find_element(By.CLASS_NAME, "MUsGO"))
            print("Switched to frame")
        except WDE:
            print("No frame")

        # assert the frame doesn't include "We can't accept online orders right now"
        fr2text = driver.find_element(By.CLASS_NAME, "maaPx").text
        print(fr2text)
        if "We can't accept online orders right now" not in fr2text:
            print("Checkout without 'cant accept online orders'")
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Checkout without: cant accept online orders"}}')
        else:
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Wrong checkout process"}}')
            raise Exception("Check checkout")
        driver.quit()

    # event reservation smoke testing
    def test_event_reservation(self):
        driver = self.driver
        driver.get(HP.url)
        self.driver.maximize_window()

        # set up faker library
        f = Faker()

        # set up wait time
        wait = WebDriverWait(driver, 3)

        # check the title is right, helper
        HP.assert_title("California Marcketing", driver)

        time.sleep(4)

        try:
            event = driver.find_element(By.XPATH, "(//a[@data-hook='ev-rsvp-button'][contains(.,'RSVP')])[1]")
            print("Event section")
        except WDE:
            print("Cant find event section")

        # name, date and place of the first event
        event_name = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "DTbMp"))).text
        print(event_name)
        event_date = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "VFsgs"))).text
        print(event_date)
        event_place = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "lNymU"))).text
        print(event_place)

        # click on "RSVP" button
        event.click()
        print("'RSVP' button was clicked")

        # assert title
        assert event_name in driver.title
        print("Its the middle event page")

        # check if event name, date and place are correct, helpers
        HP.comparison_xpath("//h1[@data-hook='event-title']", event_name, "event name", driver)
        HP.comparison_class("_6vtCb", event_date, "event date", driver)
        HP.comparison_class("-OEip", event_place, "event place", driver)

        # click on 'RSVP' button
        time.sleep(3)
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "(//button[@data-hook='rsvp-button'][contains(.,'RSVP')])[2]"))).click()
        time.sleep(3)

        # assert driver title
        assert event_name in driver.title
        print("It`s the final event page")

        # check event name and place, helpers
        HP.comparison_xpath("//*[@data-hook='event-title']", event_name, "event name", driver)
        HP.comparison_xpath("//*[@data-hook='event-location']", event_place, "event place", driver)

        # fill the form
        driver.find_element(By.ID, "firstName").send_keys(f.first_name())
        driver.find_element(By.ID, "lastName").send_keys(f.last_name())
        driver.find_element(By.ID, "email").send_keys(f.email())

        # find and click on 'Submit' page
        try:
            driver.find_element(By.XPATH, "//button[@data-hook='form-button']").click()
            print("Submit button was clicked")
        except WDE:
            print("Check the 'Submit' button")

        time.sleep(5)

        # assert 'thank you' page
        if driver.find_element(By.XPATH, "//h2[@data-hook='thank-you-message-title']").text == "Thank you! See you soon":
            print("The form was submitted")
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Event form was submitted!"}}')
        else:
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Smt is wrong with event form submition"}}')
            raise Exception("Check event form")
        driver.quit()

    # subscription form functionality
    def test_subscribe_form(self):
        driver = self.driver
        driver.get(HP.url)
        self.driver.maximize_window()

        # set up Faker library
        f = Faker()

        # set up wait time
        wait = WebDriverWait(driver, 3)

        # check the title is right, helper
        HP.assert_title("California Marcketing", driver)

        # find 'Subscription form'
        form = wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(@class,'color_15')])[14]"))).text
        if form == "Subscribe Form":
            print("'Subscription form' was found")
        else:
            print("Cant find 'Subscription form'")

        # put email
        try:
            driver.find_element(By.XPATH, "//input[@id='input_comp-ksocylga1']").send_keys(f.email())
            print("The email was sent")
        except WDE:
            print("The email wasn't sent")

        # wait and click on 'Submit' button
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-disabled='false'][contains(., 'Submit')]"))).click()
        print("Submit button was clicked")

        time.sleep(4)

        # assert the form was sent
        if driver.find_element(By.XPATH, "//span[@class='color_15'][contains(.,'Thanks for submitting!')]").is_displayed():
            print("The form was sent")
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "The form was sent!"}}')
        else:
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "The form was not sent"}}')
            raise Exception("Check subscription form")
        driver.quit()

class windows_10_1920_1080_edge(unittest.TestCase):

    def setUp(self):
        desired_cap = {
            'os_version': '10',
            'resolution': '1920x1080',
            'browser': 'Edge',
            'browser_version': 'latest',
            'os': 'Windows',
            'name': 'BStack-[Python] Sample Test',  # test name
            'build': 'BStack Build Number 1'  # CI/CD job or build name
        }
        url = KEY.my_key
        desired_cap['acceptSslCerts'] = True
        self.driver = webdriver.Remote(command_executor=url, desired_capabilities=desired_cap)

    # check if social media icons are clickable
    def test_icons_clickability(self):
        driver = self.driver
        driver.get(HP.url)
        self.driver.maximize_window()

        # random delay function, helper
        HP.delay_1_5()

        # check the title is right, helper
        HP.assert_title("California Marcketing", driver)

        # set up wait time
        wait = WebDriverWait(driver, 3)

        # verify icons are clickable, helpers
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.facebook)))
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.twitter)))
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.vk)))
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.youtube)))
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.linkedin)))
            print("Icons are clickable")
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "All icons are clickable"}}')
        except WDE:
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Some icons are not clickable"}}')
            raise Exception("Check icons clickability")
        driver.quit()

    # validate all social network links lead to right pages
    def test_social_network_links(self):
        driver = self.driver
        driver.get(HP.url)
        self.driver.maximize_window()

        # random delay function, helper
        HP.delay_1_5()

        # check the title is right, helper
        HP.assert_title("California Marcketing", driver)

        # set wait time
        wait = WebDriverWait(driver, 3)

        # find Facebook icon and click
        driver.find_element(By.XPATH, HP.facebook).click()

        # original window set up
        original_window = driver.current_window_handle

        # switch windows if more than one, helper
        HP.switching_windows(driver)

        # random delay, helper
        HP.delay_1_5()

        # verify you are on the right page, helper
        HP.assert_title("Facebook", driver)

        # verify logo, try/except, plus screenshots, helper
        HP.logo_check("Facebook", "//div[@class='l9j0dhe7 buofh1pr j83agx80 bp9cbjyn']", driver)

        # verify the specific element, try/except, plus screenshots, helper
        HP.specific_element_check("Facebook", "//a[contains(text(), 'QA at Silicon Valley California')]", driver)

        # close and switch back
        driver.close()
        driver.switch_to.window(original_window)

        # verify the title of the page when back, helper
        HP.assert_back_title(driver)

        # find TW icon and click
        driver.find_element(By.XPATH, HP.twitter).click()

        # switch windows if more than one, helper
        HP.switching_windows(driver)

        HP.delay_1_5()

        # verify you are on the right page
        HP.assert_title("Твиттер", driver)

        # verify logo, try/except, plus screenshots, helper
        HP.logo_check("TW", "//*[@role='heading']", driver)

        # verify the specific element, try/except, plus screenshots, helper
        HP.specific_element_check("TW", "//a[@dir='ltr'][contains(.,'http://QASV.US')]", driver)

        # close and switch back
        driver.close()
        driver.switch_to.window(original_window)

        # verify the title of the page when back, helper
        HP.assert_back_title(driver)

        # find VK icon and click
        driver.find_element(By.XPATH, HP.vk).click()

        # switch windows if more than one, helper
        HP.switching_windows(driver)

        HP.delay_1_5()

        # verify you are on the right page
        HP.assert_title("QA at Silicon Valley", driver)

        # verify logo, try/except, plus screenshots, helper
        HP.logo_check("VK", "//*[@class='HeaderNav__item HeaderNav__item--logo']", driver)

        # verify the specific element, try/except, plus screenshots, helper
        HP.specific_element_check("VK", "//*[@href='/away.php?to=https%3A%2F%2Fbit.ly%2F2Q8bBhW&cc_key=']", driver)

        # close and switch back
        driver.close()
        driver.switch_to.window(original_window)

        # verify the title of the page when back, helper
        HP.assert_back_title(driver)

        # find TouTube icon and click
        driver.find_element(By.XPATH, HP.youtube).click()

        # switch windows if more than one, helper
        HP.switching_windows(driver)

        HP.delay_1_5()

        # verify you are on the right page
        HP.assert_title("Sergey Efremov", driver)

        # verify logo, try/except, plus screenshots, helper
        HP.logo_check("YouTube", "//*[@id='logo-icon']", driver)

        # verify the specific element, try/except, plus screenshots, helper
        HP.specific_element_check("YouTube", "//*[contains(text(), 'Sergey Efremov_USA')]", driver)

        # close and switch back
        driver.close()
        driver.switch_to.window(original_window)

        # verify the title of the page when back, helper
        HP.assert_back_title(driver)

        # find LinkedIn icon and click
        driver.find_element(By.XPATH, HP.linkedin).click()

        # switch windows if more than one, helper
        HP.switching_windows(driver)

        HP.delay_1_5()

        # verify you are on the right page
        HP.assert_title("LinkedIn", driver)

        # verify logo, try/except, plus screenshots, helper
        HP.logo_check("LinkedIn", "//*[@id='ember16']", driver)

        # verify the specific element, try/except, plus screenshots, helper
        HP.specific_element_check("LinkedIn", "//*[@alt='QA at Silicon Valley California logo']", driver)

        # close and switch back
        driver.close()
        driver.switch_to.window(original_window)

        # verify the title of the page when back, helper
        HP.assert_back_title(driver)
        driver.quit()

    # check "Get in touch"
    def test_get_in_touch(self):
        driver = self.driver
        driver.get(HP.url)
        self.driver.maximize_window()

        # check the title is right, helper
        HP.assert_title("California Marcketing", driver)

        # set wait time
        wait = WebDriverWait(driver, 3)

        # check 'Get in touch' clickability
        try:
            wait.until(EC.element_to_be_clickable(
                (By.CLASS_NAME, "wQYUw")))
            print("'Get in touch' clickable")
        except WDE:
            print("Check 'Get in touch' clickability")

        # check the button text is correct
        button_text = driver.find_element(By.CLASS_NAME, "wQYUw").text
        if button_text == "Get In Touch":
            print("Right 'Get in Touch' button text")
        else:
            print("Incorrect button text")

        # compare on site email with the correct one
        email = driver.find_element(By.LINK_TEXT, "Get In Touch").get_attribute("href")

        # print on page email and supposed email
        print(email)
        print(HP.main_email)

        # assert on page email
        if email == HP.main_email:
            print("The email is correct")
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "The email is correctt!"}}')
        else:
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "The email is not correct"}}')
            raise Exception("The email is not correct")
        driver.quit()

    # check header menu links (except "More")
    def test_header_menu_links(self):
        driver = self.driver
        driver.get(HP.url)
        self.driver.maximize_window()

        # check the title is right, helper
        HP.assert_title("California Marcketing", driver)

        # set wait time
        wait = WebDriverWait(driver, 5)

        # list for final assertion
        wrong_list = []

        # click 'Blog'
        wait.until(EC.element_to_be_clickable((By.XPATH, "//p[@class='_1zyfI'][contains(.,'Blog')]"))).click()
        WebDriverWait(driver, 3)

        # assert 'Blog' title, hepler
        HP.check_title('Blog', driver)

        # check specific element on the page
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'All Posts')]")))
            print("The right 'Blog' page")
        except WDE:
            wrong_blog = "Smt is wrong with 'Blog' page"
            print(wrong_blog)
            wrong_list.append(wrong_blog)

        # back in the browser
        driver.back()

        # click 'Shop'
        wait.until(EC.element_to_be_clickable((By.XPATH, "//p[@class ='_1zyfI'][contains(., 'Shop')]"))).click()
        WebDriverWait(driver, 3)

        # assert 'Shop' title, hepler
        HP.check_title('Shop', driver)

        # check specific element on the page
        try:
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//h3[contains(.,'Product 1')]")))
            print("The right 'Shop' page")
        except WDE:
            wrong_shop = "Smt is wrong with 'Shop' page"
            print(wrong_shop)
            wrong_list.append(wrong_shop)

        # back in the browser
        driver.back()

        # click 'Servises'
        wait.until(EC.element_to_be_clickable((By.XPATH, "//p[@class ='_1zyfI'][contains(., 'Servises')]"))).click()
        WebDriverWait(driver, 3)

        # assert 'Servises' title, hepler
        HP.check_title('Servises', driver)

        # check specific element on the page
        try:
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//h1[contains(.,'Our Services')]")))
            print("The right 'Servises' page")
        except WDE:
            wrong_servises = "Smt is wrong with 'Servises' page"
            print(wrong_servises)
            wrong_list.append(wrong_servises)

        # back in the browser
        driver.back()

        # click 'Home'
        wait.until(EC.element_to_be_clickable((By.XPATH, "//p[@class='_1zyfI'][contains(.,'Home')]"))).click()
        WebDriverWait(driver, 3)

        # assert 'Home' title, hepler
        HP.check_title('Home', driver)

        # check specific element on the page
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "(// span[contains(., 'LET CALIFORNIA MARKETING "
                                                                   "GROW YOUR BUSINECS')])[2]")))
            print("The right 'Home' page")
        except WDE:
            wrong_home = "Smt is wrong with 'Home' page"
            print(wrong_home)
            wrong_list.append(wrong_home)

        # assert the assertion list is empty
        print(len(wrong_list))
        if len(wrong_list) == 0:
            print("All header links work correctly")
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "All header links are correct!"}}')
        else:
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Not all header links are corrrect"}}')
            raise Exception("Check header links")
        driver.quit()

    # localization test of first screen
    def test_first_screen_text(self):
        driver = self.driver
        driver.get(HP.url)
        self.driver.maximize_window()

        # check the title is right, helper
        HP.assert_title("California Marcketing", driver)

        # get the text
        first_line = driver.find_element(By.XPATH, "//a[contains(.,'CALIFORNIA MARCKETING')]").text
        second_line = driver.find_element(By.XPATH,
                                          "(//a[@href='https://qasvus.wixsite.com/ca-marketing/blog'])[2]").text
        third_line = driver.find_element(By.XPATH,
                                         "(//span[contains(.,'LET CALIFORNIA MARKETING GROW YOUR BUSINECS')])[2]").text
        print(first_line, second_line, third_line)

        # compare on site text with correct one, first line
        if first_line == "CALIFORNIA MARKETING":
            print("First line is fine")
        else:
            print("Incorrect first line")

        # compare on site text with correct one, second line
        if second_line == "A Full-Stack Creative Agency in CA":
            print("Second line is fine")
        else:
            print("Incorrect second line")

        # compare on site text with correct one, third line
        if third_line == "LET CALIFORNIA MARKETING GROW YOUR BUSINESS":
            print("Third line is fine")
        else:
            print("Incorrect third line")

        # assert full text
        if [first_line, second_line, third_line] == ["CALIFORNIA MARKETING", "A Full-Stack Creative "
                                                                                         "Agency in CA",
                                                                 'LET CALIFORNIA MARKETING GROW YOUR BUSINESS']:
            print("First screen text is correct")
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "First screen text is correct"}}')
        else:
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "First screen text is not correct""}}')
            raise Exception("Check the first screen text")
        driver.quit()

    # wix chat functionality
    def test_lets_chat(self):
        driver = self.driver
        driver.get(HP.url)
        self.driver.maximize_window()

        # check the title is right, helper
        HP.assert_title("California Marcketing", driver)

        # set up faker
        f = Faker()

        # assertion list
        list_for_assertion = []

        time.sleep(5)

        # find and switch to chat iframe
        iframe = driver.find_element(By.XPATH, "//iframe [@title='Wix Chat']")
        driver.switch_to.frame(iframe)

        # find and open the chat
        try:
            driver.find_element(
                locate_with(By.CLASS_NAME, "_28JNc").below({By.XPATH: "//*[@charset='utf-8']"})).click()
            ok_result = "Chat is on the page"
            print(ok_result)
            list_for_assertion.append(ok_result)
        except WDE:
            fail_result = "Smt is wrong with chat"
            print(fail_result)
            list_for_assertion.append(fail_result)

        time.sleep(3)

        # send fake text
        try:
            driver.find_element(By.TAG_NAME, "textarea").send_keys(f.text() + Keys.ENTER)
            ok_result = "The message was sent in the chat"
            print(ok_result)
            list_for_assertion.append(ok_result)
        except WDE:
            fail_result = "Smt is wrong with messages"
            print(fail_result)
            list_for_assertion.append(fail_result)

        # check if except prints in the list for final assertion
        list_for_assertion = ' '.join(list_for_assertion).split()
        if "wrong" not in list_for_assertion:
            print("The chat works correctly")
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Online chat works correctly!"}}')
        else:
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Smt is wrong with chat"}}')
            raise Exception("Check the chat")
        driver.quit()

    # video search bar functionality
    def test_video_selection(self):
        driver = self.driver
        driver.get(HP.url)
        self.driver.maximize_window()

        # check the title is right, helper
        HP.assert_title("California Marcketing", driver)

        time.sleep(2)

        # find video search bar and send "Big Sur"
        try:
            driver.find_element(
                locate_with(By.CLASS_NAME, "VVhXp").below({By.XPATH: "//*[@title='All Videos']"})).send_keys(
                "Big Sur" + Keys.ENTER)
            print("Search bar works")
        except WDE:
            print("Check the search bar")

        time.sleep(2)

        # assert video with "Big Sur" in the title is displayed
        if driver.find_element(By.XPATH, "//*[@src='https://i.ytimg.com/vi/X-HxnNAaioM/mqdefault.jpg']").is_displayed():
            print("The right video is displayed")
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "The right video is displayed!"}}')
        else:
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Сье is wrong with video search bar"}}')
            raise Exception("Check video search bar")
        driver.quit()

    # cart smoke testing
    def test_cart_shopping(self):
        driver = self.driver
        driver.get(HP.url)
        self.driver.maximize_window()

        # check the title is right, helper
        HP.assert_title("California Marcketing", driver)

        # set up wait time
        wait = WebDriverWait(driver, 2)

        # click 'Shop'
        shop = wait.until(EC.element_to_be_clickable((By.XPATH, "//p[@class ='_1zyfI'][contains(., 'Shop')]")))
        shop.click()

        time.sleep(3)

        # assert 'Shop' title, helper
        HP.check_title('Shop', driver)

        # check specific element on the page, helper
        HP.specific_element_check('Shop', "//h3[contains(.,'Product 1')]", driver)

        # find 'product1', get text and click
        product = driver.find_element(By.XPATH, "// h3[contains(.,'Product 1')]")
        product_text = product.text
        product.click()
        print("Successfully clicked on", product_text)

        time.sleep(5)

        # assert the title
        print(driver.title)
        assert product_text in driver.title
        print("The right product page")

        # assert the product name on the page match the one was chosen
        on_page_product_text = driver.find_element(By.XPATH, "//h1[contains(@class,'2yxAN')]").text
        if product_text == on_page_product_text:
            print("Match:", product_text, "and", on_page_product_text)
        else:
            print("Not a match")

        # find price for one piece, turn into integer
        price = driver.find_element(By.XPATH, "//span[@data-hook='formatted-primary-price']").text
        price = int(price.replace("$", "").replace(".00", ""))
        print("The price for 1 piece is:", price)

        # set color and quantity
        try:
            driver.find_element(By.XPATH, "(//div[contains(@class,'radioInner')])[1]").click()
            driver.find_element(By.XPATH, "//span[contains(@data-hook,'number-input-spinner-up-arrow')]").click()
            print("The color and quantity were set")
        except WDE:
            print("Smt is wrong with color/quantity")

        # click on "Add to cart" button
        try:
            driver.find_element(By.XPATH,
                                "//span[@class ='buttonnext1002411228__content'][contains(., 'Add to Card')]").click()
            print("The product was added to cart")
        except WDE:
            print("Smt is wrong with adding to cart")

        time.sleep(5)

        # find curtain frame and switch
        try:
            driver.switch_to.frame(driver.find_element(By.CLASS_NAME, "_2DJg7"))
            print("Switched to frame")
        except WDE:
            print("Check the frame")

        # click on "View cart" button
        wait.until(EC.element_to_be_clickable((By.ID, "widget-view-cart-button"))).click()

        time.sleep(5)

        # assert title
        assert "Cart" in driver.title

        # assert specific element on the page
        my_cart = driver.find_element(By.CLASS_NAME, "_2NsyK").text
        if my_cart == "My cart":
            print("We are on the cart page")
        else:
            print("Check the cart page")

        # assert product name
        product_name = driver.find_element(By.CLASS_NAME, "_1dkgR").text
        if product_name == product_text:
            print("Right product in the cart")
        else:
            print("Wrong product in the cart")

        # check the quantity is correct
        howMany = driver.find_element(By.XPATH, "//input[@aria-label='Choose quantity']").get_attribute("value")
        if howMany == "2":
            print("Correct quantity")
        else:
            print("Wrong quantity")

        # check the price is correct
        total_price = driver.find_element(By.CLASS_NAME, "_32Pyj").text
        total_price = int(total_price.replace("$", "").replace(".00", ""))
        if total_price == int(howMany) * price:
            print("Correct total price")
        else:
            print("Wrong total price")

        # check the color is correct, helper
        HP.product_color("(//li[contains(.,'Color: Black')])[2]", "Black", driver)

        # find and click on 'CheckOut' button
        try:
            driver.find_element(By.CLASS_NAME, "_34QVp").click()
            print("Click on 'CheckOut' button")
        except WDE:
            print("Smt is wrong with 'CheckOut' button")

        time.sleep(5)

        # find iframe and switch
        try:
            driver.switch_to.frame(driver.find_element(By.CLASS_NAME, "MUsGO"))
            print("Switched to frame")
        except WDE:
            print("No frame")

        # assert the frame doesn't include "We can't accept online orders right now"
        fr2text = driver.find_element(By.CLASS_NAME, "maaPx").text
        print(fr2text)
        if "We can't accept online orders right now" not in fr2text:
            print("Checkout without 'cant accept online orders'")
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Checkout without: cant accept online orders"}}')
        else:
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Wrong checkout process"}}')
            raise Exception("Check checkout")
        driver.quit()

    # event reservation smoke testing
    def test_event_reservation(self):
        driver = self.driver
        driver.get(HP.url)
        self.driver.maximize_window()

        # set up faker library
        f = Faker()

        # set up wait time
        wait = WebDriverWait(driver, 3)

        # check the title is right, helper
        HP.assert_title("California Marcketing", driver)

        time.sleep(4)

        try:
            event = driver.find_element(By.XPATH, "(//a[@data-hook='ev-rsvp-button'][contains(.,'RSVP')])[1]")
            print("Event section")
        except WDE:
            print("Cant find event section")

        # name, date and place of the first event
        event_name = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "DTbMp"))).text
        print(event_name)
        event_date = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "VFsgs"))).text
        print(event_date)
        event_place = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "lNymU"))).text
        print(event_place)

        # click on "RSVP" button
        event.click()
        print("'RSVP' button was clicked")

        # assert title
        assert event_name in driver.title
        print("Its the middle event page")

        # check if event name, date and place are correct, helpers
        HP.comparison_xpath("//h1[@data-hook='event-title']", event_name, "event name", driver)
        HP.comparison_class("_6vtCb", event_date, "event date", driver)
        HP.comparison_class("-OEip", event_place, "event place", driver)

        # click on 'RSVP' button
        time.sleep(3)
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "(//button[@data-hook='rsvp-button'][contains(.,'RSVP')])[2]"))).send_keys('\n')
        time.sleep(3)

        # assert driver title
        assert event_name in driver.title
        print("It`s the final event page")

        # check event name and place, helpers
        HP.comparison_xpath("//*[@data-hook='event-title']", event_name, "event name", driver)
        HP.comparison_xpath("//*[@data-hook='event-location']", event_place, "event place", driver)

        # fill the form
        driver.find_element(By.ID, "firstName").send_keys(f.first_name())
        driver.find_element(By.ID, "lastName").send_keys(f.last_name())
        driver.find_element(By.ID, "email").send_keys(f.email())

        # find and click on 'Submit' page
        try:
            driver.find_element(By.XPATH, "//button[@data-hook='form-button']").click()
            print("Submit button was clicked")
        except WDE:
            print("Check the 'Submit' button")

        time.sleep(5)

        # assert 'thank you' page
        if driver.find_element(By.XPATH, "//h2[@data-hook='thank-you-message-title']").text == "Thank you! See you soon":
            print("The form was submitted")
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Event form was submitted!"}}')
        else:
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Smt is wrong with event form submition"}}')
            raise Exception("Check event form")
        driver.quit()

    # subscription form functionality
    def test_subscribe_form(self):
        driver = self.driver
        driver.get(HP.url)
        self.driver.maximize_window()

        # set up Faker library
        f = Faker()

        # set up wait time
        wait = WebDriverWait(driver, 3)

        # check the title is right, helper
        HP.assert_title("California Marcketing", driver)

        # find 'Subscription form'
        form = wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(@class,'color_15')])[14]"))).text
        if form == "Subscribe Form":
            print("'Subscription form' was found")
        else:
            print("Cant find 'Subscription form'")

        # put email
        try:
            driver.find_element(By.XPATH, "//input[@id='input_comp-ksocylga1']").send_keys(f.email())
            print("The email was sent")
        except WDE:
            print("The email wasn't sent")

        # wait and click on 'Submit' button
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-disabled='false'][contains(., 'Submit')]"))).click()
        print("Submit button was clicked")

        time.sleep(4)

        # assert the form was sent
        if driver.find_element(By.XPATH, "//span[@class='color_15'][contains(.,'Thanks for submitting!')]").is_displayed():
            print("The form was sent")
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "The form was sent!"}}')
        else:
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "The form was not sent"}}')
            raise Exception("Check subscription form")
        driver.quit()

class monterey_1920_1080_chrome(unittest.TestCase):

    def setUp(self):
        desired_cap = {
            'os_version': 'Monterey',
            'resolution': '1920x1080',
            'browser': 'Chrome',
            'browser_version': '99.0',
            'os': 'OS X',
            'name': 'BStack-[Python] Sample Test',  # test name
            'build': 'BStack Build Number 1'  # CI/CD job or build name
        }
        url = KEY.my_key
        desired_cap['acceptSslCerts'] = True
        self.driver = webdriver.Remote(command_executor=url, desired_capabilities=desired_cap)

    # check if social media icons are clickable
    def test_icons_clickability(self):
        driver = self.driver
        driver.get(HP.url)
        self.driver.maximize_window()

        # random delay function, helper
        HP.delay_1_5()

        # check the title is right, helper
        HP.assert_title("California Marcketing", driver)

        # set up wait time
        wait = WebDriverWait(driver, 3)

        # verify icons are clickable, helpers
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.facebook)))
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.twitter)))
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.vk)))
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.youtube)))
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.linkedin)))
            print("Icons are clickable")
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "All icons are clickable"}}')
        except WDE:
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Some icons are not clickable"}}')
            raise Exception("Check icons clickability")
        driver.quit()

    # validate all social network links lead to right pages
    def test_social_network_links(self):
        driver = self.driver
        driver.get(HP.url)
        self.driver.maximize_window()

        # random delay function, helper
        HP.delay_1_5()

        # check the title is right, helper
        HP.assert_title("California Marcketing", driver)

        # find Facebook icon and click
        driver.find_element(By.XPATH, HP.facebook).click()

        # original window set up
        original_window = driver.current_window_handle

        # switch windows if more than one, helper
        HP.switching_windows(driver)

        # random delay, helper
        HP.delay_1_5()

        # verify you are on the right page, helper
        HP.assert_title("Facebook", driver)

        # verify logo, try/except, plus screenshots, helper
        HP.logo_check("Facebook", "//div[@class='l9j0dhe7 buofh1pr j83agx80 bp9cbjyn']", driver)

        # verify the specific element, try/except, plus screenshots, helper
        HP.specific_element_check("Facebook", "//a[contains(text(), 'QA at Silicon Valley California')]", driver)

        # close and switch back
        driver.close()
        driver.switch_to.window(original_window)

        # verify the title of the page when back, helper
        HP.assert_back_title(driver)

        # find TW icon and click
        driver.find_element(By.XPATH, HP.twitter).click()

        # switch windows if more than one, helper
        HP.switching_windows(driver)

        HP.delay_1_5()

        # verify you are on the right page
        HP.assert_title("Твиттер", driver)

        # verify logo, try/except, plus screenshots, helper
        HP.logo_check("TW", "//*[@role='heading']", driver)

        # verify the specific element, try/except, plus screenshots, helper
        HP.specific_element_check("TW", "//a[@dir='ltr'][contains(.,'http://QASV.US')]", driver)

        # close and switch back
        driver.close()
        driver.switch_to.window(original_window)

        # verify the title of the page when back, helper
        HP.assert_back_title(driver)

        # find VK icon and click
        driver.find_element(By.XPATH, HP.vk).click()

        # switch windows if more than one, helper
        HP.switching_windows(driver)

        HP.delay_1_5()

        # verify you are on the right page
        HP.assert_title("QA at Silicon Valley", driver)

        # verify logo, try/except, plus screenshots, helper
        HP.logo_check("VK", "//*[@class='HeaderNav__item HeaderNav__item--logo']", driver)

        # verify the specific element, try/except, plus screenshots, helper
        HP.specific_element_check("VK", "//*[@href='/away.php?to=https%3A%2F%2Fbit.ly%2F2Q8bBhW&cc_key=']", driver)

        # close and switch back
        driver.close()
        driver.switch_to.window(original_window)

        # verify the title of the page when back, helper
        HP.assert_back_title(driver)

        # find TouTube icon and click
        driver.find_element(By.XPATH, HP.youtube).click()

        # switch windows if more than one, helper
        HP.switching_windows(driver)

        HP.delay_1_5()

        # verify you are on the right page
        HP.assert_title("Sergey Efremov", driver)

        # verify logo, try/except, plus screenshots, helper
        HP.logo_check("YouTube", "//*[@id='logo-icon']", driver)

        # verify the specific element, try/except, plus screenshots, helper
        HP.specific_element_check("YouTube", "//*[contains(text(), 'Sergey Efremov_USA')]", driver)

        # close and switch back
        driver.close()
        driver.switch_to.window(original_window)

        # verify the title of the page when back, helper
        HP.assert_back_title(driver)

        # find LinkedIn icon and click
        driver.find_element(By.XPATH, HP.linkedin).click()

        # switch windows if more than one, helper
        HP.switching_windows(driver)

        HP.delay_1_5()

        # verify you are on the right page
        HP.assert_title("LinkedIn", driver)

        # verify logo, try/except, plus screenshots, helper
        HP.logo_check("LinkedIn", "//*[@id='ember16']", driver)

        # verify the specific element, try/except, plus screenshots, helper
        HP.specific_element_check("LinkedIn", "//*[@alt='QA at Silicon Valley California logo']", driver)

        # close and switch back
        driver.close()
        driver.switch_to.window(original_window)

        # verify the title of the page when back, helper
        HP.assert_back_title(driver)
        driver.quit()

    # check "Get in touch"
    def test_get_in_touch(self):
        driver = self.driver
        driver.get(HP.url)
        self.driver.maximize_window()

        # check the title is right, helper
        HP.assert_title("California Marcketing", driver)

        # set wait time
        wait = WebDriverWait(driver, 3)

        # check 'Get in touch' clickability
        try:
            wait.until(EC.element_to_be_clickable(
                (By.CLASS_NAME, "wQYUw")))
            print("'Get in touch' clickable")
        except WDE:
            print("Check 'Get in touch' clickability")

        # check the button text is correct
        button_text = driver.find_element(By.CLASS_NAME, "wQYUw").text
        if button_text == "Get In Touch":
            print("Right 'Get in Touch' button text")
        else:
            print("Incorrect button text")

        # compare on site email with the correct one
        email = driver.find_element(By.LINK_TEXT, "Get In Touch").get_attribute("href")

        # print on page email and supposed email
        print(email)
        print(HP.main_email)

        # assert on page email
        if email == HP.main_email:
            print("The email is correct")
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "The email is correctt!"}}')
        else:
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "The email is not correct"}}')
            raise Exception("The email is not correct")
        driver.quit()

    # check header menu links (except "More")
    def test_header_menu_links(self):
        driver = self.driver
        driver.get(HP.url)
        self.driver.maximize_window()

        # check the title is right, helper
        HP.assert_title("California Marcketing", driver)

        # set wait time
        wait = WebDriverWait(driver, 5)

        # list for final assertion
        wrong_list = []

        # click 'Blog'
        wait.until(EC.element_to_be_clickable((By.XPATH, "//p[@class='_1zyfI'][contains(.,'Blog')]"))).click()
        WebDriverWait(driver, 3)

        # assert 'Blog' title, hepler
        HP.check_title('Blog', driver)

        # check specific element on the page
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'All Posts')]")))
            print("The right 'Blog' page")
        except WDE:
            wrong_blog = "Smt is wrong with 'Blog' page"
            print(wrong_blog)
            wrong_list.append(wrong_blog)

        # back in the browser
        driver.back()

        # click 'Shop'
        wait.until(EC.element_to_be_clickable((By.XPATH, "//p[@class ='_1zyfI'][contains(., 'Shop')]"))).click()
        WebDriverWait(driver, 3)

        # assert 'Shop' title, hepler
        HP.check_title('Shop', driver)

        # check specific element on the page
        try:
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//h3[contains(.,'Product 1')]")))
            print("The right 'Shop' page")
        except WDE:
            wrong_shop = "Smt is wrong with 'Shop' page"
            print(wrong_shop)
            wrong_list.append(wrong_shop)

        # back in the browser
        driver.back()

        # click 'Servises'
        wait.until(EC.element_to_be_clickable((By.XPATH, "//p[@class ='_1zyfI'][contains(., 'Servises')]"))).click()
        WebDriverWait(driver, 3)

        # assert 'Servises' title, hepler
        HP.check_title('Servises', driver)

        # check specific element on the page
        try:
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//h1[contains(.,'Our Services')]")))
            print("The right 'Servises' page")
        except WDE:
            wrong_servises = "Smt is wrong with 'Servises' page"
            print(wrong_servises)
            wrong_list.append(wrong_servises)

        # back in the browser
        driver.back()

        # click 'Home'
        wait.until(EC.element_to_be_clickable((By.XPATH, "//p[@class='_1zyfI'][contains(.,'Home')]"))).click()
        WebDriverWait(driver, 3)

        # assert 'Home' title, hepler
        HP.check_title('Home', driver)

        # check specific element on the page
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "(// span[contains(., 'LET CALIFORNIA MARKETING "
                                                                   "GROW YOUR BUSINECS')])[2]")))
            print("The right 'Home' page")
        except WDE:
            wrong_home = "Smt is wrong with 'Home' page"
            print(wrong_home)
            wrong_list.append(wrong_home)

        # assert the assertion list is empty
        print(len(wrong_list))
        if len(wrong_list) == 0:
            print("All header links work correctly")
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "All header links are correct!"}}')
        else:
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Not all header links are corrrect"}}')
            raise Exception("Check header links")
        driver.quit()

    # localization test of first screen
    def test_first_screen_text(self):
        driver = self.driver
        driver.get(HP.url)
        self.driver.maximize_window()

        # check the title is right, helper
        HP.assert_title("California Marcketing", driver)

        # get the text
        first_line = driver.find_element(By.XPATH, "//a[contains(.,'CALIFORNIA MARCKETING')]").text
        second_line = driver.find_element(By.XPATH,
                                          "(//a[@href='https://qasvus.wixsite.com/ca-marketing/blog'])[2]").text
        third_line = driver.find_element(By.XPATH,
                                         "(//span[contains(.,'LET CALIFORNIA MARKETING GROW YOUR BUSINECS')])[2]").text
        print(first_line, second_line, third_line)

        # compare on site text with correct one, first line
        if first_line == "CALIFORNIA MARKETING":
            print("First line is fine")
        else:
            print("Incorrect first line")

        # compare on site text with correct one, second line
        if second_line == "A Full-Stack Creative Agency in CA":
            print("Second line is fine")
        else:
            print("Incorrect second line")

        # compare on site text with correct one, third line
        if third_line == "LET CALIFORNIA MARKETING GROW YOUR BUSINESS":
            print("Third line is fine")
        else:
            print("Incorrect third line")

        # assert full text
        if [first_line, second_line, third_line] == ["CALIFORNIA MARKETING", "A Full-Stack Creative "
                                                                                         "Agency in CA",
                                                                 'LET CALIFORNIA MARKETING GROW YOUR BUSINESS']:
            print("First screen text is correct")
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "First screen text is correct"}}')
        else:
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "First screen text is not correct""}}')
            raise Exception("Check the first screen text")
        driver.quit()

    # wix chat functionality
    def test_lets_chat(self):
        driver = self.driver
        driver.get(HP.url)
        self.driver.maximize_window()

        # check the title is right, helper
        HP.assert_title("California Marcketing", driver)

        # set up faker
        f = Faker()

        # assertion list
        list_for_assertion = []

        time.sleep(3)

        # find and switch to chat iframe
        iframe = driver.find_element(By.XPATH, "//iframe [@title='Wix Chat']")
        driver.switch_to.frame(iframe)

        # find and open the chat
        try:
            driver.find_element(
                locate_with(By.CLASS_NAME, "_28JNc").below({By.XPATH: "//*[@charset='utf-8']"})).click()
            ok_result = "Chat is on the page"
            print(ok_result)
            list_for_assertion.append(ok_result)
        except WDE:
            fail_result = "Smt is wrong with chat"
            print(fail_result)
            list_for_assertion.append(fail_result)

        time.sleep(3)

        # send fake text
        try:
            driver.find_element(By.TAG_NAME, "textarea").send_keys(f.text() + Keys.ENTER)
            ok_result = "The message was sent in the chat"
            print(ok_result)
            list_for_assertion.append(ok_result)
        except WDE:
            fail_result = "Smt is wrong with messages"
            print(fail_result)
            list_for_assertion.append(fail_result)

        # check if except prints in the list for final assertion
        list_for_assertion = ' '.join(list_for_assertion).split()
        if "wrong" not in list_for_assertion:
            print("The chat works correctly")
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Online chat works correctly!"}}')
        else:
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Smt is wrong with chat"}}')
            raise Exception("Check the chat")
        driver.quit()

    # video search bar functionality
    def test_video_selection(self):
        driver = self.driver
        driver.get(HP.url)
        self.driver.maximize_window()

        # check the title is right, helper
        HP.assert_title("California Marcketing", driver)

        time.sleep(2)

        # find video search bar and send "Big Sur"
        try:
            driver.find_element(
                locate_with(By.CLASS_NAME, "VVhXp").below({By.XPATH: "//*[@title='All Videos']"})).send_keys(
                "Big Sur" + Keys.ENTER)
            print("Search bar works")
        except WDE:
            print("Check the search bar")

        time.sleep(2)

        # assert video with "Big Sur" in the title is displayed
        if driver.find_element(By.XPATH, "//*[@src='https://i.ytimg.com/vi/X-HxnNAaioM/mqdefault.jpg']").is_displayed():
            print("The right video is displayed")
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "The right video is displayed!"}}')
        else:
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Сье is wrong with video search bar"}}')
            raise Exception("Check video search bar")
        driver.quit()

    # cart smoke testing
    def test_cart_shopping(self):
        driver = self.driver
        driver.get(HP.url)
        self.driver.maximize_window()

        # check the title is right, helper
        HP.assert_title("California Marcketing", driver)

        # set up wait time
        wait = WebDriverWait(driver, 3)

        # click 'Shop'
        shop = wait.until(EC.element_to_be_clickable((By.XPATH, "//p[@class ='_1zyfI'][contains(., 'Shop')]")))
        shop.click()

        time.sleep(5)

        # assert 'Shop' title, helper
        HP.check_title('Shop', driver)

        # check specific element on the page, helper
        HP.specific_element_check('Shop', "//h3[contains(.,'Product 1')]", driver)

        # find 'product1', get text and click
        product = driver.find_element(By.XPATH, "// h3[contains(.,'Product 1')]")
        product_text = product.text
        product.click()
        print("Successfully clicked on", product_text)

        time.sleep(5)

        # assert the title
        assert product_text in driver.title
        print("The right product page")

        # assert the product name on the page match the one was chosen
        on_page_product_text = driver.find_element(By.XPATH, "//h1[contains(@class,'2yxAN')]").text
        if product_text == on_page_product_text:
            print("Match:", product_text, "and", on_page_product_text)
        else:
            print("Not a match")

        # find price for one piece, turn into integer
        price = driver.find_element(By.XPATH, "//span[@data-hook='formatted-primary-price']").text
        price = int(price.replace("$", "").replace(".00", ""))
        print("The price for 1 piece is:", price)

        # set color and quantity
        try:
            driver.find_element(By.XPATH, "(//div[contains(@class,'ColorPickerItem2201735070__radioInner')])[1]").click()
            driver.find_element(By.XPATH, "//span[contains(@data-hook, 'number-input-spinner-up-arrow')]").click()
            print("The color and quantity were set")
        except WDE:
            print("Smt is wrong with color/quantity")

        # click on "Add to cart" button
        try:
            driver.find_element(By.XPATH,
                            "//span[@class ='buttonnext1002411228__content'][contains(., 'Add to Card')]").click()
            print("The product was added to cart")
        except WDE:
            print("Smt is wrong with adding to cart")

        time.sleep(5)

        # find curtain frame and switch
        try:
            driver.switch_to.frame(driver.find_element(By.CLASS_NAME, "_2DJg7"))
            print("Switched to frame")
        except WDE:
            print("Check the frame")

        # click on "View cart" button
        wait.until(EC.element_to_be_clickable((By.ID, "widget-view-cart-button"))).click()

        time.sleep(5)

        # assert title
        assert "Cart" in driver.title

        # assert specific element on the page
        my_cart = driver.find_element(By.CLASS_NAME, "_2NsyK").text
        if my_cart == "My cart":
            print("We are on the cart page")
        else:
            print("Check the cart page")

        # assert product name
        product_name = driver.find_element(By.CLASS_NAME, "_1dkgR").text
        if product_name == product_text:
            print("Right product in the cart")
        else:
            print("Wrong product in the cart")

        # check the quantity is correct
        howMany = driver.find_element(By.XPATH, "//input[@aria-label='Choose quantity']").get_attribute("value")
        if howMany == "2":
            print("Correct quantity")
        else:
            print("Wrong quantity")

        # check the price is correct
        total_price = driver.find_element(By.CLASS_NAME, "_32Pyj").text
        total_price = int(total_price.replace("$", "").replace(".00", ""))
        if total_price == int(howMany) * price:
            print("Correct total price")
        else:
            print("Wrong total price")

        # check the color is correct, helper
        HP.product_color("(//li[contains(.,'Color: Black')])[2]", "Black", driver)

        # find and click on 'CheckOut' button
        try:
            driver.find_element(By.CLASS_NAME, "_34QVp").click()
            print("Click on 'CheckOut' button")
        except WDE:
            print("Smt is wrong with 'CheckOut' button")

        time.sleep(5)

        # find iframe and switch
        try:
            driver.switch_to.frame(driver.find_element(By. CLASS_NAME, "MUsGO"))
            print("Switched to frame")
        except WDE:
            print("No frame")

        # assert the frame doesn't include "We can't accept online orders right now"
        fr2text = driver.find_element(By. CLASS_NAME, "maaPx").text
        print(fr2text)
        if "We can't accept online orders right now" not in fr2text:
            print("Checkout without 'cant accept online orders'")
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Checkout without: cant accept online orders"}}')
        else:
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Wrong checkout process"}}')
            raise Exception("Check checkout")
        driver.quit()

    # event reservation smoke testing
    def test_event_reservation(self):
        driver = self.driver
        driver.get(HP.url)
        self.driver.maximize_window()

        # set up faker library
        f = Faker()

        # set up wait time
        wait = WebDriverWait(driver, 3)

        # check the title is right, helper
        HP.assert_title("California Marcketing", driver)

        time.sleep(4)

        try:
            event = driver.find_element(By.XPATH, "(//a[@data-hook='ev-rsvp-button'][contains(.,'RSVP')])[1]")
            print("Event section")
        except WDE:
            print("Cant find event section")

        # name, date and place of the first event
        event_name = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "DTbMp"))).text
        print(event_name)
        event_date = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "VFsgs"))).text
        print(event_date)
        event_place = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "lNymU"))).text
        print(event_place)

        # click on "RSVP" button
        event.click()
        print("'RSVP' button was clicked")

        # assert title
        assert event_name in driver.title
        print("Its the middle event page")

        # check if event name, date and place are correct, helpers
        HP.comparison_xpath("//h1[@data-hook='event-title']", event_name, "event name", driver)
        HP.comparison_class("_6vtCb", event_date, "event date", driver)
        HP.comparison_class("-OEip", event_place, "event place", driver)

        # click on 'RSVP' button
        time.sleep(3)
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@data-hook='rsvp-button'][contains(.,'RSVP')])[2]"))).send_keys('\n')
        time.sleep(3)

        # assert driver title
        assert event_name in driver.title
        print("It`s the final event page")

        # check event name and place, helpers
        HP.comparison_xpath("//*[@data-hook='event-title']", event_name, "event name", driver)
        HP.comparison_xpath("//*[@data-hook='event-location']", event_place, "event place", driver)

        # fill the form
        driver.find_element(By.ID, "firstName").send_keys(f.first_name())
        driver.find_element(By.ID, "lastName").send_keys(f.last_name())
        driver.find_element(By.ID, "email").send_keys(f.email())

        # find and click on 'Submit' page
        try:
            driver.find_element(By.XPATH, "//button[@data-hook='form-button']").click()
            print("Submit button was clicked")
        except WDE:
            print("Check the 'Submit' button")

        time.sleep(5)

        # assert 'thank you' page
        if driver.find_element(By.XPATH, "//h2[@data-hook='thank-you-message-title']").text == "Thank you! See you soon":
            print("The form was submitted")
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Event form was submitted!"}}')
        else:
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Smt is wrong with event form submition"}}')
            raise Exception("Check event form")
        driver.quit()

    # subscription form functionality
    def test_subscribe_form(self):
        driver = self.driver
        driver.get(HP.url)
        self.driver.maximize_window()

        # set up Faker library
        f = Faker()

        # set up wait time
        wait = WebDriverWait(driver, 3)

        # check the title is right, helper
        HP.assert_title("California Marcketing", driver)

        # find 'Subscription form'
        form = wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(@class,'color_15')])[14]"))).text
        if form == "Subscribe Form":
            print("'Subscription form' was found")
        else:
            print("Cant find 'Subscription form'")

        # put email
        try:
            driver.find_element(By.XPATH, "//input[@id='input_comp-ksocylga1']").send_keys(f.email())
            print("The email was sent")
        except WDE:
            print("The email wasn't sent")

        # wait and click on 'Submit' button
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-disabled='false'][contains(., 'Submit')]"))).click()
        print("Submit button was clicked")

        time.sleep(4)

        # assert the form was sent
        if driver.find_element(By.XPATH, "//span[@class='color_15'][contains(.,'Thanks for submitting!')]").is_displayed():
            print("The form was sent")
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "The form was sent!"}}')
        else:
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "The form was not sent"}}')
            raise Exception("Check subscription form")
        driver.quit()

class monterey_1920_1080_safari(unittest.TestCase):

    def setUp(self):
        desired_cap = {
            'os_version': 'Monterey',
            'resolution': '1920x1080',
            'browser': 'Safari',
            'browser_version': '15.3',
            'os': 'OS X',
            'name': 'BStack-[Python] Sample Test',  # test name
            'build': 'BStack Build Number 1'  # CI/CD job or build name
        }
        url = KEY.my_key
        desired_cap['acceptSslCerts'] = True
        self.driver = webdriver.Remote(command_executor=url, desired_capabilities=desired_cap)

    # check if social media icons are clickable
    def test_icons_clickability(self):
        driver = self.driver
        driver.get(HP.url)
        self.driver.maximize_window()

        # random delay function, helper
        HP.delay_1_5()

        # check the title is right, helper
        HP.assert_title("California Marcketing", driver)

        # set up wait time
        wait = WebDriverWait(driver, 3)

        # verify icons are clickable, helpers
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.facebook)))
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.twitter)))
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.vk)))
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.youtube)))
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.linkedin)))
            print("Icons are clickable")
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "All icons are clickable"}}')
        except WDE:
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Some icons are not clickable"}}')
            raise Exception("Check icons clickability")
        driver.quit()

    # validate all social network links lead to right pages
    def test_social_network_links(self):
        driver = self.driver
        driver.get(HP.url)
        self.driver.maximize_window()

        # random delay function, helper
        HP.delay_1_5()

        # check the title is right, helper
        HP.assert_title("California Marcketing", driver)

        # find Facebook icon and click
        driver.find_element(By.XPATH, HP.facebook).click()

        # original window set up
        original_window = driver.current_window_handle

        # switch windows if more than one, helper
        HP.switching_windows(driver)

        # random delay, helper
        HP.delay_1_5()

        # verify you are on the right page, helper
        HP.assert_title("Facebook", driver)

        # verify logo, try/except, plus screenshots, helper
        HP.logo_check("Facebook", "//div[@class='l9j0dhe7 buofh1pr j83agx80 bp9cbjyn']", driver)

        # verify the specific element, try/except, plus screenshots, helper
        HP.specific_element_check("Facebook", "//a[contains(text(), 'QA at Silicon Valley California')]", driver)

        # close and switch back
        driver.close()
        driver.switch_to.window(original_window)

        # verify the title of the page when back, helper
        HP.assert_back_title(driver)

        # find TW icon and click
        driver.find_element(By.XPATH, HP.twitter).click()

        # switch windows if more than one, helper
        HP.switching_windows(driver)

        HP.delay_1_5()

        # verify you are on the right page
        HP.assert_title("Твиттер", driver)

        # verify logo, try/except, plus screenshots, helper
        HP.logo_check("TW", "//*[@role='heading']", driver)

        # verify the specific element, try/except, plus screenshots, helper
        HP.specific_element_check("TW", "//a[@dir='ltr'][contains(.,'http://QASV.US')]", driver)

        # close and switch back
        driver.close()
        driver.switch_to.window(original_window)

        # verify the title of the page when back, helper
        HP.assert_back_title(driver)

        # find VK icon and click
        driver.find_element(By.XPATH, HP.vk).click()

        # switch windows if more than one, helper
        HP.switching_windows(driver)

        HP.delay_1_5()

        # verify you are on the right page
        HP.assert_title("QA at Silicon Valley", driver)

        # verify logo, try/except, plus screenshots, helper
        HP.logo_check("VK", "//*[@class='HeaderNav__item HeaderNav__item--logo']", driver)

        # verify the specific element, try/except, plus screenshots, helper
        HP.specific_element_check("VK", "//*[@href='/away.php?to=https%3A%2F%2Fbit.ly%2F2Q8bBhW&cc_key=']", driver)

        # close and switch back
        driver.close()
        driver.switch_to.window(original_window)

        # verify the title of the page when back, helper
        HP.assert_back_title(driver)

        # find TouTube icon and click
        driver.find_element(By.XPATH, HP.youtube).click()

        # switch windows if more than one, helper
        HP.switching_windows(driver)

        HP.delay_1_5()

        # verify you are on the right page
        HP.assert_title("Sergey Efremov", driver)

        # verify logo, try/except, plus screenshots, helper
        HP.logo_check("YouTube", "//*[@id='logo-icon']", driver)

        # verify the specific element, try/except, plus screenshots, helper
        HP.specific_element_check("YouTube", "//*[contains(text(), 'Sergey Efremov_USA')]", driver)

        # close and switch back
        driver.close()
        driver.switch_to.window(original_window)

        # verify the title of the page when back, helper
        HP.assert_back_title(driver)

        # find LinkedIn icon and click
        driver.find_element(By.XPATH, HP.linkedin).click()

        # switch windows if more than one, helper
        HP.switching_windows(driver)

        HP.delay_1_5()

        # verify you are on the right page
        HP.assert_title("LinkedIn", driver)

        # verify logo, try/except, plus screenshots, helper
        HP.logo_check("LinkedIn", "//*[@id='ember16']", driver)

        # verify the specific element, try/except, plus screenshots, helper
        HP.specific_element_check("LinkedIn", "//*[@alt='QA at Silicon Valley California logo']", driver)

        # close and switch back
        driver.close()
        driver.switch_to.window(original_window)

        # verify the title of the page when back, helper
        HP.assert_back_title(driver)
        driver.quit()

    # check "Get in touch"
    def test_get_in_touch(self):
        driver = self.driver
        driver.get(HP.url)
        self.driver.maximize_window()

        # check the title is right, helper
        HP.assert_title("California Marcketing", driver)

        # set wait time
        wait = WebDriverWait(driver, 3)

        # check 'Get in touch' clickability
        try:
            wait.until(EC.element_to_be_clickable(
                (By.CLASS_NAME, "wQYUw")))
            print("'Get in touch' clickable")
        except WDE:
            print("Check 'Get in touch' clickability")

        # check the button text is correct
        button_text = driver.find_element(By.CLASS_NAME, "wQYUw").text
        if button_text == "Get In Touch":
            print("Right 'Get in Touch' button text")
        else:
            print("Incorrect button text")

        # compare on site email with the correct one
        email = driver.find_element(By.LINK_TEXT, "Get In Touch").get_attribute("href")

        # print on page email and supposed email
        print(email)
        print(HP.main_email)

        # assert on page email
        if email == HP.main_email:
            print("The email is correct")
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "The email is correctt!"}}')
        else:
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "The email is not correct"}}')
            raise Exception("The email is not correct")
        driver.quit()

    # check header menu links (except "More")
    def test_header_menu_links(self):
        driver = self.driver
        driver.get(HP.url)
        self.driver.maximize_window()

        # check the title is right, helper
        HP.assert_title("California Marcketing", driver)

        # set wait time
        wait = WebDriverWait(driver, 5)

        # list for final assertion
        wrong_list = []

        # click 'Blog'
        wait.until(EC.element_to_be_clickable((By.XPATH, "//p[@class='_1zyfI'][contains(.,'Blog')]"))).click()
        WebDriverWait(driver, 3)

        # assert 'Blog' title, hepler
        HP.check_title('Blog', driver)

        # check specific element on the page
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'All Posts')]")))
            print("The right 'Blog' page")
        except WDE:
            wrong_blog = "Smt is wrong with 'Blog' page"
            print(wrong_blog)
            wrong_list.append(wrong_blog)

        # back in the browser
        driver.back()

        # click 'Shop'
        wait.until(EC.element_to_be_clickable((By.XPATH, "//p[@class ='_1zyfI'][contains(., 'Shop')]"))).click()
        WebDriverWait(driver, 3)

        # assert 'Shop' title, hepler
        HP.check_title('Shop', driver)

        # check specific element on the page
        try:
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//h3[contains(.,'Product 1')]")))
            print("The right 'Shop' page")
        except WDE:
            wrong_shop = "Smt is wrong with 'Shop' page"
            print(wrong_shop)
            wrong_list.append(wrong_shop)

        # back in the browser
        driver.back()

        # click 'Servises'
        wait.until(EC.element_to_be_clickable((By.XPATH, "//p[@class ='_1zyfI'][contains(., 'Servises')]"))).click()
        WebDriverWait(driver, 3)

        # assert 'Servises' title, hepler
        HP.check_title('Servises', driver)

        # check specific element on the page
        try:
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//h1[contains(.,'Our Services')]")))
            print("The right 'Servises' page")
        except WDE:
            wrong_servises = "Smt is wrong with 'Servises' page"
            print(wrong_servises)
            wrong_list.append(wrong_servises)

        # back in the browser
        driver.back()

        # click 'Home'
        wait.until(EC.element_to_be_clickable((By.XPATH, "//p[@class='_1zyfI'][contains(.,'Home')]"))).click()
        WebDriverWait(driver, 3)

        # assert 'Home' title, hepler
        HP.check_title('Home', driver)

        # check specific element on the page
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "(// span[contains(., 'LET CALIFORNIA MARKETING "
                                                                   "GROW YOUR BUSINECS')])[2]")))
            print("The right 'Home' page")
        except WDE:
            wrong_home = "Smt is wrong with 'Home' page"
            print(wrong_home)
            wrong_list.append(wrong_home)

        # assert the assertion list is empty
        print(len(wrong_list))
        if len(wrong_list) == 0:
            print("All header links work correctly")
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "All header links are correct!"}}')
        else:
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Not all header links are corrrect"}}')
            raise Exception("Check header links")
        driver.quit()

    # localization test of first screen
    def test_first_screen_text(self):
        driver = self.driver
        driver.get(HP.url)
        self.driver.maximize_window()

        # check the title is right, helper
        HP.assert_title("California Marcketing", driver)

        # get the text
        first_line = driver.find_element(By.XPATH, "//a[contains(.,'CALIFORNIA MARCKETING')]").text
        second_line = driver.find_element(By.XPATH,
                                          "(//a[@href='https://qasvus.wixsite.com/ca-marketing/blog'])[2]").text
        third_line = driver.find_element(By.XPATH,
                                         "(//span[contains(.,'LET CALIFORNIA MARKETING GROW YOUR BUSINECS')])[2]").text
        print(first_line, second_line, third_line)

        # compare on site text with correct one, first line
        if first_line == "CALIFORNIA MARKETING":
            print("First line is fine")
        else:
            print("Incorrect first line")

        # compare on site text with correct one, second line
        if second_line == "A Full-Stack Creative Agency in CA":
            print("Second line is fine")
        else:
            print("Incorrect second line")

        # compare on site text with correct one, third line
        if third_line == "LET CALIFORNIA MARKETING GROW YOUR BUSINESS":
            print("Third line is fine")
        else:
            print("Incorrect third line")

        # assert full text
        if [first_line, second_line, third_line] == ["CALIFORNIA MARKETING", "A Full-Stack Creative "
                                                                                         "Agency in CA",
                                                                 'LET CALIFORNIA MARKETING GROW YOUR BUSINESS']:
            print("First screen text is correct")
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "First screen text is correct"}}')
        else:
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "First screen text is not correct""}}')
            raise Exception("Check the first screen text")
        driver.quit()

    # wix chat functionality
    def test_lets_chat(self):
        driver = self.driver
        driver.get(HP.url)
        self.driver.maximize_window()

        # check the title is right, helper
        HP.assert_title("California Marcketing", driver)

        # set up faker
        f = Faker()

        # assertion list
        list_for_assertion = []

        time.sleep(3)

        # find and switch to chat iframe
        iframe = driver.find_element(By.XPATH, "//iframe [@title='Wix Chat']")
        driver.switch_to.frame(iframe)

        # find and open the chat
        try:
            driver.find_element(
                locate_with(By.CLASS_NAME, "_28JNc").below({By.XPATH: "//*[@charset='utf-8']"})).click()
            ok_result = "Chat is on the page"
            print(ok_result)
            list_for_assertion.append(ok_result)
        except WDE:
            fail_result = "Smt is wrong with chat"
            print(fail_result)
            list_for_assertion.append(fail_result)

        time.sleep(3)

        # send fake text
        try:
            driver.find_element(By.TAG_NAME, "textarea").send_keys(f.text() + Keys.ENTER)
            ok_result = "The message was sent in the chat"
            print(ok_result)
            list_for_assertion.append(ok_result)
        except WDE:
            fail_result = "Smt is wrong with messages"
            print(fail_result)
            list_for_assertion.append(fail_result)

        # check if except prints in the list for final assertion
        list_for_assertion = ' '.join(list_for_assertion).split()
        if "wrong" not in list_for_assertion:
            print("The chat works correctly")
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Online chat works correctly!"}}')
        else:
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Smt is wrong with chat"}}')
            raise Exception("Check the chat")
        driver.quit()

    # video search bar functionality
    def test_video_selection(self):
        driver = self.driver
        driver.get(HP.url)
        self.driver.maximize_window()

        # check the title is right, helper
        HP.assert_title("California Marcketing", driver)

        time.sleep(2)

        # find video search bar and send "Big Sur"
        try:
            driver.find_element(
                locate_with(By.CLASS_NAME, "VVhXp").below({By.XPATH: "//*[@title='All Videos']"})).send_keys(
                "Big Sur" + Keys.ENTER)
            print("Search bar works")
        except WDE:
            print("Check the search bar")

        time.sleep(2)

        # assert video with "Big Sur" in the title is displayed
        if driver.find_element(By.XPATH, "//*[@src='https://i.ytimg.com/vi/X-HxnNAaioM/mqdefault.jpg']").is_displayed():
            print("The right video is displayed")
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "The right video is displayed!"}}')
        else:
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Сье is wrong with video search bar"}}')
            raise Exception("Check video search bar")
        driver.quit()

    # cart smoke testing
    def test_cart_shopping(self):
        driver = self.driver
        driver.get(HP.url)
        self.driver.maximize_window()

        # check the title is right, helper
        HP.assert_title("California Marcketing", driver)

        # set up wait time
        wait = WebDriverWait(driver, 3)

        # click 'Shop'
        shop = wait.until(EC.element_to_be_clickable((By.XPATH, "//p[@class ='_1zyfI'][contains(., 'Shop')]")))
        shop.click()

        time.sleep(5)

        # assert 'Shop' title, helper
        HP.check_title('Shop', driver)

        # check specific element on the page, helper
        HP.specific_element_check('Shop', "//h3[contains(.,'Product 1')]", driver)

        # find 'product1', get text and click
        product = driver.find_element(By.XPATH, "// h3[contains(.,'Product 1')]")
        product_text = product.text
        product.click()
        print("Successfully clicked on", product_text)

        time.sleep(5)

        # assert the title
        assert product_text in driver.title
        print("The right product page")

        # assert the product name on the page match the one was chosen
        on_page_product_text = driver.find_element(By.XPATH, "//h1[contains(@class,'2yxAN')]").text
        if product_text == on_page_product_text:
            print("Match:", product_text, "and", on_page_product_text)
        else:
            print("Not a match")

        # find price for one piece, turn into integer
        price = driver.find_element(By.XPATH, "//span[@data-hook='formatted-primary-price']").text
        price = int(price.replace("$", "").replace(".00", ""))
        print("The price for 1 piece is:", price)

        # set color and quantity
        try:
            driver.find_element(By.XPATH, "(//div[contains(@class,'ColorPickerItem2201735070__radioInner')])[1]").click()
            driver.find_element(By.XPATH, "//span[contains(@data-hook, 'number-input-spinner-up-arrow')]").click()
            print("The color and quantity were set")
        except WDE:
            print("Smt is wrong with color/quantity")

        # click on "Add to cart" button
        try:
            driver.find_element(By.XPATH,
                            "//span[@class ='buttonnext1002411228__content'][contains(., 'Add to Card')]").click()
            print("The product was added to cart")
        except WDE:
            print("Smt is wrong with adding to cart")

        time.sleep(5)

        # find curtain frame and switch
        try:
            driver.switch_to.frame(driver.find_element(By.CLASS_NAME, "_2DJg7"))
            print("Switched to frame")
        except WDE:
            print("Check the frame")

        # click on "View cart" button
        wait.until(EC.element_to_be_clickable((By.ID, "widget-view-cart-button"))).click()

        time.sleep(5)

        # assert title
        assert "Cart" in driver.title

        # assert specific element on the page
        my_cart = driver.find_element(By.CLASS_NAME, "_2NsyK").text
        if my_cart == "My cart":
            print("We are on the cart page")
        else:
            print("Check the cart page")

        # assert product name
        product_name = driver.find_element(By.CLASS_NAME, "_1dkgR").text
        if product_name == product_text:
            print("Right product in the cart")
        else:
            print("Wrong product in the cart")

        # check the quantity is correct
        howMany = driver.find_element(By.XPATH, "//input[@aria-label='Choose quantity']").get_attribute("value")
        if howMany == "2":
            print("Correct quantity")
        else:
            print("Wrong quantity")

        # check the price is correct
        total_price = driver.find_element(By.CLASS_NAME, "_32Pyj").text
        total_price = int(total_price.replace("$", "").replace(".00", ""))
        if total_price == int(howMany) * price:
            print("Correct total price")
        else:
            print("Wrong total price")

        # check the color is correct, helper
        HP.product_color("(//li[contains(.,'Color: Black')])[2]", "Black", driver)

        # find and click on 'CheckOut' button
        try:
            driver.find_element(By.CLASS_NAME, "_34QVp").click()
            print("Click on 'CheckOut' button")
        except WDE:
            print("Smt is wrong with 'CheckOut' button")

        time.sleep(5)

        # find iframe and switch
        try:
            driver.switch_to.frame(driver.find_element(By. CLASS_NAME, "MUsGO"))
            print("Switched to frame")
        except WDE:
            print("No frame")

        # assert the frame doesn't include "We can't accept online orders right now"
        fr2text = driver.find_element(By. CLASS_NAME, "maaPx").text
        print(fr2text)
        if "We can't accept online orders right now" not in fr2text:
            print("Checkout without 'cant accept online orders'")
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Checkout without: cant accept online orders"}}')
        else:
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Wrong checkout process"}}')
            raise Exception("Check checkout")
        driver.quit()

    # event reservation smoke testing
    def test_event_reservation(self):
        driver = self.driver
        driver.get(HP.url)
        self.driver.maximize_window()

        # set up faker library
        f = Faker()

        # set up wait time
        wait = WebDriverWait(driver, 3)

        # check the title is right, helper
        HP.assert_title("California Marcketing", driver)

        time.sleep(4)

        try:
            event = driver.find_element(By.XPATH, "(//a[@data-hook='ev-rsvp-button'][contains(.,'RSVP')])[1]")
            print("Event section")
        except WDE:
            print("Cant find event section")

        # name, date and place of the first event
        event_name = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "DTbMp"))).text
        print(event_name)
        event_date = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "VFsgs"))).text
        print(event_date)
        event_place = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "lNymU"))).text
        print(event_place)

        # click on "RSVP" button
        event.click()
        print("'RSVP' button was clicked")

        # assert title
        assert event_name in driver.title
        print("Its the middle event page")

        # check if event name, date and place are correct, helpers
        HP.comparison_xpath("//h1[@data-hook='event-title']", event_name, "event name", driver)
        HP.comparison_class("_6vtCb", event_date, "event date", driver)
        HP.comparison_class("-OEip", event_place, "event place", driver)

        # click on 'RSVP' button
        time.sleep(3)
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@data-hook='rsvp-button'][contains(.,'RSVP')])[2]"))).send_keys('\n')
        time.sleep(3)

        # assert driver title
        assert event_name in driver.title
        print("It`s the final event page")

        # check event name and place, helpers
        HP.comparison_xpath("//*[@data-hook='event-title']", event_name, "event name", driver)
        HP.comparison_xpath("//*[@data-hook='event-location']", event_place, "event place", driver)

        # fill the form
        driver.find_element(By.ID, "firstName").send_keys(f.first_name())
        driver.find_element(By.ID, "lastName").send_keys(f.last_name())
        driver.find_element(By.ID, "email").send_keys(f.email())

        # find and click on 'Submit' page
        try:
            driver.find_element(By.XPATH, "//button[@data-hook='form-button']").click()
            print("Submit button was clicked")
        except WDE:
            print("Check the 'Submit' button")

        time.sleep(5)

        # assert 'thank you' page
        if driver.find_element(By.XPATH, "//h2[@data-hook='thank-you-message-title']").text == "Thank you! See you soon":
            print("The form was submitted")
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Event form was submitted!"}}')
        else:
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Smt is wrong with event form submition"}}')
            raise Exception("Check event form")
        driver.quit()

    # subscription form functionality
    def test_subscribe_form(self):
        driver = self.driver
        driver.get(HP.url)
        self.driver.maximize_window()

        # set up Faker library
        f = Faker()

        # set up wait time
        wait = WebDriverWait(driver, 3)

        # check the title is right, helper
        HP.assert_title("California Marcketing", driver)

        # find 'Subscription form'
        form = wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(@class,'color_15')])[14]"))).text
        if form == "Subscribe Form":
            print("'Subscription form' was found")
        else:
            print("Cant find 'Subscription form'")

        # put email
        try:
            driver.find_element(By.XPATH, "//input[@id='input_comp-ksocylga1']").send_keys(f.email())
            print("The email was sent")
        except WDE:
            print("The email wasn't sent")

        # wait and click on 'Submit' button
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-disabled='false'][contains(., 'Submit')]"))).click()
        print("Submit button was clicked")

        time.sleep(4)

        # assert the form was sent
        if driver.find_element(By.XPATH, "//span[@class='color_15'][contains(.,'Thanks for submitting!')]").is_displayed():
            print("The form was sent")
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "The form was sent!"}}')
        else:
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "The form was not sent"}}')
            raise Exception("Check subscription form")
        driver.quit()

class monterey_1920_1080_edge(unittest.TestCase):

    def setUp(self):
        desired_cap = {
            'os_version': 'Monterey',
            'resolution': '1920x1080',
            'browser': 'Edge',
            'browser_version': 'latest',
            'os': 'OS X',
            'name': 'BStack-[Python] Sample Test',  # test name
            'build': 'BStack Build Number 1'  # CI/CD job or build name
        }
        url = KEY.my_key
        desired_cap['acceptSslCerts'] = True
        self.driver = webdriver.Remote(command_executor=url, desired_capabilities=desired_cap)

    # check if social media icons are clickable
    def test_icons_clickability(self):
        driver = self.driver
        driver.get(HP.url)
        self.driver.maximize_window()

        # random delay function, helper
        HP.delay_1_5()

        # check the title is right, helper
        HP.assert_title("California Marcketing", driver)

        # set up wait time
        wait = WebDriverWait(driver, 3)

        # verify icons are clickable, helpers
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.facebook)))
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.twitter)))
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.vk)))
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.youtube)))
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.linkedin)))
            print("Icons are clickable")
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "All icons are clickable"}}')
        except WDE:
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Some icons are not clickable"}}')
            raise Exception("Check icons clickability")
        driver.quit()

    # validate all social network links lead to right pages
    def test_social_network_links(self):
        driver = self.driver
        driver.get(HP.url)
        self.driver.maximize_window()

        # random delay function, helper
        HP.delay_1_5()

        # check the title is right, helper
        HP.assert_title("California Marcketing", driver)

        # find Facebook icon and click
        driver.find_element(By.XPATH, HP.facebook).click()

        # original window set up
        original_window = driver.current_window_handle

        # switch windows if more than one, helper
        HP.switching_windows(driver)

        # random delay, helper
        HP.delay_1_5()

        # verify you are on the right page, helper
        HP.assert_title("Facebook", driver)

        # verify logo, try/except, plus screenshots, helper
        HP.logo_check("Facebook", "//div[@class='l9j0dhe7 buofh1pr j83agx80 bp9cbjyn']", driver)

        # verify the specific element, try/except, plus screenshots, helper
        HP.specific_element_check("Facebook", "//a[contains(text(), 'QA at Silicon Valley California')]", driver)

        # close and switch back
        driver.close()
        driver.switch_to.window(original_window)

        # verify the title of the page when back, helper
        HP.assert_back_title(driver)

        # find TW icon and click
        driver.find_element(By.XPATH, HP.twitter).click()

        # switch windows if more than one, helper
        HP.switching_windows(driver)

        HP.delay_1_5()

        # verify you are on the right page
        HP.assert_title("Твиттер", driver)

        # verify logo, try/except, plus screenshots, helper
        HP.logo_check("TW", "//*[@role='heading']", driver)

        # verify the specific element, try/except, plus screenshots, helper
        HP.specific_element_check("TW", "//a[@dir='ltr'][contains(.,'http://QASV.US')]", driver)

        # close and switch back
        driver.close()
        driver.switch_to.window(original_window)

        # verify the title of the page when back, helper
        HP.assert_back_title(driver)

        # find VK icon and click
        driver.find_element(By.XPATH, HP.vk).click()

        # switch windows if more than one, helper
        HP.switching_windows(driver)

        HP.delay_1_5()

        # verify you are on the right page
        HP.assert_title("QA at Silicon Valley", driver)

        # verify logo, try/except, plus screenshots, helper
        HP.logo_check("VK", "//*[@class='HeaderNav__item HeaderNav__item--logo']", driver)

        # verify the specific element, try/except, plus screenshots, helper
        HP.specific_element_check("VK", "//*[@href='/away.php?to=https%3A%2F%2Fbit.ly%2F2Q8bBhW&cc_key=']", driver)

        # close and switch back
        driver.close()
        driver.switch_to.window(original_window)

        # verify the title of the page when back, helper
        HP.assert_back_title(driver)

        # find TouTube icon and click
        driver.find_element(By.XPATH, HP.youtube).click()

        # switch windows if more than one, helper
        HP.switching_windows(driver)

        HP.delay_1_5()

        # verify you are on the right page
        HP.assert_title("Sergey Efremov", driver)

        # verify logo, try/except, plus screenshots, helper
        HP.logo_check("YouTube", "//*[@id='logo-icon']", driver)

        # verify the specific element, try/except, plus screenshots, helper
        HP.specific_element_check("YouTube", "//*[contains(text(), 'Sergey Efremov_USA')]", driver)

        # close and switch back
        driver.close()
        driver.switch_to.window(original_window)

        # verify the title of the page when back, helper
        HP.assert_back_title(driver)

        # find LinkedIn icon and click
        driver.find_element(By.XPATH, HP.linkedin).click()

        # switch windows if more than one, helper
        HP.switching_windows(driver)

        HP.delay_1_5()

        # verify you are on the right page
        HP.assert_title("LinkedIn", driver)

        # verify logo, try/except, plus screenshots, helper
        HP.logo_check("LinkedIn", "//*[@id='ember16']", driver)

        # verify the specific element, try/except, plus screenshots, helper
        HP.specific_element_check("LinkedIn", "//*[@alt='QA at Silicon Valley California logo']", driver)

        # close and switch back
        driver.close()
        driver.switch_to.window(original_window)

        # verify the title of the page when back, helper
        HP.assert_back_title(driver)
        driver.quit()

    # check "Get in touch"
    def test_get_in_touch(self):
        driver = self.driver
        driver.get(HP.url)
        self.driver.maximize_window()

        # check the title is right, helper
        HP.assert_title("California Marcketing", driver)

        # set wait time
        wait = WebDriverWait(driver, 3)

        # check 'Get in touch' clickability
        try:
            wait.until(EC.element_to_be_clickable(
                (By.CLASS_NAME, "wQYUw")))
            print("'Get in touch' clickable")
        except WDE:
            print("Check 'Get in touch' clickability")

        # check the button text is correct
        button_text = driver.find_element(By.CLASS_NAME, "wQYUw").text
        if button_text == "Get In Touch":
            print("Right 'Get in Touch' button text")
        else:
            print("Incorrect button text")

        # compare on site email with the correct one
        email = driver.find_element(By.LINK_TEXT, "Get In Touch").get_attribute("href")

        # print on page email and supposed email
        print(email)
        print(HP.main_email)

        # assert on page email
        if email == HP.main_email:
            print("The email is correct")
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "The email is correctt!"}}')
        else:
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "The email is not correct"}}')
            raise Exception("The email is not correct")
        driver.quit()

    # check header menu links (except "More")
    def test_header_menu_links(self):
        driver = self.driver
        driver.get(HP.url)
        self.driver.maximize_window()

        # check the title is right, helper
        HP.assert_title("California Marcketing", driver)

        # set wait time
        wait = WebDriverWait(driver, 5)

        # list for final assertion
        wrong_list = []

        # click 'Blog'
        wait.until(EC.element_to_be_clickable((By.XPATH, "//p[@class='_1zyfI'][contains(.,'Blog')]"))).click()
        WebDriverWait(driver, 3)

        # assert 'Blog' title, hepler
        HP.check_title('Blog', driver)

        # check specific element on the page
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'All Posts')]")))
            print("The right 'Blog' page")
        except WDE:
            wrong_blog = "Smt is wrong with 'Blog' page"
            print(wrong_blog)
            wrong_list.append(wrong_blog)

        # back in the browser
        driver.back()

        # click 'Shop'
        wait.until(EC.element_to_be_clickable((By.XPATH, "//p[@class ='_1zyfI'][contains(., 'Shop')]"))).click()
        WebDriverWait(driver, 3)

        # assert 'Shop' title, hepler
        HP.check_title('Shop', driver)

        # check specific element on the page
        try:
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//h3[contains(.,'Product 1')]")))
            print("The right 'Shop' page")
        except WDE:
            wrong_shop = "Smt is wrong with 'Shop' page"
            print(wrong_shop)
            wrong_list.append(wrong_shop)

        # back in the browser
        driver.back()

        # click 'Servises'
        wait.until(EC.element_to_be_clickable((By.XPATH, "//p[@class ='_1zyfI'][contains(., 'Servises')]"))).click()
        WebDriverWait(driver, 3)

        # assert 'Servises' title, hepler
        HP.check_title('Servises', driver)

        # check specific element on the page
        try:
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//h1[contains(.,'Our Services')]")))
            print("The right 'Servises' page")
        except WDE:
            wrong_servises = "Smt is wrong with 'Servises' page"
            print(wrong_servises)
            wrong_list.append(wrong_servises)

        # back in the browser
        driver.back()

        # click 'Home'
        wait.until(EC.element_to_be_clickable((By.XPATH, "//p[@class='_1zyfI'][contains(.,'Home')]"))).click()
        WebDriverWait(driver, 3)

        # assert 'Home' title, hepler
        HP.check_title('Home', driver)

        # check specific element on the page
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "(// span[contains(., 'LET CALIFORNIA MARKETING "
                                                                   "GROW YOUR BUSINECS')])[2]")))
            print("The right 'Home' page")
        except WDE:
            wrong_home = "Smt is wrong with 'Home' page"
            print(wrong_home)
            wrong_list.append(wrong_home)

        # assert the assertion list is empty
        print(len(wrong_list))
        if len(wrong_list) == 0:
            print("All header links work correctly")
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "All header links are correct!"}}')
        else:
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Not all header links are corrrect"}}')
            raise Exception("Check header links")
        driver.quit()

    # localization test of first screen
    def test_first_screen_text(self):
        driver = self.driver
        driver.get(HP.url)
        self.driver.maximize_window()

        # check the title is right, helper
        HP.assert_title("California Marcketing", driver)

        # get the text
        first_line = driver.find_element(By.XPATH, "//a[contains(.,'CALIFORNIA MARCKETING')]").text
        second_line = driver.find_element(By.XPATH,
                                          "(//a[@href='https://qasvus.wixsite.com/ca-marketing/blog'])[2]").text
        third_line = driver.find_element(By.XPATH,
                                         "(//span[contains(.,'LET CALIFORNIA MARKETING GROW YOUR BUSINECS')])[2]").text
        print(first_line, second_line, third_line)

        # compare on site text with correct one, first line
        if first_line == "CALIFORNIA MARKETING":
            print("First line is fine")
        else:
            print("Incorrect first line")

        # compare on site text with correct one, second line
        if second_line == "A Full-Stack Creative Agency in CA":
            print("Second line is fine")
        else:
            print("Incorrect second line")

        # compare on site text with correct one, third line
        if third_line == "LET CALIFORNIA MARKETING GROW YOUR BUSINESS":
            print("Third line is fine")
        else:
            print("Incorrect third line")

        # assert full text
        if [first_line, second_line, third_line] == ["CALIFORNIA MARKETING", "A Full-Stack Creative "
                                                                                         "Agency in CA",
                                                                 'LET CALIFORNIA MARKETING GROW YOUR BUSINESS']:
            print("First screen text is correct")
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "First screen text is correct"}}')
        else:
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "First screen text is not correct""}}')
            raise Exception("Check the first screen text")
        driver.quit()

    # wix chat functionality
    def test_lets_chat(self):
        driver = self.driver
        driver.get(HP.url)
        self.driver.maximize_window()

        # check the title is right, helper
        HP.assert_title("California Marcketing", driver)

        # set up faker
        f = Faker()

        # assertion list
        list_for_assertion = []

        time.sleep(3)

        # find and switch to chat iframe
        iframe = driver.find_element(By.XPATH, "//iframe [@title='Wix Chat']")
        driver.switch_to.frame(iframe)

        # find and open the chat
        try:
            driver.find_element(
                locate_with(By.CLASS_NAME, "_28JNc").below({By.XPATH: "//*[@charset='utf-8']"})).click()
            ok_result = "Chat is on the page"
            print(ok_result)
            list_for_assertion.append(ok_result)
        except WDE:
            fail_result = "Smt is wrong with chat"
            print(fail_result)
            list_for_assertion.append(fail_result)

        time.sleep(3)

        # send fake text
        try:
            driver.find_element(By.TAG_NAME, "textarea").send_keys(f.text() + Keys.ENTER)
            ok_result = "The message was sent in the chat"
            print(ok_result)
            list_for_assertion.append(ok_result)
        except WDE:
            fail_result = "Smt is wrong with messages"
            print(fail_result)
            list_for_assertion.append(fail_result)

        # check if except prints in the list for final assertion
        list_for_assertion = ' '.join(list_for_assertion).split()
        if "wrong" not in list_for_assertion:
            print("The chat works correctly")
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Online chat works correctly!"}}')
        else:
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Smt is wrong with chat"}}')
            raise Exception("Check the chat")
        driver.quit()

    # video search bar functionality
    def test_video_selection(self):
        driver = self.driver
        driver.get(HP.url)
        self.driver.maximize_window()

        # check the title is right, helper
        HP.assert_title("California Marcketing", driver)

        time.sleep(2)

        # find video search bar and send "Big Sur"
        try:
            driver.find_element(
                locate_with(By.CLASS_NAME, "VVhXp").below({By.XPATH: "//*[@title='All Videos']"})).send_keys(
                "Big Sur" + Keys.ENTER)
            print("Search bar works")
        except WDE:
            print("Check the search bar")

        time.sleep(2)

        # assert video with "Big Sur" in the title is displayed
        if driver.find_element(By.XPATH, "//*[@src='https://i.ytimg.com/vi/X-HxnNAaioM/mqdefault.jpg']").is_displayed():
            print("The right video is displayed")
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "The right video is displayed!"}}')
        else:
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Сье is wrong with video search bar"}}')
            raise Exception("Check video search bar")
        driver.quit()

    # cart smoke testing
    def test_cart_shopping(self):
        driver = self.driver
        driver.get(HP.url)
        self.driver.maximize_window()

        # check the title is right, helper
        HP.assert_title("California Marcketing", driver)

        # set up wait time
        wait = WebDriverWait(driver, 3)

        # click 'Shop'
        shop = wait.until(EC.element_to_be_clickable((By.XPATH, "//p[@class ='_1zyfI'][contains(., 'Shop')]")))
        shop.click()

        time.sleep(5)

        # assert 'Shop' title, helper
        HP.check_title('Shop', driver)

        # check specific element on the page, helper
        HP.specific_element_check('Shop', "//h3[contains(.,'Product 1')]", driver)

        # find 'product1', get text and click
        product = driver.find_element(By.XPATH, "// h3[contains(.,'Product 1')]")
        product_text = product.text
        product.click()
        print("Successfully clicked on", product_text)

        time.sleep(5)

        # assert the title
        assert product_text in driver.title
        print("The right product page")

        # assert the product name on the page match the one was chosen
        on_page_product_text = driver.find_element(By.XPATH, "//h1[contains(@class,'2yxAN')]").text
        if product_text == on_page_product_text:
            print("Match:", product_text, "and", on_page_product_text)
        else:
            print("Not a match")

        # find price for one piece, turn into integer
        price = driver.find_element(By.XPATH, "//span[@data-hook='formatted-primary-price']").text
        price = int(price.replace("$", "").replace(".00", ""))
        print("The price for 1 piece is:", price)

        # set color and quantity
        try:
            driver.find_element(By.XPATH, "(//div[contains(@class,'ColorPickerItem2201735070__radioInner')])[1]").click()
            driver.find_element(By.XPATH, "//span[contains(@data-hook, 'number-input-spinner-up-arrow')]").click()
            print("The color and quantity were set")
        except WDE:
            print("Smt is wrong with color/quantity")

        # click on "Add to cart" button
        try:
            driver.find_element(By.XPATH,
                            "//span[@class ='buttonnext1002411228__content'][contains(., 'Add to Card')]").click()
            print("The product was added to cart")
        except WDE:
            print("Smt is wrong with adding to cart")

        time.sleep(5)

        # find curtain frame and switch
        try:
            driver.switch_to.frame(driver.find_element(By.CLASS_NAME, "_2DJg7"))
            print("Switched to frame")
        except WDE:
            print("Check the frame")

        # click on "View cart" button
        wait.until(EC.element_to_be_clickable((By.ID, "widget-view-cart-button"))).click()

        time.sleep(5)

        # assert title
        assert "Cart" in driver.title

        # assert specific element on the page
        my_cart = driver.find_element(By.CLASS_NAME, "_2NsyK").text
        if my_cart == "My cart":
            print("We are on the cart page")
        else:
            print("Check the cart page")

        # assert product name
        product_name = driver.find_element(By.CLASS_NAME, "_1dkgR").text
        if product_name == product_text:
            print("Right product in the cart")
        else:
            print("Wrong product in the cart")

        # check the quantity is correct
        howMany = driver.find_element(By.XPATH, "//input[@aria-label='Choose quantity']").get_attribute("value")
        if howMany == "2":
            print("Correct quantity")
        else:
            print("Wrong quantity")

        # check the price is correct
        total_price = driver.find_element(By.CLASS_NAME, "_32Pyj").text
        total_price = int(total_price.replace("$", "").replace(".00", ""))
        if total_price == int(howMany) * price:
            print("Correct total price")
        else:
            print("Wrong total price")

        # check the color is correct, helper
        HP.product_color("(//li[contains(.,'Color: Black')])[2]", "Black", driver)

        # find and click on 'CheckOut' button
        try:
            driver.find_element(By.CLASS_NAME, "_34QVp").click()
            print("Click on 'CheckOut' button")
        except WDE:
            print("Smt is wrong with 'CheckOut' button")

        time.sleep(5)

        # find iframe and switch
        try:
            driver.switch_to.frame(driver.find_element(By. CLASS_NAME, "MUsGO"))
            print("Switched to frame")
        except WDE:
            print("No frame")

        # assert the frame doesn't include "We can't accept online orders right now"
        fr2text = driver.find_element(By. CLASS_NAME, "maaPx").text
        print(fr2text)
        if "We can't accept online orders right now" not in fr2text:
            print("Checkout without 'cant accept online orders'")
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Checkout without: cant accept online orders"}}')
        else:
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Wrong checkout process"}}')
            raise Exception("Check checkout")
        driver.quit()

    # event reservation smoke testing
    def test_event_reservation(self):
        driver = self.driver
        driver.get(HP.url)
        self.driver.maximize_window()

        # set up faker library
        f = Faker()

        # set up wait time
        wait = WebDriverWait(driver, 3)

        # check the title is right, helper
        HP.assert_title("California Marcketing", driver)

        time.sleep(4)

        try:
            event = driver.find_element(By.XPATH, "(//a[@data-hook='ev-rsvp-button'][contains(.,'RSVP')])[1]")
            print("Event section")
        except WDE:
            print("Cant find event section")

        # name, date and place of the first event
        event_name = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "DTbMp"))).text
        print(event_name)
        event_date = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "VFsgs"))).text
        print(event_date)
        event_place = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "lNymU"))).text
        print(event_place)

        # click on "RSVP" button
        event.click()
        print("'RSVP' button was clicked")

        # assert title
        assert event_name in driver.title
        print("Its the middle event page")

        # check if event name, date and place are correct, helpers
        HP.comparison_xpath("//h1[@data-hook='event-title']", event_name, "event name", driver)
        HP.comparison_class("_6vtCb", event_date, "event date", driver)
        HP.comparison_class("-OEip", event_place, "event place", driver)

        # click on 'RSVP' button
        time.sleep(3)
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@data-hook='rsvp-button'][contains(.,'RSVP')])[2]"))).send_keys('\n')
        time.sleep(3)

        # assert driver title
        assert event_name in driver.title
        print("It`s the final event page")

        # check event name and place, helpers
        HP.comparison_xpath("//*[@data-hook='event-title']", event_name, "event name", driver)
        HP.comparison_xpath("//*[@data-hook='event-location']", event_place, "event place", driver)

        # fill the form
        driver.find_element(By.ID, "firstName").send_keys(f.first_name())
        driver.find_element(By.ID, "lastName").send_keys(f.last_name())
        driver.find_element(By.ID, "email").send_keys(f.email())

        # find and click on 'Submit' page
        try:
            driver.find_element(By.XPATH, "//button[@data-hook='form-button']").click()
            print("Submit button was clicked")
        except WDE:
            print("Check the 'Submit' button")

        time.sleep(5)

        # assert 'thank you' page
        if driver.find_element(By.XPATH, "//h2[@data-hook='thank-you-message-title']").text == "Thank you! See you soon":
            print("The form was submitted")
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Event form was submitted!"}}')
        else:
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Smt is wrong with event form submition"}}')
            raise Exception("Check event form")
        driver.quit()

    # subscription form functionality
    def test_subscribe_form(self):
        driver = self.driver
        driver.get(HP.url)
        self.driver.maximize_window()

        # set up Faker library
        f = Faker()

        # set up wait time
        wait = WebDriverWait(driver, 3)

        # check the title is right, helper
        HP.assert_title("California Marcketing", driver)

        # find 'Subscription form'
        form = wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(@class,'color_15')])[14]"))).text
        if form == "Subscribe Form":
            print("'Subscription form' was found")
        else:
            print("Cant find 'Subscription form'")

        # put email
        try:
            driver.find_element(By.XPATH, "//input[@id='input_comp-ksocylga1']").send_keys(f.email())
            print("The email was sent")
        except WDE:
            print("The email wasn't sent")

        # wait and click on 'Submit' button
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-disabled='false'][contains(., 'Submit')]"))).click()
        print("Submit button was clicked")

        time.sleep(4)

        # assert the form was sent
        if driver.find_element(By.XPATH, "//span[@class='color_15'][contains(.,'Thanks for submitting!')]").is_displayed():
            print("The form was sent")
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "The form was sent!"}}')
        else:
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "The form was not sent"}}')
            raise Exception("Check subscription form")
        driver.quit()