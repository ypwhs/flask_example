from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/sort', methods=['GET', 'POST'])
def sort():
    json_data = request.get_json()
    if not isinstance(json_data, list):
        return jsonify({'message': 'Input should be a list.'}, ), 400
    if len(json_data) > 10000:
        return jsonify({'message': f'Input length too long: {len(json_data)}'}), 413
    return jsonify(sorted(json_data))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
