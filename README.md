# Desafio das Empresas

## Descrição

O "Desafio das Empresas" é um jogo de estratégia onde os jogadores assumem o papel de CEOs de empresas competindo em um mercado dinâmico. O objetivo é maximizar o faturamento de suas empresas através de decisões estratégicas de investimento em marketing, pesquisa e desenvolvimento (P&D) e novos produtos.

## Estrutura do Projeto

-   **`jogo_console.py`**: Código do jogo em modo console. Os jogadores interagem através do terminal.

## Como Executar

1. Certifique-se de ter o Python instalado em sua máquina (versão 3.6 ou superior).
2. Navegue até o diretório do projeto.
3. Execute o arquivo console com o comando:
    ```bash
    python jogo_console.py
    ```

## Lógica de Funcionamento do Jogo

### Introdução

Os jogadores começam o jogo criando suas empresas e decidindo quanto investir em três áreas principais: **Marketing**, **P&D** e **Novos Produtos**. A cada rodada, eventos inesperados ocorrem, impactando o desempenho de cada empresa.

### Áreas de Investimento

Os investimentos são divididos nas seguintes áreas, cada uma afetando o faturamento de maneiras diferentes:

1. **Marketing**:

    - **Objetivo**: Aumentar a visibilidade da empresa e atrair mais clientes.
    - **Impacto**: Um investimento alto em marketing geralmente resulta em um aumento no faturamento, especialmente se o mercado estiver receptivo. O impacto é maior em situações de concorrência intensa.

2. **Pesquisa e Desenvolvimento (P&D)**:

    - **Objetivo**: Criar inovações que melhorem produtos existentes ou desenvolvam novos produtos.
    - **Impacto**: Investimentos em P&D podem resultar em melhorias significativas a longo prazo. Um investimento maior em P&D pode ajudar a reduzir custos operacionais, mas o retorno pode não ser imediato. É especialmente importante em cenários de novas regulamentações.

3. **Novos Produtos**:
    - **Objetivo**: Lançar novos produtos para capturar novas oportunidades de mercado.
    - **Impacto**: O lançamento bem-sucedido de novos produtos pode gerar um retorno rápido, especialmente se a demanda for alta. Um investimento maior nessa área é mais benéfico durante mudanças nas preferências do consumidor.

### Eventos do Mercado

A cada rodada, um evento aleatório é gerado, afetando o desempenho das empresas de maneiras diferentes. Os eventos são:

1. **Mudança nas preferências do consumidor**:

    - **Impacto**: Afeta positivamente os investimentos em novos produtos e tem um impacto menor nos outros investimentos.
    - **Cenário**: Os consumidores estão mudando seus hábitos de compra, preferindo produtos mais sustentáveis e inovadores.

2. **Nova regulamentação**:

    - **Impacto**: Aumenta a importância dos investimentos em P&D.
    - **Cenário**: O governo introduziu novas regulamentações que afetam diretamente a produção e o custo de operações das empresas.

3. **Crise econômica**:

    - **Impacto**: Afeta negativamente todos os investimentos, especialmente os novos produtos.
    - **Cenário**: A economia global enfrenta uma desaceleração significativa, e o poder de compra dos consumidores está em queda.

4. **Concorrência intensa**:

    - **Impacto**: Aumenta a eficácia dos investimentos em marketing.
    - **Cenário**: Novos concorrentes entraram no mercado, oferecendo produtos inovadores a preços agressivos.

5. **Inovação tecnológica**:
    - **Impacto**: Fortalece tanto os investimentos em novos produtos quanto em P&D.
    - **Cenário**: Uma nova tecnologia disruptiva está revolucionando o setor, abrindo oportunidades para empresas que investirem rapidamente.

### Vencedor do Jogo

Ao final de todas as rodadas, a empresa com o maior faturamento total é declarada vencedora. O jogo não apenas testa as habilidades estratégicas dos jogadores, mas também simula a imprevisibilidade do ambiente de negócios.

## Dependências

-   Python (recomenda-se versão 3.6 ou superior)

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.
