# totverprm
API para acesso aos Webservices do TOTVS ERP RM.

Exemplo:
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
