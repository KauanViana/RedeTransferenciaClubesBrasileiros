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

# Extrair os elementos desejados (Blocos de Transferências) usando XPath
blocos_transferencias = wait.until(
    EC.presence_of_all_elements_located(
        (By.XPATH, "//div[@class='box']")
    )
)

with open("data/raw/transferencias.txt", "w", encoding="utf-8") as arquivo:

    # Iterar pelos blocos de transferências desejados
    for i in range(3, len(blocos_transferencias)):
        # Encontra todos os links de clubes correspondentes dentro do bloco atual
        clubes = blocos_transferencias[i].find_elements(By.XPATH, ".//h2[contains(@class, 'content-box-headline')]/a[2]")
        
        # Iterar pelos elementos encontrados dentro desse bloco específico
        for clube in clubes:
            nome_clube = clube.get_attribute("textContent").strip()
            print(f'Movimentações do {nome_clube}')
            arquivo.write(f'Movimentações do {nome_clube}\n')

            # Iterar pelos elementos de movimentação dentro do bloco atual
            for movimentacao in blocos_transferencias[i].find_elements(By.XPATH, "//span[@class='hide-for-small']"):
                nome_jogador = movimentacao.get_attribute("textContent").strip()

                # Escrever as informações no arquivo de saída
                if movimentacao.find_element(By.XPATH, ".//ancestor::div[@class='box']//h2[contains(@class, 'content-box-headline')]/a[2]").get_attribute("textContent").strip() == nome_clube:
                    if movimentacao.find_element(By.XPATH, ".//ancestor::div[@class='responsive-table']//th[@class='spieler-transfer-cell']").get_attribute("textContent").strip() == "Entradas":
                        print(f'Nome: {nome_jogador} - Clube Destino: {nome_clube} - Clube Origem: {movimentacao.find_element(By.XPATH, ".//ancestor::tr//td[@class='no-border-links verein-flagge-transfer-cell']").get_attribute("textContent").strip()}')
                        arquivo.write(f'Nome: {nome_jogador} - Clube Destino: {nome_clube} - Clube Origem: {movimentacao.find_element(By.XPATH, ".//ancestor::tr//td[@class='no-border-links verein-flagge-transfer-cell']").get_attribute("textContent").strip()}\n')
                    elif movimentacao.find_element(By.XPATH, ".//ancestor::div[@class='responsive-table']//th[@class='spieler-transfer-cell']").get_attribute("textContent").strip() == "Saídas":
                        print(f'Nome: {nome_jogador} - Clube Destino: {movimentacao.find_element(By.XPATH, ".//ancestor::tr//td[@class='no-border-links verein-flagge-transfer-cell']").get_attribute("textContent").strip()} - Clube Origem: {nome_clube}')
                        arquivo.write(f'Nome: {nome_jogador} - Clube Destino: {movimentacao.find_element(By.XPATH, ".//ancestor::tr//td[@class='no-border-links verein-flagge-transfer-cell']").get_attribute("textContent").strip()} - Clube Origem: {nome_clube}\n')

            # Separador entre clubes
            print("\n-----\n")  
            arquivo.write("\n-----\n\n")  


# Fechar o driver do Selenium
driver.quit()