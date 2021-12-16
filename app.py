from flask import Flask, request, render_template, jsonify,url_for,redirect, session, Markup
import json
import os
from numpy import product
import pandas as pd
import urllib.request
url = "https://s3.amazonaws.com/open-to-cors/assignment.json"
response = urllib.request.urlopen(url)
data_json = json.loads(response.read())
df = pd.DataFrame.from_dict(data_json['products'],orient ='index')
df["popularity"] = pd.to_numeric(df["popularity"])
df = df.sort_values('popularity', ascending=[False])
result = Markup(df.to_html(classes="table table-striped table-class",table_id='table-id'))
app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/",methods=["POST","GET"])
def login():
        return render_template('base.html', table=result)


if __name__ == "__main__":
    app.run(debug=True)