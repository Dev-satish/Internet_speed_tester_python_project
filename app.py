import speedtest
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == 'POST':
        st = speedtest.Speedtest()
        st.get_best_server()
        st.download()
        st.upload()

        result = st.results.dict()
        print(result)

        download = round(result["download"] / 1000000, 2)
        upload = round(result["upload"] / 1000000, 2)
        ping = round(result["ping"])
        isp = result["client"]["isp"]


        return render_template("index.html", download=download, upload=upload, ping=ping, isp=isp)
    else:
        return render_template("index.html", download='--', upload='--', ping='--', isp='--')
