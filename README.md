### This is a simple CRUD API for notes management
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

