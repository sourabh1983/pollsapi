# Integrating Django and Angular as single deployment unit.

This project is designed for developers who want to use Angular to build front-end apps and use Django for doing backend Restful API.

This project can be helpful for developers who are looking for an example project of integrating Angular and Django applications in a single deplyable app and both running in docker containers.

### Prerequisites

You need to have Python 3.6 and Docker installed in order to run this program and tests

### Run program on your machine

Below will create dist directory in frontend folder and package frontend application

`npm run build`

Below will bring up django(port 8000) and angular app(port 4200) and will also create proxy between both apps.
```
docker-compose up
```
If everything is well, you can access applicaton on localhost:8000

### Preparing application to run

`docker-compose build`

### Run backend unit tests using pytest

`docker-compose run web pytest`

### Run frontend unit tests using karma test runner

`docker-compose run frontend npm run test`

### Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

### Authors

* **Sourabh Kumar**
