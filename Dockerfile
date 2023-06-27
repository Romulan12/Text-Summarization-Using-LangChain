FROM python:3.9

RUN pip install --upgrade pip

RUN apt-get install git -y

WORKDIR /code

COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt

RUN chmod a+x startup.sh

