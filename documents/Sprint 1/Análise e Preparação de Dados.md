# Relatório de EDA: Descrição detalhada da análise exploratória, incluindo estatísticas descritivas e visualizaçõe
(fazer) 

BIG NUMBERS: 
- 24% das pessoas ja cometeram algum ato fraudulento
- 
Distribuição de fraudes
- 92.64% fraudes são residênciais
- 0.30% fraudes são públicas

# Tratamento de Dados
Neste projeto, realizado em parceria com a AEGEA, trabalhamos com uma base de dados que abrange o consumo de água entre os anos de 2019 e 2024, além de um histórico de fraudes ocorridas ao longo desses anos. O objetivo principal é analisar o consumo de água ao longo do tempo, calcular a média de consumo por ano e investigar a distribuição de fraudes. Para alcançar esses objetivos, seguimos um processo de limpeza e pré-processamento de dados bem estruturado.

O primeiro passo foi preparar o ambiente de trabalho. Utilizamos o Google Colab como plataforma de desenvolvimento e instalamos diversas bibliotecas para auxiliar no processo de análise. Em seguida, configuramos o caminho para importar os dados, o que nos permitiu carregar e manipular grandes volumes de dados de forma eficiente.
Para facilitar a análise, unificamos os dados de consumo de água e as informações de fraudes em um único DataFrame. Isso envolveu a combinação das bases de dados, o que nos permitiu visualizar de maneira integrada todas as informações necessárias. A partir deste ponto, iniciamos o processo de tratamento dos dados, onde identificamos e tratamos campos que continham valores nulos de forma cuidadosa para garantir que não afetassem as análises subsequentes.

A normalização dos dados foi uma etapa crucial para garantir que todos os valores estivessem dentro de um intervalo comparável, especialmente para variáveis como consumo de água, que podem variar amplamente. Além disso, realizamos a codificação das variáveis categóricas, utilizando o método conhecido como one hot encoding, que converte colunas categóricas em valores numéricos binários. Isso foi fundamental para que as variáveis categóricas pudessem ser compreendidas e processadas adequadamente pelos modelos de machine learning.

Outra etapa interessante para nossa compreensão e análise dos dados foi a criação de colunas que pudessem agregar valor e gerar insights mais profundos nas análises. Com isso, criamos as seguintes quatro colunas. 
1. **Fraudes (0,1):** Esta coluna foi criada como uma variável binária, onde atribuímos '1' para indicar a presença de fraude e '0' para a ausência. Essa coluna foi construída com base na comparação do consumo de água com padrões típicos de comportamento fraudulento, permitindo uma identificação rápida de casos suspeitos.
2. **Chave Única (Matrícula + SEQ):** Para facilitar a unificação e análise dos dados, criamos uma chave única através da concatenação dos campos "Matrícula" e "SEQ". Esta coluna nos permitiu unir informações de diferentes tabelas de forma consistente e precisa, garantindo a integridade dos dados durante as operações de junção.
3. **Temperatura (Média dos Últimos 30 Dias):** Para entender a influência de fatores ambientais no consumo de água, criamos uma coluna que calcula a média da temperatura dos últimos 30 dias. Este dado foi utilizado para analisar como as variações climáticas podem afetar o consumo e possivelmente contribuir para a identificação de padrões anômalos.
4. **Endereço (Rua, Bairro, Estado):+** Criamos colunas que reúnem as informações de Rua, Bairro e Estado para nos ajudar nas análises geoespaciais e a visualizar melhor a distribuição dos clientes e fraudes em diferentes regiões.

 ![image](https://github.com/user-attachments/assets/ac6e5214-8e46-423d-ac7c-e0615d1bd274)
 **Figura 1:** Criação de colunas realizada pelo grupo

O tratamento de dados é uma etapa fundamental em qualquer projeto de ciência de dados. Ele nos permite limpar e organizar os dados de forma a garantir a precisão das análises subsequentes. Ao realizar essas etapas, conseguimos compreender melhor os dados com os quais estamos lidando, identificar padrões e anomalias e assegurar que os resultados das análises sejam confiáveis e acionáveis.

# Análise Exploratória dos Dados (EDA)
Após a etapa de tratamento e preparação dos dados, iniciamos a Análise Exploratória de Dados (EDA). O objetivo dessa análise é extrair insights relevantes, identificar padrões e relacionamentos nos dados e preparar as informações para a modelagem preditiva.
Inicialmente, criamos um Data Frame dedicado a visualizar o consumo médio de água ao longo dos anos. Utilizamos gráficos de linha e de barras para identificar tendências e variações sazonais. Em seguida, exploramos os dados de fraudes, observando a distribuição de fraudes ao longo dos anos e relacionando-as com o consumo de água.
Realizamos uma análise específica em matrículas identificadas como fraudulentas, observando seus padrões de consumo mensal. Comparamos o consumo mensal médio, máximo e mínimo para identificar mudanças bruscas que pudessem estar associadas a fraudes.
A partir das análises realizadas, identificamos a necessidade de coletar mais dados para aumentar a precisão na detecção de fraudes. Especificamente, seria crucial obter a fatura mensal de cada residência e a quantidade de litros de água bombeados para cada uma.

# Gráficos criados e insights obtidos 

1. **Densidade de clientes por região:** Criamos este gráfico para visualizar a densidade de clientes em diferentes regiões. Utilizamos uma escala de cores que varia conforme a densidade, permitindo identificar rapidamente as áreas com maior concentração de clientes. Este gráfico nos ajuda a compreender como os clientes estão distribuídos geograficamente, o que pode ser útil para correlacionar com outros fatores, como a incidência de fraudes.
![image](https://github.com/user-attachments/assets/17517787-608d-4caa-9763-cba72d82622f) <br>
 **Figura 2:** Gráfico criado pelo grupo <br> <br> 



3.  **Consumo de água (volume de água) por região**: Este gráfico foi elaborado para mostrar o volume de água consumido em diferentes regiões, novamente utilizando uma escala de cores para representar a intensidade do consumo. Através deste gráfico, podemos identificar regiões com maior ou menor consumo de água, o que pode fornecer insights sobre padrões de uso e áreas que merecem atenção especial, tanto em termos de abastecimento quanto de monitoramento de fraudes.
![image](https://github.com/user-attachments/assets/927d9819-8ec1-4dff-adb4-aa781340e180) <br>
 **Figura 3:** Gráfico criado pelo grupo <br> <br> 


4.  **Distribuição de clientes honestos e fraudulentos:** Neste gráfico, utilizamos a cor azul para representar cidadãos honestos e vermelho para aqueles que já foram identificados como fraudulentos em algum momento. O objetivo é entender como esses dois grupos estão distribuídos pelas diferentes regiões. Essa visualização nos ajuda a detectar padrões de comportamento e a identificar possíveis áreas de risco para fraudes.
![image](https://github.com/user-attachments/assets/84bde12c-cf30-410d-8e6d-247cb97e8ccc) <br>
 **Figura 4:** Gráfico criado pelo grupo <br> <br> 


5. **Distribuição de comportamento fraudulento por região:** Focando apenas nas pessoas que apresentaram comportamentos fraudulentos, este gráfico mostra como essas fraudes estão distribuídas por região. Essa análise é fundamental para identificar hotspots de fraude e direcionar esforços de monitoramento e prevenção para as áreas mais críticas.
![image](https://github.com/user-attachments/assets/5371c3e4-fe45-438c-8bd1-e04d865546bc) <br> 
 **Figura 5:** Gráfico criado pelo grupo<br> <br>
   



