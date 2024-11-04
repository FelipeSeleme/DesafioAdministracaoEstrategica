import random
import os
import time
from colorama import Fore, init
import matplotlib.pyplot as plt

# Inicializar a colorama
init(autoreset=True)

# Classe que representa uma empresa (jogador)
class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.saldo = 1000.0  # Saldo inicial de R$ 1.000,00
        self.saldo_historico = [self.saldo]  # Lista para armazenar o histórico do saldo

    def investir(self, marketing, pd, producao, multiplicadores):
        # Cálculo dos retornos com base nos multiplicadores do cenário
        retorno_marketing = marketing * multiplicadores['marketing']
        retorno_pd = pd * multiplicadores['pd']
        retorno_producao = producao * multiplicadores['producao']
        
        # Simulação do cálculo do retorno com barra de progresso
        print(f"{Fore.WHITE}Calculando retorno sobre os investimentos...", end="", flush=True)
        for _ in range(3):
            time.sleep(0.5)
            print(".", end="", flush=True)
        print("\n")
        
        # Atualizar saldo com os retornos
        self.saldo += retorno_marketing + retorno_pd + retorno_producao
        self.saldo_historico.append(self.saldo)  # Adiciona o saldo atual ao histórico

# Função para exibir o texto com efeito de digitação
def digitar_texto(texto, velocidade=0.01):
    for caractere in texto:
        print(caractere, end='', flush=True)
        time.sleep(velocidade)
    print()

# Função para exibir o ranking das empresas com efeito de digitação apenas na listagem
def exibir_ranking(empresas, rodada):
    empresas_ordenadas = sorted(empresas, key=lambda x: x.saldo, reverse=True)
    print("\n" + Fore.GREEN + "═" * 50)
    print(Fore.WHITE + "🏆  RANKING DAS EMPRESAS  🏆".center(50))
    print(Fore.GREEN + "═" * 50)
    
    for i, empresa in enumerate(empresas_ordenadas, start=1):
        # Somente exibir medalhas a partir da segunda rodada
        if rodada > 1:
            if i == 1:
                icone = "🥇"
            elif i == 2:
                icone = "🥈"
            elif i == 3:
                icone = "🥉"
            else:
                icone = "  "  # Adicionar dois espaços para alinhar corretamente
        else:
            icone = "  "  # Sem medalhas na primeira rodada

        digitar_texto(f"{icone} {i}. {empresa.nome:<20} - Saldo: R${empresa.saldo:,.2f}")
    
    print(Fore.GREEN + "═" * 50)

# Função para limpar a tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função que exibe a tela inicial com arte ASCII e cores
def tela_inicial():
    limpar_tela()
    print(Fore.GREEN + "═" * 50)
    print("""
███████╗███████╗ ██████╗ ██████╗ ██╗      █████╗     ██████╗ ███████╗                 
██╔════╝██╔════╝██╔════╝██╔═══██╗██║     ██╔══██╗    ██╔══██╗██╔════╝                 
█████╗  ███████╗██║     ██║   ██║██║     ███████║    ██║  ██║█████╗                   
██╔══╝  ╚════██║██║     ██║   ██║██║     ██╔══██║    ██║  ██║██╔══╝                   
███████╗███████║╚██████╗╚██████╔╝███████╗██║  ██║    ██████╔╝███████╗                 
╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝    ╚═════╝ ╚══════╝                 
                                                                                      
 █████╗ ██████╗ ██████╗ ███████╗███╗   ██╗██████╗ ██╗███████╗ █████╗ ██████╗  ██████╗ 
██╔══██╗██╔══██╗██╔══██╗██╔════╝████╗  ██║██╔══██╗██║╚══███╔╝██╔══██╗██╔══██╗██╔═══██╗
███████║██████╔╝██████╔╝█████╗  ██╔██╗ ██║██║  ██║██║  ███╔╝ ███████║██║  ██║██║   ██║
██╔══██║██╔═══╝ ██╔══██╗██╔══╝  ██║╚██╗██║██║  ██║██║ ███╔╝  ██╔══██║██║  ██║██║   ██║
██║  ██║██║     ██║  ██║███████╗██║ ╚████║██████╔╝██║███████╗██║  ██║██████╔╝╚██████╔╝
╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚═════╝ ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝  ╚═════╝ 
    """)
    print(Fore.GREEN + "═" * 50)
    print(Fore.LIGHTYELLOW_EX + "🖲️💻️  COMO FUNCIONA O JOGO:")
    print("Você é o CEO de uma empresa em um mercado altamente competitivo.")
    print("A cada rodada, você fará decisões estratégicas sobre onde investir seu orçamento.")
    print("\nÁreas de investimento disponíveis:")
    print(Fore.LIGHTYELLOW_EX + "  ➤ 📢️ Marketing: Aumenta a visibilidade da empresa.")
    print(Fore.LIGHTYELLOW_EX + "  ➤ 🔎️ Pesquisa e Desenvolvimento (P&D): Gera inovação e novos produtos.")
    print(Fore.LIGHTYELLOW_EX + "  ➤ 📦️ Produção: Aumenta a capacidade produtiva para atender a demanda.")
    print(Fore.GREEN + "═" * 50)
    input("Pressione Enter para iniciar o jogo...")

# Função que cria cenários sem repetição para cada rodada
def gerar_cenarios_unicos(num_rodadas):
    cenarios_disponiveis = [
        {"descricao": "Uma inesperada explosão na demanda está tomando o mercado de surpresa. \nO setor inteiro está se ajustando à nova realidade.",
         "marketing": 1.0, "pd": 0.9, "producao": 1.3},
        
        {"descricao": "A competição atingiu níveis intensos, e as grandes jogadas estão acontecendo. \nCada movimento no mercado é acompanhado de perto.",
         "marketing": 1.3, "pd": 0.9, "producao": 0.8},
        
        {"descricao": "O mercado parece estagnado, com produtos familiares saturando as prateleiras. \nAs empresas procuram desesperadamente algo que se destaque.",
         "marketing": 1.0, "pd": 1.3, "producao": 0.8},
        
        {"descricao": "Com os custos de produção disparando, a pressão financeira ameaça os lucros. \nA cautela se torna uma necessidade constante.",
         "marketing": 0.9, "pd": 1.1, "producao": 0.8},
        
        {"descricao": "As inovações tecnológicas estão dominando as conversas em todo o setor, \ne quem liderar essa corrida pode ditar as regras do futuro.",
         "marketing": 0.9, "pd": 1.3, "producao": 0.8},
        
        {"descricao": "Uma nova plataforma social emergiu, capturando a atenção global. \nO mundo digital está mais vibrante e imprevisível do que nunca.",
         "marketing": 1.3, "pd": 1.1, "producao": 1.0},
        
        {"descricao": "Uma startup ousada acaba de fazer um grande lançamento, atraindo a atenção da mídia. \nTodos os olhos estão voltados para o próximo passo.",
         "marketing": 1.1, "pd": 1.3, "producao": 0.8},
        
        {"descricao": "As taxas de juros caíram drasticamente, abrindo portas para novas expansões. \nO cenário financeiro está em plena transformação.",
         "marketing": 0.6, "pd": 0.8, "producao": 1.3},
        
        {"descricao": "Uma mudança nas regulações governamentais virou o jogo da publicidade. \nAgora, o mercado se adapta às novas regras impostas.",
         "marketing": 0.8, "pd": 1.1, "producao": 1.0},
        
        {"descricao": "O interesse por soluções sustentáveis está no auge. \nAs empresas que não se adaptarem a essa realidade podem ser deixadas para trás.",
         "marketing": 1.1, "pd": 1.3, "producao": 1.0},
        
        {"descricao": "Um surto inflacionário pegou todos de surpresa, elevando os custos \ne forçando mudanças rápidas na estratégia de negócios.",
         "marketing": 0.9, "pd": 0.9, "producao": 0.7},
        
        {"descricao": "Em meio a uma recessão, os consumidores estão mais cautelosos do que nunca. \nAtrair atenção agora exige uma abordagem estratégica única.",
         "marketing": 1.2, "pd": 1.1, "producao": 0.9},
        
        {"descricao": "Novas ferramentas de automação começaram a transformar processos produtivos. \nQuem se adapta rápido, encontra uma vantagem crucial.",
         "marketing": 0.8, "pd": 1.3, "producao": 1.0},
        
        {"descricao": "Mudanças drásticas nas políticas de publicidade online estão impactando \ncomo as empresas podem alcançar seus clientes.",
         "marketing": 1.0, "pd": 1.3, "producao": 1.1},
        
        {"descricao": "Os consumidores estão cada vez mais exigentes em relação à qualidade dos produtos. \nAdaptar-se a essa nova expectativa se tornou prioridade.",
         "marketing": 1.1, "pd": 1.3, "producao": 1.0},
        
        {"descricao": "Os custos dos materiais subiram abruptamente, \nforçando as empresas a revisarem suas operações em busca de eficiência.",
         "marketing": 0.9, "pd": 1.3, "producao": 0.8},
        
        {"descricao": "Boicotes sociais contra corporações têm ganhado força. \nA imagem pública das empresas nunca foi tão importante.",
         "marketing": 1.3, "pd": 1.0, "producao": 1.1},
        
        {"descricao": "Uma descoberta revolucionária acabou de ser anunciada, prometendo mudar os rumos do setor. \nAs implicações são imensas para quem se adaptar primeiro.",
         "marketing": 1.1, "pd": 1.3, "producao": 1.0},
        
        {"descricao": "As vendas online estão crescendo a uma taxa sem precedentes, \nmudando rapidamente as dinâmicas de mercado. O e-commerce está em expansão.",
         "marketing": 1.2, "pd": 1.3, "producao": 1.0},
        
        {"descricao": "Desastres ambientais estão afetando cadeias de suprimentos globais. \nAs empresas precisam repensar sua abordagem para manter a produção viável.",
         "marketing": 0.7, "pd": 1.3, "producao": 0.7},
        
        {"descricao": "O aumento na adoção de plataformas de streaming está mudando como as empresas anunciam, \ncom novas oportunidades surgindo.",
         "marketing": 1.2, "pd": 1.2, "producao": 1.1},
        
        {"descricao": "Os custos de energia caíram repentinamente, \ncriando uma oportunidade única para rever as operações e cortar despesas.",
         "marketing": 1.0, "pd": 1.0, "producao": 1.3},
        
        {"descricao": "O governo anunciou subsídios generosos para empresas inovadoras. \nNovas portas se abriram.",
         "marketing": 1.0, "pd": 1.3, "producao": 1.2},
        
        {"descricao": "Uma onda de incerteza tomou conta do mercado. \nEmpresas precisam se reposicionar rapidamente para restaurar a confiança dos consumidores.",
         "marketing": 1.3, "pd": 1.0, "producao": 0.7}
    ]
    return random.sample(cenarios_disponiveis, num_rodadas)


# Função para exibir gráfico ao final do jogo
def exibir_grafico(empresas):
    plt.figure(figsize=(10, 6))
    for empresa in empresas:
        plt.plot(empresa.saldo_historico, label=empresa.nome, marker='o')

    plt.title("Evolução do Saldo dos Jogadores")
    plt.xlabel("Rodadas")
    plt.ylabel("Saldo (R$)")
    plt.legend()
    plt.grid(True)
    plt.show()

# Função principal do jogo
def jogo():
    tela_inicial()
    
    # Perguntar o número de jogadores e rodadas
    num_jogadores = int(input("\nQuantos jogadores irão participar (máx. 10)? "))
    num_rodadas = int(input("Quantas rodadas terá o jogo (máx. 10)? "))
    
    # Criar as empresas (jogadores)
    empresas = [Empresa(input(f"Nome da empresa do Jogador {i+1}: ")) for i in range(num_jogadores)]
    
    # Gerar cenários únicos
    cenarios = gerar_cenarios_unicos(num_rodadas)

    # Rodar o jogo
    for rodada in range(1, num_rodadas + 1):
        limpar_tela()
        exibir_ranking(empresas, rodada)
        
        print(f"\n{Fore.GREEN}{rodada}ª RODADA")
        cenario = cenarios[rodada - 1]
        print(Fore.WHITE + f"Cenário: {cenario['descricao']}")
        print(Fore.GREEN + "═" * 50)

        for empresa in sorted(empresas, key=lambda x: x.saldo, reverse=True):
            print(f"\n{Fore.LIGHTYELLOW_EX}{empresa.nome}, faça suas escolhas de investimento (Marketing, P&D e Produção):")
            print(Fore.WHITE + f"Saldo disponível: R${empresa.saldo:.2f}")
            while True:
                try:
                    marketing = float(input(Fore.LIGHTCYAN_EX + "Investimento em Marketing (R$): "))
                    pd = float(input(Fore.LIGHTCYAN_EX + "Investimento em P&D (R$): "))
                    producao = float(input(Fore.LIGHTCYAN_EX + "Investimento em Produção (R$): "))
                except ValueError:
                    print(Fore.RED + "⚠️ Valor inválido! Tente novamente.")
                    continue

                if marketing + pd + producao > empresa.saldo:
                    print(Fore.RED + "❌ Investimento maior que o saldo disponível. Tente novamente.")
                else:
                    break

            empresa.investir(marketing, pd, producao, cenario)

        input(Fore.LIGHTYELLOW_EX + "\nRodada concluída! Pressione Enter para ver o ranking atualizado...")

    limpar_tela()
    exibir_ranking(empresas, rodada=num_rodadas + 1)
    vencedor = max(empresas, key=lambda x: x.saldo)
    print(Fore.LIGHTYELLOW_EX + f"\n🎉 A empresa vencedora é: {vencedor.nome} com um saldo final de R${vencedor.saldo:.2f}!")
    print(Fore.GREEN + "═" * 50)

    # Exibir gráfico ao final do jogo
    exibir_grafico(empresas)

# Executar o jogo
if __name__ == "__main__":
    jogo()
