# Makers Python Vol2 Group ECommerce project

* First clone from reposotory to your local folder using command
    - `git clone git@github.com:Alymbekov/eCommerce.git .`

* create virtual environment using command

    - `python3 -m venv <name of your environment>`

* activate your virtual environment
    
    - `source <name of your environment>/bin/activate`
    
* install requirements by commond

    - `pip3 install -r requirements.txt`
    
* create on near manage.py file .env, same as .env_example

    - generate secret key to put in to .env file
    
*  create database on postgresql using commands
    
    - `sudo su - postgres`
    - `psql`
    - `CREATE DATABASE <db_name>;`
    - `CREATE USER <db_user> WITH PASSWORD <'db_password'>;`
    - `ALTER ROLE root SET client_encoding TO 'utf8';`
    - `ALTER ROLE root SET default_transaction_isolation TO 'read committed';`
    - `ALTER ROLE root SET timezone TO 'UTC';`
    - `GRANT ALL PRIVILEGES ON DATABASE <db_name> TO <db_user>;`
    
* make migrations
    - `python manage.py makemigrations`
    - `python manage.py migrate`

* create superuser
    - `python manage.py createsuperuser`
    
* finally you can run your project

    - `python manage.py runserver`


