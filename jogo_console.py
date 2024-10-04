import random
import os

# Classe que representa uma empresa (jogador)
class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.saldo = 1000.0  # Saldo inicial de R$ 1.000,00

    def investir(self, marketing, pd, producao, multiplicadores):
        # Cálculo dos retornos com base nos multiplicadores do cenário (oculto para os jogadores)
        retorno_marketing = marketing * multiplicadores['marketing']
        retorno_pd = pd * multiplicadores['pd']
        retorno_producao = producao * multiplicadores['producao']
        
        # O saldo é atualizado com o retorno dos investimentos
        self.saldo += retorno_marketing + retorno_pd + retorno_producao

# Função que cria um cenário aleatório para cada rodada
def gerar_cenario():
    cenarios = [
        {"descricao": "A demanda do mercado aumentou. Produzir mais parece ser uma boa opção.", "marketing": 1.2, "pd": 1.1, "producao": 1.5},
        {"descricao": "A concorrência está feroz! Talvez seja a hora de investir em Marketing.", "marketing": 1.5, "pd": 1.1, "producao": 1.0},
        {"descricao": "O mercado está saturado. Inovar pode ser a única saída.", "marketing": 1.0, "pd": 1.6, "producao": 1.2},
        {"descricao": "Custos de produção estão subindo. Cuidados com excesso de produção.", "marketing": 1.3, "pd": 1.0, "producao": 0.8},
        {"descricao": "O setor de tecnologia está aquecido! Investimentos em P&D podem dar uma vantagem competitiva.", "marketing": 1.0, "pd": 1.8, "producao": 1.1},
        {"descricao": "Uma nova rede social viralizou, oferecendo oportunidades de Marketing digital.", "marketing": 1.7, "pd": 1.1, "producao": 1.0},
        {"descricao": "Um novo concorrente entrou no mercado com um produto inovador.", "marketing": 1.3, "pd": 1.5, "producao": 1.0},
        {"descricao": "Houve uma queda nas taxas de juros, facilitando empréstimos para expansão de produção.", "marketing": 1.0, "pd": 1.2, "producao": 1.7},
        {"descricao": "Uma mudança regulatória impôs novas regras para publicidade.", "marketing": 0.9, "pd": 1.2, "producao": 1.1},
        {"descricao": "A demanda por produtos sustentáveis está em alta, impulsionando a inovação em P&D.", "marketing": 1.1, "pd": 1.7, "producao": 1.0},
        {"descricao": "Um aumento inesperado de inflação afetou os custos de produção.", "marketing": 1.0, "pd": 1.0, "producao": 0.7},
        {"descricao": "O país está em recessão, consumidores estão cautelosos, e estratégias de Marketing precisam ser agressivas.", "marketing": 1.8, "pd": 1.2, "producao": 0.9},
        {"descricao": "Novas tecnologias de automação reduziram custos de produção.", "marketing": 1.0, "pd": 1.5, "producao": 1.6},
        {"descricao": "A mídia social passou por uma mudança nas regras de publicidade, impactando campanhas de Marketing.", "marketing": 0.8, "pd": 1.4, "producao": 1.2},
        {"descricao": "A percepção do consumidor sobre qualidade aumentou. Investimentos em P&D se tornam críticos.", "marketing": 1.1, "pd": 1.8, "producao": 1.1},
        {"descricao": "Um aumento no preço dos materiais causou um impacto nos custos de produção.", "marketing": 1.2, "pd": 1.0, "producao": 0.8},
        {"descricao": "A tendência de 'boicotes sociais' contra empresas cresceu, e as marcas precisam melhorar sua imagem pública.", "marketing": 1.6, "pd": 1.0, "producao": 1.1},
        {"descricao": "Uma inovação revolucionária foi introduzida no mercado, mudando completamente o setor.", "marketing": 1.1, "pd": 1.9, "producao": 1.3},
        {"descricao": "O setor de e-commerce está crescendo rapidamente, criando novas oportunidades para Marketing digital.", "marketing": 1.7, "pd": 1.3, "producao": 1.0},
        {"descricao": "Mudanças climáticas estão afetando a cadeia de suprimentos e a produção, exigindo inovação.", "marketing": 1.2, "pd": 1.6, "producao": 0.9},
        {"descricao": "Houve um crescimento explosivo nas plataformas de streaming, oferecendo novas opções para publicidade digital.", "marketing": 1.6, "pd": 1.2, "producao": 1.0},
        {"descricao": "Houve uma queda nos preços de energia, o que reduz os custos de produção.", "marketing": 1.0, "pd": 1.0, "producao": 1.8},
        {"descricao": "O governo anunciou novos subsídios para empresas que investem em pesquisa e desenvolvimento.", "marketing": 1.0, "pd": 2.0, "producao": 1.2},
        {"descricao": "Uma crise de confiança abalou o mercado, e as empresas precisam se reposicionar no Marketing.", "marketing": 1.8, "pd": 1.3, "producao": 1.0}
    ]
    return random.choice(cenarios)

# Função para exibir o ranking das empresas
def exibir_ranking(empresas):
    empresas_ordenadas = sorted(empresas, key=lambda x: x.saldo, reverse=True)
    print("\n" + "═" * 50)
    print("🏆  RANKING DAS EMPRESAS  🏆".center(50))
    print("═" * 50)
    for i, empresa in enumerate(empresas_ordenadas, start=1):
        print(f"{i}. {empresa.nome:<20} - Saldo: R${empresa.saldo:,.2f}")
    print("═" * 50)

# Função para limpar a tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função que exibe a tela inicial
def tela_inicial():
    limpar_tela()
    print("═" * 50)
    print(" 📊 BEM-VINDO AO DESAFIO DAS EMPRESAS 📊".center(50))
    print("═" * 50)
    print("📌 COMO FUNCIONA O JOGO:")
    print("Você é o CEO de uma empresa em um mercado altamente competitivo.")
    print("A cada rodada, você fará decisões estratégicas sobre onde investir seu orçamento.")
    print("\nÁreas de investimento disponíveis:")
    print("  ➤ Marketing: Aumenta a visibilidade da empresa.")
    print("  ➤ Pesquisa e Desenvolvimento (P&D): Gera inovação e novos produtos.")
    print("  ➤ Produção: Aumenta a capacidade produtiva para atender a demanda.")
    print("═" * 50)
    input("Pressione Enter para iniciar o jogo...")

# Função principal do jogo
def jogo():
    tela_inicial()
    
    # Perguntar o número de jogadores e rodadas
    num_jogadores = int(input("\nQuantos jogadores irão participar (máx. 10)? "))
    num_rodadas = int(input("Quantas rodadas terá o jogo (máx. 10)? "))
    
    # Criar as empresas (jogadores)
    empresas = []
    for i in range(num_jogadores):
        nome_empresa = input(f"Nome da empresa do Jogador {i+1}: ")
        empresas.append(Empresa(nome_empresa))

    # Rodar o jogo por cada rodada
    for rodada in range(1, num_rodadas + 1):
        limpar_tela()

        # Exibir o ranking fixo no início de cada rodada
        exibir_ranking(empresas)

        print(f"\n{rodada}ª RODADA".center(10, "="))
        
        # Gerar cenário aleatório
        cenario = gerar_cenario()
        print(f"Cenário: {cenario['descricao']}")
        print("=" * 50)
        
        # Para cada jogador, solicitar os investimentos
        for empresa in empresas:
            print(f"\n{empresa.nome}, faça suas escolhas de investimento:")
            print(f"Saldo disponível: R${empresa.saldo:.2f}")
            
            # Solicitar os investimentos
            try:
                marketing = float(input("Investimento em Marketing (R$): "))
                pd = float(input("Investimento em P&D (R$): "))
                producao = float(input("Investimento em Produção (R$): "))
            except ValueError:
                print("⚠️ Valor inválido! Tente novamente.")
                continue
            
            # Verificar se os investimentos não ultrapassam o saldo
            total_investido = marketing + pd + producao
            if total_investido > empresa.saldo:
                print("❌ Investimento maior que o saldo disponível. Tente novamente.")
                continue

            # Atualizar saldo com os retornos (sem mostrar os multiplicadores)
            empresa.investir(marketing, pd, producao, cenario)

        # Exibir ranking ao final da rodada (fixo no início da próxima)
        print("\nRodada concluída! Pressione Enter para ver o ranking atualizado...")
        input()

    # Exibir o vencedor ao final do jogo
    limpar_tela()
    exibir_ranking(empresas)
    vencedor = max(empresas, key=lambda x: x.saldo)
    print(f"\n🎉 A empresa vencedora é: {vencedor.nome} com um saldo final de R${vencedor.saldo:.2f}!")
    print("=" * 50)

# Executar o jogo
if __name__ == "__main__":
    jogo()