FROM public.ecr.aws/lambda/python:3.8

COPY main.py ${LAMBDA_TASK_ROOT}
COPY requirements.txt ${LAMBDA_TASK_ROOT}
COPY imgs /tmp/imgs
COPY templates ${LAMBDA_RUNTIME_DIR}/templates

RUN python3.8 -m pip install -r requirements.txt -t "${LAMBDA_TASK_ROOT}"

# Command can be overwritten by providing a different command in the template directly.
CMD ["main.handler"]
