# gtin

REST API to Convert UPC number to valid GTINs ("Global Trade Item Numbers"). 
Can specify length in JSON request. Default to GTIN `12`. 

## Usage

```
sudo docker-compose up --build
```

Make sure to use ``host="0.0.0.0"`` in `app.py` when using Docker, otherwise seems not working.


## Examples

Default is 12 digits:

```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"upc":"7447010150"}' http://localhost:5000/gtin/api/v1.0/convert
HTTP/1.0 201 CREATED
Content-Type: application/json
Content-Length: 29
Server: Werkzeug/0.14.1 Python/3.6.4
Date: Wed, 27 Mar 2019 01:40:17 GMT

{
      "gtin": "074470101505"
          
}
```

However Can convert to any GTIN. You can specify the length in the payload. For example, for 14 digit GTIN.

```bash
$ curl -i -H "Content-Type: application/json" -X POST -d '{"upc":"7447010150", "length":14}' http://localhost:5000/gtin/api/v1.0/convert
HTTP/1.0 201 CREATED
Content-Type: application/json
Content-Length: 31
Server: Werkzeug/0.14.1 Python/3.6.4
Date: Wed, 27 Mar 2019 01:40:28 GMT

{
      "gtin": "00074470101505"
          
}
```

```
$ curl -i -H "Content-Type: application/json" -X POST -d '{"upc":"63050947716"}' http://10.46.39.75:5000/gtin/api/v1.0/convert
HTTP/1.0 201 CREATED
Content-Type: application/json
Content-Length: 29
Server: Werkzeug/0.15.1 Python/3.7.2
Date: Wed, 27 Mar 2019 22:00:10 GMT

{
  "gtin": "630509477166"
}

```

## Notes

Had to upgrade python from alpine to stretch.

```
-FROM python:3.4-alpine
+FROM python:3.7-stretch
```

Alpine seems not working with Centos 7, with Docker 1.12.

```
CentOS Linux release 7.3.1611 (Core)
3.10.0-514.26.2.el7.x86_64
$ docker --version
Docker version 1.12.6, build 88a4867/1.12.6
```
