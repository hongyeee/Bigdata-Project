from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
JOB_URL = 'https://www.linkedin.com/jobs/search/?currentJobId=3862183359&geoId=103588929&keywords=PYTHON&location=%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD%20%EC%84%9C%EC%9A%B8&refresh=true'
driver.get(JOB_URL)

login = driver.find_element(By.CSS_SELECTOR, ".btn-secondary-emphasis")
login.click()

username_field = driver.find_element(By.ID, "username")
username_field.send_keys("LinkedIn 아이디 입력")

password_field = driver.find_element(By.ID, "password")
password_field.send_keys("LinkedIn 비밀번호 입력")


login_button = driver.find_element(By.CSS_SELECTOR, ".btn__primary--large")
login_button.click()

apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button--top-card")
apply_button.click()
