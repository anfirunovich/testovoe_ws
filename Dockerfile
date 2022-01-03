FROM python:3.8.10

WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update -y && \
  apt-get install -y libpq-dev build-essential



RUN pip install pipenv
COPY Pipfile Pipfile.lock /code/
RUN pipenv install --system --deploy --ignore-pipfile

COPY supplier /code/

RUN chmod +x entrypoint.sh

ENTRYPOINT ["sh", "entrypoint.sh"]