from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from anticaptchaofficial.recaptchav2proxyless import *

navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
link = "https://google.com/recaptcha/api2/demo"

navegador.get(link)

solver = recaptchaV2Proxyless()
solver.set_verbose(1)
solver.set_key()



time.sleep(15)