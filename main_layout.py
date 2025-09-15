import streamlit as st
import pandas as pd

# -----------------------
# Layout fixo das docas
# -----------------------

layout = [
    ["A012", "E048", "E049", "E050", "E051", "E052", "E053", "E054", "E055", "E056", "E057", "E058", "E059", "E060",
     "E061", "E062", "E063", "E064", "E065", "E066", "E067", "E068", "E069", "E070", "E071", "E072", "E073", "E074",
     "E075", "E076", "E085", "F090", "F091", "F092", "F093", "F094", "F095", "F120", "F121", "F122", "F123", "F124",
     "F125", "F126", "F127", "F128", "F129", "F130", "F131"],
    ["A011", "", "", "", "", "", "",       "D041"],
    ["A010", "", "","", "", "", "",        "D040"],
    ["A009", "", "","","", "", "",         "D039"],
    ["A008", "", "","", "", "", "",        "D038"],
    ["A007", "", "","", "", "", "",        "D037"],
    ["A006", "", "B020","", "C027", "", "","D036"],
    ["A005", "", "B019","", "C026", "", "","D035"],
    ["A004", "", "B018","", "C025", "", "","D034"],
    ["A003", "", "B017","", "C024", "", "","D033"],
    ["A002", "", "B016","", "C023", "", "","D032"],
    ["A001", "", "B015","", "C022", "", "","D031"],
    ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "","", "", "", "", "", "", "", "", "", "", "", "","", "G100", "G101", "G102", "G103", "G104",
     "G105", "G106", "G107", "G108", "G109", "G110", "G111", "G112", "G113", "G114", "G115", "G116"]
]


# -----------------------
# Função para desenhar grade
# -----------------------
def desenhar_grade(docas_excel, dados_completos=None, doca_selecionada=None):
    st.write("### Layout das Docas")

    html = "<table style='border-collapse: collapse;'>"
    for row in layout:
        html += "<tr>"
        for cell in row:
            if cell == "":  # passagem
                color = "white"
                text = ""
                estilo_extra = ""
            elif cell in docas_excel:  # presente no Excel
                # Verificar se é a doca selecionada
                # if doca_selecionada and cell == doca_selecionada:
                #     color = "darkgreen"
                #     estilo_extra = "box-shadow: 0 0 8px 2px yellow; transform: scale(1.05); z-index: 10; position: relative;"
                if docas_selecionadas and cell in docas_selecionadas:
                    color = "darkgreen"
                    estilo_extra = "box-shadow: 0 0 8px 2px yellow; transform: scale(1.05); z-index: 10; position: relative;"

                else:
                    color = "lightgreen"
                    estilo_extra = ""
                text = cell
            else:  # faz parte do layout mas não está no Excel
                color = "lightcoral"
                text = cell
                estilo_extra = ""

            html += f"<td style='width:40px; height:25px; border:1px solid #999; background-color:{color}; text-align:center; font-size:12px; {estilo_extra}'>{text}</td>"
        html += "</tr>"
    html += "</table>"

    st.markdown(html, unsafe_allow_html=True)

    # Adicionar legenda
    st.markdown("""
    <div style='margin-top: 20px;'>
        <div style='display: inline-block; width: 20px; height: 20px; background-color: lightgreen; margin-right: 10px; border: 1px solid #999;'></div>
        <span>Doca presente no Excel</span>
        <div style='display: inline-block; width: 20px; height: 20px; background-color: lightcoral; margin-left: 20px; margin-right: 10px; border: 1px solid #999;'></div>
        <span>Doca não encontrada</span>
        <div style='display: inline-block; width: 20px; height: 20px; background-color: white; margin-left: 20px; margin-right: 10px; border: 1px solid #999;'></div>
        <span>Espaço vazio</span>
        <div style='display: inline-block; width: 20px; height: 20px; background-color: darkgreen; margin-left: 20px; margin-right: 10px; border: 1px solid #999;'></div>
        <span>Doca selecionada</span>
    </div>
    """, unsafe_allow_html=True)


# -----------------------
# Função para processar arquivos
# -----------------------
def processar_arquivo(uploaded_file, nome_arquivo):
    try:
        df = pd.read_excel(uploaded_file)

        # Verificar se as colunas necessárias existem
        colunas_necessarias = ['DOCA']
        colunas_disponiveis = []

        for col in colunas_necessarias:
            if col in df.columns:
                colunas_disponiveis.append(col)

        if not colunas_disponiveis:
            st.error(f"O arquivo {nome_arquivo} não contém a coluna 'DOCA'")
            return None

        # Converter DOCA para string e limpar
        df['DOCA'] = df['DOCA'].astype(str).str.strip()

        return df

    except Exception as e:
        st.error(f"Erro ao processar o arquivo {nome_arquivo}: {e}")
        return None


# -----------------------
# App principal
# -----------------------
st.title("Mapa de Docas")

# Inicializar session state para armazenar os dados
if 'dados_arquivos' not in st.session_state:
    st.session_state.dados_arquivos = {}
if 'doca_selecionada' not in st.session_state:
    st.session_state.doca_selecionada = None

# Upload de múltiplos arquivos
uploaded_files = st.file_uploader(
    "Carregar arquivos Excel com coluna 'DOCA' (máximo 4)",
    type=["xlsx"],
    accept_multiple_files=True
)

# Limitar a 4 arquivos
if uploaded_files and len(uploaded_files) > 4:
    st.warning("Máximo de 4 arquivos permitidos. Apenas os primeiros 4 serão processados.")
    uploaded_files = uploaded_files[:4]

# Processar arquivos
if uploaded_files:
    for i, uploaded_file in enumerate(uploaded_files):
        nome_arquivo = uploaded_file.name

        # Processar apenas se ainda não foi processado
        if nome_arquivo not in st.session_state.dados_arquivos:
            with st.spinner(f"Processando {nome_arquivo}..."):
                df = processar_arquivo(uploaded_file, nome_arquivo)
                if df is not None:
                    st.session_state.dados_arquivos[nome_arquivo] = df
                    st.success(f"Arquivo {nome_arquivo} processado com sucesso!")

# Mostrar opções de visualização se houver arquivos
if st.session_state.dados_arquivos:
    # Selecionar qual arquivo visualizar
    arquivos_disponiveis = list(st.session_state.dados_arquivos.keys())
    arquivo_selecionado = st.selectbox(
        "Selecione o arquivo para visualizar:",
        options=arquivos_disponiveis
    )

    # Obter dados do arquivo selecionado
    df_selecionado = st.session_state.dados_arquivos[arquivo_selecionado]
    docas_excel = df_selecionado["DOCA"].dropna().astype(str).tolist()

    # # Selecionar uma doca para mostrar detalhes
    # docas_validas = [d for d in docas_excel if d != 'nan']
    # doca_selecionada = st.selectbox(
    #     "Selecione uma doca para ver detalhes:",
    #     options=[""] + sorted(docas_validas),
    #     index=0
    # )
    #
    # # Atualizar session state
    # if doca_selecionada:
    #     st.session_state.doca_selecionada = doca_selecionada
    # Selecionar uma ou várias docas para mostrar detalhes
    docas_validas = [d for d in docas_excel if d != 'nan']
    docas_selecionadas = st.multiselect(
        "Selecione uma ou mais docas para ver detalhes:",
        options=sorted(docas_validas),
        default=[]
    )

    # Atualizar session state
    st.session_state.docas_selecionadas = docas_selecionadas

    # Desenhar o layout
    desenhar_grade(docas_excel, df_selecionado, st.session_state.doca_selecionada)

    # Mostrar detalhes da doca selecionada
    # if st.session_state.doca_selecionada:
    #     st.subheader(f"Detalhes da Doca {st.session_state.doca_selecionada}")
    #
    #     # Filtrar dados para a doca selecionada
    #     dados_doca = df_selecionado[df_selecionado['DOCA'] == st.session_state.doca_selecionada]
    #
    #     # Verificar se existem as colunas DIRECAO e LINHA
    #     if 'DIRECAO' in df_selecionado.columns and 'LINHA' in df_selecionado.columns:
    #         st.dataframe(dados_doca[['DOCA', 'DIRECAO', 'LINHA']])
    #     else:
    #         st.info("Colunas 'DIRECAO' e/ou 'LINHA' não encontradas no arquivo.")
    #         st.dataframe(dados_doca)
    if st.session_state.docas_selecionadas:
        for doca in st.session_state.docas_selecionadas:
            st.subheader(f"Detalhes da Doca {doca}")
            dados_doca = df_selecionado[df_selecionado['DOCA'] == doca]

            if 'DIRECAO' in df_selecionado.columns and 'LINHA' in df_selecionado.columns:
                st.dataframe(dados_doca[['DOCA', 'DIRECAO', 'LINHA']])
            else:
                st.dataframe(dados_doca)

    # Mostrar estatísticas
    st.subheader("Estatísticas")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total de docas no arquivo", len(docas_excel))

    with col2:
        docas_presentes = sum(1 for row in layout for cell in row if cell in docas_excel)
        st.metric("Docas presentes no layout", docas_presentes)

    with col3:
        docas_faltantes = sum(1 for row in layout for cell in row if cell and cell not in docas_excel and cell != "")
        st.metric("Docas faltantes no layout", docas_faltantes)

    # Mostrar dados completos
    with st.expander("Visualizar dados completos do arquivo"):
        st.dataframe(df_selecionado)

else:
    st.info("Carregue um ou mais arquivos Excel para visualizar o layout.")

# Adicionar instruções
with st.expander("Instruções de uso"):
    st.markdown("""
    1. Faça upload de até 4 arquivos Excel que contenham a coluna 'DOCA'
    2. Selecione qual arquivo visualizar no dropdown
    3. Selecione uma doca específica para ver seus detalhes
    4. As docas presentes no arquivo aparecem em verde
    5. As docas do layout que não estão no arquivo aparecem em vermelho
    6. A doca selecionada é destacada com contorno amarelo
    """)
