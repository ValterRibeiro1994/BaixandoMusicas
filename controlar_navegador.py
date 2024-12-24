from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from ferramentas.variaveis import CAIXA_DE_PESQUISA_YOUTUBE
class Navegador:

    # iniciando e fechando gerenciador
    def __init__(self, invisivel=False):
        
        """ Configuração inicial do webdriver"""
        opcoes = webdriver.ChromeOptions()
        servico = Service(ChromeDriverManager().install())
        opcoes.page_load_strategy = "normal"

        """Definido se fica oculto"""
        if invisivel:
            opcoes.add_argument("--headless")

        """Criando webdriver"""
        navegador = webdriver.Chrome(opcoes, servico)
        navegador.maximize_window()
        self.navegador = navegador

    def fechar_navegador(self):
        return self.navegador.quit()

    # buscar, clicar e escrever
    def esperar_elemento(self, seletor, tipo, tempo=30):
        try:
            tipos_seletores = {
                'css': By.CSS_SELECTOR,
                'class': By.CLASS_NAME,
                'id': By.ID,
                'tag': By.TAG_NAME,
                'xpath': By.XPATH,
                'name': By.NAME
            }

            metodo_seletor = tipos_seletores.get(tipo.lower())
            if not metodo_seletor:
                raise ValueError(F"Seletor invalido: {tipo}")
            
            elemento = WebDriverWait(self.navegador, tempo).until(EC.element_to_be_clickable((metodo_seletor, seletor)))
            return elemento
        except Exception as Error:
            print(f"Erro: Elemento não encontrado: {seletor}, {tipo}\n{Error}")

    def clicar(self, elemento):
        try:
            elemento.click()
        except Exception as ERROR:
            print(f"Erro: Não foi possivel clicar {str(ERROR)}")    

    def escrever(self, elemento, texto):
        elemento.send_keys(texto)
        elemento.send_keys(Keys.ENTER)
        print("Texto confirmado")
    
    # gerenciando abas
    def abrir_aba(self):
        self.navegador.execute_script("window.open('');")

    def trocar_aba(self, aba_destino: int):
        self.navegador.switch_to.window(self.navegador.window_handles[aba_destino])

    # gerenciando sites
    def abrir_site(self, url: str):
        self.navegador.get(url)
    
    def fechar_site(self):
        self.navegador.close()
    
    def obter_url(self):
        return self.navegador.current_url

if __name__ == "__main__":
    from time import sleep

    navegador = Navegador()

    print("abrindo segunda aba")
    navegador.abrir_aba()
    sleep(1)

    print("Entrando no google pela segunda aba")
    navegador.trocar_aba(1)
    navegador.abrir_site("https://www.google.com.br/")
    sleep(1)

    print('voltar para a primeira aba')
    navegador.trocar_aba(0)

    print("Entrando no youtube pela primeira aba")
    navegador.navegador.get("https://www.youtube.com/")
    sleep(1)
    
    print('segunda aba')
    navegador.trocar_aba(1)
    sleep(1)
    
    print('primeira aba')
    navegador.trocar_aba(0)
    sleep(1)
    
    print('segunda aba')
    navegador.trocar_aba(1)
    sleep(1)
    
    print("Fechando segunda aba")
    navegador.fechar_site()
    navegador.trocar_aba(0)

    print("Procurando caixa de pesquisa no youtube")
    caixa_de_pesquisa = navegador.esperar_elemento(CAIXA_DE_PESQUISA_YOUTUBE, 'css')
    sleep(1)
    navegador.clicar(caixa_de_pesquisa)
    sleep(1)
    navegador.escrever(caixa_de_pesquisa, 'obrigado por fumar')

    print("fim")
    sleep(1)
    navegador.fechar_navegador()