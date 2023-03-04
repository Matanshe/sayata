FROM python:3.9-alpine

EXPOSE 5000

COPY ./app ./app

RUN apk add --no-cache gcc musl-dev libffi-dev openssl-dev python3-dev

ADD requirements.txt .
RUN python -m pip install -r requirements.txt

CMD ["python", "app/app.py"]