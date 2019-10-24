from flask import Flask, jsonify, abort
from flask import request
import json

from . import maths

app = Flask(__name__)


@app.route('/', methods=["POST"])
def kolmogorov():
    try:
        input_data = json.loads(request.data)["data_list"]
        data = {"stat": maths.get_stat(input_data)}
        return jsonify(data)
    except Exception:
        abort(400)


if __name__ == '__main__':
    app.run()
