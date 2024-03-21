from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class DwaveWebHandler:
    def __init__(self, driver=None):
        if driver is None:
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        else:
            self.driver = driver

    def login(self, email, url=None):
        if url is None:
            # default
            self.driver.get("https://cloud.dwavesys.com/leap/")
        else:
            self.driver.get(url)
        self.driver.implicitly_wait(120)

        self.driver.find_element(By.CSS_SELECTOR, "input[name='username']").send_keys(email)
        self.driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys("Hieu11111010011@")

        self.driver.find_element(By.ID, "loginFormSubmit").click()

    def get_dwave_token(self):
        self.driver.find_element(By.CSS_SELECTOR, ".component--ApiTokenField-btn").click()
        api_token_value = self.driver.find_element(By.CSS_SELECTOR, ".component--ApiTokenField.body-text").get_attribute("value")
        return api_token_value

    def signup(self, email):
        self.driver.get("https://cloud.dwavesys.com/leap/signup/")
        self.driver.implicitly_wait(120)

        self.driver.find_element(By.CSS_SELECTOR, "input[name='first_name']").send_keys("Hieu")
        self.driver.find_element(By.CSS_SELECTOR, "input[name='last_name']").send_keys("Nguyen")
        self.driver.find_element(By.CSS_SELECTOR, "input[name='username']").send_keys(email)
        self.driver.find_element(By.CSS_SELECTOR, "input[name='job_title']").send_keys("student")
        self.driver.find_element(By.CSS_SELECTOR, "input[name='company']").send_keys("vnu")
        self.driver.find_element(By.CSS_SELECTOR, "input[name='qc_interested']").send_keys("Quantum Computing Research")
        self.driver.find_element(By.ID, "id_password1_input").send_keys("Hieu11111010011@")
        self.driver.find_element(By.ID, "id_password2_input").send_keys("Hieu11111010011@")

        Select(self.driver.find_element(By.ID, "id_qc_experience_select")).select_by_visible_text(
            "Curious person interested in learning more")
        Select(self.driver.find_element(By.ID, "id_job_function")).select_by_visible_text("Student")
        Select(self.driver.find_element(By.ID, "id_industry_select")).select_by_visible_text("Education")
        Select(self.driver.find_element(By.ID, "id_country_select")).select_by_visible_text("United States")
        Select(self.driver.find_element(By.ID, "id_state_province_select")).select_by_value("Virginia")

        # Scroll through the terms
        terms_element = self.driver.find_element(By.ID, "terms")
        self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", terms_element)

        self.driver.find_element(By.CSS_SELECTOR, ".terms-checkbox").click()
        checkbox = self.driver.find_element(By.ID, "termsId")
        if not checkbox.is_selected():
            checkbox.click()
        signup_button = self.driver.find_element(By.ID, "signupFormFieldsSubmit")
        signup_button.click()

