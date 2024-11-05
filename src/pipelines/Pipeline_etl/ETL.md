### **Visão Geral do ETL**

Este projeto implementa um pipeline de ETL (extraction, tranform e load) para uso posterior pelo modelo. O processo se divide em três etapas:

1. **Extração dos Dados**: Coleta de dados de consumo e de fraudes de arquivos CSV armazenados no Google Drive.
2. **Transformação dos Dados**: Limpeza, tratamento e junção dos dados para facilitar a manipulação.
3. **Carga dos Dados**: Armazenamento dos dados processados em arquivos CSV e Parquet.

### **Estrutura do ETL**

Dividido em três módulos principais:

- **`main.py`**: Coordena o fluxo do pipeline, integrando os módulos de extração e transformação, e gerenciando a carga dos dados processados.
- **`extract.py`**: Contém as classes para extração dos dados de fontes externas e do drive.
- **`transform.py`**: Realiza a transformação dos dados, preparando-os para o modelo.
- **`load.py`**: [WIP].

### **Detalhamento dos Módulos**

#### **1. Módulo `main.py`**

Este é o script principal que coordena todo o pipeline. Ele faz uso de outras classes para realizar extração, transformação e carregamento dos dados. Os principais métodos da classe `Main` incluem:

- **`run_extract()`**: Chama os métodos de extração dos arquivos CSV de consumo e fraudes.
- **`run_transform()`**: Realiza a transformação dos dados extraídos, incluindo a criação de colunas adicionais e a junção dos dados de consumo e fraudes.
- **`load_csv()`** e **`load_parquet()`**: Salvam os dados transformados em formatos CSV e Parquet, respectivamente.
- **`check_partitioning()`**: Verifica se o particionamento dos dados está correto, escolha tomada para melhor performance em grandes volumes de dados.

#### **2. Módulo `extract.py`**

Este módulo lida com a extração dos dados. Existem duas classes principais:

- **`Extract`**: 
Lida com a extração dos dados passados pela AEGEA:
  - **`extract_csv_files()`**: Extrai dados de consumo a partir dos múltiplos arquivos CSV.
  - **`extract_frauds()`**: Extrai dados de fraudes do caminho do CSV específicado pela main.py.
  - **`get_dataframes()`** e **`get_frauds()`**: Retornam os DataFrames.

- **`ExtractExternal`**: Lida com a extração de dados de fontes externas, como APIs, e os transforma em DataFrames para posterior processamento. Esse código parece ser usado para adicionar variáveis externas ao dataset, como índices econômicos.

#### **3. Módulo `transform.py`**

Este módulo é responsável por transformar e preparar os dados para análise:

- **`Transform`**: 
  - **`create_anomes()`**: Cria uma coluna 'ANOMES' no formato MM/YY, a partir da data de referência. Essa coluna simplificará o cruzamento dos dados.
  - **`reduce_columns()`**: Remove colunas irrelevantes dos dados de consumo e de fraudes, mantendo apenas as essenciais.
  - **`transform_datatypes()`**: Formata os tipos de dados para garantir que os DataFrames de consumo e fraude estejam no mesmo formato. Etapa ainda mais necessária devido ao uso da biblioteca DASK.
  - **`set_index()`**: Define o índice das tabelas e realiza a repartição dos dados para a operação de merge.
  - **`left_join_fraudes()`**: Realiza o left join entre os dados de consumo e fraudes, marcando com 1 as linhas onde uma fraude é detectada.

- **`TransformExternal`**: Possui métodos para agregar e particionar os dados externos, se necessários.

### **Considerações Finais**

Este pipeline foi projetado para lidar com grandes volumes de dados utilizando Dask, que permite processamento paralelo e distribuído. A modularidade do código facilita a manutenção e possíveis expansões, como a adição de novas fontes de dados ou etapas de transformação.