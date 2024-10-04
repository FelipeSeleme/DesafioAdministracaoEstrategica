# Desafio das Empresas

## Descrição

O "Desafio das Empresas" é um jogo de estratégia interativo onde os jogadores assumem o papel de CEOs de empresas competindo em um mercado dinâmico e desafiador. O objetivo é maximizar o faturamento de suas empresas através de decisões estratégicas de investimento em três áreas principais: Marketing, Pesquisa e Desenvolvimento (P&D) e Produção. A cada rodada, eventos inesperados podem impactar o desempenho das empresas, exigindo adaptações rápidas nas estratégias de investimento.

## Estrutura do Projeto

-   **`jogo_console.py`**: Código-fonte do jogo, onde os jogadores interagem através do terminal em modo console.

## Como Executar

1. **Certifique-se de ter o Python instalado** em sua máquina (versão 3.6 ou superior).
2. **Navegue até o diretório do projeto** utilizando o terminal.
3. **Execute o arquivo do jogo** com o seguinte comando:
    ```bash
    python jogo_console.py
    ```

## Lógica de Funcionamento do Jogo

### Introdução

Os jogadores começam o jogo criando suas empresas e definindo quanto desejam investir em três áreas: **Marketing**, **P&D** e **Produção**. A cada rodada, um cenário aleatório é gerado, trazendo novos desafios e oportunidades para as empresas.

### Áreas de Investimento

Os investimentos são divididos nas seguintes áreas, cada uma com um impacto diferente no faturamento das empresas:

1. **Marketing**:

    - **Objetivo**: Aumentar a visibilidade da empresa e atrair mais clientes.
    - **Impacto**: Investimentos elevados em marketing podem resultar em um aumento significativo nas vendas, especialmente em um ambiente de alta concorrência.

2. **Pesquisa e Desenvolvimento (P&D)**:

    - **Objetivo**: Inovar e melhorar produtos existentes.
    - **Impacto**: Um bom investimento em P&D pode levar a melhorias a longo prazo, possibilitando a redução de custos operacionais e a criação de produtos mais competitivos.

3. **Produção**:
    - **Objetivo**: Aumentar a eficiência produtiva e atender à demanda do mercado.
    - **Impacto**: Um investimento eficaz na produção pode resultar em maiores margens de lucro e capacidade de resposta às demandas do mercado.

### Eventos do Mercado

Durante o jogo, a cada rodada, um evento aleatório é gerado, influenciando o desempenho das empresas de diferentes maneiras. Alguns exemplos de eventos são:

-   **Mudança nas preferências do consumidor**: Aumenta a eficácia dos investimentos em novos produtos.
-   **Nova regulamentação**: Impõe desafios e exige adaptações, aumentando a importância dos investimentos em P&D.
-   **Crise econômica**: Afeta negativamente todos os investimentos, exigindo uma gestão cuidadosa dos recursos.
-   **Concorrência intensa**: Aumenta a necessidade de investir em marketing para manter a visibilidade e as vendas.

### Vencedor do Jogo

Ao final de todas as rodadas, a empresa com o maior saldo acumulado é declarada vencedora. O jogo não apenas testa as habilidades estratégicas dos jogadores, mas também simula a imprevisibilidade e os desafios do ambiente de negócios.

## Dependências

-   **Python** (versão 3.6 ou superior).

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request. Agradecemos por seu interesse em melhorar o "Desafio das Empresas"!
