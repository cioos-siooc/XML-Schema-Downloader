FROM python:3.10

COPY . .

RUN pip install .

CMD [ "python", "-m", "xsd_download" ]
