from os import system

class GerenciarVideo:
    """
    Classe para gerenciar um vídeo em execução em um navegador controlado por automação.

    A classe fornece métodos para obter informações sobre o vídeo, controlar a reprodução e lidar com propagandas.
    """
    def __init__(self, navegador):
        """
        Inicializa a classe com uma instância do navegador.

        Args:
            navegador: Objeto de automação do navegador.
        """
        self.navegador = navegador
        self.duracao = False
        self.tempo_restante = False
        self.tempo_atual = False

    def obter_video(self):
        """
        Obtém o elemento de vídeo na página.

        Returns:
            None
        """
        try:
            self.video = self.navegador.esperar_elemento('video', 'tag')
            return True
        except Exception as e:
            print(f"Erro ao obter vídeo: {e}")

    def obter_url(self):
        """
        Retorna a URL atual do navegador.

        Returns:
            str: URL da página.
        """
        try:
            return self.navegador.current_url
        except Exception as e:
            print(f"Erro ao obter URL: {e}")

    def obter_duracao_total(self):
        """
        Obtém a duração total do vídeo em segundos.

        Returns:
            None
        """
        try:
            self.obter_video()
            self.duracao = self.video.get_property("duration") if isinstance(self.video.get_property("duration"), float) else False

            while not self.duracao:
                self.obter_duracao_total()
        except Exception as e:
            print(f"Erro ao obter duração total: {e}")

    def obter_tempo_restante(self):
        """
        Calcula o tempo restante do vídeo com base no tempo atual e na duração total.

        Returns:
            bool: True se o cálculo foi realizado com sucesso, False caso contrário.
        """
        try:
            self.tempo_atual = self.video.get_property("currentTime")

            if isinstance(self.tempo_atual, float) and isinstance(self.duracao, float):
                self.tempo_restante = self.duracao - self.tempo_atual
                system("cls")
                print(f"{self.tempo_restante:.2f} segundos restantes....")
                return True

            while not self.tempo_restante:
                self.obter_tempo_restante()
        except Exception as e:
            print(f"Erro ao obter tempo restante: {e}")

    def checar_pausa(self):
        """
        Verifica se o vídeo está pausado.

        Returns:
            bool: True se o vídeo está pausado, False caso contrário.
        """
        try:
            return self.video.get_property("paused")
        except Exception as e:
            print(f"Erro ao verificar pausa: {e}")
            return False

    def apertar_play(self):
        """
        Aperta o botão de play se o vídeo estiver pausado.

        Returns:
            None
        """
        try:
            if self.checar_pausa():
                botao_play = self.navegador.esperar_elemento(
                    '#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > button', 'css')
                self.navegador.clicar(botao_play)
        except Exception as e:
            print(f"Erro ao apertar play: {e}")

    def apertar_pausa(self):
        """
        Aperta o botão de pausa se o vídeo estiver em reprodução.

        Returns:
            None
        """
        try:
            if not self.checar_pausa():
                botao_pausa = self.navegador.esperar_elemento(
                    '#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > button', 'css')
                self.navegador.clicar(botao_pausa)
        except Exception as e:
            print(f"Erro ao apertar pausa: {e}")

    def acompanhar_video(self):
        """
        Acompanha a execução do vídeo, verificando tempo restante e lidando com propagandas.

        Returns:
            None
        """
        print("Fazendo acompanhamento inicial....")
        self.tela_cheia()
        while True:
            try:
                self.obter_video()
                self.apertar_play()
                self.repro_auto()
                self.obter_duracao_total()
                self.obter_tempo_restante()

                if self.duracao <= 120:
                    self.checar_propagandas()
                    continue

                if self.tempo_restante <= 0.2:
                    print("Vídeo acabou...")
                    break
            except RecursionError:
                print("Erro de recursão detectado, encerrando acompanhamento.")
                break
            except Exception as e:
                print(f"Erro ao acompanhar vídeo: {e}")

    def repro_auto(self):
        """
        Desativa a reprodução automática se estiver ativada.

        Returns:
            None
        """
        try:
            repro = self.navegador.esperar_elemento(
                "#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-right-controls > button:nth-child(2) > div > div",
                'css'
            )
            ativo = repro.get_attribute("aria-checked") == "true"
            if ativo:
                repro.click()
                print("Reprodução automática desativada.")
        except Exception as error:
            print(f"Erro ao desativar a reprodução automática: {error}")

    def checar_propagandas(self):
        """
        Verifica se há propagandas em execução e tenta pulá-las.

        Returns:
            None
        """
        try:
            propaganda = self.navegador.esperar_elemento("ytp-ad-avatar-lockup-card", 'class', 10)
            if propaganda:
                pular = self.navegador.esperar_elemento("ytp-skip-ad-button", 'class', 10)
                pular.click()
        except Exception as e:
            print(f"Erro ao checar propagandas: {e}")

    def tela_cheia(self):
        tela = self.navegador.esperar_elemento("#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-right-controls > button.ytp-fullscreen-button.ytp-button", 'css')
        self.navegador.clicar(tela)

if __name__ == "__main__":
    from controlar_navegador import Navegador
    from controlar_pesquisa import GerenciarPesquisaYoutube
    from time import sleep

    navegador = Navegador()
    youtube = GerenciarPesquisaYoutube(navegador)
    youtube.abrir()
    youtube.pesquisar('froid garota')
    resultado = youtube.obter_resultado('froid garota')
    navegador.clicar(resultado)
    sleep(1)
    video = GerenciarVideo(navegador)

    print('Buscando detalhes do vídeo...')
    while not video.obter_video():
        video.obter_video()

    system("cls")
    print("Começando a reprodução...")
    video.checar_propagandas()

    if not video.checar_pausa():
        sleep(0.1)
        print('Vídeo está em execução. Pausando...')
        video.apertar_pausa()

        for x in range(10):
            sleep(1)
            print(x + 1)

        print("Retomando reprodução...")
        video.apertar_play()

    print("Obtendo tempo restante e acompanhando vídeo...")
    video.acompanhar_video()
    print("Vídeo finalizado.")
    sleep(30)
