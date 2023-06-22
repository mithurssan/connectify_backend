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

## Users 

| Endpoint                      | Description                                          |
|-------------------------------|------------------------------------------------------|               
| GET /users                    | Retrieve a list of all users.                        |
| GET /users/{user_id}          | Retrieve details of a specific user.                 |
| POST /users                   | Create a new user.                                   |
| PATCH /users/{user_id}        | Update an existing user.                             |
| DELETE /users/{user_id}       | Delete a user.                                       |

## Posts

| Endpoint                      | Description                                          |
|-------------------------------|------------------------------------------------------|    
| GET /posts                    | Retrieve a list of all posts.                        |
| GET /posts/{post_id}          | Retrieve details of a specific post.                 |
| POST /posts                   | Create a new post.                                   |
| PATCH /posts/{post_id}        | Update an existing post.                             |
| DELETE /posts/{post_id}       | Delete a post.                                       |

## Comments

| Endpoint                      | Description                                          |
|-------------------------------|------------------------------------------------------|    
| GET /comments                 | Retrieve a list of all comments.                     |
| GET /comments/{comment_id}    | Retrieve details of a specific comment.              |
| POST /comments                | Create a new comment.                                |
| PUT /comments/{comment_id}    | Update an existing comment.                          |
| DELETE /comments/{comment_id} | Delete a comment.                                    |

## Company House

| Endpoint                      | Description                                          |
|-------------------------------|------------------------------------------------------|    
| GET /api/company/{company_number} | Retrieve summary information for a company       |

## Bookings 

| Endpoint                      | Description                                          |
|-------------------------------|------------------------------------------------------|    
| GET /bookings                 | Retrieve a list of all holidays.                     |
| POST /bookings/book           | Create a new holiday booking.                        |
| GET /bookings/{holiday_id}    | Retrieve details of a specific holiday.              |
| PUT /bookings/update/{holiday_id} | Update an existing holiday booking.              |
| DELETE /bookings/delete/{holiday_id} | Delete a holiday booking.                     |

## Journal 

| Endpoint                      | Description                                          |
|-------------------------------|------------------------------------------------------|    
| GET /entries                        | Retrieve a list of all journal entries.        |
| GET /entries/user/{user_id}         | Retrieve journal entries for a specific user.  |
| POST /entries/add                   | Create a new journal entry.                    |
| GET /entries/{entry_id}             | Retrieve details of a specific journal entry.  |
| PUT /entries/update/{entry_id}      | Update an existing journal entry.              |
| DELETE /entries/delete/{entry_id}   | Delete a journal entry.                        |

## Rotas 

| GET /rotas                           | Retrieve a list of all rotas.                 |
|-------------------------------|------------------------------------------------------|    
| GET /rotas/get/{business_id}         | Retrieve rotas for a specific business.       |
| POST /rotas/add                       | Create a new rota.                           |
| GET /rotas/{rota_id}                 | Retrieve details of a specific rota.          |
| PUT /rotas/update/{rota_id}          | Update an existing rota.                      |
| DELETE /rotas/delete/{rota_id}       | Delete a rota.                                | 
