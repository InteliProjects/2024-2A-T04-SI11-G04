# User Story e Wireframe

&emsp;&emsp;Este documento foi elaborado durante a segunda sprint do projeto de detecção de fraudes com o objetivo de transformar as necessidades dos usuários, definidas nas personas e anti-personas, em tarefas concretas e priorizadas para o desenvolvimento do produto, através de user stories, até a aplicação destas na prototipação da interface que o usuário terá com o sistema com a construção de um wireframe. Para detalhar ainda mais essas necessidades, foram documentados requisitos funcionais (o que o sistema deve fazer) e não funcionais (como o sistema deve funcionar).

&emsp;&emsp;Além disso, considerando a natureza do projeto de detecção de fraudes, identificamos a necessidade de criar uma nova persona: o usuário falsamente acusado. Essa persona representa um usuário legítimo que, por algum erro do sistema, foi identificado como fraudador. Ao incluir essa persona nas user stories, garantimos que o sistema não apenas detecte fraudes, mas também minimize o impacto negativo em usuários legítimos.

&emsp;&emsp;Os requisitos definidos neste documento servirão como base para a criação dos wireframes da interface, que nos permitirão visualizar de forma concreta como as funcionalidades do sistema serão apresentadas ao usuário. 

&emsp;&emsp;E considerando que este projeto lida com dados sensíveis de usuários dos serviços da AEGEA, e tem como propósito detectar possíveis usuários que cometem ilegalidades na utilização de serviços, este projeto deve também garantir a privacidade e a segurança dos dados dos usuários. Para isso, adotamos a abordagem de Privacy by Design, que consiste em integrar a proteção de dados desde o início do desenvolvimento do sistema, em todas as suas etapas, que podem ser verificados no item 5. deste documento. 

## 1. Requisitos do Sistema de Detecção de Fraudes


&emsp;&emsp;Os requisitos de um software definem as funcionalidades e características que ele deve ter para atender às necessidades dos usuários e aos objetivos do projeto. No caso de um sistema de detecção de fraudes, os requisitos detalham as ações que o sistema precisa realizar e as qualidades que ele deve possuir.


### 1.1 Requisitos Funcionais

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


### 1.2 Requisitos Não Funcionais


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


## 2. Persona Afetada - Maria

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

## 3. User Story

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


### 3.1 Matriz de Priorização

&emsp;&emsp;A matriz de priorização serve como um guia para a execução das nossas user stories. Nela, as user stories foram organizadas de acordo com a combinação de esforço necessário para a implementação e a prioridade de implementação, para entender o valor de negócio que cada uma delas entrega. Essa combinação permite visualizar  quais user stories devem ser realizadas primeiro. Isso ajuda no planejamento de tarefas para implementar as user stories nas sprints seguintes.

| **User Story** 	| Valor de Negócio	 | Esforço | Prioridade | Dependências | Justificativa |
|---	|---	|---	|---	|---	|---	|
| **User Story 02** 	| Alto | Alto | Alta | User Story 01 | A predição de fraudes é fundamental para o sucesso do sistema e oferece um grande valor para o negócio. |
| **User Story 01** 	| Alto | Médio | Alta | Nenhuma | A análise exploratória é o primeiro passo para entender os dados e identificar padrões de fraude. |
| **User Story 05** 	| Alto | Médio | Alta | Nenhuma | Garantir a privacidade dos dados é um requisito legal e ético fundamental. |
| **User Story 06** 	| Médio | Baixo | Média | User Story 05 | A transparência e a justiça do sistema são importantes para a confiança dos usuários. |
| **User Story 03** 	| Médio | Alto | Média | Nenhuma | O desempenho do sistema é importante, mas pode ser aprimorado gradualmente. |
| **User Story 04** 	| Baixo | Médio | Baixa | Nenhuma | A segurança é importante, mas a funcionalidade de login já existe em muitos sistemas. |


## 4. Wireframe

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


## 5. Aplicações de Privacy by Design e Recomendações

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
