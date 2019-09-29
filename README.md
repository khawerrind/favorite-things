# Favorite Things

A CURD application for managing your favorite things using **[Python](https://www.python.org/)**, **[Django](https://www.djangoproject.com/)**, **[Django REST Framework](https://www.django-rest-framework.org/)** & **[Vue](https://vuejs.org/)**

## Installation

Development environment is setup via [Docker](https://www.docker.com/) using [Docker Compose](https://docs.docker.com/compose/). To run the project simply run:

```bash
docker-compose build
docker-compose up
```

You should now be able to access the application on [http://locahost:8080](http://locahost:8080)

## Testing
For running the Django tests, run the following command:

```bash
make test
```

## Linting
For python [flake8](http://flake8.pycqa.org/en/latest/) is used for linting while using [eslint](https://eslint.org/) along with [eslint-plugin-vue](https://github.com/vuejs/eslint-plugin-vue) for frontend.

For checking the backend linting using `flake8` run the following command
```bash
make flake8
```

For checking the frontend linting using `eslint` run the following command
```bash
make eslint
```

## Deployment using Zappa:
There is a configuration file for Zappa named as `zappa_settings.json` in the project root directory. The configuration file uses AWS cli default profile. Read more about setting up AWS cli credentials [here](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html). AWS configuration settings are normally located under `~/.aws/confugration`. Make sure you have a profile with name `default` in `~/.aws/confugration` where you will define AWS keys.

Since zappa will deploy everything to cloud, you need to define your `S3 bucket` name for storing static contents.
You also need to have a RDS database up and running. In the `zappa_settings.json` file change the `vpc_config` value according to your RDS `SubnetIds` & `SecurityGroupIds` names.

Create a `.env` file in the project root directory and define the following variables

- **AWS_S3_STORAGE_ENABLED**
Should be set to `true`

- **AWS_S3_BUCKET**
Name of the S3 bucket from where the static content will be served

- **VUE_APP_PUBLIC_PATH**
The URL of the static S3 bucket. Should not end with a forward slash

- **VUE_APP_API_URL**
Set this to `/<name of your zappa stage>`. If your zappa stage name was `dev` then set this to `/dev`.

- **DATABASE_URL**
This variable is located under `zappa_settings.json`. It uses [DJ-Database-URL](https://github.com/jacobian/dj-database-url) connection string format. You can read about available formate [here](https://github.com/jacobian/dj-database-url#url-schema)

Now just run the following command to deploy using `zappa` (assuming you have setup your python virtual environment)
```bash
make deploy
```

## Database ERD diagram
![Database ERD diagram](https://i.imgur.com/gyYpYsq.png)

## Helping Material

 - [Python](https://docs.python.org/3/)
 - [Django](https://docs.djangoproject.com/en/2.2/)
 - [Django REST Framework](https://www.django-rest-framework.org/)
 - [Vue js](https://vuejs.org/v2/guide/)
 - [Vuex](https://vuex.vuejs.org/)
 - [Vuetify js](https://vuetifyjs.com/en/)
 - [Vuelidate](https://vuelidate.netlify.com/)
