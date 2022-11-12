import time

from selenium import webdriver # pip install selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager # pip install webdriver-manager & pip install packaging


options = Options()

프로필사용 = "사용"

if 프로필사용 == "사용":
    user_data = r"C:\Users\B\AppData\Local\Google\Chrome\User Data" #r"프로필 경로"
    user_folder = "Default" #프로필 폴더명
    options.add_argument(f"user-data-dir={user_data}")
    options.add_argument(f"--profile-directory={user_folder}")
else:
    pass

options.add_experimental_option('detach', True) #브라우저 안닫힘
service = Service(ChromeDriverManager().install()) #셀레니움 버전4부터 기본방식
driver = webdriver.Chrome(service=service, options=options)

driver.get('https://www.daum.net/')

# time.sleep(10)
# aa = driver.page_source # html 태그 전체 가져옴
# driver.find_element(By.CSS_SELECTOR,'#q').send_keys('aa') #센드키
# driver.get_screenshot_as_file('aa.png') #캡쳐하기