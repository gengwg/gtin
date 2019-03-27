# gtin

REST API to Convert UPC number to valid GTINs ("Global Trade Item Numbers"). 
Can specify length in JSON request. Default to GTIN `12`. 

## Usage

```
python app.py
```

## Examples

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
