FROM public.ecr.aws/lambda/python:3.8

COPY app.py main.py requirements.txt ./
COPY imgs ./
COPY templates ./

RUN python3.8 -m pip install -r requirements.txt -t .

# Command can be overwritten by providing a different command in the template directly.
CMD ["main.handler"]
