from django.conf import settings
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Create your tests here.

WEBDRIVER_PATH = "C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe"


class AccountTestCase(LiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(WEBDRIVER_PATH)
        super(AccountTestCase, self).setUp()

    def tearDown(self):
        self.driver.close()
        super(AccountTestCase, self).tearDown()

    def test_existing_user_login(self):
        self.driver.get('http://127.0.0.1:8000/login/')
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, 'username')))
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, 'password')))
        except Exception as e:
            print(e)

        self.driver.find_element_by_id('username').send_keys(settings.LOGIN_USERNAME)
        self.driver.find_element_by_id('password').send_keys(settings.LOGIN_PASSWD)
        self.driver.find_element_by_id('loginButton').click()
        page = self.driver.page_source
        self.assertIn("Logout", page)

    def test_non_existing_user_login(self):
        self.driver.get('http://127.0.0.1:8000/login/')
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, 'username')))
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, 'password')))
        except Exception as e:
            print(e)

        self.driver.find_element_by_id('username').send_keys("fadsfadsf")
        self.driver.find_element_by_id('password').send_keys("fadsfadsf")
        self.driver.find_element_by_id('loginButton').click()
        page = self.driver.page_source
        self.assertIn("Username or password incorrect!", page)

    def test_existing_user_register(self):
        self.driver.get('http://127.0.0.1:8000/register/')
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.NAME, 'username')))
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.NAME, 'email')))
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.NAME, 'password1')))
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.NAME, 'password2')))
        except Exception as e:
            print(e)
        self.driver.find_element_by_name("username").send_keys(settings.LOGIN_USERNAME)
        self.driver.find_element_by_name("email").send_keys(settings.LOGIN_USERNAME + "@hotmail.com")
        self.driver.find_element_by_name("password1").send_keys("password11")
        self.driver.find_element_by_name("password2").send_keys("password11")
        self.driver.find_element_by_id('registerButton').click()

        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.NAME, 'username')))
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.NAME, 'email')))
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.NAME, 'password1')))
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.NAME, 'password2')))
        except Exception as e:
            print(e)
        page = self.driver.page_source
        self.assertIn("A user with that username already exists.", page)

    def test_new_user_register(self):
        register_username = "adsfadsf"

        self.driver.get('http://127.0.0.1:8000/register/')
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.NAME, 'username')))
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.NAME, 'email')))
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.NAME, 'password1')))
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.NAME, 'password2')))
        except Exception as e:
            print(e)

        self.driver.find_element_by_name("username").send_keys(register_username)
        self.driver.find_element_by_name("email").send_keys(register_username + "@hotmail.com")
        self.driver.find_element_by_name("password1").send_keys("password21*")
        self.driver.find_element_by_name("password2").send_keys("password21*")
        self.driver.find_element_by_id('registerButton').click()

        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, 'username')))
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, 'password')))
        except Exception as e:
            print(e)
        page = self.driver.page_source
        self.assertIn(f"You successfuly created an account for {register_username}.", page)
