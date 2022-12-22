# QRCode-web
This is a web app created with python framework flask that helps generate qrcodes on the web, also providing a way to install the image


## Application Setup
Before running the app, the environment variables must be configured and the 
database must be initialized/prepared. 

### Configuring the environment variables
The application needs environment variables configured for it to run. These can
either be set in the system PATH OR in a .env file located in the project root
directory. If set in a .env file, it should contain the following settings in
this form (this example assumes an sqlite database is used for development and
a remote postgresql database is used for production):

SECRET_KEY=VeryLongRandomAndSecureAppSecretKey

DEV_DATABASE_URI=sqlite:///devDatabase.db

TEST_DATABASE_URI=sqlite://

DATABASE_URL=postgres://remoteusername:remotepassword@examplehost:port/remotedatabase

FLASK_APP=main.py


### Preparing the database
 If running locally via sqlite, open your terminal in the project root directory
 and run these commands:

- __flask db init__     (creates a new sqlite database if none exists)
- __flask db migrate -m "initial migration"__   (creates migration settings)
- __flask db upgrade__  (applies the migration settings to the database)

If running via a remote database (e.g a remote postgresql), just do:

- __flask db migrate -m "initial migration"__   (creates migration settings)
- __flask db upgrade__  (applies the migration settings to the database)


## Run the App
After configuring the environment variables and preparing the database, run the
app with this command:

__python main.py__
