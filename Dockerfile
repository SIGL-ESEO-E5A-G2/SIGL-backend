FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app/sigl_api

COPY requirements.txt /app/sigl_api

RUN apk update
RUN apk add git
RUN git init
RUN apk add --virtual .build-deps --no-cache gcc python3-dev musl-dev mariadb-connector-c-dev libffi-dev
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN  python3 get-pip.py
RUN rm get-pip.py
RUN pip install -r requirements.txt


COPY . /app/sigl_api/

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
