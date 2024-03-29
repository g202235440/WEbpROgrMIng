FROM python:3.10
WORKDIR /code
COPY ./requirements.txt /code/requiremets.txt
RUN pip3 install --no-cache-dir --upgrade -r /code/requiremets.txt