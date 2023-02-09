# Run guide
`git clone https://github.com/tenessy0570/django_stripe.git` <br>
`cd django_stripe` <br>
`docker-compose up`

### No need to make migrations etc.
### Superuser already exists <br> (login=admin, password=admin)
### Two test objects in database with id 1, 2

Access to api: <br>
`127.0.0.1:8000/api`<br>
GET `127.0.0.1:8000/api/item/<int:item_id>`<br>
GET `127.0.0.1:8000/api/buy/<int:item_id>`


## .env file was removed from .gitignore intentionally so you dont have to waste your time to enter test_api_key values