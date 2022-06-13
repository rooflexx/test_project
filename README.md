# test_project

test description

License: MIT

## Usage
Enter `make help` in terminal to see the list of available commands:
```
setup                   - Setup project for local development
lint                    - Lint the code with black
format                  - Format the code with black, autoflake, isort
start                   - Start the services
stop                    - Stop the services using docker-compose
stop-v                  - Stop all the services and remove the volumes
logs                    - See the logs of services - Listen for events
```

Start the application stack with docker:
```bash
make start # If you prefer using Makefile or:
docker-compose up -d --build # Manually with docker-compose commands

```

### Type checks
Running type checks with black and isort:

    $ make lint

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest

### Celery

This app comes with Celery as a background task executer.
The docker-compose will start the celery worker automatically

## Deployment
This project comes with out-of-the-box `CI` Pipeline that tests/builds the application and send the image over to `ECR`. After that
we assume that specific configuration are set up in [GitOps repo](http://github.com/CardoAI/gitops)  to deploy the application to Kubernetes. </br>
We are using `ArgoCD` and `GitOps` principles to continuously deliver the application to hosted environments. This step where image is always updated is also included in the `CI` Pipeline

The other files regarding the deployment (`docker image`) are set up in `compose` directory for all the services.
