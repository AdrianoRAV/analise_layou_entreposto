# analise_layou_entreposto
O aplicativo gere um layout pré-definido preenchendo com cor verde locais ocupados e vermelho locais livres , apartir de um excel com posição e um botão para selecionar a doca e gerr um detalhes do que está alocado
Gerador de Excel para Análise de Triagem
Este projeto é uma ferramenta de desktop simples e poderosa, construída com Python e a biblioteca Flet, para simular e analisar a triagem de CEPs. O programa processa dados de triagem em arquivos Excel, gera um painel visual para análise e exporta um relatório detalhado para uma planilha.

🚀 Funcionalidades
Carregamento de Dados: Lê arquivos .xlsx para o "Plano de Triagem" e o "Arquivo de Triagem".

Normalização Inteligente: Identifica automaticamente colunas como CEP Inicial e CEP Final, mesmo se os nomes estiverem com erros de digitação ou sem acentos.

Simulação em Tempo Real: Processa a triagem dos CEPs e exibe a distribuição de objetos por rampa e ala em um painel interativo.

Exportação para Excel: Gera um relatório detalhado com um resumo da contagem de CEPs por direção e uma lista de CEPs não encontrados.

📦 Como Usar
1. Requisitos
Certifique-se de que você tem o Python instalado. O projeto usa as seguintes bibliotecas:

pip install flet pandas openpyxl

2. Executando a Aplicação
Para iniciar o programa, execute o seguinte comando no terminal, dentro da pasta do projeto:

streamlit run seu_programa.py

Substitua seu_programa.py pelo nome do arquivo Python que contém o código da aplicação.



🛠️ Tecnologias Utilizadas
Python

Streamlit (para a interface gráfica)

Pandas (para manipulação de dados)

OpenPyXL (para leitura e escrita de arquivos Excel)

![Tela Layout](Screen.png)

![Tela Layout modo Dark](Layout.PNG)

![Tela Layout total](screens1.png)




📄 Licença
Este projeto está licenciado sob a Licença MIT.

