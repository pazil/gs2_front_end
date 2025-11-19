# FIAP GLOBAL SOLUTION
## Front End & Mobile Development

---

### Sistema de Recomendação de Profissões do Futuro

**Disciplina:** Front End & Mobile Development  
**Turma:** 2TIAPY  
**Data:** Novembro/2024

---

## 👥 Integrantes do Grupo

- **PAULO CARVALHO RUIZ BORBA** - RM: 554562
- **LORENA BAUER NOGUEIRA** - RM: 555272
- **HERBERT DI FRANCO MARQUES** - RM: 556640

---

# 1. DESCRIÇÃO DO PROJETO

## 1.1 Motivação do Projeto

Com as rápidas transformações no mercado de trabalho impulsionadas pela automação, inteligência artificial e novas tecnologias, profissionais de todas as áreas enfrentam o desafio de adaptar suas habilidades para permanecerem relevantes no futuro.

Segundo estudos do World Economic Forum, até 2025, milhões de empregos podem ser deslocados por mudanças na divisão do trabalho entre humanos e máquinas, enquanto novos papéis podem emergir. Nesse contexto, torna-se essencial que profissionais tenham ferramentas para identificar quais carreiras do futuro estão alinhadas com suas competências atuais.

Este projeto surge da necessidade de democratizar o acesso a informações sobre o futuro do trabalho e auxiliar pessoas em seu planejamento de carreira, oferecendo recomendações personalizadas baseadas em dados reais e algoritmos de Machine Learning.

### Contexto do Mercado

O mercado de trabalho está passando por transformações sem precedentes:

- **Automação crescente**: Tarefas repetitivas sendo automatizadas
- **Novas profissões**: Surgimento de carreiras que não existiam há 5 anos
- **Necessidade de requalificação**: Profissionais precisam se adaptar constantemente
- **Incerteza sobre o futuro**: Dificuldade em identificar quais habilidades serão valiosas

## 1.2 Objetivo

Desenvolver um sistema inteligente de recomendação que auxilie profissionais a identificarem carreiras do futuro compatíveis com suas habilidades atuais.

### Objetivos Específicos:

1. **Analisar** as habilidades atuais do usuário através de uma interface web intuitiva
2. **Comparar** essas habilidades com requisitos de profissões emergentes
3. **Recomendar** carreiras do futuro com maior compatibilidade utilizando Machine Learning
4. **Fornecer** informações relevantes para tomada de decisão:
   - Projeções de crescimento de cada profissão (2024-2034)
   - Salários médios anuais esperados
   - Habilidades adicionais necessárias
   - Score de compatibilidade personalizado (0-100%)

### Funcionalidades Principais:

- Sistema de recomendação baseado em similaridade do cosseno
- Interface interativa com seleção de habilidades por categorias
- Visualizações gráficas para análise de oportunidades
- Filtros avançados por salário e crescimento projetado
- Download de resultados em formato CSV

## 1.3 Resultados Esperados

### Para os Usuários:

1. **Ferramenta gratuita e acessível** para planejamento de carreira
2. **Recomendações personalizadas** baseadas em dados reais do mercado americano
3. **Insights sobre tendências** do mercado de trabalho global
4. **Orientação clara** sobre habilidades a desenvolver
5. **Redução da incerteza** no planejamento de carreira

### Indicadores de Sucesso do Sistema:

- **Taxa de precisão**: 75% das recomendações são profissões do futuro (vs 70% baseline)
- **Crescimento médio**: 22.3% projetado para recomendações (vs 18.5% baseline)
- **Tempo de resposta**: Menos de 2 segundos para gerar recomendações
- **Base de conhecimento**: 20 profissões e 40+ habilidades mapeadas
- **Interface**: Sistema web acessível e responsivo

### Impacto Educacional:

1. Aplicação prática de conceitos de Machine Learning
2. Desenvolvimento de webapp completo com Streamlit
3. Deploy em ambiente de produção (Streamlit Cloud)
4. Análise exploratória de dados reais
5. Documentação técnica completa

### Diferenciais do Projeto:

- **Dados reais**: Baseado em O*NET e Bureau of Labor Statistics
- **ML embarcado**: Algoritmo de recomendação integrado ao webapp
- **Interface intuitiva**: Navegação simples e objetiva
- **Visualizações interativas**: Gráficos Plotly para análise
- **Deploy em produção**: Aplicação acessível publicamente

---

# 2. METODOLOGIA

## 2.1 Carregamento e Limpeza dos Dados

### Fontes de Dados:

1. **O*NET Database** (Occupational Information Network)
   - Base de dados oficial americana com informações detalhadas sobre ocupações
   - Inclui habilidades, conhecimentos e atividades necessárias
   - Fonte: https://www.onetcenter.org/

2. **Bureau of Labor Statistics (BLS)**
   - Projeções de crescimento de emprego (2024-2034)
   - Dados salariais médios anuais
   - Fonte: https://www.bls.gov/

### Processo de Preparação:

#### Coleta de Dados:
- **20 profissões** relevantes para o futuro do trabalho
- **40+ habilidades** técnicas e comportamentais mapeadas
- **Projeções de crescimento** para próxima década
- **Dados salariais** anuais em USD

#### Limpeza e Normalização:
- Verificação de valores ausentes (nenhum encontrado)
- Padronização de formatos
- Validação de consistência dos dados
- Tratamento de outliers

#### Feature Engineering:
- **Categorias de salário**: Baixo, Médio, Alto, Muito Alto
- **Categorias de crescimento**: Baseadas em percentuais
- **Classificação binária**: "Profissão do Futuro" (crescimento > 15%)
- **Crescimento absoluto**: Diferença de vagas entre 2024 e 2034
- **Matriz de habilidades**: Representação binária (possui/não possui)

### Dataset Final:

| Métrica | Valor |
|---------|-------|
| Profissões analisadas | 20 |
| Habilidades únicas | 40+ |
| Registros de habilidades | 140+ |
| Período de projeção | 2024-2034 (10 anos) |

## 2.2 Análise Exploratória dos Dados (EDA)

### Principais Descobertas:

#### Análise de Salários:
- **Salário médio geral**: $94,000/ano
- **Range salarial**: $38,000 - $159,000/ano
- **Profissões de TI**: Dominam o topo da lista
- **Correlação**: Moderada entre salário e especialização

#### Análise de Crescimento:
- **Crescimento médio**: 18.5% projetado
- **Maior crescimento**: Machine Learning Engineers (40.1%)
- **Profissões do futuro**: 70% das analisadas
- **Setores em alta**: Tecnologia, Saúde, Sustentabilidade

#### Habilidades Mais Demandadas:

**Top 10:**
1. Problem Solving - 18 ocupações
2. Communication - 17 ocupações
3. Critical Thinking - 15 ocupações
4. Programming - 8 ocupações
5. Data Analysis - 7 ocupações
6. Leadership - 6 ocupações
7. Teamwork - 6 ocupações
8. Project Management - 5 ocupações
9. Research - 5 ocupações
10. Adaptability - 5 ocupações

#### Correlações Importantes:
- **Salário × Crescimento**: Correlação fraca (0.15)
  - Indica que salários altos não garantem alto crescimento
  - Oportunidades existem em diferentes faixas salariais

### Visualizações Criadas:

1. **Gráficos de barras**: Top 10 profissões por salário e crescimento
2. **Scatter plots**: Relação salário × crescimento × tamanho do mercado
3. **Heatmaps**: Correlações entre variáveis
4. **Histogramas**: Distribuição de salários e crescimento
5. **Gráficos de barras**: Habilidades mais demandadas

### Insights Principais:

- Profissões de tecnologia lideram em crescimento
- Soft skills são altamente demandadas em todas as áreas
- Salário não é o único indicador de uma boa profissão do futuro
- Diversidade de oportunidades em diferentes setores

## 2.3 Modelagem (Machine Learning)

### Escolha do Algoritmo:

**K-Nearest Neighbors (KNN) com Similaridade do Cosseno**

#### Justificativa:

1. **Interpretabilidade**: Fácil explicar por que uma profissão foi recomendada
2. **Eficiência**: Rápido para bases de dados pequenas/médias (< 1 segundo)
3. **Flexibilidade**: Não requer re-treinamento ao adicionar novos usuários
4. **Adequação**: Ideal para encontrar itens similares baseado em características
5. **Simplicidade**: Implementação direta e manutenível

### Arquitetura do Sistema:

```
┌─────────────────────────────────────┐
│   Interface Streamlit               │
│   (Seleção de habilidades)          │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│   Vetor de Habilidades do Usuário   │
│   (Binário: 1 = possui, 0 = não)    │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│   Modelo KNN                        │
│   (n_neighbors=10, metric=cosine)  │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│   Cálculo de Similaridade           │
│   Similaridade = (1 - distância) ×100│
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│   Top-N Recomendações               │
│   (Ordenadas por similaridade)     │
└─────────────────────────────────────┘
```

### Implementação:

#### Preparação:
- **Features (X)**: Matriz binária de habilidades (20 × N)
- **Normalização**: StandardScaler para testes alternativos
- **Sem labels**: Sistema de recomendação não-supervisionado

#### Modelo:
```python
KNN(n_neighbors=10, metric='cosine', algorithm='brute')
```

#### Processo de Recomendação:
1. Usuário seleciona habilidades na interface
2. Sistema cria vetor binário do usuário
3. KNN calcula distâncias cosseno para todas as ocupações
4. Retorna top-N ocupações mais similares
5. Converte distância em score de similaridade (0-100%)

### Avaliação do Modelo:

#### Métricas Utilizadas:

1. **Taxa de Profissões do Futuro**
   - Percentual de recomendações que são "profissões do futuro"
   - **Resultado**: 75%
   - **Baseline**: 70% (seleção aleatória)
   - **Melhoria**: +5 pontos percentuais

2. **Crescimento Médio das Recomendações**
   - Média de crescimento projetado das profissões recomendadas
   - **Resultado**: 22.3%
   - **Baseline**: 18.5%
   - **Melhoria**: +3.8 pontos percentuais

3. **Testes de Validação**
   - 100 perfis aleatórios gerados
   - Consistência nas recomendações: Alta
   - Diversidade de resultados: Adequada

#### Conclusão da Avaliação:

O modelo demonstrou ser **eficaz** em recomendar profissões relevantes e com bom potencial de crescimento, **superando o baseline aleatório** em todas as métricas avaliadas.

### Salvamento de Artefatos:

Arquivos gerados para uso no webapp:
- `model.pkl` - Modelo KNN treinado
- `preprocessor.pkl` - StandardScaler
- `model_info.json` - Metadados do modelo

---

# 3. TECNOLOGIAS UTILIZADAS

## 3.1 Linguagem e Frameworks

| Tecnologia | Versão | Uso |
|------------|--------|-----|
| Python | 3.9+ | Linguagem principal |
| Jupyter Notebook | 7.0.6 | Análise e documentação |
| Streamlit | 1.29.0 | Interface web |

## 3.2 Bibliotecas de Data Science

| Biblioteca | Versão | Uso |
|------------|--------|-----|
| Pandas | 2.1.4 | Manipulação de dados |
| NumPy | 1.26.2 | Operações numéricas |
| Scikit-learn | 1.3.2 | Machine Learning |

## 3.3 Visualização

| Biblioteca | Versão | Uso |
|------------|--------|-----|
| Plotly | 5.18.0 | Gráficos interativos |
| Matplotlib | 3.8.2 | Visualizações estáticas |
| Seaborn | 0.13.0 | Visualizações estatísticas |

## 3.4 Outras Ferramentas

| Ferramenta | Uso |
|------------|-----|
| GitHub | Versionamento de código |
| Streamlit Cloud | Deploy e hospedagem |
| Git | Controle de versão |

---

# 4. ESTRUTURA DO PROJETO

```
gs2_front_end/
│
├── notebook/
│   └── analise_modelagem.ipynb          # Notebook completo (3 seções)
│       ├── Seção 1: Carregamento e Limpeza
│       ├── Seção 2: Análise Exploratória (EDA)
│       └── Seção 3: Modelagem (ML)
│
├── app/
│   ├── streamlit_app.py                 # Aplicação principal
│   │   ├── Página: Início
│   │   ├── Página: Recomendações (principal)
│   │   ├── Página: Explorar Dados
│   │   └── Página: Sobre
│   │
│   ├── model/
│   │   ├── model.pkl                    # Modelo KNN treinado
│   │   ├── preprocessor.pkl             # StandardScaler
│   │   └── model_info.json              # Metadados
│   │
│   └── utils/
│       ├── __init__.py
│       ├── data_loader.py               # Funções de carregamento
│       └── recommender.py               # Lógica de recomendação
│
├── data/
│   ├── occupations_processed.csv        # Dados de profissões
│   ├── skills_processed.csv             # Dados de habilidades
│   └── occupation_skills_matrix.csv     # Matriz de features
│
├── README.md                             # Documentação principal
├── requirements.txt                      # Dependências completas
├── requirements_streamlit.txt            # Dependências para deploy
└── .gitignore                            # Arquivos ignorados
```

---

# 5. FUNCIONALIDADES DO WEBAPP

## 5.1 Página Inicial

- **Apresentação do projeto**
- **Estatísticas gerais do mercado**:
  - Profissões analisadas
  - Profissões do futuro
  - Crescimento médio
  - Salário médio
- **Como funciona**: Guia em 3 passos
- **Call-to-action**: Direcionamento para recomendações

## 5.2 Página de Recomendações (Principal)

### Seleção de Habilidades:
- **4 categorias** organizadas:
  - 💻 Técnicas (Programming, Data Analysis, etc.)
  - 💼 Negócios (Leadership, Project Management, etc.)
  - 🤝 Soft Skills (Communication, Problem Solving, etc.)
  - 🔧 Outras (Research, Design, etc.)

### Configurações Avançadas:
- Número de recomendações (5-20)
- Filtro: apenas profissões do futuro
- Filtro: salário mínimo anual

### Resultados:
- **Gráfico de barras**: Top 10 por compatibilidade
- **Scatter plot**: Salário anual vs Crescimento
- **Cards detalhados** para cada profissão:
  - Título e descrição
  - Score de compatibilidade (0-100%)
  - Salário anual (USD)
  - Crescimento projetado (%)
  - Badge "Profissão do Futuro"
  - Habilidades necessárias (expansível)
- **Download**: Resultados em CSV

## 5.3 Página Explorar Dados

### Filtros Interativos:
- Crescimento mínimo (%)
- Faixa de salário anual (USD)
- Apenas profissões do futuro

### Visualizações:
- **Aba Lista**: Tabela interativa com filtros
- **Aba Gráficos**: 
  - Top 10 por salário
  - Top 10 por crescimento
  - Distribuição de salários
- **Aba Habilidades**:
  - Top 20 habilidades mais demandadas

## 5.4 Página Sobre

- **Objetivo do projeto**
- **Como funciona** (resumo técnico)
- **Fontes de dados**
- **Tecnologias utilizadas**
- **Equipe** (nomes e RMs)
- **Metodologia** resumida
- **Resultados** alcançados

---

# 6. RESULTADOS ALCANÇADOS

## 6.1 Objetivos Cumpridos

✅ **Sistema completo implementado e funcional**
- Interface web intuitiva e responsiva
- Sistema de recomendação preciso
- Visualizações interativas
- Deploy em produção

✅ **Métricas do Modelo**
- Acurácia na identificação de profissões do futuro: 75%
- Crescimento médio das recomendações: 22.3%
- Tempo de resposta: < 2 segundos

✅ **Base de Conhecimento**
- 20 profissões analisadas
- 40+ habilidades mapeadas
- Dados de projeção até 2034
- Integração com dados reais (O*NET, BLS)

## 6.2 Estatísticas do Projeto

### Código:
- **~2000+ linhas** de código Python
- **3 arquivos** principais do webapp
- **40+ células** no notebook
- **15+ funções** implementadas

### Dados:
- **20 profissões** do futuro mapeadas
- **140+ registros** de habilidades por profissão
- **40+ habilidades** únicas catalogadas
- **10 anos** de projeção de mercado

### Visualizações:
- **10+ gráficos** no notebook
- **8+ gráficos** no webapp
- **Múltiplos tipos**: Barras, Scatter, Heatmap, Histograma

## 6.3 Impacto e Aprendizados

### Conhecimentos Técnicos Adquiridos:
1. Implementação de sistemas de recomendação
2. Desenvolvimento de webapps com Streamlit
3. Deploy em cloud (Streamlit Cloud)
4. Análise exploratória de dados
5. Visualização de dados com Plotly
6. Machine Learning aplicado

### Competências Desenvolvidas:
1. Trabalho em equipe
2. Gerenciamento de projeto
3. Versionamento de código com Git
4. Documentação técnica
5. Apresentação de resultados

---

# 7. LINKS DO PROJETO

## 7.1 Repositório GitHub

**URL**: https://github.com/pazil/gs2_front_end

**Conteúdo**:
- Código-fonte completo
- Notebook com análise
- Dados processados
- Documentação
- Histórico de commits

## 7.2 Webapp Deployado

**URL**: https://gs2frontend.streamlit.app

**Acesso**: Público, sem necessidade de login

**Disponibilidade**: 24/7 através do Streamlit Cloud

---

# 8. COMO USAR O SISTEMA

## 8.1 Acessar o Webapp

1. Acesse: https://gs2frontend.streamlit.app
2. A página inicial será exibida automaticamente

## 8.2 Obter Recomendações

1. No menu lateral, clique em **"Recomendações"**
2. Selecione suas habilidades marcando as caixas nas 4 categorias:
   - Técnicas
   - Negócios
   - Soft Skills
   - Outras
3. (Opcional) Configure filtros avançados:
   - Número de recomendações
   - Apenas profissões do futuro
   - Salário mínimo
4. Clique em **"Obter Recomendações"**
5. Explore os resultados:
   - Veja os gráficos de análise
   - Leia os cards detalhados de cada profissão
   - Baixe os resultados em CSV se desejar

## 8.3 Explorar Dados

1. No menu lateral, clique em **"Explorar Dados"**
2. Use os filtros na barra lateral:
   - Crescimento mínimo
   - Faixa de salário
   - Apenas profissões do futuro
3. Navegue pelas abas:
   - Lista: Tabela com todas as profissões
   - Gráficos: Visualizações comparativas
   - Habilidades: Análise de demanda

---

# 9. CONCLUSÃO

## 9.1 Síntese do Projeto

Este projeto desenvolveu com sucesso um **sistema inteligente de recomendação de profissões do futuro** que combina:

- **Dados reais** de fontes confiáveis (O*NET, BLS)
- **Machine Learning** para recomendações personalizadas
- **Interface web intuitiva** e acessível
- **Deploy em produção** na nuvem

O sistema atinge seu objetivo de **auxiliar profissionais** a identificarem oportunidades de carreira alinhadas às suas habilidades, fornecendo informações valiosas para planejamento de carreira em um mercado de trabalho em constante transformação.

## 9.2 Diferencial Competitivo

- ✅ **Baseado em dados oficiais** do governo americano
- ✅ **ML embarcado** no webapp
- ✅ **Interface moderna** e responsiva
- ✅ **Resultados em tempo real** (< 2 segundos)
- ✅ **Projeções de longo prazo** (2024-2034)
- ✅ **Métricas validadas** (superando baseline)

## 9.3 Possibilidades Futuras

### Expansões Possíveis:
1. Aumentar base de profissões (100+)
2. Incluir dados de múltiplos países
3. Sistema de login e perfis salvos
4. Roadmap personalizado de desenvolvimento
5. Integração com APIs de vagas de emprego
6. Recomendação de cursos e certificações

### Melhorias Técnicas:
1. Implementar modelos de Deep Learning
2. Sistema híbrido (colaborativo + conteúdo)
3. Atualização automática de dados
4. API REST para integração

## 9.4 Agradecimentos

Agradecemos à FIAP pela oportunidade de desenvolver este projeto como parte da Global Solution, permitindo-nos aplicar conhecimentos de Machine Learning e desenvolvimento web em um contexto real e relevante.

---

# 10. REFERÊNCIAS

## 10.1 Fontes de Dados

1. **O*NET Database**
   - URL: https://www.onetcenter.org/
   - Occupational Information Network
   - Descrições detalhadas de ocupações, habilidades e conhecimentos

2. **Bureau of Labor Statistics (BLS)**
   - URL: https://www.bls.gov/
   - Employment Projections (2024-2034)
   - Occupational Outlook Handbook

## 10.2 Documentação Técnica

1. **Streamlit Documentation**
   - URL: https://docs.streamlit.io
   - Framework para desenvolvimento de webapps

2. **Scikit-learn Documentation**
   - URL: https://scikit-learn.org
   - Machine Learning em Python

3. **Plotly Python**
   - URL: https://plotly.com/python/
   - Visualizações interativas

## 10.3 Estudos Relacionados

1. **World Economic Forum**
   - "The Future of Jobs Report 2023"
   - Análise de tendências do mercado de trabalho

2. **McKinsey Global Institute**
   - "Jobs Lost, Jobs Gained: Workforce Transitions in a Time of Automation"
   - Impacto da automação no trabalho

---

# ANEXOS

## A. Principais Profissões Analisadas

1. Data Scientists (35.8% crescimento)
2. Machine Learning Engineers (40.1% crescimento)
3. Cybersecurity Analysts (32.4% crescimento)
4. Physician Assistants (27.6% crescimento)
5. Telemedicine Physicians (28.3% crescimento)
6. Software Developers (25.7% crescimento)
7. Sales Representatives - Renewable Energy (24.2% crescimento)
8. Software Quality Assurance Analysts (22.4% crescimento)
9. Sustainability Specialists (19.7% crescimento)
10. Market Research Analysts (18.6% crescimento)

## B. Principais Habilidades Catalogadas

**Técnicas:**
- Programming
- Data Analysis
- Machine Learning
- Cloud Computing
- Cybersecurity
- Web Development
- Mobile Development
- AI/Deep Learning
- Database Management
- DevOps

**Negócios:**
- Leadership
- Project Management
- Business Analysis
- Marketing
- Sales
- HR Management
- Financial Analysis

**Soft Skills:**
- Communication
- Problem Solving
- Critical Thinking
- Creativity
- Teamwork
- Adaptability
- Time Management

**Outras:**
- Research
- Technical Writing
- Design
- Healthcare Knowledge
- Customer Service
- Renewable Energy
- Sustainability

## C. Métricas de Performance do Modelo

| Métrica | Valor | Baseline | Melhoria |
|---------|-------|----------|----------|
| Taxa de Profissões do Futuro | 75% | 70% | +5% |
| Crescimento Médio Recomendado | 22.3% | 18.5% | +3.8% |
| Tempo de Resposta | < 2s | N/A | N/A |
| Perfis Testados | 100 | N/A | N/A |

---

**FIM DO DOCUMENTO**

---

**Data de Elaboração**: Novembro/2024  
**Instituição**: FIAP - Faculdade de Informática e Administração Paulista  
**Disciplina**: Front End & Mobile Development  
**Turma**: 2TIAPY

**Projeto desenvolvido para a Global Solution 2024**

