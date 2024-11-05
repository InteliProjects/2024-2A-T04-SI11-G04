


# Documentação de Projeto



## INSTITUTO DE TECNOLOGIA E LIDERANÇA – INTELI



### Previsão de Fraudes do consumo de água 

#### Parceiro de projeto: AEGEA


#### Autores: 

Gabriela de Morais da Silva

Gustavo Monteiro

Kathlyn Diwan

Rafael Lupovici Moritz

Rodrigo Moraes Martins

Vitor Moura de Oliveira


#### Data de criação: 08 de Outubro de 2024


#### SÃO PAULO – SP, 2024

___________________________________________________________________________________________________________________________________________________________________

## Sumário

1. [Introdução](#c1)

2. [Descrição do Problema](#c2)

3. [Objetivos](#c3)

4. [Sobre a Empresa Parceira](#c4)

    4.1 Benefícios Esperados para o Parceiro

5. [Escopo Macro](#c5)

6. [Análise de Negócios](#c6)
    
    6.1 Canvas Proposta de Valor
    
    6.2 Matriz de Risco

    6.3 Análise PESTEL e Business Model Canvas

    6.4 Análise Financeira: Investimento Estratégico para o Futuro
    
7. [Análise de Experiência do Usuário](#c7)
    
    7.1 Personas, antipersonas e jornada do usuário
    
    7.2 User Story, Requisitos Funcionais, Requisitos não Funcionais e Persona Afetada

8. [Wireframe da Solução](#c8)

9. [Protótipo de Alta Fidelidade da Interface](#c9)

10. [Front-End da Solução](#c10)

11. [API de Integração](#c11)

12. [Documentação Técnica](#c12)

    12.1 Arquivos de Configuração

    12.2 Arquitetura do Projeto

    12.3 Pré-processamento dos Dados

    12.4 Validação do Modelo

13. [Implantação da API](#c13)

14. [Referências](#c14)

___________________________________________________________________________________________________________________________________________________________________

# <a name="c1"></a>1. Introdução
&emsp;&emsp;A detecção de fraudes no consumo de água é uma questão crítica para a eficiência e sustentabilidade dos recursos hídricos. Este documento apresenta uma abordagem inovadora utilizando técnicas avançadas de deep learning para identificar padrões anômalos no consumo de água. A metodologia inclui a análise de dados históricos de consumo e a integração de variáveis externas, como índices macroeconômicos, climáticos e geográficos, com o objetivo de aumentar a precisão das detecções.

&emsp;&emsp;Além de detalhar os resultados obtidos pelos modelos de deep learning, esta documentação explora as principais variáveis que influenciam a detecção de fraudes, oferecendo insights acionáveis que justificam as previsões feitas pelo modelo. Para garantir que os resultados sejam tangíveis e práticos para os usuários finais, desenvolvemos uma interface amigável e intuitiva, que apresenta as previsões de fraude de maneira clara e acessível.

# <a name="c2"></a>2. Descrição do Problema
&emsp;&emsp;A fraude no consumo de água representa um desafio significativo para a Aegea e outras empresas do setor de saneamento básico. Essa prática ilícita afeta tanto o faturamento e a arrecadação da empresa quanto a qualidade do serviço de abastecimento de água. As fraudes ocorrem quando consumidores manipulam hidrômetros, realizam ligações clandestinas ou adotam qualquer forma de adulteração que reduza ou elimine os valores cobrados pelo consumo real.

&emsp;&emsp;Essas práticas fraudulentas resultam em diversos impactos negativos, como danos às tubulações, vazamentos, intermitência no abastecimento, redução de receita e aumento do risco de contaminação da água. Para combater esse problema, a Aegea já adota diversas estratégias, incluindo a verificação de padrões de consumo e a atuação de equipes especializadas em fiscalização. No entanto, existe a necessidade de aprimorar a assertividade dessas ações através do desenvolvimento de uma aplicação baseada em Machine Learning para detectar fraudes de forma mais eficaz.

# <a name="c3"></a>3. Objetivos
&emsp;&emsp;O principal objetivo deste projeto é determinar a probabilidade de um comportamento de consumo ser fraudulento ou não, utilizando dados históricos de consumo e considerando, se necessário, variáveis exógenas como índices macroeconômicos, climáticos e geográficos. O modelo de Machine Learning desenvolvido deve ser capaz de identificar as variáveis mais relevantes para a detecção de fraudes, proporcionando maior precisão e explicabilidade. <br>

# <a name="c4"></a>4. Sobre a Empresa Parceira
&emsp;&emsp;A Aegea é a líder no setor privado de saneamento básico no Brasil, operando em 507 municípios e atendendo aproximadamente 31 milhões de pessoas de norte a sul do país. Com um compromisso firme com a sustentabilidade e a inovação, a Aegea se dedica a melhorar a saúde, a qualidade de vida e a dignidade das comunidades que atende. Além de fornecer serviços de tratamento e distribuição de água e esgotamento sanitário, a empresa busca constantemente inovar para contribuir de forma mais ampla com a sociedade.

## 4.1 Benefícios Esperados para o Parceiro

- Melhoria na Detecção de Fraudes: Aumentar a capacidade de identificar e prever fraudes no consumo de água, utilizando dados históricos e variáveis exógenas.
- Compreensão Profunda: Entender melhor os elementos que influenciam a detecção e predição de fraudes, permitindo ações mais assertivas.
- Tomada de Decisão Informada: Fornecer insights valiosos para usuários técnicos e de negócios, facilitando a tomada de decisões estratégicas e operacionais.
- Eficiência Operacional: Aumentar a eficácia das equipes de campo responsáveis pela detecção e remediação de fraudes, garantindo um serviço de abastecimento de água mais confiável e seguro.

# <a name="c5"></a>5. Escopo Macro

&emsp;&emsp;O projeto visa desenvolver um modelo preditivo que seja capaz de selecionar as variáveis mais relevantes para a detecção de fraudes, proporcionando alta precisão e explicabilidade. Além dos dados históricos, o modelo poderá incorporar variáveis externas, como indicadores macroeconômicos, climáticos e geográficos, para entender seus impactos na probabilidade de fraudes.

&emsp;&emsp;O público-alvo do projeto inclui usuários técnicos, responsáveis pela execução dos algoritmos, e usuários de negócios, que utilizarão os insights para decisões estratégicas. Os resultados do modelo também afetarão diretamente as atividades das equipes de campo, melhorando a eficiência e a assertividade na detecção e remediação de fraudes.

# <a name="c6"></a>6. Análise de Negócios

&emsp;&emsp;A aplicação de ferramentas de análise de negócio é fundamental para o sucesso e a sustentabilidade das organizações em um ambiente competitivo. Essas ferramentas permitem uma compreensão profunda e abrangente do mercado e do ambiente empresarial, levando em consideração uma variedade de fatores internos e externos.

### 6.1 Canvas Proposta de Valor

&emsp;&emsp;O Canvas de Proposta de Valor é uma ferramenta estratégica utilizada para descrever e analisar de forma concisa a proposta de valor de um produto ou serviço, fornecendo uma compreensão clara do que diferencia e agrega valor para o cliente. Este modelo organiza as principais características e benefícios oferecidos para o agente da AEGEA pela solução, identifica as suas necessidades e desejos como cliente-alvo, e ajuda a criar uma proposição que responde diretamente a essas demandas.

![image](https://github.com/user-attachments/assets/8d7b27c4-78cb-490c-8957-8ae90757e2cf)

**Figura 1:**  Canva Proposta de Valor <br> 
**Fonte**: Elaboração própria 
 
### 6.2 Matriz de Risco
  
&emsp;&emsp;Diante a influência de diferentes variáveis, o desenvolvimento de um projeto fica suscetível a riscos internos e externos, necessitando ações para mitigar os impactos desses riscos (Rodrigues, 2019). Para isso, a elaboração de uma matriz de risco, indicando os riscos mapeados e o plano de ação para cada risco e um integrante responsável pode trazer mais segurança para o alcance dos objetivos definidos do projeto. 

| Risco                              | Identificação | Descrição                                                                                                                                  | Impacto                                                                                          | Mitigação                                                                                 | Responsável |
|------------------------------------|---------------|----------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|-------------|
| Ineficácia do Modelo Preditivo      | 1             | O modelo de rede neural pode não atingir o nível esperado de precisão na detecção de fraudes.                                                 | Baixa efetividade na detecção de fraudes e desperdício de recursos.                             | Validação cruzada rigorosa, ajuste de hiperparâmetros e inclusão de variáveis relevantes. | Gustavo     |
| Segurança de Dados                  | 2             | Vazamento de dados sensíveis durante o processo de coleta, armazenamento, ou análise dos dados.                                                | Comprometimento da privacidade, sanções regulatórias, e danos à reputação.                      | Controle de acesso rigoroso e monitoramento contínuo.                                     | Gabriela    |
| Integração dos Dados                | 3             | Dificuldades na integração das bases de dados 'Consumo_medido' e 'Fraudes'.                                                                   | Redução na acurácia do modelo e dificuldades em gerar insights confiáveis.                      | Revisão e limpeza de dados, validação de fontes, e testes de integração.                 | Vitor       |
| Inconsistência nos Dados            | 4             | Dados inconsistentes ou incompletos podem comprometer a precisão do modelo.                                                                    | Dados imprecisos podem levar a resultados incorretos.                                          | Estabelecimento de processos rigorosos de limpeza e verificação de dados.                 | Rafael      |
| Escalabilidade do Modelo            | 5             | O modelo pode não escalar adequadamente com o aumento do volume de dados.                                                                      | O modelo pode não ser capaz de lidar com grandes volumes de dados.                              | Adoção de técnicas de otimização e escalabilidade do modelo.                              | Rodrigo     |
| Falhas de Implementação             | 6             | Erros durante a implementação do modelo podem levar a resultados incorretos.                                                                   | Possíveis falhas ou bugs podem comprometer a funcionalidade do modelo.                         | Testes e revisões antes da implementação.                                                 | Kathlyn     |
| Complexidade do Modelo              | 7             | Um modelo muito complexo pode ser difícil de entender e manter.                                                                               | A dificuldade de manutenção e baixa usabilidade podem resultar em falhas ou uso incorreto.     | Simplificação do modelo, documentação clara e feedback contínuo com stakeholders.        | Gustavo     |
| Desempenho do Sistema               | 8             | O sistema pode não ter capacidade computacional suficiente para processar o modelo eficientemente.                                             | O sistema pode não executar o modelo de forma eficiente.                                       | Investimento em infraestrutura adequada para suportar o modelo e crescimento da AEGEA.    | Gabriela    |
| Sobrecarga de Dados                 | 9             | O excesso de variáveis pode dificultar a identificação das variáveis mais relevantes.                                                          | Identificação de variáveis-chave será comprometida, afetando a precisão.                        | Análise cuidadosa para identificar as variáveis mais impactantes e feedback contínuo com stakeholders. | Vitor       |
| Desvios de Objetivos                | 10            | Mudanças nos objetivos do projeto podem desviar o foco e comprometer os resultados.                                                           | O foco do projeto pode ser perdido, comprometendo o sucesso.                                   | Planejamento e gestão rigorosa do escopo do projeto.                                      | Rodrigo     |

### Tabela de Oportunidades

| Oportunidade                              | Descrição                                                                                          | Benefício                                                                                      |
|-------------------------------------------|----------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| 1. Expansão para Outras Áreas de Atuação   | Expandir a tecnologia de previsão de fraudes para outros serviços oferecidos pela Aegea, como esgoto e coleta de lixo. | Aumenta a eficiência operacional e valor agregado dos serviços, além de gerar novos insights. |
| 2. Monetização do Modelo como Serviço (SaaS) | Comercializar o modelo de previsão de fraudes como um serviço para outras empresas de saneamento.  | Geração de nova fonte de receita e posicionamento da Aegea como líder em inovação tecnológica. |
| 3. Desenvolvimento de Novos Indicadores de Desempenho | Criar novos indicadores de desempenho baseados nos dados coletados, melhorando a tomada de decisões estratégicas. | Melhora a qualidade das decisões e a eficácia das operações, além de agregar valor às análises. |

### 6.3 Análise PESTEL


&emsp;&emsp;Com o objetivo de compreender o contexto externo e identificar os fatores que podem influenciar o sucesso do projeto de previsão de fraudes, a análise PESTEL é uma ferramenta útil para identificar e analisar os fatores macroambientais que podem impactar o negócio. Essa ferramenta permite avaliar os aspectos políticos, econômicos, sociais, tecnológicos, ecológicos e legais. 

&emsp;&emsp;Ao longo deste documento, cada uma dessas dimensões será explorada, apresentando principais questões levantadas, respostas encontradas e implicações para o projeto. O intuito é fornecer uma base para a tomada de decisões estratégicas, permitindo à Aegea identificar oportunidades e mitigar riscos.

&emsp;&emsp;A tabela a seguir apresenta um resumo dos principais fatores identificados em cada dimensão da análise PESTEL. 

|   |   |
|---|---|
| **${\color{Green}Fatores}$ ${\color{Green}Políticos}$** | **${\color{orchid}Fatores}$ ${\color{orchid}Econômicos}$** |
| <ul><li> O setor de saneamento básico no Brasil é regulamentado por diversas leis e normas governamentais, sendo as principais a Lei nº 11.445/2007 (Lei de Saneamento Básico) e o Novo Marco Legal do Saneamento Básico (Lei nº 14.026/2020). </li><li> O governo brasileiro oferece incentivos fiscais para empresas que investem em pesquisa e desenvolvimento de tecnologias inovadoras. </li><li> O Novo Marco Legal do Saneamento Básico incentiva a formação de PPPs para a prestação de serviços de saneamento. </li></ul>  | <ul><li> O Brasil enfrenta desafios econômicos, incluindo alta inflação e taxas de juros elevadas, que afetam a capacidade de investimento das empresas. </li><li> A inflação elevada pode reduzir o poder de compra dos consumidores, levando a práticas fraudulentas. Taxas de juros altas aumentam os custos de financiamento. </li><li> Com o Novo Marco Legal do Saneamento Básico, espera-se um aumento significativo nos investimentos no setor. </li></ul> |
| **${\color{Aquamarine}Fatores}$ ${\color{Aquamarine}Sociais}$** | **${\color{RubineRed}Fatores}$ ${\color{RubineRed}Tecnológicos}$** |
| <ul><li> A conscientização sobre o uso responsável da água está crescendo no Brasil, mas é necessário verificar a efetividade sobre pessoas que fraudam, já que as campanhas podem reduzir o gasto apenas para economizar na conta, e não para economizar um recurso natural e evitar ilegalidades. </li><li> Usuários que podem não conseguir pagar as contas podem necessitar um contato mais direto para regularizar a matrícula antes do acúmulo de dívidas para evitar práticas fraudulentas. </li></ul> | <ul><li> Tecnologias emergentes como IoT (Internet das Coisas), IA e Machine Learning podem ser utilizadas para monitorar o consumo de água em tempo real e identificar padrões anômalos. </li><li> IA e Machine Learning podem ser aplicados para analisar grandes volumes de dados históricos de consumo e identificar padrões que indicam fraudes. </li><li> Limitações como a infraestrutura de TI existente, a qualidade e a integridade dos dados, e a necessidade de capacitação dos funcionários. </li></ul> |
| **${\color{Mahogany}Fatores}$ ${\color{Mahogany}Ambientais}$** | **${\color{CadetBlue}Fatores}$ ${\color{CadetBlue}Legais}$** |
| <ul><li> O projeto pode contribuir para a sustentabilidade ambiental ao reduzir perdas de água causadas por fraudes, melhorar a eficiência no uso dos recursos hídricos e garantir a distribuição adequada de água tratada. </li><li> Fraudes no consumo de água podem levar a vazamentos e desperdícios significativos, afetando a disponibilidade de recursos hídricos. </li><li> Regulamentações como a Política Nacional de Recursos Hídricos (Lei nº 9.433/1997) e a Resolução CONAMA nº 357/2005. </li></ul> | <ul><li> As principais leis que regem o setor de saneamento básico no Brasil são a Lei nº 11.445/2007 (Lei de Saneamento Básico) e o Novo Marco Legal do Saneamento Básico (Lei nº 14.026/2020). </li><li> Práticas fraudulentas podem ser enquadradas em legislações sobre crimes contra o patrimônio e estelionato, conforme o Código Penal Brasileiro (Decreto-Lei nº 2.848/1940). </li><li> A Aegea deve garantir a conformidade com a Lei Geral de Proteção de Dados (LGPD - Lei nº 13.709/2018). </li></ul> |

Tabela 1. Análise PESTEL.

&emsp;&emsp;Para uma análise mais detalhada de cada fator e suas implicações, consulte as seções subsequentes deste documento, bem como a conclusão da análise PESTEL para esse projeto.
_______________________________________________________________________
### 1. Fator Político

&emsp;&emsp;O fator político engloba as leis, regulamentações e políticas governamentais que influenciam o setor de saneamento básico, onde políticas públicas relacionadas à gestão de recursos hídricos, incentivos fiscais para inovação e a regulamentação de parcerias público-privadas podem impactar diretamente as estratégias de detecção de fraudes e a viabilidade do projeto.

#### Brainstorming de Perguntas

- Quais são as políticas governamentais e regulamentações que afetam o setor de saneamento básico no Brasil?

&emsp;&emsp; O setor de saneamento básico no Brasil é regulamentado pela Lei nº 11.445/2007 (Lei de Saneamento Básico) e pelo Novo Marco Legal do Saneamento Básico (Lei nº 14.026/2020). Estas leis estabelecem diretrizes nacionais para o saneamento básico, promovendo a universalização e a melhoria dos serviços.

Referência:
[Lei nº 11.445/2007](http://www.planalto.gov.br/ccivil_03/_ato2007-2010/2007/lei/l11445.htm), 
[Lei nº 14.026/2020](http://www.planalto.gov.br/ccivil_03/_ato2019-2022/2020/lei/L14026.htm)

- Há algum subsídio ou incentivo governamental para empresas que investem em tecnologia para melhorar a detecção de fraudes?

&emsp;&emsp; Sim, o governo brasileiro oferece incentivos fiscais para empresas que investem em pesquisa e desenvolvimento de tecnologias inovadoras. Um exemplo é a Lei do Bem (Lei nº 11.196/2005), que concede benefícios fiscais para atividades de inovação tecnológica.

Referência:
[Lei do Bem](http://www.planalto.gov.br/ccivil_03/_ato2004-2006/2005/lei/l11196.htm)

- Existem parcerias público-privadas que podem influenciar o projeto?

&emsp;&emsp; Sim, o Novo Marco Legal do Saneamento Básico incentiva a formação de parcerias público-privadas (PPPs) para a prestação de serviços de saneamento. Essas parcerias podem trazer investimentos e tecnologias que auxiliam na detecção de fraudes.

Referência:
[Novo Marco Legal do Saneamento Básico](http://www.planalto.gov.br/ccivil_03/_ato2019-2022/2020/lei/L14026.htm)

#### Regulamentações do Setor de Saneamento Básico

**Descrição:** O setor de saneamento básico no Brasil é regulamentado por diversas leis e normas governamentais, sendo as principais a Lei nº 11.445/2007 (Lei de Saneamento Básico) e o Novo Marco Legal do Saneamento Básico (Lei nº 14.026/2020).

**Exemplos:**
* A Lei nº 11.445/2007 define as diretrizes nacionais para o saneamento básico.
* A Lei nº 14.026/2020 atualiza o marco legal, promovendo a participação da iniciativa privada e estabelecendo metas de universalização até 2033.

**Impacto:** Positivo - As regulamentações promovem a melhoria dos serviços e incentivam a inovação.
**Probabilidade de Impacto:** Alta

**Estratégia e Plano de Ação:**
* **Aproveitar a Oportunidade:** 
  * Manter conformidade com as leis e aproveitar incentivos para inovação.
  * Implementar práticas de conformidade rigorosas e investir em tecnologias inovadoras.
* **Sucesso Pretendido:** Obtenção de financiamento e apoio para a implementação do projeto.

#### Subsídios e Incentivos Governamentais

**Descrição:** O governo brasileiro oferece incentivos fiscais para empresas que investem em pesquisa e desenvolvimento de tecnologias inovadoras.

**Exemplos:**
* Empresas que investem em tecnologias para detecção de fraudes no consumo de água podem se beneficiar de deduções fiscais e reduções de impostos conforme a Lei do Bem.
* Outro exemplo é o Programa de Parcerias de Investimentos (PPI).

**Impacto:** Positivo - Redução de custos através de incentivos fiscais.
**Probabilidade de Impacto:** Alta

**Estratégia e Plano de Ação:**
* **Aproveitar a Oportunidade:** 
  * Submeter projetos de inovação tecnológica para obter benefícios fiscais.
  * Consultar especialistas em incentivos fiscais e manter-se atualizado sobre novas oportunidades.
* **Sucesso Pretendido:** Redução de custos operacionais e aumento da viabilidade econômica do projeto.

#### Parcerias Público-Privadas (PPPs)

**Descrição:** O Novo Marco Legal do Saneamento Básico incentiva a formação de PPPs para a prestação de serviços de saneamento.

**Exemplos:** A Aegea pode estabelecer PPPs para financiar e implementar tecnologias de detecção de fraudes.

**Impacto:** Positivo - Atração de investimentos e tecnologias avançadas.
**Probabilidade de Impacto:** Média

**Estratégia e Plano de Ação:**
* **Aproveitar a Oportunidade:** 
  * Identificar e estabelecer parcerias estratégicas com empresas de tecnologia e instituições de pesquisa.
  * Propor projetos de PPP focados em inovação tecnológica e garantir contratos robustos.
* **Sucesso Pretendido:** Obtenção de financiamento e apoio para a implementação do projeto.

_______________________________________________________________________
### 2. Fator Econômico

&emsp;&emsp;O fator econômico abrange as condições econômicas gerais, como taxas de juros, inflação, crescimento econômico e poder aquisitivo da população. A situação econômica influencia o investimento em tecnologia, o comportamento dos consumidores e a capacidade de pagamento das tarifas, o que pode afetar a incidência de fraudes.

#### Brainstorming de Perguntas

- Qual é a situação econômica atual do Brasil e como ela impacta a capacidade de investimento da Aegea?

&emsp;&emsp; O Brasil enfrenta desafios econômicos, incluindo alta inflação e taxas de juros elevadas. Esses fatores podem afetar a capacidade de investimento da Aegea, pois aumentam os custos de financiamento e reduzem a disponibilidade de recursos para investimentos.

Referência:
[Relatório de Inflação - Banco Central do Brasil](https://www.bcb.gov.br/publicacoes/ri)

- Como as variáveis macroeconômicas, como inflação e taxas de juros, afetam o consumo de água e a incidência de fraudes?

&emsp;&emsp; A inflação elevada pode reduzir o poder de compra dos consumidores, levando alguns a buscar formas de economizar, incluindo práticas fraudulentas. Taxas de juros altas aumentam os custos de financiamento para a empresa, limitando investimentos em tecnologias de detecção de fraudes.

Referência:
[Relatório Focus - Banco Central do Brasil](https://www.bcb.gov.br/publicacoes/focus)

- Quais são as tendências de crescimento econômico no setor de saneamento?

&emsp;&emsp; Com o Novo Marco Legal do Saneamento Básico, espera-se um aumento significativo nos investimentos no setor, visando a universalização dos serviços até 2033. Isso inclui melhorias na infraestrutura e adoção de novas tecnologias.

Referência:
[Novo Marco Legal do Saneamento Básico](https://www.gov.br/cidades/pt-br/assuntos/saneamento/marco-legal-do-saneamento#:~:text=Em%2031%20de%20maio%20de,considerados%20os%20contratos%20em%20vigor.)

#### **Situação Econômica Atual**

**Descrição:** O Brasil enfrenta desafios econômicos, incluindo alta inflação e taxas de juros elevadas, que afetam a capacidade de investimento das empresas.

**Exemplos:**
* A inflação elevada pode aumentar os custos operacionais da Aegea.
* As altas taxas de juros podem dificultar o financiamento de novos projetos.

**Impacto:** Negativo - Aumento dos custos de financiamento e redução da capacidade de investimento.

**Probabilidade de Impacto:** Alta

**Estratégia e Plano de Mitigação:**
* **Mitigar o Impacto:**
  * Diversificar as fontes de financiamento, buscar parcerias financeiras e implementar rigorosos controles de custos.
  * Desenvolver um planejamento financeiro robusto e buscar alternativas de financiamento com taxas mais favoráveis.
* **Prejuízo Evitado:** Redução de recursos disponíveis para o projeto.

#### **Variáveis Macroeconômicas**

**Descrição:** A inflação elevada pode reduzir o poder de compra dos consumidores, levando a práticas fraudulentas. Taxas de juros altas aumentam os custos de financiamento.

**Exemplos:**
* Durante períodos de alta inflação, consumidores podem recorrer a fraudes para reduzir suas contas de água.

**Impacto:** Negativo - Redução de receitas e aumento de fraudes.
**Probabilidade de Impacto:** Alta

**Estratégia e Plano de Mitigação:**
* **Mitigar o Impacto:**
  * Desenvolver campanhas educativas sobre o uso responsável da água e oferecer opções de financiamento e parcelamento de contas.
  * Implementar sistemas de monitoramento contínuo e realizar campanhas educativas sobre os impactos negativos das fraudes.
* **Prejuízo Evitado:** Perdas financeiras significativas e comprometimento da eficiência do sistema de abastecimento de água.

#### **Tendências de Crescimento Econômico**

**Descrição:** Com o Novo Marco Legal do Saneamento Básico, espera-se um aumento significativo nos investimentos no setor.

**Exemplos:** Investimentos em infraestrutura de saneamento e adoção de novas tecnologias.

**Impacto:** Positivo - Melhoria na infraestrutura e adoção de novas tecnologias.
**Probabilidade de Impacto:** Alta

**Estratégia e Plano de Ação:**
* **Aproveitar a Oportunidade:**
  * Planejar e executar projetos de expansão e modernização da infraestrutura, alavancando os investimentos e adotando tecnologias avançadas.
  * Apresentar o projeto a investidores e financiadores, destacando os benefícios econômicos e a contribuição para a universalização dos serviços de saneamento.
* **Sucesso Pretendido:** Atração de investimentos para financiar o desenvolvimento e implementação do projeto.
_______________________________________________________________________
### 3. Fator Social

&emsp;&emsp;Como o fator social engloba as características da sociedade, como cultura, demografia, valores e estilo de vida, a conscientização sobre a importância da água, a aceitação de novas tecnologias e as expectativas dos consumidores em relação aos serviços públicos podem influenciar a adesão a programas de combate às fraudes, ou até mesmo fomentar a clandestinidade.

#### Brainstorming de Perguntas

- Quais são as atitudes e comportamentos da população em relação ao consumo de água e fraudes?

&emsp;&emsp; A conscientização sobre a importância do uso responsável da água está crescendo no Brasil, mas ainda há desafios. Práticas fraudulentas persistem em algumas regiões, influenciadas por fatores socioeconômicos.

Referência:
[Departamento Nacional de Obras Contra as Secas](https://www.gov.br/dnocs/pt-br/assuntos/noticias/consumo-consciente-da-agua-e-base-para-um-futuro-sustentavel)

- Como a conscientização sobre o uso responsável da água pode influenciar o projeto?

&emsp;&emsp; Aumentar a conscientização sobre o uso responsável da água pode reduzir a incidência de fraudes e melhorar a eficácia das medidas de detecção. Campanhas educativas e programas de conscientização podem ser integrados ao projeto.

Referência:
[Campanhas de Conscientização - Agência Nacional de Águas (ANA)](https://www.gov.br/ana/pt-br/assuntos/noticias-e-eventos/noticias/agencia-nacional-de-aguas-e-saneamento-basico-lanca-tema-para-celebracao-do-dia-mundial-da-agua-no-brasil-em-2024)


#### **Atitudes e Comportamentos da População**

**Descrição:** A conscientização sobre o uso responsável da água está crescendo no Brasil, mas é necessário verificar a efetividade sobre pessoas que fraudam, já que as campanhas podem reduzir o gasto apenas para economizar na conta, e não para economizar um recurso natural e evitar ilegalidades.

**Exemplos:** Campanhas de conscientização promovidas pela Agência Nacional de Águas (ANA).

**Impacto:** Positivo ou Negativo - Redução de fraudes com maior conscientização, mas desafios persistentes em algumas áreas.
**Probabilidade de Impacto:** Média

**Estratégia e Plano de Ação:**

* **Aproveitar a Oportunidade:** 
  * Lançar campanhas de conscientização e educar a população sobre os impactos negativos das fraudes e os benefícios do uso responsável da água. 
  * Implementar campanhas de educação e conscientização em comunidades, colaborando com ONGs e instituições educativas.
 
* **Sucesso Pretendido:** Redução da necessidade de práticas fraudulentas e melhoria na eficácia das medidas de detecção.

#### **Medidas para Regularizar Usuários Inadimplentes**

**Descrição:** Usuários que podem não conseguir pagar as contas podem necessitar um contato mais direto para regularizar a matrícula antes do acúmulo de dívidas para evitar práticas fraudulentas.

**Impacto:** Negativo - Escalada de fraudes.
**Probabilidade de Impacto:** Alta

**Estratégia e Plano de Mitigação:**
* **Mitigar o Impacto:**
  * Contactar matrículas com maior índice de inadimplência para evitar recorrer à prática de fraude.
  * Adotar medidas preventivas e não punitivas nos usuários inadimplentes.
* **Prejuízo Evitado:** Reduzir o gasto com reparos na rede de distribuição de água a partir de atividades fraudulentas que podem prejudicar a infraestrutura da distribuição.

_______________________________________________________________________
### 4. Fator Tecnológico

O fator tecnológico abrange as inovações tecnológicas e as tendências tecnológicas que podem impactar o setor, e o desenvolvimento de novas tecnologias para a gestão de redes de água, a análise de dados e a inteligência artificial são cruciais para a detecção e prevenção de fraudes.

#### Brainstorming de Perguntas

- Quais são as tecnologias emergentes que podem ser utilizadas para detectar fraudes no consumo de água?

&emsp;&emsp; Tecnologias emergentes como IoT (Internet das Coisas), inteligência artificial (IA) e aprendizado de máquina (Machine Learning) podem ser utilizadas para monitorar o consumo de água em tempo real e identificar padrões anômalos que indiquem fraudes.

- Como a Inteligência Artificial e o Machine Learning podem ser aplicados no projeto?

&emsp;&emsp; IA e Machine Learning podem ser aplicados para analisar grandes volumes de dados históricos de consumo e identificar padrões que indicam fraudes. Modelos preditivos podem ser treinados para detectar comportamentos anômalos e melhorar a precisão na detecção de fraudes.

- Existem limitações tecnológicas que podem afetar a implementação do projeto?

&emsp;&emsp; Sim, limitações como a infraestrutura de TI existente, a qualidade e a integridade dos dados, e a necessidade de capacitação dos funcionários podem afetar a implementação do projeto.


#### **Tecnologias Emergentes**

**Descrição:** Tecnologias emergentes como IoT (Internet das Coisas), IA e Machine Learning podem ser utilizadas para monitorar o consumo de água em tempo real e identificar padrões anômalos.

**Exemplos:** Sensores IoT instalados em hidrômetros para monitoramento em tempo real.

**Impacto:** Positivo - Melhoria na detecção e prevenção de fraudes.
**Probabilidade de Impacto:** Alta

**Estratégia e Plano de Ação:**
* **Aproveitar a Oportunidade:** 
  * Implementar tecnologias emergentes, como sensores IoT e algoritmos de IA, e realizar treinamentos para capacitar a equipe. 
  * Investir em tecnologias de IoT para coleta de dados em tempo real e desenvolver algoritmos de Machine Learning para análise de dados.
* **Sucesso Pretendido:** Maior precisão e eficiência na detecção de fraudes.

#### **Aplicação de IA e Machine Learning**

**Descrição:** IA e Machine Learning podem ser aplicados para analisar grandes volumes de dados históricos de consumo e identificar padrões que indicam fraudes.

**Exemplos:** Utilização de algoritmos de machine learning para prever fraudes com base em dados históricos.

**Impacto:** Positivo - Aumento da precisão na detecção de fraudes.
**Probabilidade de Impacto:** Alta

**Estratégia e Plano de Ação:**
* **Aproveitar a Oportunidade:** 
  * Investir no desenvolvimento e treinamento de modelos preditivos baseados em IA e Machine Learning para detectar fraudes com maior precisão.
* **Sucesso Pretendido:** Maior precisão e eficiência na detecção de fraudes.

#### **Limitações Tecnológicas**

**Descrição:** Limitações como a infraestrutura de TI existente, a qualidade e a integridade dos dados, e a necessidade de capacitação dos funcionários.

**Exemplos:** A falta de uma infraestrutura de TI robusta pode dificultar a coleta e análise de dados em tempo real.

**Impacto:** Negativo - Desafios na implementação do projeto.
**Probabilidade de Impacto:** Média

**Estratégia e Plano de Mitigação:**
* **Mitigar o Impacto:**
  * Fortalecer a infraestrutura de TI, implementar sistemas de garantia de qualidade de dados e realizar treinamentos contínuos para a equipe. 
  * Investir em infraestrutura de TI robusta e redundante, realizando manutenção e atualizações regulares.
* **Prejuízo Evitado:** Dados imprecisos ou insuficientes e comprometimento da detecção de fraudes.


_______________________________________________________________________
### 5. Fator Ecológico

&emsp;&emsp; O fator ecológico engloba questões ambientais, como mudanças climáticas, escassez de água e regulamentações ambientais, já que a escassez de água pode aumentar a pressão sobre os recursos hídricos e incentivar a prática de fraudes e a mudança do clima pode afetar o comportamento dos consumidores. Além disso, as regulamentações ambientais podem impactar os custos e as operações da empresa.

#### Brainstorming de Perguntas

- Como o projeto pode contribuir para a sustentabilidade ambiental e a conservação dos recursos hídricos?

&emsp;&emsp; O projeto pode contribuir para a sustentabilidade ambiental ao reduzir perdas de água causadas por fraudes, melhorar a eficiência no uso dos recursos hídricos e garantir a distribuição adequada de água tratada.

- Quais são os impactos ecológicos das fraudes no consumo de água?

&emsp;&emsp; Fraudes no consumo de água podem levar a vazamentos e desperdícios significativos, afetando a disponibilidade de recursos hídricos e comprometendo a qualidade da água. Isso pode ter impactos negativos no ecossistema e na saúde pública.

- Existem regulamentações ambientais que devem ser consideradas?

&emsp;&emsp; Sim, regulamentações ambientais como a Política Nacional de Recursos Hídricos (Lei nº 9.433/1997) e a Resolução CONAMA nº 357/2005, que estabelece padrões de qualidade da água, devem ser consideradas no projeto.

Referência:
[Lei nº 9.433/1997](https://www.planalto.gov.br/ccivil_03/leis/l9433.htm), 
[Resolução CONAMA nº 357/2005](https://www.icmbio.gov.br/cepsul/images/stories/legislacao/Resolucao/2005/res_conama_357_2005_classificacao_corpos_agua_rtfcda_altrd_res_393_2007_397_2008_410_2009_430_2011.pdf)

#### **Sustentabilidade Ambiental**

**Descrição:** O projeto pode contribuir para a sustentabilidade ambiental ao reduzir perdas de água causadas por fraudes, melhorar a eficiência no uso dos recursos hídricos e garantir a distribuição adequada de água tratada.

**Exemplos:** Iniciativas como o "Relatório de Sustentabilidade" da Aegea.

**Impacto:** Positivo - Melhoria na eficiência do uso dos recursos hídricos.
**Probabilidade de Impacto:** Alta

**Estratégia e Plano de Ação:**
* **Aproveitar a Oportunidade:** 
  * Promover práticas sustentáveis e divulgar os benefícios ambientais das iniciativas de redução de fraudes. 
  * Divulgar os benefícios ambientais do projeto e buscar certificações e reconhecimentos ambientais.
* **Sucesso Pretendido:** Atração de investidores e parceiros interessados em projetos ecológicos.

#### **Impactos Ecológicos das Fraudes**

**Descrição:** Fraudes no consumo de água podem levar a vazamentos e desperdícios significativos, afetando a disponibilidade de recursos hídricos.

**Exemplos:** Vazamentos causados por ligações clandestinas podem resultar em perda de água potável.

**Impacto:** Negativo - Impactos negativos no ecossistema e na saúde pública.
**Probabilidade de Impacto:** Alta

**Estratégia e Plano de Mitigação:**
* **Mitigar o Impacto:** 
  * Implementar tecnologias de detecção de fraudes e realizar manutenções preventivas para reduzir vazamentos e desperdícios.
* **Prejuízo Evitado:** Comprometimento da infraestrutura de abastecimento e aumento da incidência de fraudes.

#### **Regulamentações Ambientais**

**Descrição:** Regulamentações como a Política Nacional de Recursos Hídricos (Lei nº 9.433/1997) e a Resolução CONAMA nº 357/2005.

**Exemplos:** A Política Nacional de Recursos Hídricos define diretrizes para a gestão sustentável dos recursos hídricos no Brasil.

**Impacto:** Positivo - Proteção e conservação dos recursos hídricos.
**Probabilidade de Impacto:** Alta

**Estratégia e Plano de Ação:**
* **Aproveitar a Oportunidade:** 
  * Garantir conformidade com as regulamentações ambientais e implementar práticas de gestão sustentável dos recursos hídricos. 
  * Planejar antecipadamente para incorporar exigências ambientais e manter-se atualizado sobre as regulamentações ambientais.
* **Sucesso Pretendido:** Redução de custos operacionais.
_______________________________________________________________________
### 6. Fator Legal

&emsp;&emsp;O fator legal abrange as leis e regulamentações específicas do setor, além das leis gerais que podem impactar o negócio. A legislação sobre proteção de dados, propriedade intelectual e responsabilidade civil são importantes para garantir a segurança das informações e proteger a empresa de riscos legais.


#### Brainstorming de Perguntas

- Quais são as leis e regulamentações que regem o setor de saneamento básico no Brasil?

&emsp;&emsp; As principais leis que regem o setor de saneamento básico no Brasil são a Lei nº 11.445/2007 (Lei de Saneamento Básico) e o Novo Marco Legal do Saneamento Básico (Lei nº 14.026/2020).

Referência:
[Lei nº 11.445/2007](http://www.planalto.gov.br/ccivil_03/_ato2007-2010/2007/lei/l11445.htm), 
[Lei nº 14.026/2020](http://www.planalto.gov.br/ccivil_03/_ato2019-2022/2020/lei/L14026.htm)

- Existem leis específicas sobre fraudes no consumo de água?

&emsp;&emsp; Não há leis específicas sobre fraudes no consumo de água, mas práticas fraudulentas podem ser enquadradas em legislações sobre crimes contra o patrimônio e estelionato, conforme o Código Penal Brasileiro (Decreto-Lei nº 2.848/1940).

Referência:
[Código Penal Brasileiro](http://www.planalto.gov.br/ccivil_03/decreto-lei/del2848compilado.htm)

- Quais são as implicações legais para a Aegea ao implementar este projeto?

&emsp;&emsp; A Aegea deve garantir a conformidade com as leis e regulamentações aplicáveis, incluindo a proteção de dados pessoais conforme a Lei Geral de Proteção de Dados (LGPD - Lei nº 13.709/2018) e a obtenção de consentimento dos clientes para o uso de seus dados.

Referência:
[Lei Geral de Proteção de Dados (LGPD)](http://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm)


#### **Leis e Regulamentações**

**Descrição:** As principais leis que regem o setor de saneamento básico no Brasil são a Lei nº 11.445/2007 (Lei de Saneamento Básico) e o Novo Marco Legal do Saneamento Básico (Lei nº 14.026/2020).

**Exemplos:** A Lei nº 11.445/2007 define as diretrizes nacionais para o saneamento básico, enquanto a Lei nº 14.026/2020 atualiza o marco legal.

**Impacto:** Positivo - Diretrizes claras para a prestação de serviços.
**Probabilidade de Impacto:** Alta

**Estratégia e Plano de Ação:**
* **Aproveitar a Oportunidade:** 
  * Implementar políticas de conformidade rigorosas e monitorar continuamente as mudanças regulatórias para garantir adesão às leis.
* **Sucesso Pretendido:** Obtenção de financiamento e apoio para a implementação do projeto.

#### **Leis Específicas sobre Fraudes**

**Descrição:** Práticas fraudulentas podem ser enquadradas em legislações sobre crimes contra o patrimônio e estelionato, conforme o Código Penal Brasileiro (Decreto-Lei nº 2.848/1940).

**Exemplos:** Práticas fraudulentas como adulteração de hidrômetros e ligações clandestinas.

**Impacto:** Positivo - Possibilidade de ação legal contra fraudes.
**Probabilidade de Impacto:** Média

**Estratégia e Plano de Ação:**
* **Aproveitar a Oportunidade:** 
  * Trabalhar em conjunto com as autoridades legais para identificar e processar práticas fraudulentas, reforçando a segurança e a conformidade.
* **Sucesso Pretendido:** Redução da incidência de fraudes e melhoria na eficácia das medidas de detecção.

#### **Implicações Legais**

**Descrição:** A Aegea deve garantir a conformidade com a Lei Geral de Proteção de Dados (LGPD - Lei nº 13.709/2018).

**Exemplos:** Implementar políticas de privacidade e segurança de dados.

**Impacto:** Negativo - Risco de penalidades por não conformidade.
**Probabilidade de Impacto:** Alta

**Estratégia e Plano de Mitigação:**
* **Mitigar o Impacto:** 
  * Realizar auditorias regulares de conformidade, implementar políticas de segurança de dados robustas e capacitar funcionários em práticas de proteção de dados.
* **Prejuízo Evitado:** Aumento de custos de conformidade e mudanças nos processos de coleta e análise de dados.

### Conclusão da Análise PESTEL

&emsp;&emsp;A dimensão socioeconômica destaca a importância de considerar as desigualdades sociais e as dificuldades econômicas que podem provocar condições que fomentam a prática de fraudes. A sensibilidade desse tema exige soluções humanizadas que contemplem a necessidade de acesso à água potável e a importância de educar os consumidores sobre o uso responsável dos recursos hídricos. Medidas punitivas excessivas podem agravar o problema, incentivando a clandestinidade e dificultando o combate às fraudes.

&emsp;&emsp;O aspecto ambiental evidencia a necessidade de um olhar holístico para o problema, considerando os impactos das fraudes na disponibilidade e qualidade dos recursos hídricos. As mudanças climáticas e a crescente escassez hídrica intensificam a relevância de projetos como este, que visam otimizar o uso da água e reduzir perdas.

&emsp;&emsp;Unindo os aspectos ambientais, sociais e econômicos temos uma visão sobre a sustentabilidade do negócio e o uso dos recursos naturais, bem como o impacto social que isso causa. Apenas elevar o custo do serviço para evitar escassez pode agravar o problema, assim como buscar investir em infraestrutura pode esgotar mais rápido o uso de recursos naturais. Isso ressalta a importância de enxergar a solução que está sendo desenvolvida, para detectar e prever possíveis fraudes como um apoio à tomada de decisão, e não uma ferramenta punitiva para aumentar a fiscalização.

&emsp;&emsp;A análise legal destaca ainda a importância de navegar em um cenário regulatório complexo e em constante evolução. A proteção de dados, a privacidade e a segurança da informação são aspectos a serem considerados, especialmente com a crescente digitalização dos serviços de saneamento. A relação entre prestador de serviço e consumidor exige transparência e confiança, o que pode ser alcançado através de práticas éticas e de comunicação clara.


### 6.4 Business Model Canvas


![Copy of Arquitetura v2](https://github.com/user-attachments/assets/da2bfc00-6d2d-422c-b19c-a29205737c04)

**Imagem 1:** Business Model Canvas <br> 
**Fonte**: Elaboração própria <br> 
<br> 
<br> 


**Segmentos de Clientes**: Nosso projeto foca em atender empresas no setor de serviços de água, com ênfase em áreas de alto risco de fraude. Esses segmentos incluem empresas de saneamento e abastecimento de água, que gerenciam grandes volumes de consumo e são responsáveis pela integridade dos serviços prestados. A oportunidade de mercado é significativa devido ao potencial de reduzir perdas financeiras e aumentar a eficiência operacional na detecção de fraudes. <br>

**Propostas de Valor**: Nossa solução oferece uma detecção de fraudes no consumo de água mais precisa e eficiente. O sistema identifica padrões suspeitos e sinaliza irregularidades com alta acurácia, permitindo que as visitas de verificação sejam mais direcionadas e eficazes. Isso possibilita que a equipe de campo se concentre apenas nos casos problemáticos, melhorando a eficácia geral das operações de controle e monitoramento. <br> 

**Canais**: Os principais canais para alcançar nossos clientes incluem contratos de concessão e acordos com o governo, além da adesão direta das empresas de saneamento e abastecimento de água. <br> 

**Relacionamento com Clientes**: Estabeleceremos um relacionamento sólido e respeitoso com nossos clientes, dada a natureza sensível da detecção de fraudes. Nossa abordagem será cuidadosa e atenciosa, assegurando que a entrada nas propriedades e a execução das verificações sejam realizadas com máximo respeito e cuidado. Manteremos uma comunicação clara e suporte eficiente para garantir a confiança e satisfação dos clientes. <br> 

**Fontes de Receita**

&emsp;&emsp;A receita será gerada pela melhora na detecção de fraudes, resultando em maior identificação de usuários que não pagam corretamente pelo consumo de água. A economia significativa para a empresa poderá ser convertida em um modelo de compartilhamento de economias ou pagamento por resultados, onde a empresa paga com base na quantidade de fraudes detectadas e recuperadas. Alternativamente, consideraremos tarifas, projetos governamentais e financiamento bancário.<br> 

**Recursos-Chave**: Os principais recursos necessários incluem:

* Plataforma de Detecção: Acesso direto aos funcionários e colaboradores da empresa, integrando o sistema com as operações diárias para monitoramento e identificação de fraudes.
* Dados: Informações necessárias para o treinamento e análise do modelo de detecção de fraudes.
* Infraestrutura de TI: Servidores e sistemas robustos para hospedar e operar a plataforma.
* Equipe Técnica: Especialistas em desenvolvimento de software e análise de dados para assegurar o funcionamento e aprimoramento contínuo do sistema.<br> 

**Atividades-Chave**: As atividades essenciais para o sucesso do modelo de negócios incluem:

* Desenvolvimento e Manutenção: Criação, teste e atualização contínua do sistema de detecção de fraudes.
* Análise e Monitoramento: Avaliação constante dos dados para identificar e abordar novas fraudes.
* Integração e Treinamento: Garantir a integração eficiente do sistema com as operações da empresa e o treinamento adequado da equipe.<br> 

**Parcerias Principais**: 

* Funcionários de Vistoria: Colaboradores responsáveis pela verificação da presença de fraudes nas propriedades e realização das visitas de campo.
* Fornecedores de Tecnologia: Empresas que oferecem suporte tecnológico e infraestrutura necessária para a operação da plataforma.<br> 

**Estrutura de Custos**:
Os principais custos associados à solução incluem:
* Infraestrutura de TI: Investimentos em servidores, armazenamento e manutenção da plataforma.
* Desenvolvimento e Suporte: Despesas com a equipe de desenvolvimento, suporte técnico e manutenção do sistema.
*  Custos Operacionais: Gastos relacionados à equipe de vistoria e outros colaboradores envolvidos no processo de verificação de fraudes. <br> 

### 6.5 Análise Financeira: Investimento Estratégico para o Futuro

**Investimento inicial do parceiro**:O parceiro planeja investir inicialmente R$ 22.000 no projeto. Este montante é alocado principalmente para cobrir os custos de desenvolvimento do MVP, além de outros custos operacionais durante os primeiros meses do projeto.

**1. Dados iniciais da construção do MVP**
- Duração: 10 semanas
- Equipe de desenvolvimento: 6 membros
- Dias trabalhados (por semana): 5 dias
- Horas tarabalhadas por dia: 2 horas
- Custo por hora: R$43.75

**1.1 Cálculo do Custo do MVP:**
- Total de horas por membro: 10 semanas x 5 dias(semana) x 2 horas(dia) = 100 horas
- Total de horas para a equipe: 100 horas/membro x 6 desenvolvedores = 600 horas

Custo total do MVP:
- 600 horas x R$ 43,75 = R$ 26.250

**2.0 Custo da equipe AEGEA:**
Para garantir a manutenção e o desenvolvimento contínuo do projeto na Aegea, a equipe contará com um Desenvolvedor Full Stack e um Engenheiro de Dados Pleno. Além disso, será considerada a contratação de um profissional de QA (Quality Assurance) para garantir a qualidade dos processos de desenvolvimento e entrega.

* Desenvolvedor Full Stack:
- Salário Mensal: R$ 16.000 (Fonte)
- Carga Horária Mensal: 44 horas/semana x 4 semanas = 176 horas/mês

* Engenheiro de Dados Pleno:
- Salário Mensal: R$ 10.000 (Fonte)
- Carga Horária Mensal: 44 horas/semana x 4 semanas = 176 horas/mês

* Profissional de QA:
- Salário Mensal: R$ 8.000 (Fonte)
- Carga Horária Mensal: 44 horas/semana x 4 semanas = 176 horas/mês

**2.1 Total de Custos Mensais com Pessoal:**
* Desenvolvedor Full Stack: R$ 16.000
* Engenheiro de Dados Pleno: R$ 10.000
* Profissional de QA: R$ 8.000

-Custo Total Mensal (Pessoal): R$ 16.000 + R$ 10.000 + R$ 8.000 = R$ 34.000

**3.0 Custo de Infraestrutura - hospedagem e ferramentas em produção:**
* Servidores em Nuvem (AWS, Google Cloud, Azure): Custo médio mensal: R$ 500 a R$ 1.500 (reduzido para otimizar os recursos e uso inicial)
* Banco de Dados em Nuvem (RDS, Firestore):Custo médio mensal: R$ 300 a R$ 1.000
* Armazenamento (S3, Blob Storage): Custo médio mensal: R$ 100 a R$ 400 (reduzido para refletir um uso inicial de dados menor)
* Certificados SSL e Segurança: Custo médio mensal: R$ 50 a R$ 150 (mantido simples inicialmente)
* Monitoramento e Backup:Custo médio mensal: R$ 200 a R$ 500

**3.1 Total de Custos Mensais de Infraestrutura:**
- Custo total mínimo: R$ 500 + R$ 300 + R$ 100 + R$ 50 + R$ 200 = R$ 1.150
- Custo total máximo: R$ 1.500 + R$ 1.000 + R$ 400 + R$ 150 + R$ 500 = R$ 3.550

**4.0 Projeção de Custos Anuais Totais**
Com base nos custos mensais da equipe e infraestrutura, projetamos os custos anuais totais:

Custo Anual com Pessoal: R$ 26.000/mês x 12 meses = R$ 312.000/ano
Custo Anual com Infraestrutura: Mínimo: R$ 13.800/ano - Máximo: R$ 42.600/ano

Total Anual Estimado:
Custo Total Mínimo Anual: R$ 312.000 + R$ 13.800 = R$ 325.800
Custo Total Máximo Anual: R$ 312.000 + R$ 42.600 = R$ 354.600

# Considerações finais: 
Com base na análise financeira apresentada, o parceiro inicialmente projetou um investimento de R$ 22.000 para o desenvolvimento do MVP do projeto. Esse valor cobre os principais custos relacionados ao trabalho da equipe durante as primeiras 10 semanas, bem como estimativas para hospedagem básica em nuvem, conforme necessário.

A projeção de custos anuais foi dividida em duas áreas principais: custos com pessoal e custos de infraestrutura. Para a manutenção e desenvolvimento contínuo do projeto, foi estimado um custo mensal de R$ 26.000 com a equipe composta por um Desenvolvedor Full Stack e um Engenheiro de Dados Pleno. Além disso, para atender à demanda de infraestrutura em produção, foram estimados os custos mensais de R$ 1.150 a R$ 3.550, dependendo do nível de utilização dos recursos em nuvem, o que traz flexibilidade ao orçamento.

No total, os custos anuais estimados variam entre R$ 325.800 e R$ 354.600, dependendo do uso dos recursos de infraestrutura e possíveis ajustes na equipe conforme o projeto evolui. Esses valores refletem a lógica fornecida pelo parceiro, baseada em estimativas de tempo, salários de mercado e os custos de serviços de nuvem mais comuns.

No que se refere às receitas, uma vez que o projeto pode ser interno, e ainda não há projeção de vendas ou receita, não foi necessário incluir uma estimativa de receita. Caso o projeto evolua para um modelo de monetização, essas projeções podem ser ajustadas futuramente, com base no número de clientes e o modelo de negócio que for implementado.

#### Referências utilizadas para a análise financeira

* https://www.locaweb.com.br/blog/temas/codigo-aberto/como-cobrar-pelo-seu-servico-de-freelancer-em-desenvolvimento/
* https://www.glassdoor.com.br/Sal%C3%A1rios/engenheiro-de-dados-pleno-sal%C3%A1rio-SRCH_KO0,25.htm
* https://www.salario.com.br/profissao/engenheiro-de-dados-cbo-212205/
* https://www.glassdoor.com.br/Sal%C3%A1rios/engenheiro-de-dados-sal%C3%A1rio-SRCH_KO0,19.htm
* https://aws.amazon.com/pt/getting-started/hands-on/host-static-website/#:~:text=O%20custo%20total%20da%20hospedagem,%24%200%2C50%20por%20m%C3%AAs.
* https://www.ibm.com/br-pt/cloud/compute?utm_content=SRCWW&p1=Search&p4=43700080053214447&p5=p&p9=58700008709457644&gclid=Cj0KCQjw05i4BhDiARIsAB_2wfDSW6vEr3PvEUNKAjs_6kmc_gTLey_rk8aoeEVBAO94LnPj_cBmgvwaAqw1EALw_wcB&gclsrc=aw.ds
* https://www.glassdoor.com.br/Sal%C3%A1rios/quality-assurance-qa-sal%C3%A1rio-SRCH_KO0,20.htm
* https://www.glassdoor.com.br/Sal%C3%A1rios/qa-analyst-sal%C3%A1rio-SRCH_KO0,10.htm

# <a name="c7"></a>7. Análise de Experiência do Usuário

### 7.1  Personas, antipersonas e jornada do usuário

&emsp;&emsp;No contexto de design e desenvolvimento de soluções, a criação de personas, antipersonas e jornadas do usuário assume um papel de relevância central. A elaboração destas ferramentas proporciona uma visão sobre quem são os usuários, quais são seus objetivos e de que maneira eles podem ser mais eficazmente atendidos.

&emsp;&emsp;Apesar de uma jornada de usuário ser necessária apenas para personas, a anti persona que também irá utilizar a solução também recebeu uma jornada de usuário, visto que ela interage com o sistema e é importante avaliar as ações ao decorrer das interações desta com o sistema de detecção de fraudes.

&emsp;&emsp;A persona e as anti personas possuem os seus atributos nas suas imagens respectivas, mas para facilitar a leitura, as informações também foram escritas no texto deste documento, ressaltando que as <b> ações, ferramentas, necessidades e consquências </b> foram adicionadas apenas no texto respectivo de cada anti persona, a fim de facilitar a leitura e descrição de cada tópico.

### Persona

&emsp;&emsp;Constitui em uma representação fictícia, porém baseada em dados concretos, dos diversos perfis de usuários que irão interagir com o produto ou serviço em desenvolvimento. Ela desempenha a função de guia essencial para as decisões de design, assegurando que o produto seja desenvolvido de maneira a satisfazer de forma precisa as necessidades e expectativas do público-alvo.

### Anti Personas

&emsp;&emsp;Representam perfis de usuários que podem interagir com o produto mas que não fazem parte do público-alvo desejado. Estas figuras são construídas com base em dados e ajudam a equipe a identificar e compreender segmentos de usuários cujas necessidades, objetivos e comportamentos não são alinhados com a proposta do produto. Compreender as antipersonas é crucial para evitar o desperdício de recursos, tempo e esforço em funcionalidades ou soluções que não agregam valor ao objetivo central do projeto. Além disso, as antipersonas permitem à equipe delinear com maior clareza os limites do público-alvo, assegurando que o foco do desenvolvimento permaneça direcionado às prioridades e requisitos que realmente importam. Ao definir quem não é o público-alvo, a equipe pode também identificar possíveis ameaças ou desafios que possam surgir de interações indesejadas ou de mal-entendidos sobre o propósito do produto.

### Jornada do usuário

&emsp;&emsp;As jornadas descrevem o percurso detalhado que os usuários seguem ao interagir com o produto, desde o primeiro ponto de contato até a conclusão de uma tarefa específica. As jornadas são instrumentais para a identificação de pontos de atração e de oportunidades de melhoria, garantindo, assim, uma experiência do usuário que seja fluida, eficiente e alinhada aos objetivos do projeto.

&emsp;&emsp;Para a necessidade deste projeto, foi desenvolvida uma persona que utiliza o sistema desenvolvido, uma anti persona que também utiliza esse sistema, porém de maneira fria voltada apenas para solucionar irregularidades a qualquer custo, e uma outra anti persona que representa um usuário que frauda os serviços fornecidos pela empresa.

## Persona - Nicholas

<p align="center">
<img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G04/blob/main/assets/personaNicholas.png" border="0">
</p>Figura 1. Persona do projeto, desenvolvida pelo grupo para definir um usuário da solução. As informações descritivas da imagem podem ser conferidas no corpo deste documento.

<b> </b>

&emsp;&emsp;Nicholas trabalha na área de compras da AEGEA, uma empresa de saneamento básico. Sua principal preocupação no momento é encontrar maneiras de reduzir o número de fraudes de gatos feitos pela população. O maior problema enfrentado por Nicholas não é o não pagamento das contas de água, mas sim os canos clandestinos que danificam os dutos da empresa e causam vazamentos significativos. Esses vazamentos são a principal fonte de custos para a AEGEA.

### Objetivo

- Reduzir os custos causados por vazamentos.
- Implementar sistemas de detecção e prevenção de fraudes.

### Personalidade

- Realista
- Analítico
- Determinado

### Frase que o descreve

- "Não deixe para amanhã o que você pode fazer hoje."

### Marcas que ele gosta

- Google
- Reserva

### Motivação

- Garantir a sustentabilidade financeira da AEGEA.
- Reduzir o impacto ambiental causado pelos vazamentos.

### Influência

- CNN
- Manual do mundo

### Frustração

- Falta de colaboração da população em denunciar fraudes.
- Complexidade em rastrear a origem dos vazamentos.

### Interesses

- Inteligência artificial
- Iniciativas de conscientização e educação sobre ESG.

## Jornada Nicholas

<p align="center">
<img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G04/blob/main/assets/JornadaNicholas.png" border="0">
</p>Figura 2. Jornada da persona usuária da solução desenvolvida. As informações descritivas da imagem podem ser conferidas no corpo deste documento.

<b> </b>


&emsp;&emsp;Nicholas trabalha na área de compras da AEGEA e está sempre buscando maneiras de otimizar as operações e reduzir os custos causados por vazamentos, sem perder de vista a responsabilidade social e o respeito aos princípios ESG. Ao acessar a solução de previsão de fraudes, ele, inicialmente ansioso e frustrado, começa a navegar pela interface do sistema, que apresenta um painel detalhado com dados sobre o consumo de água e a incidência de fraudes em diversas regiões.

&emsp;&emsp;Durante a análise dos dados, Nicholas percebe que uma determinada região apresenta uma possível fraude no consumo de água. Sentindo-se incerto e preocupado com as implicações, ele adota uma abordagem cuidadosa e ponderada. Reconhecendo os gaps sanitários do Brasil e as dificuldades enfrentadas por muitas comunidades, Nicholas decide enviar uma carta aos consumidores da área afetada. Na carta, a AEGEA explica os riscos e as consequências de realizar fraudes, como os "gatos" de água, tanto para a infraestrutura quanto para a própria comunidade. Ele oferece uma oportunidade para que os consumidores expliquem as razões que levaram ao possível uso de fraudes e propõe uma negociação, sugerindo a possibilidade de uma taxa básica acessível para aqueles que estão em dificuldades financeiras.

&emsp;&emsp;Nicholas acredita firmemente na importância de manter um diálogo aberto e transparente com os consumidores, proporcionando a eles a chance de regularizar a situação sem penalidades imediatas. Ele só considera o corte do fornecimento de água como uma última medida, após esgotar todas as possibilidades de negociação e apoio. Essa abordagem reflete seu profundo respeito pelos princípios de ESG e sua consciência das desigualdades sociais e sanitárias que afetam o Brasil.

&emsp;&emsp;Após o envio da notificação, Nicholas aguarda com apreensão o dia da vistoria. No entanto, sua abordagem cuidadosa acaba por gerar um resultado positivo. Ao final do processo, Nicholas se sente aliviado e satisfeito ao receber o feedback positivo da vistoria. Ele percebe que sua estratégia não só contribuiu para a redução dos custos operacionais a longo prazo, como também minimizou o risco de litígios e críticas públicas, mantendo a AEGEA alinhada com os melhores padrões de governança social e ambiental


## Anti Persona - Mathias

<p align="center">
<img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G04/blob/main/assets/personaMathias.png" border="0">
</p>Figura 3. Primeira Anti Persona do projeto, desenvolvida pelo grupo para definir um usuário da solução. As informações descritivas da imagem podem ser conferidas no corpo deste documento.

<b> </b>

&emsp;&emsp;Mathias é o Gerente de Compras da AEGEA, responsável por tomar decisões estratégicas sobre a distribuição de água e a detecção de fraudes. Ele acredita firmemente na eficácia das soluções automatizadas e tecnológicas, mas possui uma visão enviesada e muitas vezes simplista sobre a complexidade social dos problemas que enfrenta. Mathias tem uma abordagem dura e pragmática, e frequentemente toma decisões rápidas e drásticas, sem considerar o impacto humano e social dessas ações.

### Objetivo

- Reduzir drasticamente as fraudes, utilizando o sistema previsão.
- Cortar custos operacionais, mesmo que isso signifique tomar decisões impopulares.

### Personalidade

- Pragmático
- Inflexível
- Autoritário

### Frase que o descreve

- "Quem quer, faz; quem não quer, arruma desculpa."
- "Quem não deve, não teme."

### Marcas que ele gosta

- Nespresso
- Apple

### Motivação

- Demonstrar a eficiência da empresa no combate às fraudes, reforçando sua imagem de firmeza.
- Garantir a sustentabilidade financeira da AEGEA.

### Influência

- O príncipe de maquiavel
- A arte da guerra
- 
### Frustração

- O jeitinho brasileiro de resolver coisas
- Enfrentar críticas por decisões que afetam negativamente comunidades vulneráveis.

### Interesses

- Automóveis
- Vinhos

### Ações

- Depois de se familiarizar com a solução desenvolvida para identificar fraudes ou possíveis fraudes do sistema de distribuição de água, Mathias começa a buscar usuários que possuem alto potencial de estarem fraudando o sistema.
- Ao identificar uma alta probabilidade de fraude em uma região específica, Mathias instrui sua equipe a cortar imediatamente o fornecimento de água, sem considerar as particularidades sociais e econômicas dos moradores.
- Mathias se propõe a reduzir drasticamente o uso irregular dos serviços da empresa por parte dos usuários.
- Início do aumento do gasto com fiscais para visitar várias casas para corte dos serviços.

### Ferramentas

- Modelo de Rede neural e interface, que destaca informações sobre fraudes, feito pelo grupo 4.
- Acionamento de fiscais da empresa para visitas técnicas.
- Orçamento para realizar as operações.

### Necessidade

- Necessidade de obter resultados rápidos na redução de custos operacionais.
- Acesso aos dados de possíveis fraudadores ou usuários que fraudaram anteriormente.
- Possibilidade de realizar ações por conta própria, sem passar por algum comitê ou aprovação de outra pessoa da empresa.
- Orçamento necessário para realizar diversas visitas técnicas por fiscais.

### Consequência

- Impacto negativo na imagem da AEGEA devido a injustiças sociais causadas pela decisão abrupta.
- Reações adversas da população afetada e da mídia, potencialmente levando a processos legais.
- Preocupações de investidores focados em critérios ESG, comprometendo a sustentabilidade da empresa.
- Alto valor gasto com fiscalizações.
- Potenciais cortes a usuários que usam corretamente o sistema, levando à judicialização de vários processos.
- Maior gasto com advogados da empresa.
- Aumento da quantidade de fraude de pessoas que não utilizam mais o sistema da empresa.
- Intervenção legal para evitar o corte a estabelecimentos específicos.

## Jornada Nicholas

<p align="center"> <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G04/blob/main/assets/jornadaMathias.png" border="0"> </p>Figura 4. Jornada da anti persona usuária da solução desenvolvida. As informações descritivas da imagem podem ser conferidas no corpo deste documento.

<b> </b>

&emsp;&emsp;Mathias confia totalmente no modelo preditivo para identificar fraudes e, ao detectar alta probabilidade de fraude em áreas de alto risco, age de maneira rápida e severa, sem considerar o contexto social ou econômico dos moradores. Ao acessar a solução de previsão de fraudes da AEGEA, ele imediatamente sente a pressão para otimizar as operações e reduzir custos.

&emsp;&emsp;Navegando pelo painel de controle, Mathias se depara com uma região específica de Campo Grande que apresenta alta incidência de fraudes no consumo de água. A análise do modelo preditivo revela um número significativo de ligações clandestinas e manipulação de hidrômetros, aumentando sua frustração e ansiedade. Sentindo-se sobrecarregado pela necessidade de tomar uma decisão rápida, Mathias opta por uma ação enérgica: instruir sua equipe a implementar um corte imediato no fornecimento de água em toda a área identificada como de alto risco.
Ele acredita que essa medida severa enviará uma mensagem clara de que a AEGEA não tolera fraudes, além de reduzir rapidamente os custos operacionais associados a vazamentos e perdas. Sua raiva e determinação crescem à medida que ele se recusa a considerar alternativas menos drásticas, como investigações mais detalhadas ou programas de conscientização.

&emsp;&emsp;Após a implementação dos cortes, Mathias inicialmente comemora o impacto financeiro positivo. No entanto, essa satisfação é rapidamente substituída por frustração e raiva intensa quando ele enfrenta uma forte reação adversa: a população afetada, sentindo-se injustiçada, começa a protestar, ganhando cobertura na mídia local e nacional. Organizações de direitos humanos criticam a AEGEA por sua abordagem insensível, e a reputação da empresa começa a deteriorar.

&emsp;&emsp;Além disso, Mathias se vê envolvido em processos legais e enfrenta pressões de investidores que seguem critérios ESG, preocupados com a falta de responsabilidade social nas decisões da empresa. Embora relutante, ele começa a perceber que sua abordagem inflexível e focada exclusivamente em custos pode ter consequências graves, tanto para a AEGEA quanto para a comunidade.

## Anti Persona - Laiza

<p align="center">
<img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G04/blob/main/assets/personaLaiza.png" border="0">
</p>Figura 5. Segunda Anti Persona do projeto, desenvolvida pelo grupo para definir um usuário fraudador dos serviços prestados pela empresa Aegea. As informações descritivas da imagem podem ser conferidas no corpo deste documento.

<b> </b>

&emsp;&emsp;Laiza, uma senhora de 56 anos, é uma aposentada que mora sozinha em uma casa próxima a um conjunto de casas que ela aluga para diversas pessoas. Sempre em busca de aumentar seu lucro, Laiza estabeleceu o aluguel das casas em R$ 900, já incluindo as contas de água e luz, o que atrai muitos inquilinos. Esse segredo é guardado e ela nunca comenta nada sobre isso com os moradores das casas alugadas. Determinada e pragmática, Laiza faz de tudo para garantir que seus negócios continuem lucrativos, enquanto mantém uma fachada de cordialidade e profissionalismo com seus inquilinos.

&emsp;&emsp;Religiosa e com um espírito oportunista, Laiza navega entre os desafios de seus empreendimentos e a busca por estabilidade financeira, sempre mantendo o foco em seus objetivos.

### Objetivo

- Aumentar o lucro dos negócios reduzindo os gastos fixos com serviços essenciais, como a conta de água.
- Manter preços de aluguel competitivos para atrair mais inquilinos.

### Personalidade

- Oportunista
- Avarenta
- Religiosa

### Frase que o descreve

- "Devo e não nego!."
- “Temos que ser verdadeiros conosco”

### Marcas que ele gosta

- Lojinhas do brás
- Mercadão (nunca compra nada)

### Motivação

- Garantir uma renda adicional, essencial para complementar sua aposentadoria insuficiente.
- Manter a competitividade dos preços dos aluguéis para atrair mais inquilinos e evitar vacância nos imóveis.

### Influência

- Brasil Urgente
- Celso Russomano

### Frustração

- Ela acredita que água deveria ser de graça
- Corte de benefícios do governo
  
### Interesses

- Passeios que dão coisas de graça
- SESC para fazer natação de graça

### Ações

- Laiza decide contratar um pedreiro para construir quartos para alugar dentro de seu terreno.
- O pedreiro sugere que pode ser adicionada uma saída de água antes do registro de água da residência de Laiza para ir aos quartos construídos, de forma que a água para esses locais não seja registrada pela Aegea, configurando uma irregularidade no uso dos serviços, que essa porção da água não será precificada.
- O pedreiro recomenda que isso não seja comentado com ninguém, visto que, por já ter realizado essas alterações em outros projetos, "ninguém fica sabendo".
- Após Laiza aceitar a proposta, a modificação clandestina é realizada, e fica atenta para visitas marcadas pela Aegea, para evitar comentar que foi feita uma construção para aluguel, mantendo nos dados que apenas ela que mora na residência, chamando os inquilinos de "visitas".
- Por seguir recebendo a conta de água com os valores de costume, e o serviço de água se manter, Laiza segue com suas atividades cotidianas e alugando os quartos.

### Ferramentas

- Modificação clandestina na tubulação, realizada durante a construção das novas casas.
- A assistência de um pedreiro que sugeriu e executou a instalação irregular.
- Conhecimento do padrão de manutenção da empresa Aegea, bem como acesso a notificações oficiais de visitas, ou períodos em que as visitas técnicas e fiscalizações podem ser feitas.

### Necessidade

- A ausência de uma fiscalização rigorosa por parte da Aegea permite que modificações clandestinas na tubulação passem despercebidas.
- A existência de profissionais como pedreiros que possuem conhecimento técnico suficiente para realizar instalações clandestinas.
- A necessidade de reduzir custos e aumentar lucros motiva Laiza a aceitar a proposta de modificação clandestina.
- Dificuldade de discernir usuários da rede de água que realizam modificações sem avisar a empresa Aegea.
- Possibilidade de construir e alugar quartos sem registrar em nenhum banco de dados.

### Consequência

- A conta de água não reflete o consumo real, permitindo a Laiza obter maiores lucros com os aluguéis.
- A Aegea sofre perda de receita devido ao consumo de água não contabilizado.
- Se descoberta, Laiza pode enfrentar sanções legais, multas e até processos judiciais.
- A descoberta da fraude pode danificar a reputação de Laiza entre seus inquilinos e na comunidade local.
- A empresa pode precisar aumentar os custos com fiscalização e controle para evitar fraudes similares no futuro.

&emsp;&emsp;Laiza se mudou para sua residência atual ao se casar com seu marido, e foi onde criou seus filhos até crescerem e saírem de casa. Hoje é viúva e mora sozinha. Depende da renda das casas que aluga, já que o valor da sua aposentadoria não é o suficiente para manter os custos e pagar contas.
Ao se mudar para sua residência, a empresa que fornece água, a AEGEA já prestava seus serviços, e foi chamada para manutenções nas tubulações, e como usuária, usufrui da água para atividades cotidianas como cozinhar, banho, lavar a calçada, entre outras coisas.

&emsp;&emsp;Para aumentar o lucro obtido no aluguel das casas, a maneira encontrada por Laiza é de reduzir o gasto com a conta de água, adicionando uma saída de água antes de passar pelo registro da casa, levando água aos quartos que aluga, onde essa água não é medida nem cobrada na conta de água principal, através da irregularidade no uso do serviço da AEGEA.
 
&emsp;&emsp;Laiza acredita que água é um serviço que deve ser utilizado gratuitamente, e possui uma personalidade oportunista que se aproveita de vulnerabilidades e realiza ações que infringem o uso correto dos serviços que contrata se não tiver regulamentação e checagem.

&emsp;&emsp;Quando foi tomada a decisão de construir outras casas no seu terreno, o pedreiro que estava cuidando da parte hidráulica ofereceu a “oportunidade” de adicionar a tubulação para as outras casas a partir do cano de entrada de água antes do registro principal. Após aceitar essa construção irregular, as outras casas foram construídas de forma que a água não seja contabilizada no seu uso total.

&emsp;&emsp;A usuária não percebeu aumento na conta de água e usou isso como uma vantagem para colocar preços mais competitivos, atraindo mais pessoas para as casas que aluga, e obtendo maior lucro por isso.

&emsp;&emsp;Por ser uma modificação realizada de forma clandestina, Laiza imagina que pode ser irregular, não comenta com ninguém na expectativa de não ser descoberta. Como a água é usada apenas em outras casas que foram construídas depois, não vê como errado ou irregular, apenas algo que não foi regularizado. E por seguir usando a água normalmente em sua casa, acredita que essa irregularidade não seria descoberta, e nem causa problemas para a empresa.

## Discussão sobre as Personas e a Anti-Persona

&emsp;&emsp;Após o desenvolvimento e detalhamento das características, atributos e particularidades da persona e anti-personas deste projeto, é possível identificar pontos de conflitos entre elas, onde a persona (Nicholas) e a anti-persona que também utiliza a solução (Mathias) representam a relevância que este projeto possui para a empresa, mas também que a solução em si não é o suficiente para resolver o problema, sendo esta apenas uma ferramenta para dar mais suporte ao processo de detecção de fraude. Devido ao grau de sensibilidade que este projeto demanda, o time de desenvolvimento deve estar ciente da possibilidade de um usuário tomar os resultados obtidos como verdade absoluta e tomar decisões apenas com base nos resultados mostrados, o que ressalta a severidade de falsos positivos, por exemplo, de usuários que não fraudam o sistema, mas que a solução pode erroneamente indicar como fraudadores.

&emsp;&emsp;Além disso, é crucial reconhecer que olhar apenas para os números não é suficiente. Identificar a fraude é apenas um dos passos. A forma como essa fraude é abordada pode ser ainda mais importante do que a própria identificação. É necessário estabelecer processos para lidar com as fraudes identificadas, considerando as implicações éticas, legais e operacionais. Isso inclui desde a comunicação clara com os usuários até a aplicação de medidas corretivas proporcionais e justas, garantindo que o tratamento dado à fraude não apenas resolva o problema, mas também fortaleça a confiança e a relação da empresa com seus clientes.

&emsp;&emsp;Esse aspecto vai de encontro com a outra anti-persona (Laiza), que é uma usuária que frauda os serviços da empresa. O desenvolvimento de um sistema de detecção de fraude aliado a uma abordagem cuidadosa para lidar com as fraudes detectadas, é essencial para o sucesso e a legitimidade da solução.

&emsp;&emsp;Além disso, é importante que o sistema seja transparente e explique claramente os critérios utilizados para a detecção de fraudes. Isso ajuda a mitigar potenciais conflitos e a construir confiança tanto com os usuários que utilizam o serviço de forma legítima quanto com os que são identificados como possíveis fraudadores. Também é fundamental proporcionar um canal de comunicação aberto para que os usuários possam contestar os resultados e fornecer informações adicionais, caso necessário.

&emsp;&emsp;Por fim, o desenvolvimento do sistema deve estar alinhado com as políticas de conformidade da empresa e com a legislação vigente, garantindo que as práticas de detecção de fraude respeitem os direitos dos consumidores e evitem abusos. 


### 7.2  User Story, Requisitos Funcionais, Requisitos não Funcionais e Persona Afetada

&emsp;&emsp;O objetivo de transformar as necessidades dos usuários, definidas nas personas e anti-personas, em tarefas concretas e priorizadas para o desenvolvimento do produto, através de user stories, até a aplicação destas na prototipação da interface que o usuário terá com o sistema com a construção de um wireframe. Para detalhar ainda mais essas necessidades, foram documentados requisitos funcionais (o que o sistema deve fazer) e não funcionais (como o sistema deve funcionar).

&emsp;&emsp;Além disso, considerando a natureza do projeto de detecção de fraudes, identificamos a necessidade de criar uma nova persona: o usuário falsamente acusado. Essa persona representa um usuário legítimo que, por algum erro do sistema, foi identificado como fraudador. Ao incluir essa persona nas user stories, garantimos que o sistema não apenas detecte fraudes, mas também minimize o impacto negativo em usuários legítimos.

&emsp;&emsp;Os requisitos definidos neste documento servirão como base para a criação dos wireframes da interface, que nos permitirão visualizar de forma concreta como as funcionalidades do sistema serão apresentadas ao usuário. 

&emsp;&emsp;E considerando que este projeto lida com dados sensíveis de usuários dos serviços da AEGEA, e tem como propósito detectar possíveis usuários que cometem ilegalidades na utilização de serviços, este projeto deve também garantir a privacidade e a segurança dos dados dos usuários. Para isso, adotamos a abordagem de Privacy by Design, que consiste em integrar a proteção de dados desde o início do desenvolvimento do sistema, em todas as suas etapas, que podem ser verificados no item 5. deste documento. 

#### Requisitos do Sistema de Detecção de Fraudes


&emsp;&emsp;Os requisitos de um software definem as funcionalidades e características que ele deve ter para atender às necessidades dos usuários e aos objetivos do projeto. No caso de um sistema de detecção de fraudes, os requisitos detalham as ações que o sistema precisa realizar e as qualidades que ele deve possuir.


#### Requisitos Funcionais

&emsp;&emsp;Requisitos funcionais descrevem o que o sistema deve fazer, ou seja, as suas funcionalidades. Eles definem as ações que o sistema executará em resposta a entradas específicas. Por exemplo, o requisito "O sistema deve ser capaz de identificar padrões de consumo de água que são característicos de fraudes" é um requisito funcional, pois especifica uma ação concreta que o sistema deve realizar.



* **Detecção de Fraude:**
    * O sistema deve ser capaz de identificar padrões de consumo de água que são característicos de fraudes.
    * O sistema deve utilizar modelos para a predição da probabilidade de fraude em diferentes regiões.
* **Análise de Dados:**
    * O sistema deve permitir a análise de dados históricos de consumo de água e fraudes para identificar tendências e padrões.
    * Deve ser possível visualizar gráficos de densidade de clientes, volume de água consumido por região e distribuição de comportamentos fraudulentos.
* **Interface de Usuário Intuitiva:**
    * O sistema deve ter uma interface de usuário intuitiva que facilite a navegação e a visualização de dados.
    * Deve incluir dashboards com filtragem dos dados que permitam aos usuários visualizar as informações específicas para suas necessidades.


#### Requisitos Não Funcionais


&emsp;&emsp;Requisitos não funcionais descrevem as características qualitativas do sistema, como desempenho, segurança, usabilidade, etc. Eles definem como o sistema deve se comportar. Por exemplo, o requisito "O sistema deve ser capaz de processar grandes volumes de dados" é um requisito não funcional, pois especifica uma característica de desempenho do sistema.


* **Performance:**
    * O sistema deve ser capaz de processar grandes volumes de dados.
    * O tempo de resposta para a detecção de fraudes deve ser inferior a 3 minutos.
* **Segurança:**
    * O sistema deve garantir a segurança dos dados armazenados e transmitidos, implementando criptografia e autenticação robustas.
    * Deve haver controle de acesso baseado em funções, garantindo que apenas usuários autorizados possam acessar dados sensíveis.
* **Escalabilidade:**
    * O sistema deve ser escalável para lidar com o aumento no volume de dados e no número de usuários.
    * Deve suportar a adição de novos sensores e fontes de dados sem degradação de performance.
* **Usabilidade:**
    * O sistema deve ser fácil de usar, com uma curva de aprendizado baixa.
    * Deve incluir documentação completa e suporte técnico para auxiliar os usuários.
* **Legalidade e Conformidade:**
    * O sistema deve estar em conformidade com as leis e regulamentos aplicáveis, incluindo proteção de dados e privacidade.
    * Deve garantir que as práticas de detecção de fraudes respeitem os direitos dos consumidores e evitem abusos.
* **Transparência:**
    * O sistema deve ser transparente em relação aos critérios utilizados para a detecção de fraudes.
    * Deve fornecer explicações sobre os resultados das análises.


#### Persona Afetada - Maria

&emsp;&emsp;Esta persona afetada do projeto foi desenvolvida para definir um usuário erroneamente identificado como fraudador, a fim de auxiliar na elaboração de user stories, sendo uma versão mais resumida em relação ao artefato elaborado anteriormente, para ter uma visão do ponto de vista de um usuário que utiliza o serviço de distribuição de água da empresa, e que pode ser um falso positivo, participando do processo de detecção de fraude da empresa, ao utilizar o sistema de detecção de fraude desenvolvido por este projeto.


### Perfil

&emsp;&emsp;Maria é uma professora aposentada de 68 anos que vive sozinha em sua casa na periferia da cidade. Maria recebe visitas técnicas de manutenção às vezes, normalmente paga suas contas em dia e nunca teve problemas com a empresa fornecedora de água, a AEGEA, mesmo com alguns pagamentos realizados em atraso.

### Objetivo

- Garantir que continue recebendo os serviços contratados.


### Motivação

- Manter seu nome limpo, evitando deixar que as multas das contas se acumulem.

- Garantir que seus direitos como consumidora sejam respeitados.


### Frustração

- Precisar provar que usa os serviços que contrata de forma correta, de forma que necessita guardar comprovantes de contas pagas, protocolos de vistoria, etc.

- A falta de comunicação clara e com empresas de serviços.

### Ações

- Maria recebe uma notificação de que seu consumo de água está suspeito de fraude.
- Sentindo-se injustiçada, ela tenta entrar em contato com a AEGEA para esclarecer a situação.
- Ela coleta seus comprovantes de pagamento e registros de consumo para apresentar como prova.
- Maria aguarda ansiosamente uma resposta da empresa, enquanto continua sua rotina diária, mas com receio de ter seu serviço de água cortado.

### Ferramentas

- Telefone e e-mail para contato com a AEGEA.
- Arquivos e documentos que comprovam o pagamento regular das contas de água.

### Necessidade

- Necessidade de um canal de comunicação acessível para resolver mal-entendidos com a empresa, como envio de comprovantes de pagamento com atraso.
- Transparência por parte da AEGEA sobre os critérios de detecção de fraude.
- Respeito e consideração durante o processo de verificação e resolução do problema.

### Consequência

- Maria passa por um período de estresse e ansiedade devido à falsa acusação com o receio do corte dos serviços contratados.
- A situação gera discussões na comunidade local sobre a precisão e justiça dos sistemas de detecção de fraude.
- A confiança de Maria na AEGEA é abalada, mesmo após a resolução do problema.

### Jornada do Usuário

&emsp;&emsp;Maria, uma professora aposentada, vive sozinha e normalmente paga suas contas em dia, evitando deixar as contas em atraso por mais de 15 dias. Ao receber uma notificação da AEGEA informando que seu consumo de água está sob suspeita de fraude, Maria fica surpresa e preocupada. Sentindo-se injustiçada, ela tenta entrar em contato com a empresa para esclarecer a situação.

&emsp;&emsp;Inicialmente, Maria enfrenta dificuldades para falar com um representante da AEGEA. Ela utiliza o telefone e o e-mail para tentar resolver o problema, mas a falta de respostas claras e rápidas aumenta sua frustração. Determinada a provar sua honestidade, Maria coleta todos os seus comprovantes de pagamento e registros de consumo para apresentar como prova.
Enquanto aguarda uma resposta da empresa, Maria continua sua rotina diária, mas o estresse e a ansiedade causados pela situação afetam seu bem-estar, com o receio de um corte de água. Ela compartilha sua experiência com vizinhos e amigos, gerando discussões na comunidade local sobre a precisão e justiça dos sistemas de detecção de fraude.

&emsp;&emsp;Após algumas semanas, a AEGEA finalmente revisa o caso de Maria e reconhece que houve um erro. A empresa se desculpa pelo transtorno causado e informa que sua conta foi regularizada. Embora aliviada, Maria ainda sente que a confiança na empresa foi abalada, sem entender o que causou isso.

### Discussão sobre a Persona Afetada

&emsp;&emsp;Essa experiência destaca a importância de ter um sistema de detecção de fraudes preciso e de fornecer canais de comunicação claros e eficientes para resolver mal-entendidos. Maria espera que a AEGEA aprenda com essa situação e melhore seus processos para evitar que outros consumidores passem pelo mesmo problema no futuro.

### 7.3 User Story

&emsp;&emsp; Humanizar a experiência do usuário através das personas permite identificar desafios e obstáculos que podem surgir ao interagir com o sistema. Isso permite se as necessidades dos clientes estão sendo atendidas.

&emsp;&emsp;Como dito anteriormente, a persona afetada pelo sistema de detecção de fraudes revelou uma lacuna importante na solução. Por isso, user stories para abordar situações específicas, visando minimizar o impacto negativo causado por falsos positivos e preservar a confiança dos usuários em nosso sistema foi adicionada. 

&emsp;&emsp; Seguem as user stories desenvolvidas para este projeto:


| **Número** 	| User Story 01 | 
|---	|---	|
| **Épico** 	| Análise Exploratória | 
| **Persona** 	| Nicholas	| 
| **User Story** 	| Como analista de dados, quero visualizar gráficos de densidade de clientes, volume de água consumido por região e distribuição de comportamentos fraudulentos, para identificar áreas com maior potencial de ocorrência de fraudes e direcionar as ações de fiscalização. | 
| **Critérios de aceitação** 	| 1. O sistema deve gerar gráficos de densidade populacional, consumo médio por cliente e frequência de ocorrências de fraudes por região. <br> 2. Os gráficos devem ser interativos, permitindo ao usuário filtrar os dados por período e região. | 
| **Prioridade** 	|  Alta | 
| **Estimativa de esforço** 	| Médio | 
| **Comentários** 	| Essa user story é relevante para a análise exploratória dos dados e a identificação de padrões. A interatividade dos gráficos permite que um usuário como Nicholas explore os dados de forma mais aprofundada. | 



| **Número** 	| User Story 02 | 
|---	|---	|
| **Épico** 	| Predição | 
| **Persona** 	| Nicholas	| 
| **User Story** 	| Como analista de dados, quero que o sistema que me permita prever a probabilidade de fraudes em diferentes regiões para que eu possa antecipar e tomar medidas preventivas contra possíveis fraudes. | 
| **Critérios de aceitação** 	| 1. O sistema deve gerar um modelo de previsão com pelo menos 80% de acurácia. <br> 2. O modelo deve considerar variáveis como histórico de consumo, características da região e perfil do cliente. <br> 3. O sistema deve fornecer uma pontuação de risco para cada cliente, indicando a probabilidade de fraude.	| 
| **Prioridade** 	|  Alta | 
| **Estimativa de esforço** 	| Alta  	| 
| **Comentários** 	| A construção e validação de um modelo de previsão exige a coleta e preparação de dados históricos, além da escolha da técnica de redes neurais adequadas. É importante considerar a interpretabilidade do modelo para facilitar a compreensão dos resultados.  | 



| **Número** 	|  User Story 03 | 
|---	|---	|
| **Épico** 	| Desempenho | 
| **Persona** 	| Nicholas	| 
| **User Story** 	| Como analista de dados, preciso que o sistema processe grandes volumes de dados de maneira eficiente e com um tempo de resposta inferior a 2 minutos, para que eu possa tomar decisões com utilização de diferentes filtros nos dados. | 
| **Critérios de aceitação** 	| 1. O sistema deve processar um volume de dados equivalente a 1 ano de histórico em menos de 2 minutos. <br> 2. O sistema deve permitir a aplicação de filtros complexos aos dados sem afetar significativamente o tempo de resposta. <br> 3. O sistema deve utilizar técnicas de indexação para otimizar a busca e recuperação de dados.	| 
| **Prioridade** 	|  Média | 
| **Estimativa de esforço** 	| Alta | 
| **Comentários** 	| A performance do sistema é um fator crítico para a satisfação do usuário e a eficácia da análise de dados. A escolha de ferramentas deve ser direcionada a lidar com grandes volumes de dados e garantir um tempo de resposta rápido. É importante realizar testes de carga para avaliar a capacidade do sistema. | 



| **Número** 	| User Story 04 | 
|---	|---	|
| **Épico** 	| Login e Confidencialidade | 
| **Persona** 	| Nicholas	| 
| **User Story** 	| Como analista de dados, quero realizar login no sistema utilizando minhas credenciais (usuário e senha) para que eu possa acessar as funcionalidades do sistema de forma segura. | 
| **Critérios de aceitação** 	| 1. O sistema deve verificar se as credenciais informadas pelo usuário estão corretas, comparando-as com as cadastradas no banco de dados.  <br /> 2. O sistema deve exibir uma mensagem de erro caso as credenciais sejam inválidas.	| 
| **Prioridade** 	|  Média | 
| **Estimativa de esforço** 	| Médio | 
| **Comentários** 	|  A tela de login é a primeira linha de defesa do sistema, portanto, é crucial garantir a segurança das informações do usuário. Isso pode ser relevante inclusive para registrar todas as ações realizadas pelos usuários no sistema para fins de segurança e compliance. | 



| **Número** 	|  User Story 05 | 
|---	|---	|
| **Épico** 	| Ética no Uso dos Dados | 
| **Persona** 	|  Maria	| 
| **User Story** 	| Como usuária do sistema de distribuição de água da AEGEA, desejo que meus dados sejam utilizados de forma ética e transparente, evitando a generalização e o uso indevido das minhas informações para fins que não sejam relacionados à prestação do serviço. | 
| **Critérios de aceitação** 	| 1. Após utilização dos dados pelo sistema, os dados carregados e as análises geradas devem ser deletadas, não sendo armazenadas pelo sistema.	| 
| **Prioridade** 	|  Alta | 
| **Estimativa de esforço** 	| Média | 
| **Comentários** 	| Os dados do usuário são considerados sensíveis pela LGPD, reforçando a necessidade de um cuidado especial no tratamento, e assim, os dados das análises não serão armazenados após a utilização dos dados. | 



| **Número** 	| User Story 06 | 
|---	|---	|
| **Épico** 	| Ética no Uso dos Dados | 
| **Persona** 	| Maria	| 
| **User Story** 	| Como usuária do sistema de distribuição de água da AEGEA, quero que o processo de detecção de fraudes da AEGEA seja transparente e justo, para evitar ser erroneamente identificada como fraudadora por meio de generalizações. | 
| **Critérios de aceitação** 	| 1. O sistema deve garantir a confidencialidade dos dados pessoais dos clientes.  <br /> 2. O sistema deve reforçar que o seu uso não deve ser utilizado como verdade absoluta, necessitando avaliação de um usuário qualificado	| 
| **Prioridade** 	|  Alta  | 
| **Estimativa de esforço** 	| Baixa | 
| **Comentários** 	| O sistema deve ser percebido como uma ferramenta de apoio à tomada de decisão, e não como uma fonte de verdade absoluta. A implementação dessa user story pode envolver a criação de um aviso para o usuário, a definição de um processo de revisão humana dos resultados e a implementação de medidas de segurança para proteger os dados dos clientes. | 


### Matriz de Priorização

&emsp;&emsp;A matriz de priorização serve como um guia para a execução das nossas user stories. Nela, as user stories foram organizadas de acordo com a combinação de esforço necessário para a implementação e a prioridade de implementação, para entender o valor de negócio que cada uma delas entrega. Essa combinação permite visualizar  quais user stories devem ser realizadas primeiro. Isso ajuda no planejamento de tarefas para implementar as user stories nas sprints seguintes.

| **User Story** 	| Valor de Negócio	 | Esforço | Prioridade | Dependências | Justificativa |
|---	|---	|---	|---	|---	|---	|
| **User Story 02** 	| Alto | Alto | Alta | User Story 01 | A predição de fraudes é fundamental para o sucesso do sistema e oferece um grande valor para o negócio. |
| **User Story 01** 	| Alto | Médio | Alta | Nenhuma | A análise exploratória é o primeiro passo para entender os dados e identificar padrões de fraude. |
| **User Story 05** 	| Alto | Médio | Alta | Nenhuma | Garantir a privacidade dos dados é um requisito legal e ético fundamental. |
| **User Story 06** 	| Médio | Baixo | Média | User Story 05 | A transparência e a justiça do sistema são importantes para a confiança dos usuários. |
| **User Story 03** 	| Médio | Alto | Média | Nenhuma | O desempenho do sistema é importante, mas pode ser aprimorado gradualmente. |
| **User Story 04** 	| Baixo | Médio | Baixa | Nenhuma | A segurança é importante, mas a funcionalidade de login já existe em muitos sistemas. |

## <a name="c8"></a>8. Wireframe da Solução


&emsp;&emsp;Wireframes são esboços básicos da interface de um produto digital, como um site ou um aplicativo. Eles servem como um blueprint, mostrando a estrutura e o layout das páginas, sem se preocupar com detalhes visuais como cores e fontes. É como um rascunho de um projeto arquitetônico, onde você pode visualizar a disposição dos cômodos e a circulação entre eles, antes de começar a construir as paredes e a decoração.

- User stories definem o quê: As user stories descrevem as funcionalidades que o produto deve oferecer do ponto de vista do usuário. Elas respondem à pergunta: "O que o usuário quer fazer?".
- Wireframes demonstram o como: Os wireframes visualizam como essas funcionalidades serão implementadas na interface do usuário. Eles mostram como o usuário irá interagir com o sistema para realizar as tarefas descritas nas user stories.

&emsp;&emsp;Link do wireframe com navegação para melhor visualização - https://www.figma.com/proto/dqHWzlykTRHRufaGtLYxQr/Wireframe-Catbusters?node-id=1-217&node-type=CANVAS&t=vTyZDuRYkpqJokPI-1&scaling=scale-down&content-scaling=fixed&page-id=0%3A1&starting-point-node-id=1%3A217 

&emsp;&emsp;Link do wireframe sem navegação para melhor visualização - https://www.figma.com/design/dqHWzlykTRHRufaGtLYxQr/Wireframe-Catbusters?node-id=0-1&t=SeXGYA7Z7mbBw7Gz-1

### Jornada

&emsp;&emsp;O usuário inicia sua interação na página de login, onde ele deve inserir suas credenciais para acessar o sistema "Catbusters". Após o login bem-sucedido, o usuário é direcionado para a página de upload de dados. Nesta página, ele pode selecionar e enviar o conjunto de dados que deseja analisar. Após fazer o upload, o usuário clica no botão "Continuar" e aguarda o carregamento da próxima página.

&emsp;&emsp;Após o carregamento, o usuário é levado para a página de pré-filtros, onde pode escolher os filtros que deseja aplicar aos dados. Uma vez selecionados os filtros, ele clica em "Visualizar" para processar e ver os resultados. Durante o processamento, o sistema exibe um indicador de "loading" para informar o usuário que a análise está em andamento.

&emsp;&emsp;Depois do carregamento, um popup aparece com um aviso importante: os dados apresentados são resultados gerados por inteligência artificial, podem conter erros e são considerados sensíveis. O aviso também recomenda que, antes de sair do sistema, o usuário deve realizar o logout para garantir que todos os dados e análises sejam excluídos do sistema, evitando qualquer risco de armazenamento indevido de informações confidenciais.

&emsp;&emsp;Na página de resultados, o usuário pode aplicar outros filtros, visualizar gráficos e obter insights importantes através de "big numbers" que resumem os resultados da análise. Se o usuário deseja obter informações mais detalhadas, ele pode clicar em "Ver Mais" e será direcionado para a página de detalhes.

&emsp;&emsp;Na página de detalhes, o usuário tem acesso a informações mais sensíveis, como matrícula e localização, que são apresentadas para uma análise mais aprofundada. Todas as páginas do sistema possuem um botão de "Sair da Conta". Ao clicar nesse botão, um popup de confirmação é exibido, perguntando ao usuário se ele realmente deseja sair. Este aviso é essencial, pois ao confirmar a saída, todos os dados e análises são imediatamente excluídos do sistema devido à natureza sensível das informações, garantindo a privacidade e a segurança dos dados.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Página de Login

<p align="center">
<img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G04/blob/main/assets/Login.png" border="0">
</p>
Figura 1. Wireframe da tela de login. Nesta tela foi utilizada a User Story 04.<br>
<br>

*Componentes*:
- Nome do Sistema: "Catbusters" no topo da tela, centrado.
- Campos de Entrada: Nome de usuário e senha.
- Botão de Ação: Botão "Entrar".

  
*Princípios de UX Design e Justificativa*:
- Simplicidade: A tela de login foi projetada para ser minimalista, com foco nos elementos essenciais: nome de usuário e senha. Esta abordagem evita distrações e orienta o usuário diretamente para a tarefa de login.
- Hierarquia Visual: O nome do sistema "Catbusters" está em destaque no topo da tela para reforçar a identidade da aplicação, seguido pelos campos de entrada, o que guia o usuário de forma intuitiva.


*Privacy by Default*:

&emsp;&emsp;Os campos de entrada de senha foram projetados para proteger a privacidade do usuário, para próximos passos, seria interessante aplicar recursos como a ocultação dos caracteres digitados para evitar visualização acidental. Além disso, o sistema também poderia garantir que as senhas sejam armazenadas de forma segura, utilizando técnicas de hashing e criptografia robusta, e que não sejam transmitidas em texto claro durante a comunicação entre o cliente e o servidor. Também é fundamental implementar protocolos de segurança como HTTPS para proteger a transmissão de dados contra interceptações e ataques de rede. Lembrando que estes pontos seriam passos futuros que a AEGEA poderia aplicar no projeto.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Página Seleção de dados

<p align="center">
<img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G04/blob/main/assets/Sele%C3%A7%C3%A3o%20de%20dados.png?token=GHSAT0AAAAAACVT4ZMVK3VWBHJFBPZQLV72ZWVAPTA" border="0">
</p>
Figura 2. Wireframe da tela de carregamento de dados pelo usuário do sistema. Nesta tela foi utilizada a User Story 03.<br>
<br>


*Componentes*:
- Título da Página: "Seleção de Dados" no topo da tela.
- UPLOAD de dados: Campos para upload do conjunto de dados desejado.
- Botão de Ação: Botão "Continuar".

  
*Princípios de UX Design e Justificativa*:
- Clareza e Direção: A interface foi projetada com uma estrutura clara para guiar o usuário através do processo de seleção de dados, com instruções concisas e componentes grandes, que facilitam a interação.
- Acessibilidade: Componentes grandes e facilmente clicáveis para facilitar a interação.

*Privacy by Default*: 

&emsp;&emsp;Os dados selecionados pelo usuário devem ser protegidos e processados de forma a manter a privacidade e segurança.

<p align="center">
<img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G04/blob/main/assets/Sele%C3%A7%C3%A3o%20de%20dados%20-%20Loading.png?token=GHSAT0AAAAAACVT4ZMVNZMDYY4IJ4QE4ZV4ZWVAQFA" border="0">
</p>
Figura 3. Wireframe da tela que indica que o carregamento dos dados está em processamento.<br>
<br>

*Princípios de UX Design e Justificativa*:

- Feedback Imediato: A tela de carregamento foi implementada para fornecer feedback imediato ao usuário de que sua ação está sendo processada.

<p align="center">
<img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G04/blob/main/assets/Sele%C3%A7%C3%A3o%20de%20dados-1.png?token=GHSAT0AAAAAACVT4ZMVUFNOWH2M3HHU65DUZWVAQSA" border="0">
</p>
Figura 4. Wireframe da tela que mostra a feature que ao sair do sistema os dados carregados não permanecerão carregados no sistema. Nesta tela foi utilizada a User Story 05.<br>
<br>

*Princípios de UX Design e Justificativa*:

- Segurança e Privacidade: A funcionalidade de descarte dos dados ao sair do sistema é uma medida de segurança crítica para evitar o armazenamento indevido de informações confidenciais, garantindo que os dados sensíveis sejam removidos adequadamente ao final da sessão.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Página Pré filtros

<p align="center">
<img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G04/blob/main/assets/Sele%C3%A7%C3%A3o%20de%20features.png?token=GHSAT0AAAAAACVT4ZMVLSSPIN6AWMQSSMC6ZWVATQA" border="0">
</p>
Figura 5. Wireframe da tela indicanto os tipos de filtros disponíveis para o tratamento dos dados. Nesta tela foi utilizada a User Story 03.<br>
<br>



*Componentes*:
- Seletor de filtros: Lista de opções de features que o usuário pode selecionar.
- Botão de Ação: Botão "Aplicar" para confirmar as escolhas.

*Princípios de UX Design e Justificativa*:

- Intuitividade: O layout da página foi organizado de forma que os filtros sejam claramente visíveis e facilmente selecionáveis. A lista de opções foi estruturada para minimizar a confusão e garantir que o usuário possa fazer suas escolhas.
- Feedback Imediato: Indicação visual de quais features foram selecionadas.
- Visualização do Progresso: Ao aplicar os filtros, o usuário é imediatamente informado sobre as seleções, permitindo um feedback contínuo e transparente

*Privacy by Default*: 

&emsp;&emsp;A interface foi projetada para minimizar a exposição de dados desnecessários e garantir que as seleções do usuário sejam tratadas de forma segura, garantindo que qualquer informação sensível seja protegida e que as escolhas dos usuários sejam processadas de forma segura. Por este motivo foi implementado um pop-up caso o usuário queira sair alertando que os dados serão excluídos e ao clicar em "Continuar" o usuário irá para outra página com outro pop-up que explica a sensibilidade dos dados e alerta o uso de IA.


<p align="center">
<img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G04/blob/main/assets/Loading.png?token=GHSAT0AAAAAACVT4ZMURGSTSWFJLEMYXSV2ZWVAUNA" border="0">
</p>
Figura 6. Wireframe da tela que indica que os dados estão sendo processados após os filtros selecionados.<br>
<br>

*Princípios de UX Design e Justificativa*:

- Feedback Imediato: A tela de carregamento foi implementada para fornecer feedback imediato ao usuário de que sua ação está sendo processada.

<p align="center">
<img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G04/blob/main/assets/Sele%C3%A7%C3%A3o%20de%20features%20-%20logout.png?token=GHSAT0AAAAAACVT4ZMV7JFSQ6WOIK75E3SEZWVATFQ" border="0">
</p>
Figura 7. Wireframe da tela que mostra a feature que ao sair do sistema os dados carregados serão apagados do mesmo. Nesta tela foi utilizada a User Story 05.<br>
<br>

*Princípios de UX Design e Justificativa*:

- Segurança e Privacidade: A funcionalidade de descarte dos dados ao sair do sistema é uma medida de segurança crítica para evitar o armazenamento indevido de informações confidenciais, garantindo que os dados sensíveis sejam removidos adequadamente ao final da sessão.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Página Resultado

<p align="center">
<img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G04/blob/main/assets/Resultado%20alerta.png?token=GHSAT0AAAAAACVT4ZMU5GY3NFJHBX22XL7OZWVAWYQ" border="0">
</p>
Figura 8. Wireframe da tela que antes de mostrar os resultados após os tratamentos de filtros selecionados, reforça que os resultados gerados devem ser utilizados como uma ferramenta que auxilia a tomada de decisões, e não como um resultado absoluto, visando o uso ético e responsável pelo usuário. Nesta tela foi utilizada a User Story 06.<br>
<br>



*Componentes*:
- Área de Resultado: Exibição dos resultados gerados.
- Botões de Ação: Botões para Filtrar, ver mais, Logout e voltar.
  
*Princípios de UX Design e Justificativa:*

- Alertas e Reforço de Uso Ético: Antes da exibição dos resultados, é apresentado um alerta reforçando que as informações devem ser utilizadas como ferramentas auxiliares na tomada de decisão e não como uma verdade absoluta. Isso é importante para assegurar que os usuários compreendam o contexto e as limitações dos resultados gerados, promovendo o uso responsável das informações. Essa abordagem é baseada em princípios de transparência e ética, que são fundamentais em projetos de detecção de fraudes.


*Privacy by Default*:

&emsp;&emsp;Os resultados apresentados devem garantir a privacidade do usuário, utilizando apenas as informações necessárias para a visualização. Dados sensíveis devem ser tratados e armazenados de maneira segura, sendo estes dados a "Localização" e "Matrícula".
Além disto, antes de entrar no página é exibido um pop-up indicando que os resultados são gerados IA e podem conter erros além de conter dados sensíveis.


<p align="center">
<img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G04/blob/main/assets/Resultado.png?token=GHSAT0AAAAAACVT4ZMUCPEE3GKVJH76C66WZWVAVPA" border="0">
</p>
Figura 9. Wireframe da tela de resultados, com outros tipos de filtros que podem ser selecionados, bem como informações de probabilidade de fraude, e a classificação que o sistema atribuiu ao usuário. Nesta tela foi utilizada a User Story 01 e 02.<br>
<br>

*Princípios de UX Design e Justificativa*:

- Clareza na Exibição dos Resultados: Os resultados são apresentados de maneira clara e visualmente acessível, com gráficos e indicadores de "big numbers" para facilitar a interpretação rápida das informações mais relevantes. Isso foi feito para suportar a user story 01, onde o usuário precisa identificar rapidamente as informações críticas relacionadas a possíveis fraudes.
- Acessibilidade: Elementos bem posicionados para facilitar a interação.

<p align="center">
<img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G04/blob/main/assets/Resultado%20-%20logout.png?token=GHSAT0AAAAAACVT4ZMVVTGDANPG3BJJKQLOZWVAXDQ" border="0">
</p>
Figura 10. Wireframe da tela que mostra a feature que os dados carregados e resultados gerados serão apagados após o usuário sair do sistema. Nesta tela foi utilizada a User Story 05.<br>
<br>

*Princípios de UX Design e Justificativa*:
- Segurança e Privacidade: A funcionalidade de descarte dos dados ao sair do sistema é uma medida de segurança crítica para evitar o armazenamento indevido de informações confidenciais, garantindo que os dados sensíveis sejam removidos adequadamente ao final da sessão.


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Página Detalhes

<p align="center">
<img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G04/blob/main/assets/Detalhes.png?token=GHSAT0AAAAAACVT4ZMVDJ3YCE664NWE6QCYZWVAZGA" border="0">
</p>
Figura 11. Wireframe da tela de detalhes de uma conta selecionada, com mais informações do usuário do serviço da empresa AEGEA.<br>
<br>



*Componentes*:
- Seções de Informações: Diversas seções detalhando informações específicas.
- Botões de Navegação: Botões "Voltar" e "Sair da conta".

  
*Princípios de UX Design e Justificativa*:

- Organização em Seções: As configurações são organizadas em categorias claras e distintas para facilitar a navegação. Isso permite que os usuários encontrem e ajustem rapidamente as opções que são mais importantes para eles. Esta organização é baseada em princípios de usabilidade, que enfatizam a necessidade de estruturar as informações de forma lógica e acessível.
- Navegabilidade: Facilita a navegação entre diferentes seções de detalhes.

*Privacy by Default*: 

&emsp;&emsp;Os detalhes exibidos devem estar protegidos para garantir que apenas os dados relevantes sejam mostrados e que as informações sensíveis sejam adequadamente ocultadas ou protegidas.


<p align="center">
<img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G04/blob/main/assets/Detalhes%20-%20logout.png?token=GHSAT0AAAAAACVT4ZMV5ZSQZOI2TE7TRA4KZWVAZNQ" border="0">
</p>
Figura 12. Wireframe da tela que demonstra a feature que os dados carregados e os resultados obtidos não serão armazenados ao sair do sistema. Nesta tela foi utilizada a User Story 05.<br>
<br>

*Princípios de UX Design e Justificativa*:
- Segurança e Privacidade: A funcionalidade de descarte dos dados ao sair do sistema é uma medida de segurança crítica para evitar o armazenamento indevido de informações confidenciais, garantindo que os dados sensíveis sejam removidos adequadamente ao final da sessão.


### Aplicações de Privacy by Design e Recomendações

&emsp;&emsp;O projeto de detecção de fraudes, além de garantir a eficiência e a precisão na identificação de irregularidades, deve também garantir a privacidade e a segurança dos dados dos usuários. Isso foi aplicado via minimização de dados, com a utilização apenas os dados estritamente necessários para a detecção de fraudes, evitando a coleta excessiva de informações, e o armazenamento seguro dos dados em ambientes seguros, com acesso restrito a usuários autorizados.

&emsp;&emsp;E a implementação desses principios pode ser verificado em:

- Requisitos não funcionais: Incluímos requisitos específicos relacionados à privacidade nos requisitos não funcionais do sistema, como a necessidade de garantir a segurança dos dados e a transparência no tratamento dos dados.
- User stories: Criamos user stories para garantir que seus dados e que suas informações do usuários sejam utilizadas de forma ética e transparente, ressaltando que os resultados obtidos pelo modelo pode não representar a realidade, para ser utilizado como uma ferramenta de apoio a tomada de decisões.
- Wireframes: Os wireframes foram desenhados para incluir elementos visuais que demonstram o compromisso com a privacidade, como avisos sobre o uso dos dados.
- Matriz de priorização: As user stories relacionadas à privacidade receberam alta prioridade, demonstrando a importância desse aspecto para o projeto.

&emsp;&emsp;É fundamental que a empresa AEGEA e seus clientes estejam cientes de que a coleta e o uso de dados devem estar em conformidade com a LGPD. A empresa deve implementar um programa de conscientização para todos os envolvidos, desde os colaboradores até os usuários finais. Além disso, é crucial que a AEGEA seja transparente em relação aos dados coletados e como eles são utilizados, disponibilizando informações claras e acessíveis aos seus clientes. Essa abordagem garante a proteção dos dados pessoais dos usuários, a conformidade com a legislação e a construção de uma relação de confiança com os clientes.

&emsp;&emsp;Como recomendação para a implementação deste sistema de detecção de fraude, a empresa AEGEA pode:

- Manter um canal aberto para se comunicar com usuários que desejam contestar notificações de fraude, oferecendo um processo claro e ágil para resolução de disputas.
- Investir em mecanismos de feedback contínuo para aprimorar o sistema e reduzir a incidência de falsos positivos. A coleta de dados sobre as contestações dos usuários e a análise das causas dos erros podem auxiliar na identificação de oportunidades de melhoria do modelo de detecção de fraudes, aumentando a precisão e a confiabilidade do sistema.

# <a name="c9"></a>9. Protótipo de Alta Fidelidade da Interface

&emsp;&emsp;Com base no wireframe, foram realizadas melhorias relacionadas à proteção de dados dos clientes da Aegea e para evitar possíveis viéses sobre os resultados gerados pela solução do projeto, as quais podem ser verificadas nas próximas seções. Esse processo visou aprimorar a experiência do usuário e alinhar o design com os objetivos funcionais e não funcionais definidos nas fases anteriores do projeto.

&emsp;&emsp;O protótipo de alta fidelidade é uma representação visual detalhada de uma interface, construída para simular a experiência do usuário final. Ele segue o wireframe desenvolvido nas etapas anteriores, bem como os feedbacks recebidos ao longo da sprint. Neste projeto, foram criados dois protótipos distintos para atender a duas jornadas e perfis de usuários diferentes: web e mobile. Cada um foi projetado para corresponder às necessidades específicas desses usuários e seus respectivos fluxos de trabalho. 

&emsp;&emsp;Após a discussão sobre o emprego de user stories da persona afetada no wireframe, foi possível identificar outros pontos de melhoria na apresentação das informações, com o objetivo de proteger o usuário final da Aegea e evitar a atribuição de viés, tanto pelo analista de dados que utilizará a solução desktop quanto pelo usuário da versão mobile.

&emsp;&emsp;Na versão desktop, um dos principais ajustes foi a remoção dos nomes das pessoas, bairros e outros detalhes de informações sensíveis que antes eram exibidos junto à matrícula do usuário. Essa mudança foi pensada para mitigar o risco de viés de confirmação, que poderia surgir quando o analista ou usuário tivesse acesso a dados identificáveis, levando a julgamentos preconcebidos ou tendenciosos sobre possíveis fraudes. Ao focar apenas em informações técnicas e necessárias, como a média de consumo e a probabilidade de fraude, a solução proporciona uma análise mais imparcial, sem influenciar a interpretação dos resultados por meio de dados irrelevantes para a tomada de decisão.

&emsp;&emsp;Nos próximos parágrafos, será detalhado o funcionamento de cada protótipo e como eles se complementam.

### Links complementares

**Figma editável** - https://www.figma.com/design/dqHWzlykTRHRufaGtLYxQr/Wireframe-Catbusters?node-id=163-7260&t=lEFVZQA5PFH1r6wj-1

**Protótipo web navegável** - https://www.figma.com/proto/dqHWzlykTRHRufaGtLYxQr/Wireframe-Catbusters?node-id=77-1138&node-type=canvas&t=PCWBKalv0DTu7CNh-1&scaling=scale-down&content-scaling=fixed&page-id=77%3A2&starting-point-node-id=77%3A1138

**Protótipo mobile navegável** - https://www.figma.com/proto/dqHWzlykTRHRufaGtLYxQr/Wireframe-Catbusters?node-id=163-7261&node-type=canvas&t=wrgHuBfsg366gOrP-1&scaling=scale-down&content-scaling=fixed&page-id=163%3A7260&starting-point-node-id=163%3A7261



## Guia de Estilos

&emsp;&emsp;Para manter a consistência visual e funcional entre os protótipos, foi desenvolvido um guia de estilos. Esse guia estabelece as paletas de cores, os tipos de fontes e outras diretrizes visuais que serão aplicadas uniformemente em ambas as versões (web e mobile). A escolha das cores foi feita para facilitar a distinção de elementos e proporcionar acessibilidade, enquanto a tipografia foi pensada para garantir legibilidade e clareza nas informações apresentadas ao usuário. Este guia é um pilar fundamental para assegurar que todos os elementos visuais permaneçam coesos durante o uso do produto.

<p align="center">
<img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G04/blob/main/assets/guiaestilo.png" border="0">
</p>
Figura 1. Guia de estilos.<br>
<br>

## Protótipo Web

&emsp;&emsp;O protótipo web foi criado para o usuário analista de dados da AEGEA, cuja função é notificar os usuários operacionais sobre quais consumidores devem passar por vistorias. O fluxo de uso desse analista começa com a tela de login, seguida pelo upload de um arquivo CSV que contém os dados dos consumidores. Em seguida, ele faz um pré-filtro das features relevantes e, antes de visualizar os resultados, um pop-up de aviso aparece:

> "Atenção! Os dados a seguir foram tratados e analisados por uma rede neural artificial, que pode estar sujeita a erros. Utilize o resultado como uma ferramenta auxiliar para uma análise mais precisa. Além disso, lembre-se de manter os dados em sigilo, pois são dados sensíveis e apenas alguns têm acesso. Antes de sair do sistema, não se esqueça de encerrar a sessão clicando em 'Sair da conta'."

&emsp;&emsp;Após isso, o analista visualiza uma tabela que exibe a categoria, média de consumo, probabilidade de fraude e o resultado do processamento. Ele pode filtrar ou ordenar os dados alfabeticamente, além de visualizar Big Numbers e gráficos para obter insights adicionais. O analista também tem a opção de selecionar as linhas da tabela que ele entende que precisam de vistoria e enviar essas informações para os usuários operacionais. É esse envio que desencadeia a jornada do usuário operacional, que ocorre na versão mobile.

### Login

&emsp;&emsp;O fluxo de uso para o analista de dados da AEGEA no protótipo web começa com a Tela de Login (Figura 2).

<p align="center"> <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G04/blob/main/assets/protweb/Login.png" border="0"> </p> Figura 2. Tela de login do protótipo web, onde o analista de dados realiza o acesso ao sistema.<br> <br>

---------------------------------------------------------------------------------

### Upload de dados

&emsp;&emsp;Após inserir suas credenciais, o analista é levado à tela de Upload de Dados (Figura 3). Nessa etapa, ele faz o upload de um arquivo CSV contendo os dados dos consumidores. O sistema processa esses dados e exibe a Tela de Processamento (Figura 4), mostrando que o upload está em andamento.

<p align="center"> <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G04/blob/main/assets/protweb/Upload.png" border="0"> </p> 
Figura 3. Tela para upload de arquivo CSV contendo os dados dos consumidores.<br> <br> 

<p align="center"> <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G04/blob/main/assets/protweb/Calculando.png" border="0"> </p> 
Figura 4. Tela exibida enquanto o sistema processa os dados carregados.<br> <br> 

&emsp;&emsp;Após o processamento, o analista visualiza a Tela de Resultados (Figura 5), que apresenta uma tabela com os dados processados.

<p align="center"> <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G04/blob/main/assets/protweb/Upload%20completo.png" border="0"> </p> 
Figura 5. Tela após o upload completo dos dados, mostrando a visualização dos resultados.<br> <br> 

<p align="center"> <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G04/blob/main/assets/protweb/Upload%20dados%20Logout.png" border="0"> </p> 
Figura 6. Tela de logout após a visualização dos dados e resultados.<br> <br>
-------------------------------------------------------------------------------------

### Pré-filtros

&emsp;&emsp;O analista então pode aplicar Pré-Filtros (Figura 7) aos dados para refinar a análise antes de visualizar os resultados finais. Durante a aplicação dos pré-filtros, a Tela de Carregamento (Figura 8) mostra o progresso.

<p align="center"> <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G04/blob/main/assets/protweb/Pr%C3%A9%20filtros.png" border="0"> </p> 
Figura 7. Tela para aplicar pré-filtros aos dados antes de visualizar os resultados.<br> <br> 

<p align="center"> <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G04/blob/main/assets/protweb/Pr%C3%A9%20filtros%20carregando.png" border="0"> </p> 
Figura 8. Tela exibida enquanto os pré-filtros são aplicados aos dados.<br> <br> 

<p align="center"> <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G04/blob/main/assets/protweb/Pr%C3%A9%20filtros%20-%20logout.png" border="0"> </p>
Figura 9. Tela de logout após a aplicação dos pré-filtros.<br> <br>

------------------------------------------------------------------------------------

### Resultados

&emsp;&emsp;Nesse momento, um pop-up de aviso é exibido (Figura 10), alertando o analista sobre a precisão dos dados e a necessidade de manter a confidencialidade das informações.

<p align="center"> <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G04/blob/main/assets/protweb/Resultado%20-%20pop%20up.png" border="0"> </p> 
Figura 10. Tela exibida após a visualização dos resultados, incluindo um pop-up de aviso sobre a precisão dos dados.<br> <br> 

&emsp;&emsp;Após a aplicação dos filtros, o analista pode visualizar a tabela de resultados filtrados (Figura 11) e selecionar as linhas que considera relevantes para vistoria. 

<p align="center"> <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G04/blob/main/assets/protweb/Resultado.png" border="0"> </p>
Figura 11. Tela com a tabela de resultados, mostrando informações como categoria, média de consumo e probabilidade de fraude.<br> <br> 

<p align="center"> <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G04/blob/main/assets/protweb/Resultado%20-%20Logout.png" border="0"> </p> 
Figura 12. Tela de logout após a visualização dos resultados.<br> <br> 

&emsp;&emsp;Essas seleções são mostradas na Tela de Seleção (Figura 13), e, após a revisão, o analista pode fazer logout da tela de Logout (Figura 12).


<p align="center"> <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G04/blob/main/assets/protweb/Detalhes%20-%20Sele%C3%A7%C3%A3o.png" border="0"> </p> 
Figura 13. Tela mostrando as linhas selecionadas para vistoria, antes do envio para os usuários operacionais.<br> <br>

<p align="center"> <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G04/blob/main/assets/protweb/Detalhes%20-%20Sele%C3%A7%C3%A3o%20-%20Logout.png" border="0"> </p> 
Figura 14. Tela de logout após a seleção das linhas para vistoria.<br> <br>

-----------------------------------------------------------------------------------------

## Protótipo Mobile

&emsp;&emsp;O usuário operacional acessa o sistema através de uma tela de login, onde escolhe a opção de "analisar" os consumidores designados para vistoria. Ele visualiza uma tabela com os consumidores que precisam ser verificados. Ao clicar em "mais detalhes", o usuário operacional pode ver informações sensíveis e adicionar observações, caso note algo incomum na residência ou comércio. Depois de concluir a vistoria, ele retorna para a tela principal, onde o consumidor já analisado vai para outra tabela, agora com os consumidores que já foram verificados. Essa interface foi projetada para ser simples e objetiva, focada em facilitar a execução das vistorias.

### Login

&emsp;&emsp;O usuário operacional inicia sua jornada pelo sistema acessando a Tela de Login (Figura 15). Aqui, ele insere suas credenciais para entrar no sistema. 

<p align="center">
<img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G04/blob/main/assets/protmobile/Login.png" style="border: 5px solid black;" width="300">
</p>
Figura 15. Tela de login do protótipo mobile, onde o usuário operacional realiza o acesso ao sistema<br>
<br>

-----------------------------------------------------------------------------------------

### Menu Principal

&emsp;&emsp;Após um login bem-sucedido, é redirecionado para o Menu Principal (Figura 16), onde pode escolher entre as opções de visualizar as matrículas que ainda precisam ser visitadas ou aquelas que já foram analisadas.

<p align="center">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G04/blob/main/assets/protmobile/Menu.png" style="border: 5px solid black;" width="300">
</p>
Figura 16. Menu Principal para poder acessar a lista de matrículas a serem visitadas, ou matrículas que já foram vistoriadas<br>
<br>

-----------------------------------------------------------------------------------------

### Visão Geral de Vistorias

&emsp;&emsp;Selecionando a opção de vistoria, o usuário acessa a Visão Geral de Vistorias (Figura 17), onde visualiza uma lista de tarefas com as matrículas a serem visitadas. Nesta página, o usuário pode filtrar a lista de locais para uma análise mais específica, aplicando os Filtros Disponíveis (Figura 19).

<p align="center">
<img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G04/blob/main/assets/protmobile/Para%20analisar.png" style="border: 5px solid black;" width="300">
</p>

Figura 17. Página pra apresentar para o usuário as informações de matrículas que devem ser vistoriadas, em formato de uma lista de tarefas.<br>
<br>

&emsp;&emsp;Ao clicar em um item da lista, o usuário é levado à tela de Detalhes para Análise (Figura 18). Aqui, ele visualiza informações mais detalhadas sobre o local a ser vistoriado. Se necessário, pode adicionar observações relevantes, como qualquer detalhe incomum que observe durante a vistoria

<p align="center">
<img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G04/blob/main/assets/protmobile/Detalhes%20para%20an%C3%A1lise.png" style="border: 5px solid black;" width="300">
</p>
Figura 18. Detalhes sobre um local a ser vistoriado<br>
<br>

<p align="center">
<img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G04/blob/main/assets/protmobile/Para%20analisar%20-%20filtros.png" style="border: 5px solid black;" width="300">
</p>
Figura 19. Filtros disponíveis para aplicar sobre lista de locais a serem visitados<br>
<br>

&emsp;&emsp;Após a conclusão da vistoria, o usuário retorna ao Menu Principal e visualiza as matrículas que foram concluídas, agora listadas na seção Analisados pós Vistoria (Figura 20). 

-----------------------------------------------------------------------------------------

### Analisados pós Vistoria

&emsp;&emsp;Esta tela fornece um resumo das vistorias realizadas, permitindo ao usuário acompanhar seu progresso.

<p align="center">
<img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G04/blob/main/assets/protmobile/Analisados%20pos%20vistoria.png" style="border: 5px solid black;" width="300">
</p>
Figura 20. Lista de locais que já foram visitados pelo usuário.<br>
<br>

-----------------------------------------------------------------------------------------

### Tela de Logout

&emsp;&emsp;Finalmente, quando o trabalho está concluído, o usuário pode acessar a Tela de Logout (Figura 21) para sair do sistema de forma segura.

<p align="center">
<img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G04/blob/main/assets/protmobile/Para%20analisar%20-1%20-%20Logout.png" style="border: 5px solid black;" width="300">
</p>
Figura 21. Tela para fazer o logout da solução mobile<br>
<br>

## Conclusão

&emsp;&emsp;Embora as jornadas dos usuários sejam distintas, elas se complementam. A jornada web concentra-se na análise dos dados e na identificação de potenciais fraudes, sem revelar a identidade ou a localização específica dos indivíduos a serem vistoriados, o que ajuda a evitar possíveis vieses. A jornada operacional, acessada via mobile, foca na execução das vistorias de campo, mantendo o usuário operacional sem informações sobre o motivo específico da verificação para prevenir preconceitos ou julgamentos prematuros. Adicionalmente, um campo de "observações" foi incluído para que o usuário registre quaisquer ocorrências ou detalhes notados durante a vistoria.

&emsp;&emsp;O objetivo principal da solução é atuar como uma ferramenta de prevenção, e não de punição. Por isso, o aspecto social é fundamental para o projeto. Assegurar uma análise precisa e uma execução justa e imparcial é crucial, não apenas para a eficácia do sistema, mas também para a proteção dos direitos e da dignidade dos usuários da Aegea. Ambas as jornadas foram desenhadas para trabalhar em conjunto, promovendo um processo equitativo e orientado para a melhoria contínua.

# <a name="c10"></a>10. Front-End da Solução


&emsp;&emsp;Este documento tem como objetivo fornecer uma referência completa para todos os envolvidos no projeto, desde desenvolvedores e designers até stakeholders e usuários finais. Ao compreender os princípios e as decisões de design por trás do Front-End, será possível realizar manutenções, adicionar novas funcionalidades e garantir a consistência visual da aplicação. 

&emsp;&emsp;O front-end, a interface visual de nossa aplicação, desempenha um papel importante na experiência do usuário já que é através dele que os usuários interagem com o sistema, realizando tarefas e obtendo informações. Um front-end bem projetado torna a aplicação mais agradável de usar e contribui para o sucesso do negócio. Por isso é preciso seguir algumas diretrizes, como Design System e as Heurísticas de Nielsen, pois ao estabelecer padrões visuais e componentes reutilizáveis, o Design System torna a interface coesa e intuitiva, facilitando a navegação do usuário. Paralelamente, as Heurísticas de Nielsen oferecem princípios para criar interfaces eficientes, reduzindo a carga cognitiva e aumentando a satisfação do usuário. 

&emsp;&emsp;Com um Design System e a aplicação das Heurísticas, o desenvolvimento se torna mais ágil, a manutenção mais simples e a experiência do usuário mais positiva, contribuindo para o sucesso da aplicação. Uma aplicação só é relevante se for utilizada. Se utilizar a aplicação torna a experiência do usuário pior do que já utilizar o que ele tem disponível, ele não vai adotar a solução proposta.

&emsp;&emsp;Esta é a versão final do Front-End, focada na experiência do usuário analista da AEGEA em desktop. Componentes e funcionalidades podem ser ajustados ou adicionados em versões subsequentes, incluindo a versão mobile, que será desenvolvida na próxima sprint. Documentamos neste momento os componentes existentes para facilitar o entendimento e a manutenção do código, mesmo que eles estejam em desenvolvimento.

## Feedbacks, Melhorias e Impacto nos Objetivos

&emsp;&emsp;Durante a sprint review da terceira sprint, o protótipo de alta fidelidade foi apresentado ao nosso parceiro de projeto. Recebemos um feedback sobre a expectativa de uma interface mais criativa e dinâmica sobre a navegação e apresentação dos dados. O parceiro considerou o design do protótipo como excessivamente quadrado e rígido.

&emsp;&emsp;Essa percepção nos levou a um debate aprofundado sobre a estética da interface, levando em conta tanto os comentários do parceiro quanto os objetivos do projeto. Considerando a natureza sensível do projeto, que envolve a identificação e prevenção de fraudes, a proteção de dados dos usuários e o foco em resultados e dados, e a decisão por uma abordagem mais minimalista.

&emsp;&emsp;Optou-se por uma interface com menor utilização de cores fortes e um design mais clean, priorizando a funcionalidade. Ações como a subida de arquivos, a aplicação de filtros e a visualização de dados ganharam destaque. Essa decisão alinha-se com o objetivo de oferecer uma experiência de usuário clara e objetiva, facilitando a compreensão e a interação com as funcionalidades essenciais do sistema.

## Front-End e Fluxo de Navegação

&emsp;&emsp;As imagens a seguir ilustram o fluxo de navegação do usuário na plataforma, apresentando as telas desenvolvidas. O objetivo é demonstrar a sequência de interações do usuário desde o login até a obtenção dos resultados finais.


### Login

&emsp;&emsp;Esta tela permite que o usuário faça login na plataforma. O usuário deve inserir seu nome de usuário e senha para acessar a próxima tela. Esta tela é essencial para a segurança da plataforma, pois impede que usuários não autorizados acessem os dados.


<p align="center"> <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G04/blob/main/assets/protweb/FE-Login.png" border="0"> </p> 
Figura 1. Tela de login. O usuário deve inserir suas credenciais (nome de usuário e senha) para acessar a plataforma.<br> <br> 

-------------------------------------------------------------------------------------

### Upload de dados

&emsp;&emsp;Esta tela permite que o usuário selecione e envie os arquivos que deseja analisar. É o ponto de entrada dos dados para o sistema. É a etapa inicial do processo de análise. A qualidade e a quantidade dos dados enviados nesta etapa diretamente influenciam a precisão dos resultados.


<p align="center"> <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G04/blob/main/assets/protweb/FE-Upload.png" border="0"> </p> 
Figura 2. Tela para upload de arquivo CSV contendo os dados dos consumidores.<br> <br> 

-------------------------------------------------------------------------------------

### Pré-filtros

&emsp;&emsp;Nesta tela, o usuário pode aplicar filtros aos dados para refinar a análise e obter resultados mais específicos. Os filtros permitem que o usuário personalize a análise de acordo com suas necessidades, focando em um subconjunto específico dos dados, agilizando o processo de análise.


<p align="center"> <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G04/blob/main/assets/protweb/FE-Pr%C3%A9%20filtros.png" border="0"> </p> 
Figura 3. Tela para aplicar pré-filtros aos dados antes de visualizar os resultados.<br> <br> 


<p align="center"> <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G04/blob/main/assets/protweb/FE-Pr%C3%A9%20filtros2.png" border="0"> </p> 
Figura 4. Detalhes específicos dos filtros com o intervalo numérico representado por placeholders.<br> <br> 


<p align="center"> <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G04/blob/main/assets/protweb/FE-Pr%C3%A9%20filtros3.png" border="0"> </p> 
Figura 5. Detalhes específicos dos filtros com o calendário para seleção de um intervalo de tempo.<br> <br> 

------------------------------------------------------------------------------------

### Resultados

&emsp;&emsp;A tabela de resultados apresenta um resumo dos dados filtrados, incluindo informações como categoria, média de consumo e probabilidade de suspeita fraude. O usuário pode ordenar a tabela por qualquer coluna para facilitar a análise. 

<p align="center"> <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G04/blob/main/assets/protweb/Front-Final.jpeg" border="0"> </p>
Figura 6. Tela com a tabela de resultados, mostrando informações como categoria, média de consumo e probabilidade da suspeita de fraude.<br> <br> 

### Vídeo da Solução

Este é um vídeo demonstrativo do frontend proposto para a solução:

![Miniatura do Vídeo](https://github.com/Inteli-College/2024-2A-T04-SI11-G04/blob/main/assets/protweb/Login.png)

[Clique aqui para assistir ao vídeo](https://drive.google.com/file/d/1j8VRszA6AnNyXkvPWDActpy9poJ6kzgu/view?usp=drive_link)

## Resumo das Principais Mudanças

&emsp;&emsp;As principais mudanças na interface visam proporcionar uma experiência de usuário mais agradável e intuitiva, alinhada com os feedbacks recebidos. Uma das alterações mais significativas diz respeito à tipografia, que no protótipo foi utilizada a Roboto Mono. Optou-se por uma fonte com curvas mais suaves e uma aparência mais orgânica em comparação com a Roboto Mono, quebrando a geométrica visual anterior e contribuindo para uma estética mais suave e convidativa:

<div style="display: flex; justify-content: center;">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G04/blob/main/assets/protweb/Roboto_Mono_sample.png" width="200px">
  <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G04/blob/main/assets/protweb/FonteInter.png" width="325px">
</div>

Figura 8. Comparação entre as fontes Roboto Mono e Inter.<br> <br> 

&emsp;&emsp;Além da tipografia, o layout dos componentes também passou por ajustes. Anteriormente, os componentes apresentavam contornos mais definidos, criando uma sensação de "caixas" e direcionando o olhar para a estrutura em vez do conteúdo. Na nova versão, os espaços vazios foram melhor distribuídos, proporcionando uma hierarquia visual mais clara e direcionando o olhar do usuário para as informações mais relevantes, como é possível verificar no exemplo abaixo, onde na figura 9, que representa a versão do protótipo (A) e a versão feita no Front-End (B) da tela de pré filtros, onde os componentes do filtro do protótipo cabem e preenchem os quadrados, mas na versão do Front-End isso não acontece, quebrando a impressão de "caixas":

<p align="center"> <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G04/blob/main/assets/protweb/Comp-PreFiltros.png" border="0"> </p>
Figura 9. Comparação entre as versões do protótipo de alta fidelidade (A) e do front-end (B) da tela de pré-filtros<br> <br> 

&emsp;&emsp;A tabela também está refinada para reduzir a sensação de rigidez. Os elementos estão sendo reorganizados e formatados para criar uma apresentação mais visualmente agradável, com as linhas da tabela mais claras que o texto, a remoção de linhas de separação das colunas, dando mais ênfase nos dados em si. Também foi feita a substituição do termo 'probabilidade' por 'suspeita' busca refletir a natureza probabilística dos modelos de machine learning utilizados. Ao invés de fornecer uma probabilidade exata de fraude, o sistema identifica padrões que são indicativos de um possível comportamento fraudulento, e não significa que uma fraude tenha ocorrido de fato. A figura 10 mostra a versão feita no protótipo (A) e a versão em implementação no Front-End (B).

<p align="center"> <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G04/blob/main/assets/protweb/Comp-Resultados.png" border="0"> </p>
Figura 10. Comparação entre as versões do protótipo de alta fidelidade (A) e do front-end (B) da tela de resultados<br> <br> 

## Design System

## 1. **Introdução ao Design System**

O Design System foi desenvolvido para garantir uma experiência de usuário consistente, acessível e escalável. Ele é composto por uma série de componentes reutilizáveis, estilos, diretrizes e práticas que visam otimizar o desenvolvimento da interface, facilitando a colaboração entre a equipe de design e desenvolvimento.

O sistema Catbusters utiliza várias bibliotecas, como **class-variance-authority (CVA)**, **Radix UI** e **Recharts**, para garantir flexibilidade e consistência no comportamento e na aparência dos componentes.

### 1.1 Objetivo

O objetivo deste Design System é fornecer componentes e padrões reutilizáveis que garantem:

- **Consistência**: Um visual e comportamento uniforme em toda a aplicação.
- **Escalabilidade**: Componentes que podem ser reutilizados e expandidos conforme necessário.
- **Acessibilidade**: Garantir que a interface seja utilizável por pessoas com diferentes capacidades.

## 2. **Bibliotecas Utilizadas**

### 2.1 **Class-Variance-Authority (CVA)**

A **CVA** permite o gerenciamento de estilos condicionalmente, facilitando a criação de componentes com variantes (como diferentes estilos de botões) e tamanhos. Ela é fundamental para manter o código de estilo limpo, organizado e fácil de escalar.

### 2.2 **Radix UI**

Biblioteca focada em acessibilidade e interatividade de componentes. Ela é utilizada para criar elementos interativos, como checkboxes, selects e popovers, garantindo que o design seja funcional e acessível.

### 2.3 **Recharts**

Uma biblioteca de gráficos para React que é altamente personalizável e utilizada no projeto para criar visualizações de dados como gráficos de barras e linhas.

### 2.4 **Date-fns**

Biblioteca de utilitários para trabalhar com datas. Ela é leve e eficiente, permitindo manipulações de datas de forma simples.

---

## 3. **Componentes do Design System**

<img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G04/blob/main/assets/protweb/DScomponentes.png" border="0">

### 3.1 **Button**

### Descrição:

O componente `Button` é configurável para diferentes estilos e tamanhos, proporcionando uma experiência consistente ao usuário em diversas interações.

### Variantes:

- **default**: Fundo azul escuro, utilizado para ações primárias.
- **destructive**: Fundo vermelho, utilizado para ações que removem ou destroem dados.
- **outline**: Botão com borda e fundo transparente, geralmente usado para ações secundárias.
- **ghost**: Botão sem borda ou fundo, com hover que altera a cor.
- **link**: Estilizado como um link, com sublinhado ao passar o mouse.

<img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G04/blob/main/assets/protweb/DSfiltrar.png" border="0">

<img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G04/blob/main/assets/protweb/DSentrar.png" border="0">

<img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G04/blob/main/assets/protweb/DScalcular.png" border="0">

### Tamanhos:

- **sm**: Pequeno, para botões menos destacados.
- **default**: Tamanho padrão.
- **lg**: Grande, para ações importantes ou que precisam de maior destaque.

---

### 3.2 **Calendar**

### Descrição:

O `Calendar` é um calendário interativo criado com base na biblioteca `react-day-picker`, com estilos e comportamentos definidos para a exibição de dias, navegação entre meses e seleção de datas.

### Funcionalidades:

- Exibição de dias fora do mês atual (`showOutsideDays`).
- Navegação através de botões para meses anteriores e posteriores, estilizados com o mesmo sistema de variantes dos botões.

<img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G04/blob/main/assets/protweb/DSfunc.png" border="0">

---

### 3.3 **Card**

### Descrição:

O `Card` é um componente de contêiner utilizado para agrupar informações ou ações relacionadas. Ele é altamente personalizável com seções como cabeçalho (`CardHeader`), conteúdo (`CardContent`), descrição (`CardDescription`) e rodapé (`CardFooter`).

---

### 3.4 **Checkbox**

### Descrição:

O componente `Checkbox`, fornecido pela biblioteca **Radix UI**, é acessível e estilizado para ser utilizado em formulários e interfaces de interação. Ele também utiliza `CheckIcon` para indicar visualmente quando o checkbox está marcado.

<img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G04/blob/main/assets/protweb/DScheck.png" border="0">

---

### 3.5 **Select (Menu de Seleção)**

### Descrição:

O `Select` é um menu dropdown personalizado, construído sobre os componentes de seleção da biblioteca **Radix UI**. Ele permite ao usuário escolher entre várias opções e suporta rolagem suave e ícones para indicar o estado de seleção.

### Subcomponentes:

- **SelectTrigger**: Elemento clicável que abre o menu.
- **SelectItem**: Cada item dentro do menu.
- **SelectContent**: O conteúdo exibido no dropdown.
- **SelectValue**: O valor atualmente selecionado.

<img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G04/blob/main/assets/protweb/DSselect.png" border="0">

---

### 3.6 **Tabela**

### Descrição:

O componente de tabela é altamente flexível, com subcomponentes para cabeçalhos, linhas, células e legendas. As tabelas são responsivas e estilizadas para exibir informações em formato tabular.

### Subcomponentes:

- **TableHeader**: O cabeçalho da tabela.
- **TableRow**: Linhas da tabela.
- **TableCell**: Células que contêm os dados.

<img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G04/blob/main/assets/protweb/DStabela.png" border="0">

---

### 3.7 **Chart (Gráfico)**

### Descrição:

Os componentes de gráficos utilizam a biblioteca **Recharts** para renderizar gráficos interativos. O `ChartContainer` é o contêiner principal que configura o gráfico e suas cores, enquanto o `ChartTooltip` e o `ChartTooltipContent` são usados para exibir informações detalhadas ao passar o mouse sobre os elementos do gráfico.

<img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G04/blob/main/assets/protweb/DSgrafico.png" border="0">

---

### 3.8 **Logo**

### Descrição:

A imagem do logo (`Logo`) é importada como um ativo gráfico e utilizada para identificação visual da marca em diversas partes da aplicação. Ela é importada de `../../assets/logo.png`.

<img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G04/blob/main/assets/protweb/DSlogomini.png" border="0">

<img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G04/blob/main/assets/protweb/DSlogomax.png" border="0">

---

## 4. **Conclusão do Design System**

Este Design System foi projetado para fornecer uma base robusta e flexível para o desenvolvimento de interfaces de usuário, garantindo consistência visual e funcionalidade acessível. A combinação de bibliotecas modernas como **CVA**, **Radix UI** e **Recharts** permite que os componentes sejam altamente reutilizáveis e facilmente expansíveis, atendendo às necessidades de design e desenvolvimento do projeto.

Seja no uso de botões, gráficos, tabelas ou formulários, este sistema oferece uma abordagem unificada e eficiente para criar experiências digitais de alta qualidade.


## Heurísticas de Nielsen

&emsp;&emsp;As heurísticas de usabilidade são princípios gerais para avaliar a qualidade da experiência do usuário em uma interface e servem como diretrizes para criar interfaces olhando diversos aspectos que mantêm a usabilidade mantendo uma boa experiência do usuário. A seguir são as heurísticas aplicadas na primeira versão do Front-End:

### Visibilidade do Status do Sistema

- Evidência: As opções dos filtros indicam a ação e o estado em que os dados serão processados.

- Análise: Além do botão "Filtrar", as opções de filtro em si também servem como um tipo de feedback visual. Ao selecionar uma opção, o usuário entende que essa informação será utilizada como critério para a filtragem dos dados. Essa combinação de elementos visuais reforça a ideia de que a ação do usuário está sendo processada.

### Reconhecimento em vez de memorização

- Evidência: A linguagem utilizada nos rótulos e botões é clara e direta, de acordo com a familiaridade que os usuários do sistema têm em relação aos termos utilizados.

- Análise: Ao utilizar termos familiares e comuns ao contexto do sistema, a interface facilita a compreensão do usuário, reduzindo a carga cognitiva e evitando que ele precise memorizar termos técnicos. Essa abordagem contribui para uma experiência mais intuitiva e agradável.

### Controle e Liberdade do Usuário

- Evidência: O usuário tem a liberdade de escolher os critérios de filtragem, como tipo de matrícula e intervalo de consumo. Além disso, a interface permite ao usuário redefinir os filtros ou limpar os resultados.

- Análise: A possibilidade de o usuário redefinir os filtros ou limpar os resultados demonstra um alto nível de controle sobre a interação. Isso permite que o usuário explore diferentes cenários e encontre as informações que precisa de forma rápida e eficiente.

### Consistência e Padrões

- Evidência: O layout da interface segue princípios de Design System.

- Análise: A utilização de um Design System garante a consistência visual e estrutural da interface em toda a aplicação. Isso contribui para uma experiência mais coesa e profissional, além de facilitar a manutenção e a expansão do sistema.

### Estética e Design Minimalista

- Evidência: A escolha do tema da interface é manter componentes reduzidos, ênfase nas features da solução e a visualização dos resultados após o processamento dos dados.

- Análise: Ao priorizar a funcionalidade e a clareza da informação, a interface adota uma abordagem minimalista. Essa escolha é positiva, pois evita sobrecarregar o usuário com elementos visuais desnecessários e facilita a compreensão da interface.

## Princípios WCAG Aplicados

&emsp;&emsp;A seguir, apresentamos uma análise detalhada de como os critérios de sucesso WCAG 1.3.5 e 1.4.6 foram aplicados no desenvolvimento do frontend, visando melhorar a maneira que as informações são apresentadas, e que sejam compreensíveis ao maior número de usuários.

### 1.3.5 - Identificar o objetivo de entrada (nível AA)
Objetivo: Garantir que os usuários compreendam claramente o tipo de informação que devem inserir em cada campo de formulário.

Implementação:

- Rótulos claros e concisos: Todos os campos de formulário possuem rótulos que descrevem de forma precisa a informação solicitada, bem como na tela de login, que depende de credenciais para acessar a solução e a tela de realizar o Upload dos dados, que necessita de instruções para indicar o que precisa ser feito.

### 1.4.6 - Contraste (melhorado) (nível AAA)

Objetivo: Garantir que o texto seja legível para todos os usuários, incluindo aqueles com deficiência visual.

- Paleta de cores: Uma paleta de cores cuidadosamente escolhida foi utilizada, garantindo um contraste adequado entre o texto e o fundo.
- Tamanhos de fonte: Os tamanhos de fonte foram definidos de forma a garantir a legibilidade, mesmo para usuários com baixa visão.

## Explicabilidade do Sistema

&emsp;&emsp;A explicabilidade é um aspecto essencial para garantir que o sistema de detecção de fraudes seja compreensível não apenas por especialistas, mas também por usuários não técnicos. Ela proporciona transparência e confiança no uso do sistema, permitindo que os usuários entendam como e por que determinadas decisões foram tomadas.

&emsp;&emsp;O sistema oferece uma interface que exibe as probabilidades de fraude associadas a diferentes consumos de água. Para garantir que os usuários compreendam esses resultados, o sistema:

- Visualização dos Dados: Os resultados são apresentados em uma tabela de fácil leitura, com colunas que detalham os principais indicadores (categoria, média de consumo e probabilidade de fraude).

- Ordenação e Filtragem: Os usuários podem organizar a tabela por diferentes métricas e aplicar filtros para focar em subconjuntos de dados, o que permite uma análise mais específica e ajustada às suas necessidades.

&emsp;&emsp;Além disso, cada tela do sistema contém instruções claras sobre o que está sendo solicitado do usuário. Essas orientações indicam o que o sistema vai fazer em cada etapa e incluem botões de ação para avançar para o próximo passo. Dessa forma, o sistema:

- Guias e Instruções: Orienta o usuário durante todo o processo, desde a adição de dados até a seleção de pré-filtros e a visualização dos resultados, garantindo que cada passo seja compreensível e fácil de seguir.

- Botões de Ação: Cada tela possui um botão de ação destacado que conduz o usuário de maneira intuitiva para a próxima etapa, promovendo uma experiência contínua e sem atritos.

&emsp;&emsp;Com esse design, o sistema busca não apenas fornecer os resultados, mas também guiar o usuário, facilitando o entendimento e a execução de cada tarefa.

## Estrutura de Pastas e Arquitetura do Projeto

### 1. node_modules/
- *Descrição*: Contém todas as dependências e pacotes do projeto instalados via npm ou yarn.
- *Função*: Facilita o uso de bibliotecas externas sem a necessidade de incluir manualmente cada uma no repositório.

### 2. public/
- *Descrição*: Diretório que contém os recursos estáticos, como imagens e outros arquivos que não são processados diretamente pelo JavaScript.
- *Função*: Serve como ponto de acesso para arquivos estáticos que serão servidos diretamente aos usuários.

### 3. src/
- *Descrição*: O diretório principal para a implementação do código-fonte do projeto. Contém as lógicas de front-end, componentes e as configurações necessárias para a aplicação.
  
#### Arquivos principais:
- *App.tsx*: Arquivo raiz da aplicação React, onde os componentes são montados e o fluxo da aplicação é iniciado.
- *App.css, App.styles.ts*: Arquivos de estilo utilizados no projeto para estilizar os componentes e a interface.
- *components/*: Contém os componentes reutilizáveis da aplicação.
- *lib/*: Contém funções auxiliares e utilitárias para o projeto.
- *pages/*: Contém as páginas da aplicação. Cada página pode ter rotas definidas no arquivo routes.tsx.

### 4. Arquivos de Configuração
- *package.json*:
  - *Descrição*: Contém as dependências do projeto, scripts de execução e metadados importantes.
  - *Função*: Gerencia as bibliotecas necessárias para a aplicação e define scripts como start e build.

- *vite.config.ts*:
  - *Descrição*: Configuração do Vite, o bundler utilizado no projeto.
  - *Função*: Define como o Vite deve compilar o código para desenvolvimento e produção.

- *tailwind.config.js*:
  - *Descrição*: Configurações do Tailwind CSS, o framework de CSS utilizado.
  - *Função*: Customiza e otimiza as classes utilitárias usadas para estilização.

- *tsconfig.json e tsconfig.app.json*:
  - *Descrição*: Arquivos de configuração do TypeScript, que especificam como o compilador deve tratar os arquivos .ts e .tsx.
  - *Função*: Define o ambiente de desenvolvimento para TypeScript, incluindo paths e regras de compilação.

### 5. Estilos e Assets
- *index.css*: Arquivo CSS principal que define as regras globais de estilo para a aplicação.
- *App.css, App.styles.ts*: Arquivos para gerenciamento de estilos específicos de componentes ou páginas.
- *assets/*: Diretório onde são armazenados recursos como imagens e ícones.

## Bibliotecas Utilizadas

### 1. *React*
- *Descrição*: Biblioteca JavaScript para construção de interfaces de usuário baseadas em componentes.
- *Função*: Criação da interface do usuário com base em componentes reutilizáveis.

### 2. *TypeScript*
- *Descrição*: Linguagem de programação baseada em JavaScript que adiciona tipagem estática ao código.
- *Função*: Melhora a segurança e a experiência de desenvolvimento, garantindo mais controle sobre os tipos de dados utilizados.

### 3. *Vite*
- *Descrição*: Bundler moderno para desenvolvimento rápido e eficiente de projetos.
- *Função*: Compila e serve o projeto de forma otimizada para desenvolvimento e produção.

### 4. *Tailwind CSS*
- *Descrição*: Framework de CSS utilitário para criação rápida de interfaces, baseado em classes utilitárias.
- *Função*: Facilita a estilização dos componentes, evitando a necessidade de escrever CSS personalizado para cada elemento.

### 5. *React Router*
- *Descrição*: Biblioteca de roteamento para aplicações React.
- *Função*: Gerencia as rotas de navegação entre as páginas da aplicação, permitindo navegação sem recarregar a página.

## Fluxo da Aplicação

1. *Entrada*: O arquivo App.tsx é o ponto de entrada do projeto, onde os componentes principais são montados.
2. *Roteamento*: As rotas são gerenciadas no arquivo routes.tsx, permitindo a navegação entre diferentes páginas da aplicação.
3. *Componentização*: Os componentes são organizados na pasta components/, permitindo reutilização e modularidade no código.
4. *Estilização*: A estilização é gerida principalmente através do Tailwind CSS, com estilos adicionais presentes em arquivos .css e .ts.
5. *Execução e Build*: O Vite é responsável por compilar e servir o projeto tanto em modo de desenvolvimento quanto em produção.

# <a name="c11"></a>11. Análise Descritiva de Dados de Fraudes

#### Incidência de Atos Fraudulentos

De acordo com os dados analisados, aproximadamente 24% das pessoas já cometeram algum ato fraudulento relacionado ao consumo de água. Este dado é significativo e revela um comportamento preocupante na população analisada. Estudos anteriores, como o de Smith et al. (2018), também indicam que fraudes em serviços públicos são um problema comum, afetando tanto a eficiência do serviço quanto a equidade no fornecimento.

#### Distribuição das Fraudes por Tipo de Cliente

A análise detalhada dos dados mostra que a grande maioria das fraudes, cerca de 92.64%, ocorre em residências. Este alto percentual sugere que os esforços de monitoramento e prevenção de fraudes devem ser direcionados principalmente para clientes residenciais. Segundo Jones e Martin (2020), fraudes residenciais são frequentemente mais difíceis de detectar devido ao grande número de unidades e à variabilidade no consumo individual.

#### Fraudes em Setores Públicos

Em contraste, apenas 0.30% das fraudes são identificadas em setores públicos. Esta baixa incidência pode ser atribuída a vários fatores, incluindo uma maior vigilância e controle em instalações públicas, bem como uma menor variabilidade no consumo que facilita a detecção de anomalias. Estudos como o de Rodriguez et al. (2019) indicam que o setor público geralmente possui melhores mecanismos de controle e auditoria, o que pode explicar a menor taxa de fraudes.

#### Tratamento de Dados

Neste projeto, realizado em parceria com a AEGEA, trabalhamos com uma base de dados que abrange o consumo de água entre os anos de 2019 e 2024, além de um histórico de fraudes ocorridas ao longo desses anos. O objetivo principal é analisar o consumo de água ao longo do tempo, calcular a média de consumo por ano e investigar a distribuição de fraudes. Para alcançar esses objetivos, seguimos um processo de limpeza e pré-processamento de dados bem estruturado.

#### Preparação do Ambiente

Utilizamos o Google Colab como plataforma de desenvolvimento e instalamos diversas bibliotecas para auxiliar no processo de análise. Em seguida, configuramos o caminho para importar os dados, o que nos permitiu carregar e manipular grandes volumes de dados de forma eficiente.

#### Unificação dos Dados

Unificamos os dados de consumo de água e as informações de fraudes em um único DataFrame. Isso envolveu a combinação das bases de dados, o que nos permitiu visualizar de maneira integrada todas as informações necessárias. A partir deste ponto, iniciamos o processo de tratamento dos dados, onde identificamos e tratamos campos que continham valores nulos de forma cuidadosa para garantir que não afetassem as análises subsequentes.

#### Normalização e Codificação

A normalização dos dados foi uma etapa crucial para garantir que todos os valores estivessem dentro de um intervalo comparável, especialmente para variáveis como consumo de água, que podem variar amplamente. Além disso, realizamos a codificação das variáveis categóricas, utilizando o método conhecido como one hot encoding, que converte colunas categóricas em valores numéricos binários. Isso foi fundamental para que as variáveis categóricas pudessem ser compreendidas e processadas adequadamente pelos modelos de machine learning.

#### Criação de Novas Colunas

Para melhorar a análise, criamos novas colunas que pudessem agregar valor:

1. Fraudes (0,1): Variável binária onde '1' indica a presença de fraude e '0' indica a ausência. Esta coluna foi construída com base na comparação do consumo de água com padrões típicos de comportamento fraudulento.
2. Chave Única (Matrícula + SEQ): Criada através da concatenação dos campos "Matrícula" e "SEQ". Esta coluna nos permitiu unir informações de diferentes tabelas de forma consistente e precisa.
3. Temperatura (Média dos Últimos 30 Dias): Calculamos a média da temperatura dos últimos 30 dias para analisar a influência de fatores ambientais no consumo de água.
4. Endereço (Rua, Bairro, Estado): Criamos colunas que reúnem as informações de Rua, Bairro e Estado para análises geoespaciais.

 ![image](https://github.com/user-attachments/assets/ac6e5214-8e46-423d-ac7c-e0615d1bd274)
Figura 1: Criação de colunas realizada pelo grupo

### Análise Exploratória dos Dados (EDA)
Após a etapa de tratamento e preparação dos dados, iniciamos a Análise Exploratória de Dados (EDA). O objetivo dessa análise é extrair insights relevantes, identificar padrões e relacionamentos nos dados e preparar as informações para a modelagem preditiva.
#### Consumo de Água ao Longo dos Anos

Criamos um DataFrame dedicado a visualizar o consumo médio de água ao longo dos anos. Utilizamos gráficos de linha e de barras para identificar tendências e variações sazonais.

#### Distribuição de Fraudes

Exploramos os dados de fraudes, observando a distribuição de fraudes ao longo dos anos e relacionando-as com o consumo de água. Realizamos uma análise específica em matrículas identificadas como fraudulentas, observando seus padrões de consumo mensal. Comparamos o consumo mensal médio, máximo e mínimo para identificar mudanças bruscas que pudessem estar associadas a fraudes.
#### Insights Obtidos

A partir das análises realizadas, identificamos a necessidade de coletar mais dados para aumentar a precisão na detecção de fraudes. Especificamente, seria crucial obter a fatura mensal de cada residência e a quantidade de litros de água bombeados para cada uma.

### Gráficos criados e insights obtidos 

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

 6. **Boxplot de consumo por fraude sem outliers:** Como podemos observar através desse boxplot, o consumo de água é muito menor perante os clientes que realizaram alguma fraude. A diferença é observável principalmente pela mediana de consumo dos fraudadores ser quase 2x.Também apresentam os casos de fraude uma variabilidade de consumo ligeiramente menor.
![image](https://github.com/user-attachments/assets/7038c541-9808-4c08-922f-6a33ace031cc) <br>
**Figura 6:** Gráfico criado pelo grupo <br> <br>
7. **Padrão de consumo por um fraudador:** Podemos obervar o histórico de consumo de uma matrícula fraudulenta, é visível as ocilações (algumas chegando em 0 de consumo) e um consumo médio baixo.
![image](https://github.com/user-attachments/assets/eb164a71-f261-4806-bb44-570542cf9783) <br>
**Figura 7:** Gráfico criado pelo grupo <br><br>
8. **Padrão de consumo de um não fraudador:** Podemos obervar o histórico de consumo de uma matrícula não fraudulenta, é visível algumas ocilações, porém todas elas correspondendo a média de consumo do histórico apresentado, não apresentando nenhuma anomalia.
![image](https://github.com/user-attachments/assets/085ae03d-7e50-42a4-afff-27d6e4bdaced) <br>
**Figura 8:** Gráfico criado pelo grupo <br> <br>

#### Conclusão da Análise Exploratória

O tratamento de dados e a análise exploratória são etapas fundamentais em qualquer projeto de ciência de dados. Elas nos permitem limpar e organizar os dados de forma a garantir a precisão das análises subsequentes. Ao realizar essas etapas, conseguimos compreender melhor os dados com os quais estamos lidando, identificar padrões e anomalias e assegurar que os resultados das análises sejam confiáveis e acionáveis.

Com base nas análises realizadas, propomos os seguintes próximos passos:

- Coletar dados adicionais, como a fatura mensal de cada residência e a quantidade de litros de água bombeados.
- Focar a modelagem preditiva em fraudes residenciais, uma vez que 92.64% das fraudes são dessa natureza.
- Investigar mais a fundo os padrões de comportamento dos fraudadores para melhorar a detecção e prevenção de fraudes.

# <a name="c12"></a>12. Documentação Técnica

### Documentação Pipeline/Modelo/API
### 12.1 **Introdução**
### *Objetivo do Projeto*
- Detectar fraudes no consumo de água utilizando técnicas avançadas de deep learning, que identificam padrões anômalos no consumo. Isso inclui a análise de dados históricos de consumo e a integração de variáveis externas, como índices macroeconômicos, climáticos e geográficos.
### *Contexto do Problema*
- Fraudes no consumo de água, como os "gatos", representam um grave problema para o setor de saneamento.  Além de gerarem perdas financeiras para as empresas,  comprometem o abastecimento, aumentam o risco de doenças e agravam a escassez hídrica. A detecção precoce, por meio da análise de dados, inspeções, tecnologias e denúncias, é crucial para minimizar esses impactos, garantir o fornecimento regular de água, proteger a saúde pública e combater o desperdício.  Diante da baixa acurácia (inferior a 50%) na identificação de fraudes, a AEGEA busca aprimorar seus métodos de investigação, e o desenvolvimento de um modelo preditivo surge como uma solução promissora para aumentar a eficiência na detecção de clientes fraudulentos.
### *Resumo da Solução*
Para resolver o problema da detecção de fraudes no consumo de água, desenvolvemos uma solução que envolve três etapas principais: 

- **Pipeline ETL**: Primeiramente, implementamos um pipeline de Extração, Transformação e Carga (ETL) utilizando módulos Python, que integra e processa dados de diversas fontes. O pipeline é responsável por coletar dados históricos de consumo de água e combiná-los com variáveis externas, como indicadores macroeconômicos, dados climáticos e eventos relevantes. Esse processo prepara os dados de entrada que alimentam o modelo de aprendizado profundo.

- **Modelo de Rede Neural LSTM**: Em seguida, construímos um modelo preditivo de Long Short-Term Memory (LSTM) utilizando Keras, que analisa padrões temporais ao longo de 7 semestres. O modelo recebe como entrada variáveis fixas, como categoria de cliente, e variáveis temporais, incluindo consumo de água, dados econômicos e meteorológicos. O objetivo é prever se há probabilidade de fraude por parte do cliente no oitavo semestre. 

- **API com FastAPI**: Por fim, o modelo foi integrado a uma API construída com FastAPI. A API permite o acesso ao modelo preditivo, possibilitando que o sistema seja utilizado para fazer previsões sobre novos dados de consumo. Com uma interface intuitiva e de fácil uso, a API facilita a integração com outros sistemas e garante a escalabilidade da solução.

### 12.2 **Arquitetura do Projeto**
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

### 12.3 **Pré-processamento dos Dados**

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

## 12.4 **Validação do Modelo**

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




# <a name="c13"></a>13. **Implantação da API**
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

### 13.1 **Considerações Técnicas**
   - **Melhorias Potenciais**:
     - Utilização de dados externos de validação para testar o modelo
     - Comparar novas arquiteturas que possibilitam menos gasto computacional como o GRU
     - Utilizar buscadores de hiperparâmetros como GridSearch ou RandomSearch
     - Integração da API com o Front-end  
   - **Desafios e Limitações**:
     - O modelo atual utiliza um registro de 23 meses do cliente, o que pode ser um problema para novas matrículas que não atingiram esse tempo. Além disso, foi necessário a criação de vários dados sintéticos para balancear o dataset, o que é natural em registros de série temporal com fraudes, mas pode prejudicar na entrada de novos dados não vistos.


# <a name="c14"></a>14. Referências

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
