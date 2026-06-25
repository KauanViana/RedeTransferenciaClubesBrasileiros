# Importar as bibliotecas necessárias (Certifique-se de ter o Selenium instalado: pip install selenium)
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configurar o driver do Selenium
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.transfermarkt.com.br/campeonato-brasileiro-serie-a/transfers/wettbewerb/BRA1/plus/?saison_id=2024&s_w=&leihe=1&intern=0&intern=1")

# Aguardar até que os elementos criados via JavaScript estejam presentes na página
wait = WebDriverWait(driver, 10)

# Extrair os elementos desejados (Clube de Destino) usando XPath
clube_destino = wait.until(
    EC.presence_of_all_elements_located(
        (By.XPATH, "//h2[contains(@class,'content-box-headline')]/a[2]")
    )
)

# Imprimir os elementos extraídos
for elemento in clube_destino:
    print(elemento.get_attribute("textContent"))

# Fechar o driver do Selenium
driver.quit()