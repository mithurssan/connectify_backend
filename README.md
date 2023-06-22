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

![Screenshot 2023-06-22 at 19 26 42](https://github.com/mithurssan/connectify_backend/assets/112406576/2e71509f-00bb-4add-b0c4-e944d16589e4)
![Screenshot 2023-06-22 at 19 26 54](https://github.com/mithurssan/connectify_backend/assets/112406576/75515510-a2ee-440c-a4d3-f7946d567d35)
![Screenshot 2023-06-22 at 19 27 02](https://github.com/mithurssan/connectify_backend/assets/112406576/bb2ccc7b-0f75-4c1b-83c1-0063316880f9)
