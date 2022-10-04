FROM python:3.10-slim-buster

RUN apt-get update
RUN apt-get install curl -y

ENV FLASK_APP retail.py
ENV FLASK_CONFIG production

COPY requirements.txt .

RUN python -m venv venv
RUN . venv/bin/activate

ENV PIP_ROOT_USER_ACTION=ignore
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY app app
COPY retail.py config.py ./

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]