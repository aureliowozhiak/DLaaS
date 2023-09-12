<!-- Sobre o Serviço -->
# Data Lake as a Service

Bem-vindo ao nosso Data Lake as a Service Open Source. Nosso software é especialistas em gerenciar e disponibilizar um Data Lake totalmente gerenciado para a sua empresa, proporcionando uma solução robusta e escalável para armazenamento e análise de dados.

Com o Data Lake as a Service, você não precisa se preocupar com a infraestrutura, configuração ou manutenção do ambiente. Nosso código cuidará de tudo, permitindo que você se concentre na extração de insights valiosos dos seus dados.

<!-- Benefícios -->
## Benefícios do Data Lake as a Service Open Source

- Escalabilidade: Expanda sua capacidade de armazenamento de dados de acordo com as necessidades do seu negócio.
- Segurança: Mantenha seus dados seguros com medidas avançadas de segurança e criptografia.
- Facilidade de Uso: Interface intuitiva e amigável para acessar e analisar seus dados de maneira simples.
- Redução de Custos: Elimine gastos com infraestrutura e mão de obra para manutenção do ambiente.
- Análise de Dados Avançada: Realize análises detalhadas e obtenha insights valiosos para a tomada de decisões estratégicas.

![Data Lake as a Service](https://dataengineer.help/DLaaS/DLaaS.png)

## Projeto no Miro

https://miro.com/app/board/uXjVMr3ALEo=/?share_link_id=493109150457

<!-- Setup do Projeto -->
## Setup do Projeto

Siga as etapas abaixo para configurar e rodar o projeto Data Lake as a Service em seu ambiente usando o Poetry.

### Instalar o Poetry

Se você ainda não tem o Poetry instalado, você pode fazê-lo usando o gerenciador de pacotes pip. Abra seu terminal e execute o seguinte comando:

```bash
pip install poetry
```

### Instalar as Dependências

Para instalar as dependências do projeto, execute o seguinte comando no diretório raiz do projeto:

```bash
poetry install
```

Isso garantirá que todas as dependências necessárias sejam instaladas no ambiente virtual do projeto.

### Rodar o Projeto
Para iniciar o projeto, execute o seguinte comando:

```bash
poetry run python -m main
```


Lembre-se de configurar as variáveis de ambiente e qualquer outra configuração necessária antes de executar o projeto. Certifique-se também de consultar a documentação para obter informações adicionais sobre como usar o Data Lake as a Service Open Source.

Aproveite o uso do Data Lake as a Service e comece a explorar os benefícios que ele oferece para o armazenamento e análise de dados em sua empresa!

## Sistema de Log no Projeto

O projeto Data Lake as a Service incorpora um sistema de log usando a biblioteca `logging` do Python. Esse sistema de log foi implementado para auxiliar no acompanhamento da execução do código e na identificação de possíveis problemas durante o processamento.

### Funcionamento Básico

O sistema de log funciona da seguinte forma:

1. **Configuração do Log**: No início do código, configuramos o sistema de log para direcionar as mensagens para um arquivo chamado "init.log" no diretório "logs". As mensagens de log são registradas com diferentes níveis, sendo o nível principal utilizado `INFO`, que é usado para mensagens informativas.

2. **Registro de Mensagens**: Ao longo do código, utilizamos a função `logging.info()` para registrar mensagens informativas em momentos relevantes da execução. Por exemplo, registramos informações sobre URLs processadas, solicitações API e operações de banco de dados.

3. **Benefícios**: O sistema de log proporciona vários benefícios, incluindo:
   - Acompanhamento do Progresso: As mensagens de log ajudam a rastrear o que está acontecendo durante a execução do código.
   - Depuração: Facilita a identificação de problemas e erros, permitindo uma depuração mais eficaz.
   - Auditoria: As mensagens de log podem ser usadas para auditoria e análise pós-execução.

4. **Localização dos Registros**: Todas as mensagens de log são registradas no arquivo "init.log" no diretório "logs". Certifique-se de criar a pasta "logs" no mesmo diretório onde o script está localizado ou ajuste o caminho do arquivo de log conforme necessário.

### Uso Recomendado

Ao executar o projeto Data Lake as a Service, é aconselhável consultar o arquivo de log "init.log" para obter informações sobre o progresso da execução. Se ocorrerem problemas, as mensagens de log fornecerão pistas valiosas para solucioná-los.

Lembre-se de configurar as variáveis de ambiente e qualquer outra configuração necessária antes de executar o projeto. Consulte também a documentação para obter informações adicionais sobre o uso do Data Lake as a Service.

A utilização do sistema de log ajuda a manter a transparência e a visibilidade durante a execução do projeto, contribuindo para uma experiência mais suave e confiável.
