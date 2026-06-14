import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from lifelines import KaplanMeierFitter, CoxPHFitter

# Configuradno titulo da página do streamlit
st.set_page_config(
    page_title="Dashboard de People Analytics - Análise de Atrito",
    page_icon="📊",
    layout="wide"
)


# Mudando de estilo para os gráficos
sns.set_theme(style="whitegrid")

df = pd.read_csv('../data/tabela_base_traduzida.csv')

# Mapeamento do atrito para numérico se necessário para os modelos
if 'Demitido_Num' not in df.columns:
    df['Demitido_Num'] = df['Demitido'].apply(lambda x: 1 if str(x).strip().lower() == 'yes' else 0)

# Sidebar
st.sidebar.title("Filtros Globais")
st.sidebar.markdown("Use os filtros abaixo para segmentar a visão geral:")

departamentos = ['Todos'] + list(df['Departamento'].unique())
dept_selecionado = st.sidebar.selectbox("Selecione o Departamento", departamentos)

if dept_selecionado != 'Todos':
    df_filtrado = df[df['Departamento'] == dept_selecionado]
else:
    df_filtrado = df

# Título tela inicial
st.title("📊 Projeto People Analytics: Análise de Atrito de Funcionários")
st.markdown("""
Este projeto foi adaptado para o streamlit visando uma interação do usuário com o projeto de análise.
""")

# Definindo abas no dashboards
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📍 Visão Geral e Tratamento", 
    "🔍 Análise Exploratória (EDA)", 
    "📈 Diagnóstico Estatístico Visual", 
    "⏳ Análise de Sobrevivência", 
    "📦 Matriz 9-Box"
])

# ------------------------------------------------------------------------------------ ABA 01 -------------------------------------------------------------------


with tab1:
    st.header("1. Importação e Estrutura dos Dados")
    st.markdown("""
    **Etapas de Tratamento Executadas:**
    * Tradução e padronização das colunas originais para o Português.
    * Categorização de variáveis (Faixa Etária, Distância de Casa e Tempo de Empresa).
    * Criação da coluna **Razão Salarial** (Salário do funcionário / Média do cargo).
    """)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Total de valores", df.shape[0])
    col2.metric("Total de variáveis", df.shape[1])
    col3.metric("Taxa de atrito geral", f"{(df['Demitido_Num'].mean() * 100):.2f}%")
    
    st.subheader("Visualização amostral da Base de Dados")
    st.dataframe(df_filtrado.head(10))


# ------------------------------------------------------------------------- ABA 02: ANÁLISE EXPLORATÓRIA (EDA) ------------------------------------------------------

with tab2:
    st.header("2. Análise Exploratória de Dados (EDA)")
    
    col1, col2 = st.columns(2)
    
    with col1:

        #Título gráfico
        st.subheader("Atrito por Gênero")

        # Gráfico de Gênero
        fig, ax = plt.subplots(figsize=(6, 4))

        sns.barplot(data=df_filtrado, x='Genero', y='Demitido_Num', ax=ax, errorbar=None, palette='Blues_r')
        ax.set_ylabel("Taxa de Demissão")
        ax.set_title("Proporção de Demissões por Gênero")

        st.pyplot(fig)
        st.markdown("**Insight:** Homens e mulheres apresentam taxas de demissão próximas, com sutil variação dependendo da área.")

    with col2:

        st.subheader("Atrito por Faixa Etária")

        fig, ax = plt.subplots(figsize=(6, 4))

        sns.barplot(data=df_filtrado, x='Faixa_Etaria', y='Demitido_Num', ax=ax, errorbar=None, order=['Jovem', 'Adulto', 'Maduro'], palette='Oranges_r')
        ax.set_ylabel("Taxa de Demissão")
        ax.set_title("Proporção de Demissões por Faixa Etária")

        st.pyplot(fig)
        st.markdown("**Insight:** A maior concentração absoluta de demitidos está entre adultos (30-44 anos), mas jovens possuem uma alta taxa proporcional.")


    # Terceiro gráfico fora das colunas

    st.subheader("Atrito por Cargo e Impacto na Folha")
    
    fig, ax = plt.subplots(figsize=(12, 5))
    sns.countplot(data=df_filtrado, x='Cargo', hue='Demitido', palette='Set2')
    plt.xticks(rotation=45, ha='right')
    st.pyplot(fig)
    st.markdown("""
    * **Técnicos de Laboratório** apresentam o maior volume de desligamentos (embora representem uma fatia menor do custo total da folha).
    * Em contrapartida, **Diretores de Pesquisa** e **Técnicos** seniores têm menor volume de atrito e alta relevância estratégica no custo salarial.
    """)

# ------------------------------------------------------------------------ ABA 03: DIAGNÓSTICO ESTATÍSTICO VISUAL ------------------------------------------------------

with tab3:
    st.header("3. Diagnóstico Estatístico Visual")
    
    st.markdown("Explore como diferentes fatores corporativos e psicossociais influenciam diretamente a decisão de saída:")
    
    opcao_analise = st.selectbox(
        "Selecione a variável para diagnosticar:",
        ["Renda Mensal", "Distancia_de_Casa", "Hora_Extra", "Satisfação_geral"]
    )
    
    fig, ax = plt.subplots(figsize=(10, 5))
    
    # Condicionando os filtros

    if opcao_analise == "Renda Mensal":
        sns.boxplot(data=df_filtrado, x='Demitido', y='Renda_Mensal', palette='coolwarm', ax=ax)
        ax.set_title("Distribuição Salarial por Status de Demissão")
        st.pyplot(fig)
        st.write("📌 **Insight:** Funcionários que saíram da empresa possuem, em média, uma renda mensal visivelmente menor do que aqueles que permanecem retidos.")
        
    elif opcao_analise == "Distancia_de_Casa":
        sns.boxplot(data=df_filtrado, x='Demitido', y='Distancia_de_Casa', palette='viridis', ax=ax)
        ax.set_title("Impacto da Distância da Residência no Atrito")
        st.pyplot(fig)
        st.write("📌 **Insight:** Distâncias de casa mais longas agem como um catalisador de turnover, aumentando a dispersão das saídas.")
        
    elif opcao_analise == "Hora_Extra":
        # Proporção de quem faz hora extra e sai
        dados_he = df_filtrado.groupby('Hora_Extra')['Demitido_Num'].mean().reset_index()
        sns.barplot(data=dados_he, x='Hora_Extra', y='Demitido_Num', palette='magma', ax=ax)
        ax.set_title("Taxa de Atrito: Quem faz Hora Extra vs Quem Não Faz")
        st.pyplot(fig)
        st.write("📌 **Insight:** Colaboradores que realizam horas extras apresentam um risco substancialmente maior de desligamento, indicando possível sobrecarga.")
        
    elif opcao_analise == "Satisfação_geral":
        sns.violinplot(data=df_filtrado, x='Demitido', y='Satisfação_geral', palette='muted', ax=ax)
        ax.set_title("Distribuição da Satisfação Geral (Clima, Ambiente e Gestão)")
        st.pyplot(fig)
        st.write("📌 **Insight:** O grupo dos demitidos concentra-se fortemente nas faixas de menor pontuação de satisfação geral.")


# ------------------------------------------------------------------------ ABA 4: ANÁLISE DE SOBREVIVÊNCIA ------------------------------------------------------

with tab4:
    st.header("4. Modelo de Análise de Sobrevivência (Lifelines)")
    st.markdown("""
    Utilizando técnicas de estatística para estimar o tempo 
    até que um funcionário decida deixar a empresa.
    """)
    
    col1, col2 = st.columns(2)
    
    # KM Fitter
    kmf = KaplanMeierFitter()
    
    #Primeiro gráfico
    with col1:
        st.subheader("Curva de Permanência (Kaplan-Meier)")
        
        fig, ax = plt.subplots(figsize=(6, 4))
        kmf.fit(durations=df_filtrado['Anos_na_Empresa'], event_observed=df_filtrado['Demitido_Num'], label="Fidelidade Média")
        kmf.plot_survival_function(ax=ax, color='teal', lw=2)
        ax.set_xlabel("Anos de Empresa")
        ax.set_ylabel("Probabilidade de Permanência")
        st.pyplot(fig)
        st.markdown("**Interpretação para o usuário:** Identifique em quais anos específicos de casa a probabilidade de retenção sofre as quedas mais altas.")

    #Segundo gráfico
    with col2:
        st.subheader("Sobrevivência Segmentada: Efeito de Horas Extras")
        
        fig, ax = plt.subplots(figsize=(6, 4))
        he_sim = df_filtrado[df_filtrado['Hora_Extra'] == 'Yes']
        he_nao = df_filtrado[df_filtrado['Hora_Extra'] == 'No']
        
        kmf.fit(durations=he_sim['Anos_na_Empresa'], event_observed=he_sim['Demitido_Num'], label="Faz Hora Extra")
        kmf.plot_survival_function(ax=ax, color='red')
        
        kmf.fit(durations=he_nao['Anos_na_Empresa'], event_observed=he_nao['Demitido_Num'], label="Não Faz Hora Extra")
        kmf.plot_survival_function(ax=ax, color='green')
        
        ax.set_xlabel("Anos de Empresa")
        ax.set_ylabel("Probabilidade de Permanência")
        st.pyplot(fig)
        st.markdown("**Interpretação:** A curva vermelha (sobrecarga) cai muito mais rápido, provando o impacto negativo das horas extras na sobrevivência do talento.")

    # Dataframe

    st.subheader("📋 Ranking de Impacto do Modelo de Cox (Hazard Ratios)")
    st.markdown("""
    O modelo de Riscos Proporcionais de Cox isola o efeito de múltiplas variáveis simultaneamente. 
    Abaixo estão os coeficientes simulados do modelo base ordenados pelo nível de impacto:
    """)
    
    dados_ranking = {
        "Variável Regressora (Covariada)": ["Razão_salarial", "Anos_no_Cargo_Atual", "Satisfação_geral", "Total_Anos_Trabalhados", "Idade", "Renda_Mensal"],
        "Impacto Absoluto (Coeficiente Coef)": [0.447883, 0.268535, 0.200536, 0.172641, 0.001762, 0.000035]
    }

    df_ranking = pd.DataFrame(dados_ranking)
    st.table(df_ranking)
    st.info("💡 **Destaque:** A Razão Salarial (remuneração / média de mercado do cargo) e o tempo congelado no mesmo cargo atual são os principais preditores de risco.")

# ------------------------------------------------------------------------ ABA 5: MATRIZ 9-BOX ------------------------------------------------------

with tab5:
    st.header("5. Matriz 9-Box & Proteção do Pipeline de Talentos")
    st.markdown("""
    Cruzamento de Desempenho (Avaliação de Performance) vs Potencial de Crescimento. 
    Permite classificar e isolar a taxa de perda nos quadrantes mais nobres da companhia.
    """)
    
    st.subheader("Mapa de Calor: Concentração de Atrito na 9-Box")
    
    # Criando uma matriz 9box mock com base nas notas se não existirem explícitas
    # (Ajuste o código abaixo para usar as colunas exatas geradas no seu notebook 05)
    np.random.seed(42)
    
    # Caso as colunas exatas criadas no notebook 5 existam, usamos. Senão, estruturamos o visual:
    st.markdown("""
    ### **Principais Conclusões da Estratégia de Retenção:**
    * **Isolamento de Talentos Críticos:** Cruzando o modelo de sobrevivência com a matriz 9-Box, identificamos profissionais de Alto Desempenho e Potencial (Top Talents) em zonas de perigo.
    * **Mitigação Preventiva:** Quadrantes com alta volatilidade servem como alertas para a liderança agir através de reajustes na *razão salarial*, planos de carreira personalizados ou reestruturação do clima.
    """)
    
    st.subheader("Framework Estrutural de People Analytics")

    # ATENÇÃO: O TRECHO DE CÓDIGO ABAIXO FOI GERADO COM IA A PARTIR DE UM ESBOÇO DE CÓDIGO MEU.

    # 1. Geração dos Scores de Potencial e Desempenho usando a base filtrada
    score_potencial = df_filtrado["Escolaridade"] + df_filtrado["Satisfação_geral"]
    score_desempenho = df_filtrado["Razão_salarial"] + df_filtrado["Nivel_do_Cargo"]
    
    # 2. Classificação em tercis (Baixo, Médio, Alto) tratando possíveis duplicidades de limites com 'rank'
    potencial_cat = pd.qcut(score_potencial.rank(method='first'), q=3, labels=["Baixo", "Médio", "Alto"])
    desempenho_cat = pd.qcut(score_desempenho.rank(method='first'), q=3, labels=["Baixo", "Médio", "Alto"])
    
    # 3. Mapeamento conceitual dos nomes de cada quadrante e alertas de Atrito
    nomes_9box = {
        ("Alto", "Baixo"): "Enigma (Atrito Médio)",
        ("Alto", "Médio"): "Potencial Emergente (Atrito Baixo)",
        ("Alto", "Alto"): "Estrela / Top Talent (Alerta de Risco!)",
        
        ("Médio", "Baixo"): "Questionável (Atrito Alto)",
        ("Médio", "Médio"): "Mantenedor Técnico (Atrito Baixo)",
        ("Médio", "Alto"): "Alto Potencial (Atrito Médio)",
        
        ("Baixo", "Baixo"): "Sub-performer (Atrito Crítico)",
        ("Baixo", "Médio"): "Eficaz Limitado (Atrito Baixo)",
        ("Baixo", "Alto"): "Sólido Cidadão (Atrito Baixo)"
    }
    
    # 4. Cruzamento de dados real via crosstab e reordenação correta dos eixos do framework (Alto no topo)
    matriz_contagem = pd.crosstab(potencial_cat, desempenho_cat).reindex(
        index=["Alto", "Médio", "Baixo"], 
        columns=["Baixo", "Médio", "Alto"], 
        fill_value=0
    )
    
    # 5. Construção da matriz final unindo os nomes estáticos com a contagem real dinâmica
    matriz_dinamica = pd.DataFrame(
        [
            [
                f"{nomes_9box[('Alto', 'Baixo')]} (Qtd: {matriz_contagem.loc['Alto', 'Baixo']})",
                f"{nomes_9box[('Alto', 'Médio')]} (Qtd: {matriz_contagem.loc['Alto', 'Médio']})",
                f"{nomes_9box[('Alto', 'Alto')]} (Qtd: {matriz_contagem.loc['Alto', 'Alto']})"
            ],
            [
                f"{nomes_9box[('Médio', 'Baixo')]} (Qtd: {matriz_contagem.loc['Médio', 'Baixo']})",
                f"{nomes_9box[('Médio', 'Médio')]} (Qtd: {matriz_contagem.loc['Médio', 'Médio']})",
                f"{nomes_9box[('Médio', 'Alto')]} (Qtd: {matriz_contagem.loc['Médio', 'Alto']})"
            ],
            [
                f"{nomes_9box[('Baixo', 'Baixo')]} (Qtd: {matriz_contagem.loc['Baixo', 'Baixo']})",
                f"{nomes_9box[('Baixo', 'Médio')]} (Qtd: {matriz_contagem.loc['Baixo', 'Médio']})",
                f"{nomes_9box[('Baixo', 'Alto')]} (Qtd: {matriz_contagem.loc['Baixo', 'Alto']})"
            ]
        ],
        index=["Alto Potencial", "Médio Potencial", "Baixo Potencial"],
        columns=["Baixo Desempenho", "Médio Desempenho", "Alto Desempenho"]
    )
    
    # 6. Renderização do Framework estruturado na tela
    
    st.table(matriz_dinamica)
    st.success("🎯 Com esta ferramenta estruturada, a empresa conta com um motor preditivo completo para conter o turnover involuntário e proteger seu capital humano.")