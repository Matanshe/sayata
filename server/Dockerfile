FROM python:3.9-alpine

EXPOSE 5001

COPY ./app .

WORKDIR app

RUN apk add --no-cache gcc musl-dev libffi-dev openssl-dev python3-dev

ADD requirements.txt .
RUN python -m pip install -r requirements.txt

CMD ["python", "app/app.py"]