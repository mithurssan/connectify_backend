# Connectify_Backend
## Running the server
- Run `pipenv shell` to create a virtual env
- Run `pipenv install` to install the dependencies
- Create `.flaskenv` file in the project root directory with the following contents:
    - FLASK_APP=app
    - FLASK_DEBUG=1
    - KEY=`<YOUR_SECRET_KEY>`
    - DB_URL=`<YOUR_DB_URL_HERE>`
- Run `pipenv run dev` to  start the server. The server starts at [5000](http://127.0.0.1:5000)

## Generating secret key
- Run `python/python3` on command line to start python interpreter
- Run `import secrets` to import secrets
- Run `secrets.token_hex(16)` to get secret key
- Run `exit()` to close interpreter

## EndPoints 

### User 
---------------------------------
GET    /users
GET    /users/{user_id}
POST   /users
PATCH  /users/{user_id}
DELETE /users/{user_id}

### Post
---------------------------------
GET    /posts
GET    /posts/{post_id}
POST   /posts
PATCH  /posts/{post_id}
DELETE /posts/{post_id}

### Comment Endpoints
---------------------------------
GET    /comments
GET    /comments/{comment_id}
POST   /comments
PUT    /comments/{comment_id}
DELETE /comments/{comment_id}

### Company Endpoints
---------------------------------
GET    /api/company/{company_number}

### Holiday Endpoints
---------------------------------
GET    /bookings
POST   /bookings/book
GET    /bookings/{holiday_id}
PUT    /bookings/update/{holiday_id}
DELETE /bookings/delete/{holiday_id}

### Journal 
---------------------------------
GET    /entries
GET    /entries/user/{user_id}
POST   /entries/add
GET    /entries/{entry_id}
PUT    /entries/update/{entry_id}
DELETE /entries/delete/{entry_id}

### Rota 
---------------------------------
GET    /rotas
GET    /rotas/get/{business_id}
POST   /rotas/add
GET    /rotas/{rota_id}
PUT    /rotas/update/{rota_id}
DELETE /rotas/delete/{rota_id}

