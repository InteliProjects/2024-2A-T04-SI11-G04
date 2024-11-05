# Protótipo de alta fidelidade

&emsp;&emsp;O protótipo de alta fidelidade foi desenvolvido para a entrega da sprint 3, incorporando os feedbacks recebidos em relação às user stories. Com base no wireframe, foram realizadas melhorias relacionadas à proteção de dados dos clientes da Aegea e para evitar possíveis viéses sobre os resultados gerados pela solução do projeto, as quais podem ser verificadas nas próximas seções. Esse processo visou aprimorar a experiência do usuário e alinhar o design com os objetivos funcionais e não funcionais definidos nas fases anteriores do projeto.

## Introdução

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

