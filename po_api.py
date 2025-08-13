from flask import Flask, jsonify
import pandas as pd
import requests
from io import StringIO

app = Flask(__name__)

CSV_URL = "https://raw.githubusercontent.com/saifsidir/SupplySense/main/po_data.csv"

@app.route("/purchase-orders", methods=["GET"])
def get_purchase_orders():
    try:
        # Fetch CSV from GitHub
        response = requests.get(CSV_URL)
        response.raise_for_status()

        # Read into DataFrame
        df = pd.read_csv(StringIO(response.text))

        # Convert to JSON
        data = df.to_dict(orient="records")
        return jsonify(data)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
