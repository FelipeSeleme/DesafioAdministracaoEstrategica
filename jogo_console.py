import random
import time
import sys
import os

# Função para limpar a tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Definir a classe Empresa
class Empresa:
    def __init__(self, nome, orcamento_inicial=100):
        self.nome = nome
        self.faturamento = 100  # Faturamento inicial
        self.custos = 50  # Custos iniciais
        self.orcamento = orcamento_inicial  # Orçamento inicial
        self.investimento_marketing = 0
        self.investimento_pd = 0
        self.investimento_novos_produtos = 0
    
    def tomar_decisao(self):
        print(f"\n💼 Decisões da Empresa {self.nome} (Orçamento restante: R${self.orcamento:.2f}):")
        self.investimento_marketing = int(input("Quanto investir em marketing? "))
        self.investimento_pd = int(input("Quanto investir em P&D? "))
        self.investimento_novos_produtos = int(input("Quanto investir em novos produtos? "))
        
        total_investido = self.investimento_marketing + self.investimento_pd + self.investimento_novos_produtos
        if total_investido > self.orcamento:
            print("❌ Investimento excede o orçamento disponível! Tente novamente.")
            self.tomar_decisao()
        else:
            self.orcamento -= total_investido

    def calcular_resultados(self, evento_mercado):
        impacto_evento = evento_mercado['impacto']
        
        # Lógica para calcular o crescimento com base no evento
        if evento_mercado['nome'] == "Mudança nas preferências do consumidor":
            crescimento = (self.investimento_novos_produtos * 0.3) + (self.investimento_pd * 0.1) - (self.custos * 0.1)
        
        elif evento_mercado['nome'] == "Nova regulamentação":
            crescimento = (self.investimento_pd * 0.4) + (self.investimento_marketing * 0.1) - (self.custos * 0.1)
        
        elif evento_mercado['nome'] == "Crise econômica":
            crescimento = (self.investimento_marketing * 0.05) + (self.investimento_novos_produtos * 0.1) - (self.custos * 0.2)
        
        elif evento_mercado['nome'] == "Concorrência intensa":
            crescimento = (self.investimento_marketing * 0.3) + (self.investimento_novos_produtos * 0.1) - (self.custos * 0.1)
        
        elif evento_mercado['nome'] == "Inovação tecnológica":
            crescimento = (self.investimento_novos_produtos * 0.2) + (self.investimento_pd * 0.3) - (self.custos * 0.1)
        
        # Adicionando o impacto do evento
        crescimento += impacto_evento
        
        # Ajuste de custos com base em investimentos em P&D
        if self.investimento_pd > 20:
            self.custos -= self.investimento_pd * 0.05
        
        # Atualiza o faturamento
        self.faturamento += crescimento

        # Atualiza o orçamento com base no desempenho
        self.orcamento += crescimento

    def valor_empresa(self):
        # O valor da empresa é baseado no orçamento restante
        return self.orcamento

# Função para gerar eventos de mercado e cenários relacionados
def gerar_evento_e_cenario():
    eventos = [
        {"nome": "Mudança nas preferências do consumidor", "impacto": random.uniform(-10, 10),
         "cenario": "Os consumidores estão mudando seus hábitos de compra, preferindo produtos mais sustentáveis e inovadores."},
        {"nome": "Nova regulamentação", "impacto": random.uniform(-5, 5),
         "cenario": "O governo introduziu novas regulamentações que afetam diretamente a produção e o custo de operações das empresas."},
        {"nome": "Crise econômica", "impacto": random.uniform(-20, -5),
         "cenario": "A economia global está enfrentando uma desaceleração significativa, e o poder de compra dos consumidores está em queda."},
        {"nome": "Concorrência intensa", "impacto": random.uniform(-15, 0),
         "cenario": "Novos concorrentes entraram no mercado, com ofertas agressivas e inovação tecnológica, desafiando sua posição de mercado."},
        {"nome": "Inovação tecnológica", "impacto": random.uniform(5, 15),
         "cenario": "Uma nova tecnologia disruptiva está revolucionando o setor, abrindo oportunidades para empresas que investirem rapidamente."},
    ]
    return random.choice(eventos)

# Função para revelar os rankings com efeito de digitação
def revelar_resultados(empresas):
    print("\n🔍 CALCULANDO OS RESULTADOS", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="")
        sys.stdout.flush()
    time.sleep(1)
    
    print("\n=== 🏆 RANKING DAS EMPRESAS ===")
    # Ordenar empresas pelo valor total
    empresas.sort(key=lambda e: e.valor_empresa(), reverse=True)
    
    for i, empresa in enumerate(empresas, 1):
        for char in f"{i}. {empresa.nome} - Valor da Empresa: R${empresa.valor_empresa():.2f}\n":
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.03)
        time.sleep(0.3)

# Função para exibir o cenário fixo e ranking a cada rodada
def exibir_ranking_fixo(empresas):
    limpar_tela()
    print("\n=== 🏆 RANKING ATUAL DAS EMPRESAS ===")
    # Ordenar empresas pelo valor total
    empresas.sort(key=lambda e: e.valor_empresa(), reverse=True)
    
    for i, empresa in enumerate(empresas, 1):
        print(f"{i}. {empresa.nome} - Valor da Empresa: R${empresa.valor_empresa():.2f}")

# Função para destacar o vencedor
def destacar_vencedor(empresa):
    print("\n*** 🎉 PARABÉNS! ***")
    for char in f"A empresa vencedora é {empresa.nome}, com um Valor da Empresa de R${empresa.valor_empresa():.2f}!\n":
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)

# Função para apresentar o jogo com introdução e regras
def apresentar_jogo():
    print("""
    === 📊 BEM-VINDO AO DESAFIO DAS EMPRESAS ===
    
    Cenário: Você é o CEO de uma empresa em um mercado altamente competitivo e dinâmico. A cada rodada, você tomará decisões estratégicas sobre como investir seu orçamento nas seguintes áreas:

    1. **Marketing**: Investir em marketing aumenta a visibilidade da sua empresa e pode atrair mais clientes. Quanto mais você investir, maior será o impacto no seu faturamento, especialmente se o mercado estiver receptivo às suas campanhas.
    
    2. **Pesquisa e Desenvolvimento (P&D)**: Investimentos em P&D podem resultar em inovações que melhoram seus produtos ou criam novos produtos. Isso pode levar a um aumento significativo no faturamento a longo prazo, mas geralmente exige um investimento inicial alto e pode não gerar resultados imediatos.
    
    3. **Novos Produtos**: Lançar novos produtos pode abrir novas oportunidades de mercado e atrair diferentes segmentos de consumidores. Esse tipo de investimento pode ter um retorno rápido se a demanda for alta, mas também pode acarretar riscos se os novos produtos não atenderem às expectativas do mercado.

    Objetivo: O objetivo é maximizar o valor da sua empresa, que é o orçamento restante disponível. O mercado enfrentará eventos inesperados a cada rodada, como crises econômicas, mudanças tecnológicas e novas regulamentações, que afetarão o desempenho de todas as empresas.
    
    Como jogar:
    - A cada rodada, você terá um orçamento disponível para investir.
    - Tome decisões de investimento em três áreas: marketing, P&D e novos produtos.
    - Ajuste suas decisões com base nos eventos de mercado e na sua estratégia.
    - A empresa com o maior Valor da Empresa no final do jogo será a vencedora.
    
    Prepare-se, pois cada decisão conta!
    """)
    input("Pressione ENTER para começar o jogo...")

# Função principal do jogo
def jogar(num_rodadas):
    limpar_tela()
    apresentar_jogo()

    num_jogadores = int(input("Quantos jogadores irão participar? (Máximo 10): "))
    empresas = []

    # Criar as empresas
    for i in range(num_jogadores):
        nome = input(f"Nome da Empresa {i+1}: ")
        empresas.append(Empresa(nome))
    
    for rodada in range(1, num_rodadas + 1):
        exibir_ranking_fixo(empresas)
        print(f"=== 📊 Rodada {rodada} ===")
        
        # Gerar evento e cenário relacionados
        evento = gerar_evento_e_cenario()
        print(f"\n⚠️ Cenário: {evento['cenario']}")
        print(f"⚠️ Evento de Mercado: {evento['nome']} com impacto de {evento['impacto']:.2f}")
        
        # Jogadores tomam decisões
        for empresa in empresas:
            empresa.tomar_decisao()
        
        # Calcular resultados
        for empresa in empresas:
            empresa.calcular_resultados(evento)

        # Revelar ranking da rodada com efeito
        revelar_resultados(empresas)
    
    # Destacar o vencedor
    empresas.sort(key=lambda x: x.valor_empresa(), reverse=True)
    destacar_vencedor(empresas[0])

# Iniciar o jogo com 10 rodadas
jogar(10)
