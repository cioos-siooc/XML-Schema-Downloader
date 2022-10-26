FROM python:3.10.5

COPY . .

RUN pip install .

ENTRYPOINT [ "python", "-m", "xsd_download" ]
