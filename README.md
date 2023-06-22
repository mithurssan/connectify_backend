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

+--------------------------------+----------------------------------+
| Endpoint                       | Description                      |
+--------------------------------+----------------------------------+
| **User Endpoints**             |                                  |
+--------------------------------+----------------------------------+
| GET /users                     | Retrieve a list of all users     |
| GET /users/{user_id}           | Retrieve details of a user       |
| POST /users                    | Create a new user                |
| PATCH /users/{user_id}         | Update an existing user          |
| DELETE /users/{user_id}        | Delete a user                    |
+--------------------------------+----------------------------------+
| **Post Endpoints**             |                                  |
+--------------------------------+----------------------------------+
| GET /posts                     | Retrieve a list of all posts     |
| GET /posts/{post_id}           | Retrieve details of a post       |
| POST /posts                    | Create a new post                |
| PATCH /posts/{post_id}         | Update an existing post          |
| DELETE /posts/{post_id}        | Delete a post                    |
+--------------------------------+----------------------------------+
| **Comment Endpoints**          |                                  |
+--------------------------------+----------------------------------+
| GET /comments                  | Retrieve a list of all comments  |
| GET /comments/{comment_id}     | Retrieve details of a comment    |
| POST /comments                 | Create a new comment             |
| PUT /comments/{comment_id}     | Update an existing comment       |
| DELETE /comments/{comment_id}  | Delete a comment                 |
+--------------------------------+----------------------------------+
| **Company Endpoints**          |                                  |
+--------------------------------+----------------------------------+
| GET /api/company/{company_number} | Retrieve company information   |
+--------------------------------+----------------------------------+
| **Holiday Endpoints**          |                                  |
+--------------------------------+----------------------------------+
| GET /bookings                  | Retrieve a list of all holidays  |
| POST /bookings/book            | Create a new holiday booking     |
| GET /bookings/{holiday_id}     | Retrieve details of a holiday    |
| PUT /bookings/update/{holiday_id} | Update a holiday booking       |
| DELETE /bookings/delete/{holiday_id} | Delete a holiday booking    |
+--------------------------------+----------------------------------+
| **Journal Endpoints**          |                                  |
+--------------------------------+----------------------------------+
| GET /entries                   | Retrieve a list of all entries   |
| GET /entries/user/{user_id}    | Retrieve entries of a user       |
| POST /entries/add              | Create a new entry               |
| GET /entries/{entry_id}        | Retrieve details of an entry     |
| PUT /entries/update/{entry_id} | Update an existing entry         |
| DELETE /entries/delete/{entry_id} | Delete an entry                |
+--------------------------------+----------------------------------+
| **Rota Endpoints**             |                                  |
+--------------------------------+----------------------------------+
| GET /rotas                     | Retrieve a list of all rotas     |
| GET /rotas/get/{business_id}   | Retrieve rotas of a business     |
| POST /rotas/add                | Create a new rota                |
| GET /rotas/{rota_id}           | Retrieve details of a rota       |
| PUT /rotas/update/{rota_id}    | Update an existing rota          |
| DELETE /rotas/delete/{rota_id} | Delete a rota                    |
+--------------------------------+----------------------------------+
