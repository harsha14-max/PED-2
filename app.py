from flask import Flask, render_template, request


app = Flask(__name__)


def calculate_ped(p1: float, p2: float, q1: float, q2: float) -> float:
    """
    Calculate price elasticity of demand using the arc elasticity formula:
    PED = (ΔQ / Q_avg) / (ΔP / P_avg)
    """
    delta_q = q2 - q1
    delta_p = p2 - p1
    q_avg = (q1 + q2) / 2.0
    p_avg = (p1 + p2) / 2.0

    if delta_p == 0 or p_avg == 0 or q_avg == 0:
        raise ValueError("Price and quantity changes must be non-zero for PED calculation.")

    ped = (delta_q / q_avg) / (delta_p / p_avg)
    return ped


def classify_ped(ped: float) -> str:
    """
    Classify the elasticity value.
    """
    ped_abs = abs(ped)
    if ped_abs < 1:
        return "Inelastic demand"
    elif ped_abs == 1:
        return "Unit elastic demand"
    else:
        return "Elastic demand"


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        try:
            p1 = float(request.form.get("p1", ""))
            p2 = float(request.form.get("p2", ""))
            q1 = float(request.form.get("q1", ""))
            q2 = float(request.form.get("q2", ""))

            ped_value = calculate_ped(p1, p2, q1, q2)
            classification = classify_ped(ped_value)

            result = {
                "p1": p1,
                "p2": p2,
                "q1": q1,
                "q2": q2,
                "ped": round(ped_value, 3),
                "classification": classification,
            }
        except (TypeError, ValueError) as exc:
            error = str(exc) or "Invalid input values. Please check your numbers."

    return render_template("index.html", result=result, error=error)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)

