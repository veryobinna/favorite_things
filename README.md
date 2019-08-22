### About
This is a simple app to keep track of your favorite things.

#### Thought process
I  started the app by first figuring out how many tables I needed and the relationship. I figured out two tables will be needed, one for categories, and the other for favorite things,  and the relationship, as can be seen in the [ERD](Favorite_things_erd.vpd.jpg). After that, I figured out the best way to reorder the ranking on each addition. Fetching all the data from the DB and reordering each rank was the obvious way, but that would be wasteful, so I used an update query instead. The logic is simple, on each new insert or delete, and add a value of 1 or subtract a value of 1 accordingly from each subsequent rows.

#### Deployment process
This app is deployed on Heroku and the steps are as follows:
- Compile and minify the client
- Update the settings of Django to point to the compiled code
- Create a script to run the migration and run the server on Heroku (Procfile)
- Create an online DB
- Create the app on Heroku
- Run a script that sets the production env variables (Database credentials, secret keys, env and base domain address)
- Push the code to Heroku.


#### To run the file, clone this repo
- clone this repo 
- Change directory into the app root directory

```bash 
cd server
pip install -r requirements.txt
```

#### Running the server
- Edit `settings_local.py.example` file and in the DATABASES section, add your database config, and rename to `settings_local.py`
- Edit `env.example` file and put in your credentials and rename to `.env`

```bash
source .env
python manage.py runserver
```
  
#### Running the server test
```bash
python manage.py test
```

### Compiles and hot-reloads web client for development
```
npm run serve
```

### Compiles and minifies web client for production
```
npm run build
```

### Run your tests
```
npm run test
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

### Lints and fixes files on server
```
black favorite_things
```

#### Server Endpoints

* **URL**

  /api/favorite_things

* **Method:**
  
  `GET`


* **URL**

  /api/favorite_things

* **Method:**
  
  `POST`

* **Data Params**

  **Required:**

   `title=[string]`

   `ranking=[int]`

   `category=[int]`

* **URL**

  /api/favorite_things/int:favorite_thing_id

* **Methods:**
  
  `GET`
  `PUT`
  `DELETE`

* **URL**

  /api/categories

* **Method:**
  
  `POST`

* **Data Params**

  **Required:**

   `name=[string]`


* **URL**

  /api/categories

* **Method:**
  
  `GET`

* **URL**

  /api/categories/int:category_id

* **Methods:**
  
  `PUT`
  `DELETE`

