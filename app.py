import os

from flask import Flask, render_template, request

from ped import calculate_ped_arc, classify_ped, percent_change_arc


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    form_values = {"p1": "", "p2": "", "q1": "", "q2": ""}

    if request.method == "POST":
        try:
            form_values = {
                "p1": (request.form.get("p1") or "").strip(),
                "p2": (request.form.get("p2") or "").strip(),
                "q1": (request.form.get("q1") or "").strip(),
                "q2": (request.form.get("q2") or "").strip(),
            }

            p1 = float(form_values["p1"])
            p2 = float(form_values["p2"])
            q1 = float(form_values["q1"])
            q2 = float(form_values["q2"])

            ped_value = calculate_ped_arc(p1, p2, q1, q2)
            classification = classify_ped(ped_value)

            result = {
                "p1": p1,
                "p2": p2,
                "q1": q1,
                "q2": q2,
                "ped": round(ped_value, 3),
                "ped_raw": ped_value,
                "classification": classification,
                "delta_p": p2 - p1,
                "delta_q": q2 - q1,
                "pct_change_p": round(percent_change_arc(p1, p2), 3),
                "pct_change_q": round(percent_change_arc(q1, q2), 3),
            }
        except (TypeError, ValueError) as exc:
            error = str(exc) or "Invalid input values. Please check your numbers."

    return render_template("index.html", result=result, error=error, form_values=form_values)


if __name__ == "__main__":
    debug = os.getenv("PED_APP_DEBUG", "0") == "1"
    app.run(host="127.0.0.1", port=5000, debug=debug)

