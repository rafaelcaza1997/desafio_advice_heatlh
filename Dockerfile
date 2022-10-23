FROM python:3.8-alpine

COPY ./requirements.txt /flask_app/requirements.txt

WORKDIR /flask_app

RUN pip install -r requirements.txt

COPY . /flask_app

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD ["main.py"]