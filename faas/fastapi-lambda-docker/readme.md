# FastAPI to AWS Lambda using Docker images

This is a simple project to learn to publish web apps built using FastAPI 
framework to AWS Lambda service. For this project, the deployment mechanism
will be Docker Images using SAM framework, instead of zip file uploaded to S3.

## Set Up
As of Sep 2021, building Docker images still rely on installing using Pip and requirements.txt.
So, we will use virtualenv instead of `Pipenv`.

```cmd
$ fastapi-lambda-docker git:(master) conda activate aws_lambda_default

>>> (aws_lambda_default) ➜  fastapi-lambda-docker git:(main) python -m venv venv  # this creates the venv folder in pwd
>>> (aws_lambda_default) ➜  fastapi-lambda-docker git:(main) ✗ . venv/bin/activate

(venv) (aws_lambda_default) ➜  fastapi-lambda-docker git:(master) ✗ pip install fastapi  # installs fastapi, pydandic, starlette
(venv) (aws_lambda_default) ➜  fastapi-lambda-docker git:(master) ✗ pip install uvicorn[standard]
(venv) (aws_lambda_default) ➜  fastapi-lambda-docker git:(master) ✗ pip install jinja2
(venv) (aws_lambda_default) ➜  fastapi-lambda-docker git:(master) ✗ pip install mangum
(venv) (aws_lambda_default) ➜  fastapi-lambda-docker git:(master) ✗ pip install aiofiles # needed to serve files
```

The above will get you started with running the FastAPI application. To publish the server on the web using SAM install
the following

```
> docker ps   # to verify docker engine is running
> brew --versrion  # to verify brew is running

> brew tap aws/tap
> brew install aws-sam-cli   # takes a while to finish

> sam --version
> 1.31.0
```

## SAM hello-world configuration


## Resources
FastAPI is based on Starlette and Pydantic. To get an overview, do this:

 - Watch the Youtube video by its founder: https://www.youtube.com/watch?v=37CcB2GBdlY
 - Read the tutorial https://fastapi.tiangolo.com/tutorial/
 - Use the advanced tutorial for parts that involve serving out HTML and Templates

Making FastAPI compatible with Lambda:
 - https://medium.com/analytics-vidhya/python-fastapi-and-aws-lambda-container-3e524c586f01 using Mangum

SAM for AWS Lambda
 - https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install-mac.html