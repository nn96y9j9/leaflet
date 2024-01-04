from flask import Flask, make_response
import requests as req
import json

app = Flask(__name__)

"""
Web API 的來源
"""


@app.route("/cafe_taipei", methods=["GET"])
def get_cafe_info_taipei():
    # 對咖啡廳發送GET請求
    url = "https://cafenomad.tw/api/v1.2/cafes/taipei"
    res = req.get(url)

    # 自訂回應
    response = make_response(json.dumps(res.json(), ensure_ascii=False))

    # 自訂回應標頭
    response.headers["Content-Type"] = "application/json"
    response.headers["Access-Control-Allow-Origin"] = "*"

    # 回傳自訂回應
    return response


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
