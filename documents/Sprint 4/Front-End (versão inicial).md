# Front-End: Versão Inicial

- Mínimo de duas telas em vias de finalização.
- Relatório detalhado da utilização do Design System escolhido, com exemplos de implementação na aplicação.
- Códigos-fonte da implementação, devidamente comentados e organizados.
- Screenshots ou vídeos da aplicação em funcionamento, destacando os pontos mencionados acima.

- Utilização do Design System
- Heurísticas de Nielsen
- Explicabilidade 

&emsp;&emsp;A primeira versão do frontend deste projeto foi desenvolvido durante a Sprint 4, com base nos feedbacks recebidos na review da Sprint 3, em conjunto com o nosso parceiro. As informações obtidas a partir do protótipo de alta fidelidade foram necessárias para aprimorar a interface do usuário e assegurar uma experiência e um fluxo de navegação mais intuitivo e eficiente, com foco nos resultados e nos dados.

&emsp;&emsp;Neste projeto, utilizamos técnicas de deep learning para identificar e prever potenciais casos de fraude em sistemas de abastecimento de água. O frontend, desenvolvido é responsável por receber os dados processados pelo modelo de rede neural e apresentar os resultados aos usuários, como analistas e gestores da AEGEA, protegendo os dados sensíveis dos usuários dos serviços da empresa, que são os que geram os dados para o modelo.

Esta documentação refere-se à primeira versão do Front-End para desktop. Componentes podem sofrer alterações em versões futuras e algumas funcionalidades para mobile ainda estão em desenvolvimento.

## Introdução

&emsp;&emsp;Este documento tem como objetivo fornecer uma referência completa para todos os envolvidos no projeto, desde desenvolvedores e designers até stakeholders e usuários finais. Ao compreender os princípios e as decisões de design por trás do Front-End, será possível realizar manutenções, adicionar novas funcionalidades e garantir a consistência visual da aplicação. 

&emsp;&emsp;O front-end, a interface visual de nossa aplicação, desempenha um papel importante na experiência do usuário já que é através dele que os usuários interagem com o sistema, realizando tarefas e obtendo informações. Um front-end bem projetado torna a aplicação mais agradável de usar e contribui para o sucesso do negócio. Por isso é preciso seguir algumas diretrizes, como Design System e as Heurísticas de Nielsen, pois ao estabelecer padrões visuais e componentes reutilizáveis, o Design System torna a interface coesa e intuitiva, facilitando a navegação do usuário. Paralelamente, as Heurísticas de Nielsen oferecem princípios para criar interfaces eficientes, reduzindo a carga cognitiva e aumentando a satisfação do usuário. 

&emsp;&emsp;Com um Design System e a aplicação das Heurísticas, o desenvolvimento se torna mais ágil, a manutenção mais simples e a experiência do usuário mais positiva, contribuindo para o sucesso da aplicação. Uma aplicação só é relevante se for utilizada. Se utilizar a aplicação torna a experiência do usuário pior do que já utilizar o que ele tem disponível, ele não vai adotar a solução proposta.

&emsp;&emsp;Esta é a primeira versão do Front-End, focada na experiência do usuário analista da AEGEA em desktop. Componentes e funcionalidades podem ser ajustados ou adicionados em versões subsequentes, incluindo a versão mobile, que será desenvolvida na próxima sprint. Documentamos neste momento os componentes existentes para facilitar o entendimento e a manutenção do código, mesmo que eles estejam em desenvolvimento.

## Feedbacks, Melhorias e Impacto nos Objetivos

&emsp;&emsp;Durante a sprint review da terceira sprint, o protótipo de alta fidelidade foi apresentado ao nosso parceiro de projeto. Recebemos um feedback sobre a expectativa de uma interface mais criativa e dinâmica sobre a navegação e apresentação dos dados. O parceiro considerou o design do protótipo como excessivamente quadrado e rígido.

&emsp;&emsp;Essa percepção nos levou a um debate aprofundado sobre a estética da interface, levando em conta tanto os comentários do parceiro quanto os objetivos do projeto. Considerando a natureza sensível do projeto, que envolve a identificação e prevenção de fraudes, a proteção de dados dos usuários e o foco em resultados e dados, e a decisão por uma abordagem mais minimalista.

&emsp;&emsp;Optou-se por uma interface com menor utilização de cores fortes e um design mais clean, priorizando a funcionalidade. Ações como a subida de arquivos, a aplicação de filtros e a visualização de dados ganharam destaque. Essa decisão alinha-se com o objetivo de oferecer uma experiência de usuário clara e objetiva, facilitando a compreensão e a interação com as funcionalidades essenciais do sistema.

## Front-End e Fluxo de Navegação

&emsp;&emsp;As imagens a seguir ilustram o fluxo de navegação do usuário na plataforma, apresentando as telas desenvolvidas até o momento. É importante ressaltar que este é uma primeira versão, e algumas funcionalidades, como pop-ups de notificação, ainda estão em desenvolvimento e podem sofrer alterações. O objetivo é demonstrar a sequência de interações do usuário desde o login até a obtenção dos resultados finais.


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

&emsp;&emsp;A tabela de resultados apresenta um resumo dos dados filtrados, incluindo informações como categoria, média de consumo e probabilidade de fraude. O usuário pode ordenar a tabela por qualquer coluna para facilitar a análise. 

<p align="center"> <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G04/blob/main/assets/protweb/FE-Resultado.png" border="0"> </p>
Figura 6. Tela com a tabela de resultados, mostrando informações como categoria, média de consumo e probabilidade de fraude.<br> <br> 


<p align="center"> <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G04/blob/main/assets/protweb/FE-Resultado2.png" border="0"> </p>
Figura 7. Continuação da tela com ênfase no gráfico.<br> <br> 


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

&emsp;&emsp;A tabela também está sendo refinada para reduzir a sensação de rigidez. Os elementos estão sendo reorganizados e formatados para criar uma apresentação mais visualmente agradável, com as linhas da tabela mais claras que o texto, a remoção de linhas de separação das colunas, dando mais ênfase nos dados em si. A figura 10 mostra a versão feita no protótipo (A) e a versão em implementação no Front-End (B).

Observação: Em relação à tabela, algumas alterações ainda estão sendo feitas, como adição de cores no texto "Fraude" para realçar a informação, e a adição da coluna para seleção de matrículas para enviar para o fiscal que recebe uma lista para vistorias de matrículas.

<p align="center"> <img src="https://github.com/Inteli-College/2024-2A-T04-SI11-G04/blob/main/assets/protweb/Comp-Resultados.png" border="0"> </p>
Figura 10. Comparação entre as versões do protótipo de alta fidelidade (A) e do front-end (B) da tela de resultados<br> <br> 

## Design System

&emsp;&emsp;Design System é um conjunto de regras, componentes e padrões de design que servem como guia para a criação de interfaces digitais consistentes e escaláveis, garantindo que todos os elementos visuais e interativos de um produto digital sigam uma mesma linguagem visual e ofereçam uma experiência de usuário unificada. Abaixo estão os itens em que foram utilizados os princípios de Design System:

### 1. Paleta de Cores
   
&emsp;&emsp;A paleta de cores foi escolhida para transmitir uma sensação de profissionalismo, modernidade, confiança.

- Cor Primária: #072C59 (Azul Marinho Escuro)

&emsp;&emsp;Utilização: Botões, elementos de destaque, títulos e outros componentes principais.

Essa cor, escolhida como cor primária, confere um ar de seriedade e confiabilidade ao projeto, sendo utilizada nos elementos em geral.

- Cor Neutra: #FFFFFF (Branco)

&emsp;&emsp;Utilização: Fundo das telas, espaços vazios e como cor de texto em botões.

&emsp;&emsp;A cor branca, por sua vez, proporciona um contraste claro com o azul marinho, garantindo alta legibilidade e criando um ambiente visual limpo e organizado. É utilizada como fundo das telas e como cor de texto em botões com fundo azul marinho.

### 2. Tipografia

&emsp;&emsp;Fonte principal: Inter

&emsp;&emsp;Variações:

- Bold: Utilizada em títulos, cabeçalhos e para destacar elementos importantes.

- Regular: Utilizada para o corpo do texto e rótulos.

- Thin: Utilizada para textos menores ou secundários.

&emsp;&emsp;A fonte Inter foi escolhida por sua legibilidade e versatilidade, onde as variações da fonte (Bold, Regular e Thin) permitem criar hierarquias visuais claras e destacar os elementos mais importantes da interface.

### 3. Componentes

&emsp;&emsp;Botões: São elementos interativos da interface. Seu design foi padronizado para garantir uma experiência de usuário consistente.

&emsp;&emsp;Formato: Retangular com bordas arredondadas.

&emsp;&emsp;Cor: Primária #072C59 (Azul Marinho Escuro)

&emsp;&emsp;Cor do texto: #FFFFFF (Branco)


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

## Próximos Passos

&emsp;&emsp;Como esta é uma primeira versão, os feedbacks coletados durante a sprint review serão analisados para identificar melhorias e ajustes necessários. O foco será no refinamento da interface com base nas observações dos usuários e stakeholders.

&emsp;&emsp;Além disso, o processo de finalização do front-end será encaminhado em paralelo à integração com o back-end, visando a consistência entre as camadas da aplicação.

&emsp;&emsp;Outra importante etapa será o desenvolvimento de uma versão mobile, que será projetada com foco em um novo tipo de usuário: o fiscal de campo. Esta versão permitirá que os fiscais recebam e visualizem listas de matrículas a serem vistoriadas.

