from flask import Flask, jsonify, abort, make_response, request
from gtin import GTIN

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/gtin/api/v1.0/convert', methods=['POST'])
def convert_upc_to_gtin():
    if not request.json or not 'upc' in request.json:
        abort(400)
    #print (request.json)
    upc = request.json['upc']
    length = request.json['length'] if 'length' in request.json else 12
    res = str(GTIN(raw=request.json['upc'], length=length))

    return jsonify({'gtin': res}), 201

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
