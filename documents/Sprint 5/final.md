
# Documentação Pipeline/Modelo/API
## 1. **Introdução**
### *Objetivo do Projeto*
- Detectar fraudes no consumo de água utilizando técnicas avançadas de deep learning, que identificam padrões anômalos no consumo. Isso inclui a análise de dados históricos de consumo e a integração de variáveis externas, como índices macroeconômicos, climáticos e geográficos.
### *Contexto do Problema*
- Fraudes no consumo de água, como os "gatos", representam um grave problema para o setor de saneamento.  Além de gerarem perdas financeiras para as empresas,  comprometem o abastecimento, aumentam o risco de doenças e agravam a escassez hídrica. A detecção precoce, por meio da análise de dados, inspeções, tecnologias e denúncias, é crucial para minimizar esses impactos, garantir o fornecimento regular de água, proteger a saúde pública e combater o desperdício.  Diante da baixa acurácia (inferior a 50%) na identificação de fraudes, a AEGEA busca aprimorar seus métodos de investigação, e o desenvolvimento de um modelo preditivo surge como uma solução promissora para aumentar a eficiência na detecção de clientes fraudulentos.
### *Resumo da Solução*
Para resolver o problema da detecção de fraudes no consumo de água, desenvolvemos uma solução que envolve três etapas principais: 

- **Pipeline ETL**: Primeiramente, implementamos um pipeline de Extração, Transformação e Carga (ETL) utilizando módulos Python, que integra e processa dados de diversas fontes. O pipeline é responsável por coletar dados históricos de consumo de água e combiná-los com variáveis externas, como indicadores macroeconômicos, dados climáticos e eventos relevantes. Esse processo prepara os dados de entrada que alimentam o modelo de aprendizado profundo.

- **Modelo de Rede Neural LSTM**: Em seguida, construímos um modelo preditivo de Long Short-Term Memory (LSTM) utilizando Keras, que analisa padrões temporais ao longo de 7 semestres. O modelo recebe como entrada variáveis fixas, como categoria de cliente, e variáveis temporais, incluindo consumo de água, dados econômicos e meteorológicos. O objetivo é prever se há probabilidade de fraude por parte do cliente no oitavo semestre. 

- **API com FastAPI**: Por fim, o modelo foi integrado a uma API construída com FastAPI. A API permite o acesso ao modelo preditivo, possibilitando que o sistema seja utilizado para fazer previsões sobre novos dados de consumo. Com uma interface intuitiva e de fácil uso, a API facilita a integração com outros sistemas e garante a escalabilidade da solução.

## 2. **Arquitetura do Projeto**
### *Visão Geral* 
![image](https://github.com/user-attachments/assets/65bdd33d-eb71-4eb2-858d-9a2edd5e87a3)


Os ícones de serviços do AWS são ilustrativos e podem ser usados para replicar a solução nessa núvem

### *Pipeline ETL*

O projeto implementa um pipeline ETL (Extract, Transform, Load) robusto e escalável utilizando Dask para processamento paralelo de grandes volumes de dados. A arquitetura é dividida em três principais componentes:

#### **Extração (Extract)**
- **Dados de Consumo e Fraudes**
  - Utiliza `dask.dataframe` para leitura eficiente de arquivos CSV
  - Processamento distribuído de múltiplos arquivos de consumo
  - Extração seletiva por ano através de filtros temporais
  
- **Dados Externos**
  - **Dados Econômicos**: Integração com API do Banco Central (BCB)
    - Índices: IGPM, SELIC, IPCA
    - Utiliza `requests` para chamadas HTTP
    
  - **Dados Meteorológicos**
    - Integração com biblioteca `meteostat`
    - Coleta de métricas como temperatura, precipitação, umidade
    - Dados específicos para a região de interesse
    
  - **Eventos e Shows**
    - Web scraping com `BeautifulSoup`
    - Extração de dados de eventos da plataforma Setlist.fm
    
  - **Calendário e Feriados**
    - Utiliza biblioteca `holidays`
    - Identificação de dias úteis, fins de semana e feriados

#### **Transformação (Transform)**
- **Processamento de Dados de Consumo**
  - Criação de chave temporal ANOMES
  - Redução e seleção de colunas relevantes
  - Transformação de tipos de dados para otimização
  - Indexação temporal para particionamento eficiente
  
- **Processamento de Dados Externos**
  - Agregação de dados meteorológicos por período
  - Conversão de tipos e normalização de formatos temporais
  - Criação de variáveis dummy para tipos de dias
  - Agregação de quantidade de eventos por período
  
- **Integração de Dados**
  - Join entre dados de consumo e fraudes
  - Merge de todas as fontes externas
  - Remoção de duplicatas
  - Alinhamento temporal das diferentes fontes

#### **Carregamento (Load)**
- **Estratégia de Persistência**
  - Utiliza formato Parquet para armazenamento otimizado
  - Separação em diferentes diretórios por tipo de dado
    - `/consumption`: Dados de consumo e fraudes
    - `/external`: Dados externos integrados
  - Dataset final unificado com todas as fontes
  
- **Otimizações**
  - Particionamento inteligente dos dados
  - Compressão eficiente com engine PyArrow
  - Monitoramento de progresso com `ProgressBar`

#### **Bibliotecas Principais**
- **Processamento de Dados**
  - `dask`: Computação paralela e distribuída
  - `pandas`: Manipulação e análise de dados
  - `numpy`: Operações numéricas
  
- **Integração Externa**
  - `requests`: Chamadas HTTP
  - `beautifulsoup4`: Web scraping
  - `meteostat`: Dados meteorológicos
  
- **Persistência e Formato**
  - `pyarrow`: Engine para formato Parquet
  - `holidays`: Gestão de calendário

O pipeline é configurado através de um dicionário central que permite fácil adaptação para diferentes períodos, regiões e fontes de dados, mantendo a flexibilidade e reusabilidade do código.
### *Modelo LSTM*

#### **Arquitetura do Modelo**

O modelo implementa uma arquitetura híbrida que combina redes LSTM (Long Short-Term Memory) para processamento de séries temporais com uma rede neural feed-forward para características fixas. A arquitetura foi projetada para detecção de fraudes em consumo de água, processando tanto dados temporais quanto características estáticas.

#### **Camadas e Componentes**:

- **Camadas de Entrada**
   - **Entrada Temporal**
     - Shape: `(7, n_features_temporais)`
     - Sequência de 7 timesteps
     - Processa features variáveis no tempo (consumo, clima, etc.)
   
   - **Entrada Fixa**
     - Shape: `(n_features_fixas,)`
     - Características estáticas das unidades consumidoras
     - Informações demográficas e categoricas

- **Camada LSTM**
   - **Configuração**
     - Unidades: 64
     - Return Sequences: False
     - Função de ativação: tanh (padrão)
   
   - **Regularização**
     - Dropout: 0.3
     - Previne overfitting na camada LSTM

- **Camada de Concatenação**
   - Merge das features:
     - Saída LSTM (64 unidades)
     - Features fixas (n_features_fixas)
   - Permite processamento conjunto de ambos tipos de dados

- **Camadas Densas**
   - **Primeira Camada**
     - Unidades: 64
     - Ativação: ReLU
     - Processa features combinadas
   
   - **Camada de Saída**
     - Unidades: 1
     - Ativação: Sigmoid
     - Probabilidade de fraude (0-1)

#### **Configuração do Treinamento**

- **Otimizador**: Adam
- **Função de Perda**: Binary Crossentropy
- **Métricas**: Accuracy
- **Hiperparâmetros**:
  - Epochs: 50
  - Batch Size: 64
  - Validation Split: 0.2

#### **Tratamento de Features**

- **Features Temporais**
  - Normalização de séries temporais
  - Janela deslizante de 7 trimestres
  - Inclusão de variáveis sazonais e tendências

- **Features Fixas**
  - Normalização de variáveis numéricas
  - Encoding de variáveis categóricas
  - Seleção baseada em importância de features

O modelo demonstra capacidade de capturar tanto padrões temporais quanto características estáticas para identificação de fraudes, com mecanismos de regularização para prevenir overfitting e métricas abrangentes para avaliação de performance.
### *API FastAPI*

### **Visão Geral**
A API foi desenvolvida usando FastAPI para servir o modelo de detecção de fraudes, oferecendo um endpoint principal para previsões e monitoramento de saúde do serviço. A API é documentada automaticamente através do Swagger UI (disponível em `/docs`).

### **Configuração Base**
```python
app = FastAPI(
    title="API de Detecção de Fraudes",
    description="API para previsão de fraudes usando features temporais e fixas",
    version="1.0.0"
)
```

### **Arquitetura da API**

#### **Modelo de Dados**
   - **PredictionInput** (Pydantic BaseModel)
   ```python
   class PredictionInput(BaseModel):
         features_temporais: list
         features_fixas: list
   ```
   - Validação automática de tipos
   - Exemplo de payload incluído na documentação
   - Configuração de schema JSON para documentação clara

#### **Endpoints**

##### **Previsão de Fraudes**
   - **Rota**: `/predict`
   - **Método**: POST
   - **Funcionalidade**: Realiza previsões de fraude usando o modelo carregado
   - **Entrada**:
   ```json
   {
      "features_temporais": [[[...]] * 7],  // Matriz 3D (1, 7, 26)
      "features_fixas": [[...]]             // Matriz 2D (1, 5)
   }
   ```
   - **Resposta**:
   ```json
   {
      "prediction": float,
      "fraud_probability": float,
      "status": "success"
   }
   ```
   - **Validações**:
   - Dimensões das features temporais: (1, 7, 26)
   - Dimensões das features fixas: (1, 5)
   - Tipos de dados: float32

#### **Verificação de Saúde**
   - **Rota**: `/health`
   - **Método**: GET
   - **Resposta**: Status de saúde do serviço
   ```json
   {
      "status": "healthy"
   }
   ```

### Segurança e Performance
1. **Carregamento do Modelo**
   - Carregamento único na inicialização
   - Tratamento de erros de carregamento
   - Logging de status de carregamento

2. **Validação de Dados**
   - Validação automática via Pydantic
   - Verificação de dimensões das features
   - Conversão segura de tipos de dados

3. **Logging**
   - Debug de formas dos arrays
   - Logging detalhado de erros
   - Rastreamento de exceções

## 3. **Pré-processamento dos Dados**

### *Fonte dos Dados*

O conjunto de dados utilizado neste projeto combina informações de múltiplas fontes:

1. **Dados de Consumo**
   - Consumo medido por matrícula
   - Referência temporal
   - Categoria do consumidor
   - Localização (latitude e longitude)
   - Status de fraude

2. **Variáveis Macroeconômicas**
   - SELIC
   - IPCA
   - IGPM

3. **Dados Meteorológicos**
   - Temperatura (°C)
   - Velocidade do Vento (km/h)
   - Direção do Vento (°)

4. **Dados Contextuais**
   - Tipo do dia (dia útil, feriado, fim de semana)
   - Quantidade de shows

### *Transformação e Engenharia de Features*

#### **1. Organização Temporal dos Dados**

- #### Estruturação Trimestral
  - Conversão da coluna 'REFERENCIA' para formato datetime
  - Criação de identificadores trimestrais sequenciais (Q1, Q2, etc.)
  - Agrupamento dos dados por matrícula e trimestre

- #### Criação de Features Temporais Relativas
Para cada variável numérica, foram criadas três medidas temporais:
  - M0: Valor atual
  - M1: Valor do próximo mês
  - M2: Valor do mês subsequente

### *2. Agregação de Features*

#### **Features Estatísticas Trimestrais**
Para cada variável, foram calculadas métricas estatísticas por trimestre:
- Média (MEAN)
- Desvio Padrão (STD)

Variáveis agregadas:
```python
variaveis = [
    'CONS_MEDIDO', 'valor_SELIC', 'valor_IPCA', 'valor_IGPM',
    'Temperature (°C)', 'Wind Speed (km/h)', 'Wind Direction (°)',
    'tipo_dia_dia_util', 'tipo_dia_feriado', 'tipo_dia_fim_de_semana',
    'quantidade_shows'
]
```

### *3. Preparação para Modelagem LSTM*

#### **Estruturação Sequencial**
- Organização dos dados em sequências de 7 trimestres
- Cada ponto temporal contém 26 features por step
- Shape final: (num_samples, 7, 26)

#### **Tratamento de Variáveis Geográficas**
- Encoding cíclico para coordenadas geográficas:
  - Transformação de latitude e longitude em componentes sin/cos
  - Features resultantes: lat_sin, lat_cos, lon_sin, lon_cos

#### **Normalização**
- Aplicação do RobustScaler para normalização das features numéricas
- Escolha do RobustScaler devido à sua robustez a outliers

### *4. Balanceamento de Dados*

#### **Aplicação de técnica híbrida de balanceamento:**
Como cada técnica contribui:

- SMOTE (Synthetic Minority Over-sampling Technique):  Gera exemplos sintéticos da classe minoritária, aumentando sua representatividade sem simplesmente duplicar os dados existentes. Isso ajuda a evitar overfitting e melhora a generalização do modelo. No projeto, o SMOTE aumenta a classe minoritária para 50% da classe majoritária.

- Undersampling (RandomUnderSampler): Remove aleatoriamente exemplos da classe majoritária, reduzindo sua dominância no dataset.  No projeto, o RandomUnderSampler mantém uma proporção de 80% para a classe majoritária após a aplicação do SMOTE.

#### **Vantagens da combinação:**

- Mitigar perda de informação: Undersampling sozinho pode descartar informações importantes da classe majoritária. Ao usar SMOTE antes, você aumenta a classe minoritária e reduz a chance de perder dados relevantes ao realizar o undersampling.
- Evitar overfitting do SMOTE: SMOTE pode gerar exemplos sintéticos que são muito similares aos originais ou que invadem o espaço da classe majoritária. O undersampling ajuda a "limpar" o dataset, removendo alguns desses exemplos problemáticos e melhorando a separação entre as classes.
- Ajustar o balanceamento: A combinação permite um controle mais preciso do balanceamento final. No projeto, aumentamos a classe minoritária para 50% da majoritária com SMOTE e depois reduzimos a majoritária para 80% com undersampling, buscando uma proporção que beneficie o aprendizado do modelo.

### *5. Divisão dos Dados*

- Separação em conjuntos de treino e teste (80/20)
- Preservação da estrutura temporal nas divisões
- Manutenção da distribuição das classes nos conjuntos

## 4. **Validação do Modelo**

**Análise das Métricas**

- **Acurácia no conjunto de teste**: 0.8712
- **Coeficiente de Correlação de Matthews (MCC)**: 0.7388
- **Precisão**: 0.8654

Essas métricas indicam que o modelo possui um bom desempenho geral, com uma precisão elevada e um coeficiente de correlação de Matthews que mostra uma correlação forte entre as previsões e os resultados reais.

**Explicando o Coeficiente de Correlação de Matthews (MCC)**

**O que é o MCC?**

O Coeficiente de Correlação de Matthews (MCC) é uma métrica usada para avaliar o desempenho de modelos de classificação binária. Ele leva em consideração todos os quatro valores da matriz de confusão: verdadeiros positivos (VP), verdadeiros negativos (VN), falsos positivos (FP) e falsos negativos (FN).

**Fórmula**

A fórmula do MCC é:

```
MCC = (VP * VN - FP * FN) / √((VP + FP) * (VP + FN) * (VN + FP) * (VN + FN))
```

**Utilidade**

* **Robustez a dados desbalanceados:** O MCC é especialmente útil quando as classes estão desbalanceadas, ou seja, quando uma classe é muito mais frequente do que a outra. Em tais casos, métricas como a acurácia podem ser enganosas, pois um modelo pode obter uma alta acurácia simplesmente prevendo a classe majoritária para todas as amostras. O MCC, por levar em consideração todos os quadrantes da matriz de confusão, é menos sensível a esse problema.

* **Interpretação intuitiva:** O MCC varia de -1 a 1, com os seguintes significados:

    * **MCC = 1:** Classificação perfeita.
    * **MCC = 0:** O modelo não é melhor do que uma escolha aleatória.
    * **MCC = -1:** Classificação completamente errada.

* **Considera todos os aspectos da classificação:** Ao contrário de métricas como precisão e recall, que se concentram em aspectos específicos da classificação (positivos ou negativos), o MCC fornece uma avaliação mais completa do desempenho do modelo, considerando tanto a capacidade de identificar corretamente as amostras positivas quanto as negativas.

* **Matriz de Confusão:** A matriz de confusão fornece uma visão detalhada do comportamento do modelo, revelando a distribuição de verdadeiros positivos (VP), verdadeiros negativos (VN), falsos positivos (FP) e falsos negativos (FN).

    * O alto número de VN e VP reforça a capacidade do modelo de realizar classificações corretas.
    * A presença de FP e FN destaca áreas onde o modelo pode ser otimizado. Os FP indicam uma tendência do modelo a classificar algumas amostras como positivas quando, na verdade, são negativas, o que pode ser problemático em aplicações com alto custo de falsos positivos. Por outro lado, os FN representam amostras positivas que o modelo classificou incorretamente como negativas, o que pode ser crítico em situações onde o custo de falsos negativos é alto.
![image](https://github.com/user-attachments/assets/2dbed032-1b0a-4ee5-a7d5-806952231542)
* **Análise da Curva de Aprendizado**: O gráfico da **Curva de Acurácia** ao longo das épocas de treinamento destaca o progresso do modelo em termos de aprendizado:

 * **Acurácia de Treinamento (linha azul)**: A acurácia no conjunto de treino continua subindo de forma consistente, atingindo cerca de 88,5% após 50 épocas.
 * **Acurácia de Validação (linha laranja)**: A acurácia de validação segue um padrão similar ao da curva de treino, mas estabiliza após 40 épocas, flutuando entre 85% e 86%. Esse padrão sugere que o modelo está generalizando bem, embora haja uma leve diferença entre a performance em treino e validação.
<br></br>
![image](https://github.com/user-attachments/assets/7f37b2e6-d394-4685-8bfc-a8579a125b70)
<br></br>
![image](https://github.com/user-attachments/assets/74c6ccca-90f9-4139-ae55-a09c29e4c5fc)
 * **Interpretação:**

   * **Tendência positiva**: Ambas as curvas mostram um aumento contínuo na acurácia, sugerindo que o modelo está aprendendo de forma eficaz.
   * **Estabilização da validação**: A curva de validação se estabiliza após um certo número de épocas, enquanto a curva de treino continua a melhorar. Isso pode indicar um início de **overfitting**, onde o modelo começa a se ajustar muito aos dados de treino e menos aos dados de validação.

**Interpretação Holística**

A análise conjunta das métricas, da curva ROC e da matriz de confusão oferece uma visão completa do desempenho do modelo. O modelo demonstra uma excelente capacidade de discriminação entre as classes, com alta precisão e bom desempenho geral. No entanto, a presença de FP e FN indica que há espaço para aprimoramento, especialmente em relação ao equilíbrio entre esses dois tipos de erros, dependendo dos requisitos específicos da aplicação.

<br></br>
**Conclusão**

O modelo avaliado apresenta um desempenho promissor na tarefa de classificação, conforme evidenciado pelas métricas, pela curva ROC e pela matriz de confusão. A análise integrada dessas informações permite uma compreensão abrangente das capacidades do modelo, seus pontos fortes e áreas potenciais de aprimoramento. A análise da curva de aprendizado sugere que o modelo está sofrendo um leve ajuste, mas pode se beneficiar de técnicas adicionais para evitar overfitting, sendo possível uma refinação.




## 5. **Implantação da API**
### *Instalação*

1. Clone o repositório:
```bash
git clone https://github.com/Inteli-College/2024-2A-T04-SI11-G04.git
cd src/backend
```

2. Crie um ambiente virtual e instale as dependências:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
.\venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

### *Estrutura do Projeto*

```
backend/
│
├── main.py              # Código principal da API
├── requirements.txt     # Dependências do projeto
├──modelo_fraude.h5      # Modelo Serializado
└── README.md           # Este arquivo
```

### *Uso da API*

#### Iniciar o servidor

```bash
uvicorn main:app --reload
```

A API estará disponível em `http://localhost:8000`

### *Documentação da API*

Acesse a documentação interativa em:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### *Exemplo de Requisição*

```python
import requests
import numpy as np

# Preparar dados de exemplo
features_temporais = np.random.rand(1, 7, 26)  # 1 amostra, 7 timesteps, 26 features
features_fixas = np.random.rand(1, 5) # 1 amostra, 5 features fixas

# Fazer requisição
response = requests.post(
    "http://localhost:8000/predict",
    json={
        "features_temporais": features_temporais,
        "features_fixas": features_fixas
    }
)

print(response.json())
```
ou usar o **Thunder Client**
![image](https://github.com/user-attachments/assets/cf817ec4-680c-483a-995a-653f0f5e689b)


### *Formato dos Inputs*

#### Features Temporais
- Shape: `(1, 7, 26)`
- Representam 7 timesteps com 26 features cada
- Inclui médias e desvios padrão de:
  - Consumo
  - Indicadores econômicos (SELIC, IGPM, IPCA)
  - Dados meteorológicos
  - Eventos (shows, feriados, etc.)

#### Features Fixas
- Shape: `(1, 5)`
- Inclui:
  - Categoria do local
  - Encoding cíclico de latitude e longitude

### *Dependências*

```
fastapi==0.104.1
uvicorn==0.24.0
tensorflow==2.15.0
pydantic==2.4.2
python-multipart==0.0.6
typing-extensions>=4.8.0
```

## 6. **Considerações Técnicas**
   - **Melhorias Potenciais**:
     - Utilização de dados externos de validação para testar o modelo
     - Comparar novas arquiteturas que possibilitam menos gasto computacional como o GRU
     - Utilizar buscadores de hiperparâmetros como GridSearch ou RandomSearch
     - Integração da API com o Front-end  
   - **Desafios e Limitações**:
     - O modelo atual utiliza um registro de 23 meses do cliente, o que pode ser um problema para novas matrículas que não atingiram esse tempo. Além disso, foi necessário a criação de vários dados sintéticos para balancear o dataset, o que é natural em registros de série temporal com fraudes, mas pode prejudicar na entrada de novos dados não vistos.

## 8. **Referências e Anexos**
AGÊNCIA NACIONAL DE ÁGUAS E SANEAMENTO BÁSICO. Campanhas de Conscientização. Disponível em: https://www.gov.br/ana/pt-br/assuntos/noticias-e-eventos/noticias/agencia-nacional-de-aguas-e-saneamento-basico-lanca-tema-para-celebracao-do-dia-mundial-da-agua-no-brasil-em-2024.

BANCO CENTRAL DO BRASIL. Relatório de Inflação. Disponível em: https://www.bcb.gov.br/publicacoes/ri.

BANCO CENTRAL DO BRASIL. Relatório Focus. Disponível em: https://www.bcb.gov.br/publicacoes/focus.

BRASIL. Decreto-Lei nº 2.848, de 7 de dezembro de 1940. Código Penal Brasileiro. Disponível em: http://www.planalto.gov.br/ccivil_03/decreto-lei/del2848compilado.htm.

BRASIL. Lei nº 9.433, de 8 de janeiro de 1997. Institui a Política Nacional de Recursos Hídricos. Disponível em: https://www.planalto.gov.br/ccivil_03/leis/l9433.htm.

BRASIL. Lei nº 11.196, de 21 de novembro de 2005. Institui a Lei do Bem. Disponível em: http://www.planalto.gov.br/ccivil_03/_ato2004-2006/2005/lei/l11196.htm.

BRASIL. Lei nº 11.445, de 5 de janeiro de 2007. Estabelece diretrizes nacionais para o saneamento básico. Disponível em: http://www.planalto.gov.br/ccivil_03/_ato2007-2010/2007/lei/l11445.htm.

BRASIL. Lei nº 14.026, de 15 de julho de 2020. Atualiza o marco legal do saneamento básico. Disponível em: http://www.planalto.gov.br/ccivil_03/_ato2019-2022/2020/lei/L14026.htm.

BRASIL. Lei nº 14.026, de 15 de julho de 2020. Novo Marco Legal do Saneamento Básico. Disponível em: https://www.gov.br/cidades/pt-br/assuntos/saneamento/marco-legal-do-saneamento#:~:text=Em%2031%20de%20maio%20de,considerados%20os%20contratos%20em%20vigor..

BRASIL. Resolução CONAMA nº 357, de 17 de março de 2005. Classificação dos corpos de água e diretrizes ambientais para o seu enquadramento. Disponível em: https://www.icmbio.gov.br/cepsul/images/stories/legislacao/Resolucao/2005/res_conama_357_2005_classificacao_corpos_agua_rtfcda_altrd_res_393_2007_397_2008_410_2009_430_2011.pdf.

DEPARTAMENTO NACIONAL DE OBRAS CONTRA AS SECAS. Consumo consciente da água é base para um futuro sustentável. Disponível em: https://www.gov.br/dnocs/pt-br/assuntos/noticias/consumo-consciente-da-agua-e-base-para-um-futuro-sustentavel.

DOWDING, D.; MERRILL, J. A. The Development of Heuristics for Evaluation of Dashboard Visualizations. Thieme - Applied Clinical Informatics, 2018. Disponível em: https://www.thieme-connect.com/products/ejournals/pdf/10.1055/s-0038-1666842.pdf.

FERREIRA, A. Usabilidade e Acessibilidade no design para a Web. Universidade do Porto, 2008.

MOMA, G. 10 Heurísticas de Nielsen para o Design de Interface. Brasil UX Design, 2017. Disponível em: https://brasil.uxdesign.cc/10-heur%C3%ADsticas-de-nielsen-para-o-design-de-interface-58d782821840.

OPENAI. Chatbot GPT-3 [Large language model]. Disponível em: https://chat.openai.com/chat.

RODRIGUES, R. C. Métodos adotados na Administração Pública para elaborar Matrizes de Risco. UNIFUCAMP, 2019.

SALES, M. WCAG 2.2 de forma simples! Guia WCAG, 2024. Disponível em: https://guia-wcag.com/.

SILVA, J. C. S., et al. Usabilidade de um dashboard destinado à autorregulação de estudantes em Sala de Aula Invertida. CINTED-UFRGS, 2018.

