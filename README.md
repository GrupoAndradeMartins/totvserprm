# totverprm
API para acesso aos Webservices do TOTVS ERP RM.

## Instalação

pip install totverprm

### Exemplo para criação de um aluno:
```python
from datetime import datetime
from totvserprm.educational import Student

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
  nome='Fulano de tal',
  ra=35
)
```

### Exemplo para criação de um cliente:
```python
from datetime import datetime
from totvserprm.financial import Client

server = '192.168.1.100:8051'
username = 'admin'
password = 'admin'

client = Client(server, username, password)
client.create(
  ativo=True,
  codexterno=1,
  codcoligada=1,
  cpf_cnpj='11781328110',
  tipo_rua=1,
  tipo_bairro=1,
  bairro='Belvedere',
  rua='Rua Professor Pedro Aleixo',
  numero=695,
  estado='MG',
  cidade='Belo Horizonte',
  codigo_municipio=3106200,
  pais=1,
  data_nascimento=datetime(1990,5,14),
  nome='Cliente Teste Vetrol',
  classificacao=1,
  categoria='F',
  cep='30320-300'
)
```

### Exemplo para criação de um boleto:
```python
from datetime import datetime
from totvserprm.financial import Billet

server = '192.168.1.100:8051'
username = 'admin'
password = 'admin'

boleto = Billet(server, username, password)
boleto.create(
  codcoligada=1,
  data_vencimento=datetime(2017,10,30),
  valor=100,
  codcliente='0000470',
  codfilial=1,
  classificacao=1,
  tipo_documento='999',
  conta=1,
  historico='teste',
  centro_custo='01.019'
)
```
