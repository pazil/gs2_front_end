"""
Sistema de Recomendação de Profissões do Futuro
FIAP Global Solution - Front End & Mobile Development
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import json
from pathlib import Path
import sys

# Adicionar path para importar módulos utils
sys.path.append(str(Path(__file__).parent))

from utils.data_loader import (
    load_occupations_data,
    load_skills_data,
    load_occupation_skills_matrix,
    get_all_skills,
    get_skills_for_occupation
)
from utils.recommender import get_recommendations

# ============================================================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================================================

st.set_page_config(
    page_title="Profissões do Futuro",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS customizado
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #1f77b4;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.5rem;
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
    }
    .future-job-badge {
        background-color: #28a745;
        color: white;
        padding: 0.25rem 0.75rem;
        border-radius: 15px;
        font-weight: bold;
        font-size: 0.85rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #1f77b4;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 0.75rem;
    }
    .stButton>button:hover {
        background-color: #145a8d;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# FUNÇÕES AUXILIARES
# ============================================================================

@st.cache_data
def load_all_data():
    """Carrega todos os dados necessários"""
    occupations = load_occupations_data()
    skills = load_skills_data()
    skills_matrix = load_occupation_skills_matrix()
    all_skills = get_all_skills()
    
    return occupations, skills, skills_matrix, all_skills

def display_occupation_card(occ_data, similarity_score=None):
    """Exibe card com informações da ocupação"""
    with st.container():
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.markdown(f"### {occ_data['occupation_title']}")
            if 'description' in occ_data:
                st.write(occ_data['description'])
        
        with col2:
            if similarity_score:
                st.metric("Match", f"{similarity_score:.1f}%")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Salário Anual", f"${occ_data['median_salary']:,.0f}")
        
        with col2:
            growth = occ_data['projected_growth']
            st.metric("Crescimento", f"{growth:.1f}%", 
                     delta=f"{growth - 15:.1f}%" if growth > 15 else None)
        
        with col3:
            if 'num_jobs_2024' in occ_data:
                st.metric("Vagas 2024", f"{occ_data['num_jobs_2024']:,.0f}")
        
        with col4:
            if occ_data.get('is_future_job', False):
                st.markdown('<span class="future-job-badge">Profissão do Futuro</span>', 
                           unsafe_allow_html=True)
        
        # Habilidades necessárias
        if st.checkbox(f"Ver habilidades - {occ_data['occupation_code']}", key=f"skills_{occ_data['occupation_code']}"):
            skills_info = get_skills_for_occupation(occ_data['occupation_code'])
            if skills_info:
                st.write("**Principais habilidades:**")
                skills_list = [s['skill'] for s in skills_info[:10]]
                st.write(", ".join(skills_list))
        
        st.markdown("---")

def create_radar_chart(user_skills, occ_skills, occ_title):
    """Cria gráfico radar comparando habilidades"""
    # Selecionar até 8 habilidades para o radar
    all_relevant_skills = list(set(user_skills + occ_skills))[:8]
    
    user_values = [1 if skill in user_skills else 0 for skill in all_relevant_skills]
    occ_values = [1 if skill in occ_skills else 0 for skill in all_relevant_skills]
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=user_values,
        theta=all_relevant_skills,
        fill='toself',
        name='Suas Habilidades'
    ))
    
    fig.add_trace(go.Scatterpolar(
        r=occ_values,
        theta=all_relevant_skills,
        fill='toself',
        name=occ_title[:30]
    ))
    
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 1])),
        showlegend=True,
        height=400
    )
    
    return fig

# ============================================================================
# INTERFACE PRINCIPAL
# ============================================================================

def main():
    # Carregar dados
    try:
        occupations_df, skills_df, skills_matrix, all_skills_list = load_all_data()
        
        # Verificar se os dados foram carregados
        if occupations_df.empty:
            st.error("ATENÇÃO: Dados não encontrados! Execute o notebook primeiro para gerar os dados.")
            st.info("Execute: jupyter notebook notebook/analise_modelagem.ipynb")
            st.stop()
            
    except Exception as e:
        st.error(f"Erro ao carregar dados: {e}")
        st.info("Execute o notebook primeiro para gerar os dados necessários.")
        st.stop()
    
    # ========================================================================
    # SIDEBAR - Navegação
    # ========================================================================
    
    st.sidebar.markdown("### FIAP Global Solution")
    st.sidebar.markdown("---")
    
    st.sidebar.title("Navegação")
    page = st.sidebar.radio("Escolha uma página:", 
                            ["Início", "Recomendações", "Explorar Dados", "Sobre"])
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### Integrantes")
    st.sidebar.markdown("""
    - PAULO CARVALHO RUIZ BORBA - RM: 554562
    - LORENA BAUER NOGUEIRA - RM: 555272
    - HERBERT DI FRANCO MARQUES - RM: 556640
    """)
    
    # ========================================================================
    # PÁGINA: INÍCIO
    # ========================================================================
    
    if page == "Início":
        st.markdown('<h1 class="main-header">Profissões do Futuro</h1>', unsafe_allow_html=True)
        st.markdown('<p class="sub-header">Descubra carreiras alinhadas às suas habilidades</p>', 
                   unsafe_allow_html=True)
        
        # Banner de destaque
        st.markdown("---")
        st.info("""
        **Bem-vindo ao Sistema de Recomendação de Profissões do Futuro!**
        
        Este sistema utiliza Machine Learning para recomendar carreiras do futuro baseadas nas suas habilidades atuais.
        Explore as funcionalidades através do menu lateral e descubra oportunidades de carreira alinhadas ao seu perfil.
        """)
        st.markdown("---")
        
        # Estatísticas gerais
        st.markdown("## Panorama do Mercado")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Profissões Analisadas", f"{len(occupations_df)}")
        
        with col2:
            future_jobs = occupations_df[occupations_df['is_future_job']].shape[0]
            st.metric("Profissões do Futuro", f"{future_jobs}")
        
        with col3:
            avg_growth = occupations_df['projected_growth'].mean()
            st.metric("Crescimento Médio", f"{avg_growth:.1f}%")
        
        with col4:
            avg_salary = occupations_df['median_salary'].mean()
            st.metric("Salário Médio", f"${avg_salary:,.0f}/ano")
        
        st.markdown("---")
        
        # Como funciona
        st.markdown("## Como Funciona")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("### 1. Selecione")
            st.write("Escolha suas habilidades atuais em nossa lista completa")
        
        with col2:
            st.markdown("### 2. Analise")
            st.write("Nosso algoritmo encontra profissões compatíveis")
        
        with col3:
            st.markdown("### 3. Decida")
            st.write("Explore recomendações e planeje sua carreira")
        
        st.markdown("---")
        
        # Call to action
        st.info("Use o menu lateral para começar sua jornada!")
    
    # ========================================================================
    # PÁGINA: RECOMENDAÇÕES
    # ========================================================================
    
    elif page == "Recomendações":
        st.title("Sistema de Recomendações")
        st.write("Selecione suas habilidades atuais e descubra as profissões do futuro mais adequadas para você!")
        st.info("**Nota**: Os salários apresentados são valores anuais em dólares americanos (USD), baseados em dados do Bureau of Labor Statistics.")
        
        # Seleção de habilidades
        st.markdown("### Suas Habilidades")
        st.write("Selecione as habilidades que você possui marcando as caixas abaixo:")
        
        # Categorizar habilidades
        tech_skills = ['Programming', 'Data Analysis', 'Machine Learning', 'Cloud Computing', 
                      'Cybersecurity', 'Web Development', 'Mobile Development', 'AI/Deep Learning',
                      'Database Management', 'DevOps', 'Data Visualization', 'Statistical Analysis']
        business_skills = ['Leadership', 'Project Management', 'Business Analysis', 
                         'Marketing', 'Sales', 'HR Management', 'Financial Analysis']
        soft_skills = ['Communication', 'Problem Solving', 'Critical Thinking', 'Creativity', 
                      'Teamwork', 'Adaptability', 'Time Management']
        other_skills = ['Research', 'Technical Writing', 'Design', 'Healthcare Knowledge',
                       'Customer Service', 'Renewable Energy', 'Sustainability']
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown("**💻 Técnicas**")
            tech_selected = [skill for skill in tech_skills if st.checkbox(skill, key=f"tech_{skill}")]
        
        with col2:
            st.markdown("**💼 Negócios**")
            biz_selected = [skill for skill in business_skills if st.checkbox(skill, key=f"biz_{skill}")]
        
        with col3:
            st.markdown("**🤝 Soft Skills**")
            soft_selected = [skill for skill in soft_skills if st.checkbox(skill, key=f"soft_{skill}")]
        
        with col4:
            st.markdown("**🔧 Outras**")
            other_selected = [skill for skill in other_skills if st.checkbox(skill, key=f"other_{skill}")]
        
        selected_skills = tech_selected + biz_selected + soft_selected + other_selected
        
        # Mostrar habilidades selecionadas
        if selected_skills:
            st.success(f"{len(selected_skills)} habilidades selecionadas: {', '.join(selected_skills)}")
        else:
            st.warning("Selecione pelo menos uma habilidade para obter recomendações")
        
        # Configurações avançadas
        with st.expander("Configurações Avançadas"):
            num_recommendations = st.slider("Número de recomendações:", 5, 20, 10)
            filter_future_only = st.checkbox("Mostrar apenas profissões do futuro (crescimento > 15%)")
            min_salary = st.slider("Salário mínimo anual (USD):", 0, 200000, 0, 10000)
        
        # Botão de recomendação
        if st.button("Obter Recomendações", type="primary"):
            if not selected_skills:
                st.error("Por favor, selecione pelo menos uma habilidade!")
            else:
                with st.spinner("Analisando e gerando recomendações..."):
                    # Obter recomendações
                    recommendations = get_recommendations(
                        selected_skills, 
                        skills_matrix, 
                        occupations_df,
                        top_n=num_recommendations
                    )
                    
                    # Aplicar filtros
                    if filter_future_only:
                        recommendations = recommendations[recommendations['is_future_job']]
                    
                    if min_salary > 0:
                        recommendations = recommendations[recommendations['median_salary'] >= min_salary]
                    
                    if recommendations.empty:
                        st.warning("Nenhuma profissão encontrada com os filtros aplicados. Tente ajustar os critérios.")
                    else:
                        st.success(f"Encontradas {len(recommendations)} recomendações!")
                        
                        # Visualização geral
                        st.markdown("### Visão Geral das Recomendações")
                        
                        # Gráfico de scores
                        fig = px.bar(
                            recommendations.head(10),
                            x='similarity_score',
                            y='occupation_title',
                            orientation='h',
                            title='Top 10 Profissões por Compatibilidade',
                            labels={'similarity_score': 'Score de Compatibilidade (%)', 
                                   'occupation_title': 'Profissão',
                                   'median_salary': 'Salário Anual (USD)'},
                            color='projected_growth',
                            color_continuous_scale='RdYlGn',
                            hover_data=['median_salary']
                        )
                        fig.update_layout(height=500, yaxis={'categoryorder':'total ascending'})
                        st.plotly_chart(fig, use_container_width=True)
                        
                        # Scatter plot: Salário vs Crescimento
                        fig2 = px.scatter(
                            recommendations,
                            x='median_salary',
                            y='projected_growth',
                            size='similarity_score',
                            color='similarity_score',
                            hover_data=['occupation_title'],
                            title='Oportunidades: Salário Anual vs Crescimento',
                            labels={
                                'median_salary': 'Salário Anual (USD)',
                                'projected_growth': 'Crescimento Projetado (%)',
                                'similarity_score': 'Compatibilidade (%)'
                            },
                            color_continuous_scale='Viridis'
                        )
                        fig2.update_layout(height=500)
                        st.plotly_chart(fig2, use_container_width=True)
                        
                        st.markdown("---")
                        st.markdown("### Detalhes das Recomendações")
                        
                        # Exibir cards de recomendações
                        for idx, row in recommendations.iterrows():
                            display_occupation_card(row, similarity_score=row['similarity_score'])
                        
                        # Opção de download
                        st.markdown("---")
                        csv = recommendations.to_csv(index=False)
                        st.download_button(
                            label="Baixar Recomendações (CSV)",
                            data=csv,
                            file_name="recomendacoes_profissoes.csv",
                            mime="text/csv"
                        )
    
    # ========================================================================
    # PÁGINA: EXPLORAR DADOS
    # ========================================================================
    
    elif page == "Explorar Dados":
        st.title("Explorar Profissões")
        st.info("**Nota**: Os salários são valores anuais em dólares americanos (USD).")
        
        # Filtros
        st.sidebar.markdown("### Filtros")
        
        # Filtro por crescimento
        min_growth = st.sidebar.slider("Crescimento mínimo (%):", 0, 50, 0)
        
        # Filtro por salário
        salary_range = st.sidebar.slider(
            "Faixa de salário anual (USD):",
            int(occupations_df['median_salary'].min()),
            int(occupations_df['median_salary'].max()),
            (int(occupations_df['median_salary'].min()), int(occupations_df['median_salary'].max()))
        )
        
        # Filtro de profissões do futuro
        only_future = st.sidebar.checkbox("Apenas profissões do futuro")
        
        # Aplicar filtros
        filtered_df = occupations_df.copy()
        filtered_df = filtered_df[filtered_df['projected_growth'] >= min_growth]
        filtered_df = filtered_df[
            (filtered_df['median_salary'] >= salary_range[0]) & 
            (filtered_df['median_salary'] <= salary_range[1])
        ]
        
        if only_future:
            filtered_df = filtered_df[filtered_df['is_future_job']]
        
        st.info(f"Exibindo {len(filtered_df)} de {len(occupations_df)} profissões")
        
        # Tabs para diferentes visualizações
        tab1, tab2, tab3 = st.tabs(["Lista", "Gráficos", "Habilidades"])
        
        with tab1:
            # Tabela interativa
            st.dataframe(
                filtered_df[['occupation_title', 'median_salary', 'projected_growth', 
                            'is_future_job']].sort_values('projected_growth', ascending=False),
                use_container_width=True,
                hide_index=True
            )
        
        with tab2:
            # Gráficos
            col1, col2 = st.columns(2)
            
            with col1:
                # Top 10 por salário
                fig1 = px.bar(
                    filtered_df.nlargest(10, 'median_salary'),
                    x='median_salary',
                    y='occupation_title',
                    orientation='h',
                    title='Top 10 por Salário Anual',
                    labels={'median_salary': 'Salário Anual (USD)'},
                    color='median_salary',
                    color_continuous_scale='Blues'
                )
                fig1.update_layout(showlegend=False, height=400)
                st.plotly_chart(fig1, use_container_width=True)
            
            with col2:
                # Top 10 por crescimento
                fig2 = px.bar(
                    filtered_df.nlargest(10, 'projected_growth'),
                    x='projected_growth',
                    y='occupation_title',
                    orientation='h',
                    title='Top 10 por Crescimento',
                    color='projected_growth',
                    color_continuous_scale='Greens'
                )
                fig2.update_layout(showlegend=False, height=400)
                st.plotly_chart(fig2, use_container_width=True)
            
            # Distribuição
            fig3 = px.histogram(
                filtered_df,
                x='median_salary',
                nbins=20,
                title='Distribuição de Salários Anuais',
                labels={'median_salary': 'Salário Anual (USD)'}
            )
            st.plotly_chart(fig3, use_container_width=True)
        
        with tab3:
            # Análise de habilidades
            st.markdown("### Habilidades Mais Demandadas")
            
            skill_counts = skills_df['skill_name'].value_counts().head(20)
            
            fig = px.bar(
                x=skill_counts.values,
                y=skill_counts.index,
                orientation='h',
                title='Top 20 Habilidades',
                labels={'x': 'Número de Profissões', 'y': 'Habilidade'}
            )
            fig.update_layout(height=600)
            st.plotly_chart(fig, use_container_width=True)
    
    # ========================================================================
    # PÁGINA: SOBRE
    # ========================================================================
    
    elif page == "Sobre":
        st.title("Sobre o Projeto")
        
        st.markdown("""
        ## Objetivo
        
        Este projeto foi desenvolvido como parte da **FIAP Global Solution - Front End & Mobile Development** 
        com o objetivo de auxiliar profissionais a identificarem carreiras do futuro alinhadas às suas 
        habilidades atuais.
        
        ## Como Funciona
        
        O sistema utiliza **Machine Learning** (algoritmo K-Nearest Neighbors com similaridade do cosseno) 
        para recomendar profissões baseadas em:
        
        - **Habilidades do usuário**: Selecionadas através da interface
        - **Dados de mercado**: Projeções de crescimento e salários
        - **Análise de compatibilidade**: Match entre habilidades atuais e requisitos futuros
        
        ## Fontes de Dados
        
        - **O*NET Database**: Ocupações, habilidades e conhecimentos
        - **Bureau of Labor Statistics (BLS)**: Projeções de emprego e salários
        
        ## Tecnologias Utilizadas
        
        - **Python**: Linguagem principal
        - **Streamlit**: Framework web
        - **Scikit-learn**: Machine Learning
        - **Plotly**: Visualizações interativas
        - **Pandas & NumPy**: Análise de dados
        
        ## Equipe
        
        - PAULO CARVALHO RUIZ BORBA - RM: 554562
        - LORENA BAUER NOGUEIRA - RM: 555272
        - HERBERT DI FRANCO MARQUES - RM: 556640
        
        ## Metodologia
        
        ### 1. Coleta e Preparação de Dados
        - Download e limpeza de dados do O*NET e BLS
        - Feature engineering e normalização
        
        ### 2. Análise Exploratória (EDA)
        - Análise de distribuições
        - Identificação de padrões
        - Visualizações interativas
        
        ### 3. Modelagem
        - Sistema de recomendação baseado em similaridade
        - Validação e otimização
        - Métricas de performance
        
        ## Resultados
        
        O modelo alcançou uma taxa de recomendação de profissões do futuro significativamente 
        superior ao baseline aleatório, demonstrando eficácia na identificação de oportunidades 
        de carreira alinhadas ao perfil do usuário.
        
        ---
        
        ### Contato
        
        Para mais informações, entre em contato através do portal FIAP.
        
        ### Links
        
        - [Repositório GitHub](#)
        - [Documentação Completa](#)
        """)
        
        st.info("**Dica**: Use o menu lateral para explorar as funcionalidades do sistema!")

# ============================================================================
# EXECUÇÃO
# ============================================================================

if __name__ == "__main__":
    main()

