# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/decyzja", methods=["GET"])
def decyzja_api():
    try:
        wiek = int(request.args.get("wiek"))
        dochod = float(request.args.get("dochod"))
        if wiek > 25 and dochod > 5000:
            wynik = "Kredyt przyznany"
        else:
            wynik = "Kredyt odrzucony"
        return jsonify({"wynik": wynik})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
