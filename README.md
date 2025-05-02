**💡 Objetivo**
Permitir o ajuste do volume de alerta de um veículo via linha de comando, enviando as configurações para um servidor que realiza o controle dos dispositivos.

**⚙️ Funcionamento**
Instale as LIBS contidas no requirements.txt, e para testar o Script execute o comando:
jupyter notebook

**📌 Observação**
Certifique-se de que a API e o Jupyter esteja em execução paralelamente no endereço http://localhost:8000/ e aceite requisições no endpoint /api/dispositivos/configurar. 


**NÍVEL 1**

Função que ajusta o volume de um veículo identificado pela sua placa.
Envia uma requisição POST para um servidor que configura o volume de alerta.

Parâmetros:
placa (str): A placa do veículo a ser configurado (ex: 'ABC1234').
volume (int): O volume de alerta desejado, que deve estar entre 0 e 100.

Retorna:
str: Mensagem indicando sucesso ou erro na configuração do volume.


**NÍVEL 2**

Função que ajusta vários veículo de uma vez identificado pela sua placa.
Envia uma requisição POST para um servidor que configura o volume de alerta.

Parâmetros:
placa (str): A placa do veículo a ser configurado (ex: 'ABC1234').
volume (int): O volume de alerta desejado, que deve estar entre 0 e 100.

Retorna:
str: Mensagem indicando sucesso ou erro na configuração do volume.

**NÍVEL 3**

Este script permite enviar comandos de configuração de volume em paralelo para uma API, utilizando programação assíncrona com asyncio e aiohttp.
É útil para melhorar a performance ao lidar com múltiplas requisições simultâneas.

Parâmetros:
placa (str): A placa do veículo a ser configurado (ex: 'ABC1234').
volume (int): O volume de alerta desejado, que deve estar entre 0 e 100.

Retorna:
str: Mensagem indicando sucesso ou erro na configuração do volume.

**NÍVEL 4**

**°Verifique se a placa está em um formato válido**

Antes de enviar a requisição, o código verifica se a placa do veículo está em um **formato válido**:

- Deve conter exatamente **7 caracteres**.
- Todos os caracteres devem ser **alfanuméricos** (letras e números, sem traços ou espaços).

Essa validação evita o envio de dados inválidos para a API.

**°Verifique se o volume está dentro do intervalo permitido (0-100)**

O código também verifica se o valor do volume está dentro do intervalo permitido:

- O volume deve estar entre **0 e 100**.
- Qualquer valor fora desse intervalo é considerado **inválido** e a requisição não será enviada.

Essa verificação previne o envio de configurações incorretas para o servidor.

**°Trate erros de conexão com o servidor**

O código utiliza um bloco `try-except` para **tratar falhas de conexão com o servidor**:

- Caso a API esteja offline, indisponível ou ocorra qualquer erro de rede, o programa captura a exceção com `requests.RequestException`.
- Em vez de interromper a execução, ele exibe uma mensagem de erro informando qual placa falhou e o motivo.

Esse tratamento garante que o programa continue rodando mesmo se um ou mais envios falharem.

**°Implemente logs para acompanhar o progresso das operações**

- Cada linha indica a **placa do veículo**, o **código de status HTTP** e a **mensagem retornada** pela API.
- Em caso de erro, também é exibida uma mensagem descritiva com a falha capturada.
