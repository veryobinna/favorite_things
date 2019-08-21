### This is a simple CRUD API for notes management
#### To run the file, clone this repo
- clone this repo 
- Change directory into the app root directory

```bash 
cd server
pip install -r requirements.txt
```

#### Running the app
- Edit `settings.py.example` file and in the DATABASES section, add your database config

```bash
python manage.py runserver
```
  
#### Running the test
```bash
python manage.py test
```

#### Endpoints

* **URL**

  /favorite_things

* **Method:**
  
  `GET`


* **URL**

  /favorite_things

* **Method:**
  
  `POST`

* **Data Params**

  **Required:**

   `title=[string]`

   `ranking=[int]`

   `category=[int]`

* **URL**

  /favorite_things/int:favorite_thing_id

* **Methods:**
  
  `GET`
  `PUT`
  `DELETE`

* **URL**

  /categories

* **Method:**
  
  `POST`

* **Data Params**

  **Required:**

   `name=[string]`


* **URL**

  /categories

* **Method:**
  
  `GET`

* **URL**

  /categories/int:category_id

* **Methods:**
  
  `PUT`
  `DELETE`

