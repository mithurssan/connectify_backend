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
