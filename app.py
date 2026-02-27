import os

from flask import Flask, render_template, request

from ped import (
    calculate_ped_arc,
    calculate_ped_proportionate,
    classify_ped,
    percent_change_arc,
)


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

            ped_arc = calculate_ped_arc(p1, p2, q1, q2)
            ped_prop = calculate_ped_proportionate(p1, p2, q1, q2)

            ped_arc_abs = abs(ped_arc)
            ped_prop_abs = abs(ped_prop)

            classification = classify_ped(ped_arc)

            result = {
                "p1": p1,
                "p2": p2,
                "q1": q1,
                "q2": q2,
                # Expose only the absolute PED to the template
                "ped": round(ped_arc_abs, 3),
                "ped_abs": round(ped_arc_abs, 3),
                "ped_arc_abs": round(ped_arc_abs, 3),
                "ped_prop_abs": round(ped_prop_abs, 3),
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

