"""
Módulo para carregar e processar dados do O*NET e BLS
"""

import pandas as pd
import numpy as np
import os
from pathlib import Path

def get_data_path():
    """Retorna o caminho para o diretório de dados"""
    return Path(__file__).parent.parent.parent / 'data'

def load_occupations_data():
    """
    Carrega dados de ocupações processados
    
    Returns:
        pd.DataFrame: DataFrame com informações de ocupações
    """
    data_path = get_data_path()
    try:
        df = pd.read_csv(data_path / 'occupations_processed.csv')
        return df
    except FileNotFoundError:
        print("Arquivo de ocupações não encontrado. Execute o notebook primeiro.")
        return pd.DataFrame()

def load_skills_data():
    """
    Carrega dados de habilidades processados
    
    Returns:
        pd.DataFrame: DataFrame com informações de habilidades
    """
    data_path = get_data_path()
    try:
        df = pd.read_csv(data_path / 'skills_processed.csv')
        return df
    except FileNotFoundError:
        print("Arquivo de habilidades não encontrado. Execute o notebook primeiro.")
        return pd.DataFrame()

def load_occupation_skills_matrix():
    """
    Carrega matriz de habilidades por ocupação
    
    Returns:
        pd.DataFrame: Matriz com ocupações x habilidades
    """
    data_path = get_data_path()
    try:
        df = pd.read_csv(data_path / 'occupation_skills_matrix.csv', index_col=0)
        return df
    except FileNotFoundError:
        print("Matriz de habilidades não encontrada. Execute o notebook primeiro.")
        return pd.DataFrame()

def get_all_skills():
    """
    Retorna lista de todas as habilidades disponíveis
    
    Returns:
        list: Lista de habilidades
    """
    skills_df = load_skills_data()
    if not skills_df.empty:
        return sorted(skills_df['skill_name'].unique().tolist())
    return []

def get_occupation_details(occupation_code):
    """
    Obtém detalhes de uma ocupação específica
    
    Args:
        occupation_code (str): Código da ocupação
        
    Returns:
        dict: Dicionário com detalhes da ocupação
    """
    occupations_df = load_occupations_data()
    
    if occupations_df.empty:
        return {}
    
    occupation = occupations_df[occupations_df['occupation_code'] == occupation_code]
    
    if occupation.empty:
        return {}
    
    return occupation.iloc[0].to_dict()

def get_skills_for_occupation(occupation_code):
    """
    Retorna as habilidades necessárias para uma ocupação
    
    Args:
        occupation_code (str): Código da ocupação
        
    Returns:
        list: Lista de tuplas (habilidade, nível)
    """
    skills_df = load_skills_data()
    
    if skills_df.empty:
        return []
    
    occupation_skills = skills_df[skills_df['occupation_code'] == occupation_code]
    
    skills_list = []
    for _, row in occupation_skills.iterrows():
        skills_list.append({
            'skill': row['skill_name'],
            'level': row.get('level', 0),
            'importance': row.get('importance', 0)
        })
    
    return sorted(skills_list, key=lambda x: x.get('importance', 0), reverse=True)

