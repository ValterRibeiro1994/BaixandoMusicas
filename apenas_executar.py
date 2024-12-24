import os

from ferramentas.controlar_navegador import Navegador
from ferramentas.controlar_pesquisa import GerenciarPesquisaYoutube
from ferramentas.controlar_video import GerenciarVideo
from ferramentas.controle_de_dados import GerenciarDados
# apenas executar e fazer pequenos ajustes iniciais(desativar reprodutor automatico e pular propaganda inicial)
def apenas_executar2(dicio, dados, navegador):
    musica = f'{dicio['artista']} {dicio['musica']}'

    # sem url
    if not isinstance(dicio['url'], str):
        print("Executando Sem URL....")
        pesquisando = GerenciarPesquisaYoutube(navegador)
        pesquisando.abrir()
        pesquisando.pesquisar(musica)
        resultado_pesquisa = pesquisando.obter_resultado(musica)
        navegador.clicar(resultado_pesquisa)
        dicio['escutada'] += 1
        url = navegador.obter_url()
        if isinstance(url, str) and 'watch?v' in url:
            dicio['url'] = url
        dados.salvar_registro()
    else:
        print("Abrindo diretamente com a URL salva....")
        print(dicio['url'])
        navegador.abrir_site(dicio['url'])
        dicio['escutada'] += 1
        dados.salvar_registro()
        # video = GerenciarVideo(navegador)
        # while not video.obter_video(): video.obter_video()
        # video.apertar_play()
        # video.checar_propagandas()
        # os.system('cls')

def apenas_executar():
    
    dados = GerenciarDados()
    navegador = Navegador()
    for dicio in dados.lista_de_musicas:
        apenas_executar2(dicio, dados, navegador)
        video = GerenciarVideo(navegador)
        video.acompanhar_video()
    
    navegador.fechar_navegador()

if __name__ == "__main__":
    apenas_executar()
