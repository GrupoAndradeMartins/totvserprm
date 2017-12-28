# totverprm
API para acesso aos Webservices do TOTVS ERP RM.

## Instalação

pip install totvserprmgam

### Exemplo para retornar dados de um cliente:
```python
from totvserprmgam.financial import Client

server = '192.168.1.100:8051'
username = 'admin'
password = 'admin'

client = Client(server, username, password)

client_1 = client.get(codcoligada=0, id='0000496')

```

### Exemplo para retornar dados de todos clientes:
```python
from totvserprmgam.financial import Client

server = '192.168.1.100:8051'
username = 'admin'
password = 'admin'

client = Client(server, username, password)

clients = client.all(codcoligada=0)

```

### Exemplo para criação de um aluno:
```python
from datetime import datetime
from totvserprmgam.educational import Student

server = '192.168.1.100:8051'
username = 'admin'
password = 'admin'

stundet = Student(server, username, password)
stundet.create(
  codcoligada=1,
  codtipocurso=1,
  data_nascimento=datetime(1992, 2, 3, 4, 5),
  estado_natal='MG',
  naturalidade='Belo Horizonte',
  cpf='11781328110',
  nome='Fulano de tal',
  sexo='Masculino',
  tipo_rua=1, # RUA = 1 / AVENIDA = 6
  tipo_bairro=1, # BAIRRO = 1
  bairro='Belvedere',
  rua='Rua Professor Pedro Aleixo',
  numero=695,
  estado='MG', # EX = Exterior
  cidade='Belo Horizonte',
  codigo_municipio=06200, # Ultimos 5 digitos do codigo do ibge do município
  pais='Brasil',
  cep='30320-300',
  codcurso='00001',
  codcliente='0000001',
  codcoligada_cliente=0,
  email='teste@vetrol.com.br',
  telefone1='(32) 99999-9999',
  telefone2='(31) 99999-9998',
  telefone3='(31) 99999-9997'
)
```

### Exemplo para criação de um cliente:
```python
from datetime import datetime
from totvserprmgam.financial import Client

server = '192.168.1.100:8051'
username = 'admin'
password = 'admin'

client = Client(server, username, password)
client.create(
  ativo=True,
  codexterno=1,
  codcoligada=0,
  codcoligada_contexto=1,
  tipo_cliente='000', # 000 para Aluno
  cpf_cnpj='11781328110', # Sem formatação
  tipo_rua=1, # RUA = 1 / AVENIDA = 6
  tipo_bairro=1, # BAIRRO = 1
  bairro='Belvedere',
  rua='Rua Professor Pedro Aleixo',
  numero=695,
  estado='MG', # EX = Exterior
  cidade='Belo Horizonte',
  codigo_municipio=06200, # Ultimos 5 digitos do codigo do ibge do município
  pais=1, # 1 = Brasil, 2 = Portugal, 11 = Angola
  data_nascimento=datetime(1990,5,14),
  nome='Fulano de tal',
  classificacao=1, # 1 = Cliente, 2 = Fornecedor, 3 = Ambos
  categoria='F', # F = Pessoa Física, J = Pessoa Jurídica
  cep='30320-300',
  email='teste@vetrol.com.br',
)

```

### Exemplo para criação de um boleto:
```python
from datetime import datetime
from totvserprmgam.financial import Billet

server = '192.168.1.100:8051'
username = 'admin'
password = 'admin'

boleto = Billet(server, username, password)
boleto.create(
  codcoligada=1,
  codcoligada_contexto=1,
  codcoligada_cfo=0,
  codcoligada_fin=0,
  data_vencimento=datetime(2017,10,30),
  valor='100,55', # Enviar string com separação por vírgula
  codcliente='0000470',
  codfilial=1,
  classificacao=1, # 1 = Receber, 2 = Pagar
  tipo_documento='999', # 999 = Taxa de adesão
  historico='Teste', # Descrição
  centro_custo='01.019',
  codnatfinanceira='01.001.0001',
  id_vendedor=1400
)
```


### Exemplo de consulta SQL:
```python
from totvserprmgam.retrieve import ConsultSQL

server = '192.168.1.100:8051'
username = 'admin'
password = 'admin'

consultsql = ConsultSQL(server, username, password)
consultsql.get(
  codcoligada=0,
  codsistema='F',
  codsentenca='CODIGO_CONSULTA',
  parameters={'PARAMETRO_1': 'VALOR_1', 'PARAMETRO_2': 'VALOR_1'}
)
```
