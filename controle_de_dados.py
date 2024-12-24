from json import dump, load 
from os import path, system

class GerenciarDados:
    """
    Classe para gerenciar um registro de músicas, permitindo adicionar, remover, listar e apagar registros.
    Os dados são salvos em um arquivo JSON.
    """

    caminho_musicas = 'RegistroDeMusicas.json'

    def __init__(self):
        """
        Inicializa a classe.
        - Cria o arquivo JSON vazio caso ele não exista.
        - Carrega os registros de músicas existentes no arquivo JSON.
        """
        if not path.exists(self.caminho_musicas):
            print("Criando novo arquivo de músicas...")
            self.lista_de_musicas = []
            with open(self.caminho_musicas, 'w', encoding='utf-8') as documento:
                dump(self.lista_de_musicas, documento, ensure_ascii=False, indent=4)
                print("Arquivo de músicas criado com sucesso.")

        with open(self.caminho_musicas, 'r', encoding='utf-8') as documento:
            self.lista_de_musicas = load(documento)
        
        if self.lista_de_musicas:
            self.lista_de_musicas = sorted(self.lista_de_musicas, key=lambda x: x['escutada'], reverse=False)

    def adicionar_registro(self, nome, musica, estilo, categoria):
        """
        Adiciona uma nova música ao registro.

        Args:
            nome (str): Nome do artista.
            musica (str): Nome da música.
            estilo (str): Gênero musical da música.
        """

        nova_musica = {
            "artista": nome,
            "musica": musica,
            "escutada": 0,
            "baixada": False,
            "url": None,
            "estilo": estilo,
            "deseja_baixar": True,
            "categoria": categoria
        }
        self.lista_de_musicas.append(nova_musica)
        self.salvar_registro()
        print("Registro salvo com sucesso.")

    def remover_registro(self, nome, musica):
        """
        Remove uma música específica do registro.

        Args:
            nome (str): Nome do artista.
            musica (str): Nome da música.
        """
        self.lista_de_musicas = [
            dicio for dicio in self.lista_de_musicas
            if dicio['artista'] != nome or dicio['musica'] != musica
        ]
        self.salvar_registro()
        print("Registro removido com sucesso.")

    def salvar_registro(self):
        """
        Salva a lista de músicas no arquivo JSON.
        """
        with open(self.caminho_musicas, 'w', encoding='utf-8') as documento:
            dump(self.lista_de_musicas, documento, ensure_ascii=False, indent=4)

    def apagar_todos_os_registros(self):
        """
        Apaga todos os registros de músicas, incluindo o arquivo JSON.
        """
        self.lista_de_musicas = []
        self.salvar_registro()
        print("Todos os registros foram apagados.")

    def exibir_todos_os_registros(self):
        """
        Exibe todos os registros de músicas armazenados.
        """
        print("\nNome do cantor\t  Nome da música:")
        for registro in self.lista_de_musicas:
            print(f"{registro['artista']}: {registro['musica']}")
    
# apenas para teste
def menu_da_lista_de_musicas(dados):
    """
    Exibe o menu de opções para gerenciar a lista de músicas.

    Args:
        dados (GerenciarDados): Instância da classe GerenciarDados para manipular os registros.
    """
    while True:
        print("_" * 50)
        print("\n\tGerenciador de lista de músicas\n")
        print("Escolha digitando com números...")
        print("[ 0 ] Finalizar menu")
        print("[ 1 ] Adicionar músicas na lista")
        print("[ 2 ] Remover músicas da lista")
        print("[ 3 ] Exibir todas as músicas")
        print("[ 4 ] Apagar todo o registro de arquivos")
        print()

        escolha = input("Digite um número entre 0 a 4: ")

        if escolha == '0':
            print("Finalizando o menu...")
            break

        if not escolha.isdigit():
            print("Erro: Escolha NÚMEROS entre 0 a 4.")
            continue

        escolha = int(escolha)


        if escolha == 1:
            nome = input("Informe o nome do cantor: ")
            musica = input("Informe o nome da música: ")
            genero = input("Informe o gênero musical da música (rap, funk, jazz, etc.): ")
            categoria = input("Em que categoria(musicas para treino, relaxar e etc.): ")
            dados.adicionar_registro(nome, musica, genero, categoria)

        elif escolha == 2:
            nome = input("Informe o nome do cantor para apagar: ")
            musica = input("Informe o nome da música para apagar: ")
            dados.remover_registro(nome, musica)

        elif escolha == 3:
            dados.exibir_todos_os_registros()

        elif escolha == 4:
            dados.apagar_todos_os_registros()

if __name__ == "__main__":
    print("Iniciando...")
    dados = GerenciarDados()
    menu_da_lista_de_musicas(dados)
    print("Fim.")
