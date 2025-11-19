# 🚀 Sistema de Recomendação de Profissões do Futuro

## FIAP Global Solution - Front End & Mobile Development

Sistema inteligente que recomenda profissões do futuro baseado nas habilidades atuais do usuário, utilizando Machine Learning e dados do O*NET e Bureau of Labor Statistics.

## 👥 Integrantes do Grupo

- PAULO CARVALHO RUIZ BORBA - RM: 554562
- LORENA BAUER NOGUEIRA - RM: 555272
- HERBERT DI FRANCO MARQUES - RM: 556640

## 📋 Sobre o Projeto

### Motivação

Com as rápidas transformações no mercado de trabalho impulsionadas pela automação, inteligência artificial e novas tecnologias, profissionais enfrentam o desafio de adaptar suas habilidades para permanecerem relevantes. Este projeto visa auxiliar pessoas a identificarem profissões do futuro alinhadas às suas competências atuais.

### Objetivo

Desenvolver um sistema de recomendação baseado em Machine Learning que:
- Analise as habilidades atuais do usuário
- Compare com requisitos de profissões emergentes
- Recomende carreiras do futuro com maior compatibilidade
- Forneça informações sobre projeções de crescimento e requisitos

### Resultados Esperados

- Sistema de recomendação preciso e confiável
- Interface intuitiva e responsiva
- Insights sobre tendências do mercado de trabalho
- Ferramenta útil para planejamento de carreira

## 🛠️ Tecnologias Utilizadas

- **Python 3.9+**
- **Jupyter Notebook** - Análise e modelagem
- **Streamlit** - Interface web
- **Scikit-learn** - Machine Learning
- **Pandas & NumPy** - Manipulação de dados
- **Plotly & Matplotlib** - Visualizações

## 📊 Fontes de Dados

1. **O*NET Database** - Ocupações, habilidades e conhecimentos
2. **Bureau of Labor Statistics (BLS)** - Projeções de emprego e salários

## 🚀 Como Executar

### Instalação

```bash
# Clone o repositório
git clone [URL_DO_REPOSITORIO]
cd GS2-FRONT_END

# Crie um ambiente virtual
python -m venv venv

# Ative o ambiente virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt
```

### Executar o Notebook

```bash
jupyter notebook notebook/analise_modelagem.ipynb
```

### Executar o Webapp Localmente

```bash
streamlit run app/streamlit_app.py
```

O aplicativo estará disponível em: `http://localhost:8501`

## 📁 Estrutura do Projeto

```
GS2-FRONT_END/
├── notebook/
│   └── analise_modelagem.ipynb     # Análise completa e modelagem
├── app/
│   ├── streamlit_app.py            # Aplicação Streamlit
│   ├── model/                      # Modelos treinados
│   └── utils/                      # Funções auxiliares
├── data/                           # Dados processados
├── requirements.txt                # Dependências
└── README.md                       # Este arquivo
```

## 🌐 Deploy

O webapp está deployado no Streamlit Cloud:
**[Link será adicionado após deploy]**

### Instruções de Deploy

Para instruções detalhadas de como fazer o deploy, consulte:
- `INSTRUCTIONS.md` - Guia passo a passo
- `DEPLOY_CHECKLIST.md` - Checklist completo

## 📝 Metodologia

### 1. Carregamento e Limpeza de Dados
- Coleta de dados do O*NET e BLS
- Limpeza e normalização
- Feature engineering

### 2. Análise Exploratória (EDA)
- Análise de distribuição de habilidades
- Correlações e padrões
- Visualizações interativas

### 3. Modelagem
- Sistema de recomendação baseado em similaridade
- Treinamento e validação
- Avaliação de métricas

## 📄 Licença

Este projeto foi desenvolvido para fins acadêmicos como parte da Global Solution da FIAP.

## 🔗 Links

- **Repositório GitHub**: [URL_DO_REPOSITORIO]
- **Webapp Deployado**: [URL_DO_WEBAPP]
- **Documentação Completa**: Ver arquivo PDF entregue no portal FIAP

