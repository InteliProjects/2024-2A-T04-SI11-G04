# 1. Introdução

A Aegea Saneamento enfrenta desafios significativos relacionados à detecção de fraudes no consumo de água, o que tem causado impactos financeiros e operacionais substanciais na empresa. Essas fraudes ocorrem por meio de diversas práticas que subnotificam o consumo real, prejudicando a arrecadação e a distribuição eficiente dos recursos. Em resposta a essa problemática, foi desenvolvido um modelo de rede neural artificial utilizando dados históricos de consumo e de fraudes detectadas. O objetivo deste modelo é prever potenciais fraudes, permitindo à empresa agir de maneira proativa para mitigar esses efeitos negativos.

# 2. Desenvolvimento da Rede Neural 

## Arquitetura da Rede Neural
A escolha da arquitetura de rede neural para o projeto de detecção de fraudes no consumo de água da Aegean Saneamento foi fundamentada em uma análise detalhada das características dos dados e das necessidades específicas do problema. Os dados utilizados possuem uma componente temporal significativa, representando o consumo de água ao longo do tempo, o que adiciona uma camada de complexidade ao problema de previsão de fraudes.

Optamos por utilizar essa arquitetura que é reconhecida por capturar padrões complexos em conjuntos de dados com múltiplas características. Dessa forma, permite uma implementação mais direta, facilitando ajustes rápidos e iterações durante o desenvolvimento inicial. Essa escolha também possibilita uma integração mais ágil com os sistemas existentes da Aegean Saneamento, garantindo que o modelo possa ser testado e validado em ambientes reais com maior rapidez.

Dessa forma, essa escolha se alinha perfeitamente com os objetivos do projeto, oferecendo um equilíbrio entre simplicidade, eficiência e capacidade de aprendizado, tudo isso enquanto permite a análise dos padrões temporais essenciais para a identificação de fraudes.


### Arquitetura do Modelo:

```python
# Importando as bibliotecas necessárias
from tensorflow.keras.models import Sequential 
from tensorflow.keras.layers import Dense, BatchNormalization, Dropout

# Definição do modelo
model = Sequential()

# Camada de entrada
model.add(Dense(128, input_dim=273, activation='relu')) 
model.add(BatchNormalization()) 
model.add(Dropout(0.2))

# Camadas ocultas
model.add(Dense(64, activation='relu')) 
model.add(BatchNormalization()) 
model.add(Dropout(0.2))

model.add(Dense(64, activation='relu')) 
model.add(BatchNormalization()) 
model.add(Dropout(0.2))

model.add(Dense(32, activation='relu')) 
model.add(BatchNormalization()) 
model.add(Dropout(0.2))

model.add(Dense(32, activation='relu')) 
model.add(BatchNormalization()) 
model.add(Dropout(0.2))

# Camada de saída
model.add(Dense(1, activation='sigmoid'))

# Compilação do modelo
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy', 'Recall']) 

```
###  Justificativa para a Seleção da Arquitetura
* Camadas Densas (Dense Layers): As camadas densas foram escolhidas por sua capacidade de aprender representações complexas dos dados, essenciais para a detecção de fraudes. A quantidade de neurônios em cada camada foi determinada com base na necessidade de equilibrar a capacidade de aprendizado e a eficiência computacional.

* Função de Ativação ReLU: A função de ativação ReLU (Rectified Linear Unit) foi selecionada por ser eficaz em evitar o problema do desaparecimento do gradiente, comum em redes neurais profundas, permitindo que o modelo aprenda mais rapidamente e de forma mais eficaz.

* BatchNormalization: A normalização por batch foi aplicada após cada camada densa para estabilizar e acelerar o processo de treinamento, além de contribuir para a regularização do modelo.

* Dropout: O dropout com taxa de 20% foi introduzido para reduzir o risco de overfitting, incentivando o modelo a generalizar melhor os padrões aprendidos.

* Função de Perda Binary Crossentropy: Esta função de perda é a mais adequada para problemas de classificação binária, como a detecção de fraudes.

* Otimizador Adam: O Adam foi escolhido por combinar as vantagens de dois outros otimizadores populares (Adagrad e RMSprop), proporcionando um processo de treinamento eficiente e robusto com uma taxa de aprendizado inicial de 0.01.



# Hiperparâmetros
A configuração dos hiperparâmetros do modelo de rede neural é uma etapa crucial no desenvolvimento de um sistema eficaz para a detecção de fraudes no consumo de água. Cada hiperparâmetro foi escolhido com base em considerações específicas do problema, visando otimizar o desempenho do modelo enquanto se evita problemas comuns, como overfitting. Abaixo está o detalhamento dos hiperparâmetros selecionados e a justificativa para suas escolhas.


Os hiperparâmetros utilizados no modelo são os seguintes:
1. Arquitetura da Rede
   - Camada de entrada: 128 neurônios, input_dim=273, ativação ReLU: A camada de entrada foi configurada com 128 neurônios para fornecer uma representatividade robusta dos dados de entrada, que possuem 273 características. A função de ativação ReLU (Rectified Linear Unit) foi escolhida por sua capacidade de acelerar o processo de treinamento, evitar o problema do desaparecimento do gradiente e introduzir não linearidade ao modelo, permitindo a captura de padrões complexos nos dados.

   - Camadas ocultas: 
     - 1ª camada: Dense com 64 neurônios, função de ativação relu.
     - 2ª camada: Dense com 64 neurônios, função de ativação relu.
     - 3ª camada: Dense com 32 neurônios, função de ativação relu.
     - 4ª camada: Dense com 32 neurônios, função de ativação relu.
       
   - Camada de saída: 1 neurônio, ativação Sigmoid: A camada de saída foi configurada com 1 neurônio utilizando a função de ativação Sigmoid, ideal para problemas de classificação binária, como a detecção de fraudes (fraude ou não fraude). A função Sigmoid converte as saídas em probabilidades entre 0 e 1, permitindo uma interpretação direta como a probabilidade de uma instância ser fraudulenta.

2. Normalização e Regularização:
   - BatchNormalization: Aplicada após cada camada densa: A normalização por batch foi introduzida após cada camada densa para estabilizar o processo de aprendizado e acelerar a convergência. Essa técnica ajuda a mitigar a variação das ativações ao longo das camadas, tornando o treinamento mais eficiente e reduzindo o impacto de inicializações aleatórias dos pesos.
   - Dropout: Taxa de 20% (0.2) após cada camada densa: A regularização com Dropout foi implementada para prevenir overfitting, um problema comum em modelos complexos como redes neurais. Com uma taxa de 20%, o Dropout desativa aleatoriamente 20% dos neurônios em cada camada durante o treinamento, forçando o modelo a aprender representações mais generalizadas dos dados e não se tornar excessivamente dependente de neurônios específicos.

3. Função de Perda: Binary Crossentropy: Adequada para classificação binária: A função de perda escolhida, binary_crossentropy, é ideal para problemas de classificação binária. Ela mede a divergência entre as previsões do modelo e os rótulos reais, penalizando mais as previsões que estão longe das reais. Isso é essencial para treinar o modelo a distinguir claramente entre fraudes e não fraudes.

4. Otimização:
   - Otimizador: Taxa de aprendizado (learning_rate) de 0.01: O otimizador Adam foi selecionado por sua eficiência e capacidade de ajustar dinamicamente as taxas de aprendizado para diferentes parâmetros durante o treinamento. Com uma taxa de aprendizado inicial de 0.01, o modelo é capaz de realizar atualizações suficientemente rápidas para melhorar seu desempenho, sem que o aprendizado se torne instável. Adam combina as vantagens.

5. Métricas:
   - Métricas de Avaliação
* Acurácia: Mede a proporção de previsões corretas feitas pelo modelo, sendo uma métrica básica para avaliar o desempenho geral.
* Recall: Focado na capacidade do modelo de identificar fraudes, o recall é crucial, dado que o objetivo é maximizar a detecção de fraudes sem deixar casos não detectados.
* F1-Score: Fornece um equilíbrio entre precisão e recall, especialmente importante em cenários onde a distribuição de classes é desbalanceada, como no caso das fraudes.


A escolha cuidadosa desses hiperparâmetros foi guiada pela necessidade de construir um modelo que não apenas apresente bons resultados em dados de treinamento, mas que também generalize bem para novos dados. A arquitetura da rede foi projetada para capturar a complexidade dos padrões de consumo de água, enquanto as técnicas de regularização garantem que o modelo seja robusto e não superestime sua capacidade de detecção. A combinação de uma função de perda apropriada, um otimizador eficiente e métricas de avaliação cuidadosamente escolhidas reflete a intenção de maximizar a eficácia do modelo no ambiente operacional da Aegean Saneamento.

# Análise Preliminar
Os resultados preliminares obtidos a partir do modelo de rede neural desenvolvido para a detecção de fraudes no consumo de água indicam um desempenho promissor, porém com áreas que necessitam de melhorias para alcançar um nível de eficácia mais elevado. A seguir, são detalhadas as principais observações com base nas métricas apresentadas.

### Acurácia:
O modelo apresentou uma acurácia de 66% ao longo das 100 épocas de treinamento. Embora este valor seja um indicativo de que o modelo está conseguindo classificar corretamente uma boa parte das instâncias, é crucial notar que, em problemas de detecção de fraudes, a acurácia por si só pode não ser suficiente para avaliar o desempenho do modelo devido ao possível desbalanceamento das classes. Isso se deve ao fato de que a acurácia pode ser alta mesmo se o modelo estiver apenas identificando corretamente as instâncias da classe majoritária.

### Recall:
O recall, que mede a capacidade do modelo de identificar todas as fraudes no conjunto de dados, foi registrado em 57,59%. Este resultado sugere que o modelo ainda está deixando de identificar cerca de 42,41% das fraudes, o que é uma lacuna significativa, especialmente considerando o impacto financeiro e operacional que essas fraudes podem ter sobre a Aegean Saneamento. Melhorar o recall é, portanto, uma prioridade para futuras iterações do modelo.

### F1-Score:
O F1-Score, que é uma métrica que combina precisão e recall para fornecer uma visão equilibrada do desempenho do modelo, foi registrado em 0,6678. Embora esse valor mostre que o modelo está conseguindo manter um equilíbrio razoável entre a detecção de fraudes e a minimização de falsos positivos, ele também indica que há espaço para melhorias, especialmente em relação ao recall.

### Função de Perda:
A função de perda (binary_crossentropy) mostrou uma diminuição consistente ao longo das épocas, o que é um sinal de que o modelo está aprendendo. No entanto, a taxa de decaimento da perda parece ter se estabilizado, sugerindo que o modelo pode estar próximo de seu ponto de saturação com os parâmetros atuais. Isso indica que ajustes adicionais nos hiperparâmetros, ou mesmo na arquitetura do modelo, podem ser necessários para avançar o desempenho.

### Estrutura do Modelo: 
O modelo é composto por uma série de camadas densas, cada uma seguida por normalização por batch e camadas de dropout. Essa arquitetura foi projetada para capturar a complexidade dos dados enquanto mitiga os riscos de overfitting. Com 115.296 parâmetros treináveis, o modelo é suficientemente complexo para lidar com o volume de dados, mas ao mesmo tempo gerenciável, evitando um aumento excessivo do tempo de treinamento ou a perda de generalização.


# Conclusão
A documentação aqui apresentada detalha o desenvolvimento e a implementação de um modelo de rede neural para a detecção de fraudes no consumo de água, uma problemática crítica enfrentada pela Aegean Saneamento. Através de uma abordagem sistemática e orientada por boas práticas de aprendizado de máquina, foi possível criar um modelo robusto, capaz de capturar padrões complexos nos dados históricos da empresa.

Em resumo, os resultados preliminares indicam que o modelo possui uma base sólida, mas melhorias são necessárias, especialmente no que diz respeito ao recall, para garantir que ele seja capaz de identificar uma maior proporção de fraudes. Recomenda-se a realização de ajustes nos hiperparâmetros, possivelmente combinados com técnicas de balanceamento de classes e experimentação com outras arquiteturas, como redes neurais recorrentes ou convolucionais, para explorar diferentes aspectos dos dados.

Esses ajustes são essenciais para garantir que a Aegean Saneamento possa contar com um modelo robusto e eficaz na detecção de fraudes, minimizando as perdas financeiras e melhorando a eficiência operacional da empresa.
