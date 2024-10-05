# 🏆 Desafio das Empresas - Jogo de Simulação em Python

## 📋 Sobre o Jogo

**Desafio das Empresas** é um jogo de simulação estratégico onde cada jogador assume o papel de **CEO** de uma empresa. O objetivo é gerenciar bem os recursos financeiros e tomar decisões estratégicas para aumentar o saldo da empresa, enfrentando cenários de mercado variados. Cada decisão afeta o desempenho em áreas como Marketing, Pesquisa & Desenvolvimento (P&D) e Produção. Ao final do jogo, o jogador com o maior saldo vence.

Este jogo foi desenvolvido para fins educacionais, como parte de uma dinâmica de grupo sobre **teorias de aprendizado**, ensinando os participantes a tomarem decisões estratégicas sob condições de incerteza e competição.

## 🎮 Como Jogar

### 1. Início do Jogo

1. Ao iniciar o jogo, os jogadores são apresentados a uma **tela inicial** com um resumo das regras.
2. Pressione `Enter` para avançar e iniciar a configuração do jogo.

### 2. Configuração

-   **Número de Jogadores**: Cada jogo pode ter de 1 a 10 jogadores.
-   **Número de Rodadas**: O jogo pode ter de 1 a 10 rodadas.

### 3. Nome das Empresas

Cada jogador deve escolher o nome da sua empresa. O nome será utilizado para identificar os jogadores durante o jogo e no ranking.

### 4. Rodadas e Decisões

1. **Cenário da Rodada**: Em cada rodada, será apresentado um **cenário de mercado** único. O cenário inclui descrições que destacam tendências ou mudanças no mercado e indicam quais áreas podem ter maior impacto.

    Exemplo de cenário: "A demanda do mercado aumentou. Produzir mais parece ser uma boa opção."

2. **Investimentos**: Cada jogador terá que decidir como investir seus recursos em três áreas:

    - **Marketing**: Aumenta a visibilidade e reputação da empresa.
    - **Pesquisa e Desenvolvimento (P&D)**: Cria inovação e novos produtos, garantindo vantagem competitiva.
    - **Produção**: Aumenta a capacidade de atender à demanda do mercado.

    Os jogadores devem informar quanto do saldo disponível desejam investir em cada área. O saldo inicial de cada empresa é de **R$1.000,00**, e esse valor é atualizado ao longo do jogo.

3. **Cálculo dos Retornos**: Os retornos dos investimentos são calculados com base nos **multiplicadores ocultos** de cada cenário. O saldo de cada empresa será atualizado ao fim da rodada com base no sucesso das suas decisões.

### 5. Exibição do Ranking

Ao final de cada rodada, o ranking das empresas é exibido na tela com um efeito de digitação. O ranking mostra o nome da empresa de cada jogador e o saldo atualizado, permitindo que todos acompanhem quem está na frente.

### 6. Vencedor

Ao término das rodadas, o jogo exibe o ranking final e a empresa vencedora será aquela que acumulou o maior saldo.

## 🛠️ Instalação e Execução

### Pré-requisitos

-   **Python 3.x** instalado no sistema.

### Como Executar

1. Clone este repositório ou baixe os arquivos do jogo.
2. No terminal, navegue até a pasta onde o arquivo do jogo está localizado.
3. Execute o seguinte comando para iniciar o jogo:

    ```bash
    python desafio_empresas.py
    ```
