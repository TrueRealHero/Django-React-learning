FROM python:3.9

RUN mkdir -p /react/

COPY Pipfile* /react/

RUN pip install --no-cache-dir pipenv && \
    pipenv install --system --deploy --clear 

COPY . /react/

EXPOSE 8000 