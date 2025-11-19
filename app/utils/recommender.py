"""
Módulo para sistema de recomendação de profissões
"""

import pandas as pd
import numpy as np
import joblib
from pathlib import Path
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.neighbors import NearestNeighbors

def get_model_path():
    """Retorna o caminho para o diretório de modelos"""
    return Path(__file__).parent.parent / 'model'

def load_model():
    """
    Carrega o modelo treinado
    
    Returns:
        object: Modelo carregado
    """
    model_path = get_model_path()
    try:
        model = joblib.load(model_path / 'model.pkl')
        return model
    except FileNotFoundError:
        print("Modelo não encontrado. Execute o notebook primeiro.")
        return None

def load_preprocessor():
    """
    Carrega o pré-processador
    
    Returns:
        object: Pré-processador carregado
    """
    model_path = get_model_path()
    try:
        preprocessor = joblib.load(model_path / 'preprocessor.pkl')
        return preprocessor
    except FileNotFoundError:
        print("Pré-processador não encontrado. Execute o notebook primeiro.")
        return None

def create_user_skills_vector(selected_skills, all_skills):
    """
    Cria vetor de habilidades do usuário
    
    Args:
        selected_skills (list): Lista de habilidades selecionadas pelo usuário
        all_skills (list): Lista de todas as habilidades disponíveis
        
    Returns:
        np.array: Vetor binário de habilidades
    """
    skills_vector = np.zeros(len(all_skills))
    
    for skill in selected_skills:
        if skill in all_skills:
            idx = all_skills.index(skill)
            skills_vector[idx] = 1
    
    return skills_vector

def calculate_similarity(user_vector, occupation_matrix):
    """
    Calcula similaridade entre vetor do usuário e ocupações
    
    Args:
        user_vector (np.array): Vetor de habilidades do usuário
        occupation_matrix (pd.DataFrame): Matriz de ocupações x habilidades
        
    Returns:
        pd.Series: Série com scores de similaridade por ocupação
    """
    # Reshape para 2D se necessário
    if len(user_vector.shape) == 1:
        user_vector = user_vector.reshape(1, -1)
    
    # Calcula similaridade do cosseno
    similarities = cosine_similarity(user_vector, occupation_matrix.values)
    
    # Cria série com índices das ocupações
    similarity_scores = pd.Series(
        similarities[0], 
        index=occupation_matrix.index
    )
    
    return similarity_scores

def get_recommendations(selected_skills, occupation_skills_matrix, occupations_df, top_n=10):
    """
    Obtém recomendações de profissões baseadas nas habilidades do usuário
    
    Args:
        selected_skills (list): Lista de habilidades selecionadas
        occupation_skills_matrix (pd.DataFrame): Matriz ocupações x habilidades
        occupations_df (pd.DataFrame): DataFrame com informações das ocupações
        top_n (int): Número de recomendações a retornar
        
    Returns:
        pd.DataFrame: DataFrame com as top_n recomendações
    """
    if occupation_skills_matrix.empty or occupations_df.empty:
        return pd.DataFrame()
    
    # Obtém lista de todas as habilidades
    all_skills = occupation_skills_matrix.columns.tolist()
    
    # Cria vetor de habilidades do usuário
    user_vector = create_user_skills_vector(selected_skills, all_skills)
    
    # Calcula similaridade
    similarity_scores = calculate_similarity(user_vector, occupation_skills_matrix)
    
    # Ordena por similaridade
    top_occupations = similarity_scores.nlargest(top_n)
    
    # Prepara DataFrame de resultados
    recommendations = []
    for occupation_code, similarity in top_occupations.items():
        occupation_info = occupations_df[
            occupations_df['occupation_code'] == occupation_code
        ]
        
        if not occupation_info.empty:
            occupation_data = occupation_info.iloc[0].to_dict()
            occupation_data['similarity_score'] = similarity * 100  # Converte para porcentagem
            recommendations.append(occupation_data)
    
    return pd.DataFrame(recommendations)

def filter_future_jobs(recommendations_df, growth_threshold=5):
    """
    Filtra profissões com alto crescimento projetado
    
    Args:
        recommendations_df (pd.DataFrame): DataFrame com recomendações
        growth_threshold (float): Threshold mínimo de crescimento (%)
        
    Returns:
        pd.DataFrame: DataFrame filtrado
    """
    if 'projected_growth' in recommendations_df.columns:
        return recommendations_df[
            recommendations_df['projected_growth'] >= growth_threshold
        ]
    return recommendations_df

def calculate_match_percentage(user_skills, occupation_skills):
    """
    Calcula porcentagem de match entre habilidades do usuário e ocupação
    
    Args:
        user_skills (set): Set de habilidades do usuário
        occupation_skills (set): Set de habilidades da ocupação
        
    Returns:
        float: Porcentagem de match
    """
    if not occupation_skills:
        return 0.0
    
    intersection = len(user_skills.intersection(occupation_skills))
    union = len(occupation_skills)
    
    return (intersection / union) * 100

