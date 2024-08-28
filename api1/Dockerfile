FROM python:3.11
COPY ./requirements.txt /requirements.txt
WORKDIR /
RUN pip install -r requirements.txt
COPY . /
ENTRYPOINT [ "python" ]
CMD [ "api1.py" ]
EXPOSE 8001