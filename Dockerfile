FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app/sigl_api

COPY requirements.txt /app/sigl_api

# Build psycopg2-binary from source -- add required required dependencies
RUN apk add --virtual .build-deps --no-cache gcc python3-dev musl-dev && \
        pip install --no-cache-dir -r requirements.txt && \
        apk --purge del .build-deps

COPY . /app/sigl_api/

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
