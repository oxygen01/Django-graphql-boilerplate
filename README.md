# Docker-django-development-env

Docker Compose to set up and run a Django/PostgreSQL app

## To start the project

To create Django project

```sh
$ docker-compose run web django-admin startproject project_name .
```

If in linux: Change the ownership of the new files in the host

```sh
$ sudo chown -R $USER:$USER .
```
```sh
 $ docker-compose run web chmod -R 777 .
```

Replace the DATABASES = ... with the following:

```
DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': 'postgres',
       'USER': 'postgres',
       'HOST': 'db',
       'PORT': 5432,
   }
}
```

## Start coding

```sh
 $ docker-compose up
```

## Enter the docker container to create env

```sh
$ docker exec -it <container-name> /bin/bash
```

Inside the container To install an venv and active it

```sh
 $ virtualenv venv -p python
```

```sh
 $ source venv/bin/activate
```
```sh
 $ pip install -r requirements.txt
```
```sh
 $ python manage.py migrate
```

```sh
 $ python manage.py createsuperuser
```


## To shutdown

```sh
$ docker-compose down
```



### More info

[django_compose](https://docs.docker.com/compose/django/)


# Development

## Add new app
1. Add the app
2. Add the model
3. Add the app to the installed Apps
4. Make migrations
5. add the schema folder
6. add the query @see: links.schemes.link.query
6. add the mutation @see: links.schemes.link.mutation
7. add the query and the mutation to the main schema in the root project

## GraphQl APIs
after starting the server visit [graphql](http://localhost:8000/gqapi/) 

## To test 
* to obtain the token use createUser mutation 
* with authorization use Insomnia clint or postman and set 
the Authorization in the Header to jwt <token>


### More info

[graphql-python](https://www.howtographql.com/graphql-python/5-links-and-voting/)

