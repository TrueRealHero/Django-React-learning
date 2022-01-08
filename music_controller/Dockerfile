FROM python:4.0


WORKDIR /react

COPY Pipfile* /react/ 

RUN pip install --no-cache-dir pipenv && \
    pipenv install --system --deploy --clear 

COPY . /react/ 

EXPOSE 8000 