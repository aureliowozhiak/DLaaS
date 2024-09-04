# Projeto de Extração e Transformação de Dados

Este projeto contém diversos módulos para extração, transformação e salvamento de dados. Abaixo está uma descrição de cada módulo e suas funcionalidades.

## Estrutura do Projeto

- `src/methods/loaders/fileSavers.py`
- `src/methods/extractors/apiRequests.py`
- `src/methods/extractors/databaseConnectors.py`
- `src/methods/extractors/webPageDataScrappers.py`
- `src/methods/transformers/dataCleaners.py`

## Módulos

### FileSavers

Localização: `src/methods/loaders/fileSavers.py`

Este módulo contém a classe `FileSavers` que é responsável por salvar conteúdo em arquivos. Suporta salvamento em formato CSV e texto simples.

#### Métodos

- `save_content(content, file_name, columns=[], sep=",")`: Salva o conteúdo em um arquivo. Se o arquivo for CSV, escreve as colunas e o conteúdo separado por vírgulas.

### ApiRequests

Localização: `src/methods/extractors/apiRequests.py`

Este módulo contém a classe `ApiRequests` que facilita a realização de requisições HTTP para APIs.

#### Métodos

- `make_request(endpoint, method="GET", params=None, data=None)`: Faz uma requisição HTTP para o endpoint especificado.
- `make_full_request(endpoint, method="GET", params=None, data=None, pagination=None)`: Faz requisições paginadas e retorna todas as respostas.

### DatabaseConnector

Localização: `src/methods/extractors/databaseConnectors.py`

Este módulo contém a classe `DatabaseConnector` que gerencia a conexão com um banco de dados e a execução de consultas.

#### Métodos

- `connect()`: Conecta ao banco de dados.
- `disconnect()`: Desconecta do banco de dados.
- `sanitize_query(query)`: Sanitiza uma consulta SQL para evitar injeções de SQL.
- `build_query_string(table, columns=None, where=None, limit=None)`: Constrói uma string de consulta SQL.
- `extract(table, columns=None, where=None, limit=None, return_type="json")`: Extrai dados do banco de dados e retorna no formato especificado.
- `query_data(table, columns=None, where=None, limit=None)`: Executa uma consulta SQL e retorna os dados.

### WebPageDataScrappers

Localização: `src/methods/extractors/webPageDataScrappers.py`

Este módulo contém a classe `WebPageDataScrappers` que facilita a extração de dados de páginas web.

#### Métodos

- `get_tag_content(tag_name)`: Retorna o conteúdo de todas as tags especificadas.
- `get_html()`: Retorna o HTML completo da página.
- `handle_content(tag_name, attrs)`: Extrai atributos específicos de tags.
- `count_words()`: Conta o número de palavras na página.
- `get_images()`: Retorna os URLs de todas as imagens na página.
- `count_tags(tag_name)`: Conta o número de tags específicas na página.
- `get_meta_tags()`: Retorna os meta tags da página.
- `search_text(search_text)`: Procura por um texto específico na página.
- `get_page_links(url)`: Retorna todos os links da página.

### DataCleaner

Localização: `src/methods/transformers/dataCleaners.py`

Este módulo contém a classe `DataCleaner` que realiza a limpeza de dados em um DataFrame.

#### Métodos

- `remove_duplicates()`: Remove duplicatas do DataFrame.
- `handle_missing_values(method="drop", columns=None)`: Lida com valores nulos no DataFrame usando o método especificado.
- `clean_data()`: Remove duplicatas e lida com valores nulos.
- `get_cleaned_dataframe()`: Retorna o DataFrame limpo.

## Requisitos

Os requisitos do projeto serão especificados em um arquivo `requirements.txt` que deve ser gerado posteriormente.

## Como Usar

1. Clone o repositório.
2. Instale os requisitos.
3. Importe e utilize as classes conforme necessário em seu projeto.

## Contribuição

Sinta-se à vontade para abrir issues e pull requests para melhorias e correções.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.