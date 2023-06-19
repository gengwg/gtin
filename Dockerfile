FROM python:3.7-stretch
LABEL org.opencontainers.image.source=https://github.com/gengwg/gtin
LABEL org.opencontainers.image.description="Convert UPC number to valid GTINs"
LABEL org.opencontainers.image.licenses=MIT

ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
