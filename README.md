# Connections Demo

A demo app showing a simple service using flask and some supporting packages

## Requirements

 * [Docker Desktop](https://www.docker.com/products/docker-desktop/) (Mac or Windows)

## Stack Information

* Python / Flask
* MySQL and SQLAlchemy
* Gunicorn

## Getting Started

It is recommended that you run two terminal tabs/windows, one for running the services and the other for running tests.

### Building and Running

To build and run the services, run this:

```
docker-compose up
```

The application will automatically restart with any changes you make to the source files. The API is available
at http://localhost:5005 for you to test manually.

Once the services are up, the database is empty. Run this to migrate the database:

```
docker-compose exec connections flask db upgrade
```

### Running Tests

The following will run all tests. None should be failing as part of the submission.

```
docker-compose exec connections pytest
```

Optionally, you can run a specific test by matching keywords

```
docker-compose exec connections pytest -k test_create_person
```

Adding the `-s` option will run tests without swallowing print statements and may be useful for debugging:

```
docker-compose exec connections pytest -s
```

### Cleaning up

When you are complete, you can Control-C on the window running the services to stop them.
This command will cleanup any volumes created (also allows starting fresh if something is not working):

```
docker-compose down -v
```
