# ELPRICE TEST


### Requisitos:
- Python 3.7.3
- Django 2.1.5
- Django Rest Framework 3.9.2
- Docker 18.09.2
- Docker Compose 1.24.0
- PostgresQL 9.5.15

### Branch:
- Master


### Como executar este:
Dentro de `conf/` renomei o arquivo `settings.ini.sample` para `settings.ini`.  

Por meio do Makefile rode o seguinte comando: 

``` bash
$ make up
```
Após o termino do mesmo precisamos executar a inserção de dados, para isso eu tenho dois métodos, por meio de `schema` ou manualmente.  
Para uma melhor analize eu prefiro usar o segundo método, no caso o manual, vamos ao mesmo.

Execute o seguinte comando: 

``` bash
$ make mmigrate
```

Com isso precisamos apenas importar a fixture para core. rode o seguinte comando:

```bash
$ make load
```

Se tudo ocorreu bem basta rodar o comando a baixo:
```bash
make runserver
```
E acessar o link `localhost:8000/api/v1/products/` que o mesmo estará funcionando :D.
para acessar o endpoint para o crawler acesse `localhost:8000/api/v1/items/`

- Em `/products/`, podemos visualizar os produtos criados e ou criar novos produtos.
- Já em `/products/id`, podemos visualizar um determinado produto, atualizar o mesmo ou deleta-lo. 


Have Fun!!!
