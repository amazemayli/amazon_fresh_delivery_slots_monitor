import sys, os, re, requests, time
import itertools
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from twilio.rest import Client
from random import randint
import datetime

# Load configuration file
from config import * 

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)
chromedriver = ROOT_DIR + "/chromedriver"

# Create Twilio client
client = Client(account_sid, auth_token)

def create_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(chromedriver, chrome_options=chrome_options)
    return driver

def terminate(driver):
    driver.quit()

def check_slots():
    try:
        # Login and get to the checkout page
        print('Loading Selenium ...')
        driver = create_driver()

        print('Loading Amazon ...')
        driver.get('https://www.amazon.com/gp/sign-in.html')
        email_field = driver.find_element_by_css_selector('#ap_email')
        email_field.send_keys(amazon_username)
        driver.find_element_by_css_selector('#continue').click()
        time.sleep(1.5)
        password_field = driver.find_element_by_css_selector('#ap_password')
        password_field.send_keys(amazon_password)
        driver.find_element_by_css_selector('#signInSubmit').click()
        print('You have 30 seconds to do 2FA ...')
        time.sleep(10)
        print('You have 20 more seconds to do 2FA ...')
        time.sleep(10)
        print('You have 10 more seconds to do 2FA ...')
        time.sleep(5)
        print('You have 5 more seconds to do 2FA ...')
        time.sleep(1)
        print('You have 4 more seconds to do 2FA ...')
        time.sleep(1)
        print('You have 3 more seconds to do 2FA ...')
        time.sleep(1)
        print('You have 2 more seconds to do 2FA ...')
        time.sleep(1)
        print('You have 1 more second to do 2FA ...')
        time.sleep(1)
        print('Loading Shopping Cart ...')
        driver.get('https://www.amazon.com/gp/cart/view.html')
        time.sleep(1.5)
        print('Checking Out Page 1 ...')
        driver.find_element_by_xpath("//span[contains(.,'Checkout Amazon Fresh Cart')]").click()
        time.sleep(1.5)
        print('Checking Out Page 2 ...')
        driver.find_element_by_name('proceedToCheckout').click()

        # Main loop
        more_dows = True
        slots_available = False
        available_slots = ""
        while not slots_available:
            while more_dows:
                # Add some randominess in click timing
                time.sleep(randint(2,5))
                slots = driver.find_elements_by_css_selector('.ss-carousel-item')
                for slot_index, slot in zip(range(amazon_date_limit), slots):
                    if slot.value_of_css_property('display') != 'none':
                        slot.click()
                        date_containers = driver.find_elements_by_css_selector('.Date-slot-container')
                        for date_container in date_containers:
                            if date_container.value_of_css_property('display') != 'none':
                                unattended_slots = date_container.find_element_by_css_selector('#slot-container-UNATTENDED')
                                if 'No doorstep delivery' not in unattended_slots.text:
                                    available_slots = unattended_slots.text.replace('Select a time', '').strip()
                                    slots_available = True
                                else:
                                    print(unattended_slots.text.replace('Select a time', '').strip())
                next_button = driver.find_element_by_css_selector('#nextButton')
                more_dows = not next_button.get_property('disabled')
                if more_dows:
                    next_button.click()
                    time.sleep(randint(1,3))
                else:
                    more_dows = False

            if slots_available:
                client.messages.create(to=to_mobilenumber,
                        from_=from_mobilenumber,
                        body=available_slots)
                print('Slots Available!')
                print(available_slots)
            else:
                # Add some randominess in before we retry
                random_wait = randint(45,555)
                now = datetime.datetime.now()
                now_string = now.strftime("%Y-%m-%d %H:%M:%S")
                wait_message = "As of " + now_string + ", no Amazon Fresh slots available. Will retry in " + str(random_wait) + " seconds ..."
                # For people who want to also receive a text message when there are no slots available
                # client.messages.create(to=to_mobilenumber,
                #        from_=from_mobilenumber,
                #        body=wait_message)
                print(wait_message)
                more_dows = True
                time.sleep(random_wait-30)
                print('There are 30 more seconds until retry ...')
                time.sleep(10)
                print('There are 20 more seconds until retry ...')
                time.sleep(10)
                print('There are 10 more seconds until retry ...')
                time.sleep(5)
                print('There are 5 more seconds until retry ...')
                time.sleep(1)
                print('There are 4 more seconds until retry ...')
                time.sleep(1)
                print('There are 3 more seconds until retry ...')
                time.sleep(1)
                print('There are 2 more seconds until retry ...')
                time.sleep(1)
                print('There is 1 more second until retry ...')
                time.sleep(1)
                driver.refresh()

        terminate(driver)
    except Exception as e:
        terminate(driver)
        raise ValueError(str(e))

if __name__ == "__main__":
    check_slots()
