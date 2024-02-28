from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Abrir o Chromium
driver = webdriver.Chrome()

# Abrir Instagram
driver.get('https://www.instagram.com/accounts/login/')

# Esperar um pouco para carregar a página
time.sleep(5)

# Preencher usuário e senha
driver.find_element_by_name('username').send_keys('andr3y.real')
driver.find_element_by_name('password').send_keys('vader@123')

# Clicar no botão de login
driver.find_element_by_css_selector('button[type="submit"]').click()

# Esperar um pouco para carregar a página
time.sleep(5)

# Acessar a página do perfil privado
driver.get('https://www.instagram.com/_maraxzy')

# Esperar um pouco para carregar a página
time.sleep(5)

# Obter seguidores
seguidores = driver.find_element_by_css_selector('a[href="/_maraxzy/followers/"] > span').text

# Obter pessoas seguidas
seguindo = driver.find_element_by_css_selector('a[href="/_maraxzy/following/"] > span').text

# Fechar o navegador
driver.quit()

print(f'Seguidores: {seguidores}')
print(f'Seguindo: {seguindo}')
