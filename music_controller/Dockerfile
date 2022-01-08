FROM python:3.9

WORKDIR /react

COPY . /react

RUN pip install --no-cache-dir pipenv && \
    pipenv install --system --deploy --clear 

COPY . /react

EXPOSE 8000 