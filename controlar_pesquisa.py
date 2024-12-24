from ferramentas.variaveis import CAIXA_DE_PESQUISA_YOUTUBE, SITE_YOUTUBE
from selenium.webdriver.common.by import By
from ferramentas.utilidades import checar_nome
from time import sleep

class GerenciarPesquisaYoutube:
    def __init__(self, navegador):
        self.navegador = navegador

    def abrir(self):
        self.navegador.abrir_site(SITE_YOUTUBE)
        print("Youtube aberto com sucesso...")
    
    def fechar(self):
        self.navegador.fechar_site()
        print("Yotube fechado com sucesso")
    
    def pesquisar(self, musica: str):
        # buscar caixa de pesquisa
        pesquisar = self.navegador.esperar_elemento(CAIXA_DE_PESQUISA_YOUTUBE, 'css')

        # selecionar e clicar na caixa de pesquisa
        self.navegador.clicar(pesquisar)

        # escrever nome da musica e confirmar pesquisa
        self.navegador.escrever(pesquisar, musica)
    
    def obter_resultado(self, musica: str):
        sleep(5)
        lista = self.navegador.navegador.find_elements(By.ID, 'video-title')

        for video in lista:
            titulo = video.get_attribute("title")
            if isinstance(titulo, str):
                titulo = titulo.lower()
                musica = musica.lower()
                if checar_nome(musica, titulo):
                    print("Video escolhido...")
                    return video

if __name__ =="__main__":
    from controlar_navegador import Navegador
    from time import sleep
    navegador = Navegador()
    youtube = GerenciarPesquisaYoutube(navegador)
    youtube.abrir()
    youtube.pesquisar('Froid extremo oriental')
    video_selecionado = youtube.obter_resultado('Froid extremo oriental')
    navegador.clicar(video_selecionado)
    sleep(30)
    youtube.fechar()
    navegador.fechar_navegador()

