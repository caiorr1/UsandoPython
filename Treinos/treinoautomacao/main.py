from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from anticaptchaofficial.recaptchav2proxyless import *

navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
site = "https://google.com/recaptcha/api2/demo"

navegador.get(site)
chave_captcha = navegador.find_element(By.ID, 'recaptcha-demo').get_attribute('data-sitekey')

solver = recaptchaV2Proxyless()
solver.set_verbose(1)
solver.set_key() # -> chave api da sua conta
solver.set_website_url(site) # -> link do site
solver.set_website_key() # -> pegar data-sitekey

resposta = solver.solve_and_return_solution()



time.sleep(15)