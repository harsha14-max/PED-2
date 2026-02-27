def percent_change_arc(v1: float, v2: float) -> float:
    avg = (v1 + v2) / 2.0
    if avg == 0:
        raise ValueError("Average value is 0; percent change is undefined.")
    return ((v2 - v1) / avg) * 100.0


def calculate_ped_arc(p1: float, p2: float, q1: float, q2: float) -> float:
    """
    Arc elasticity (midpoint) PED:
      PED = (ΔQ / Q_avg) / (ΔP / P_avg)
    """
    delta_q = q2 - q1
    delta_p = p2 - p1
    q_avg = (q1 + q2) / 2.0
    p_avg = (p1 + p2) / 2.0

    if delta_p == 0 or p_avg == 0 or q_avg == 0:
        raise ValueError("Price and quantity changes must be non-zero for PED calculation.")

    return (delta_q / q_avg) / (delta_p / p_avg)


def classify_ped(ped: float) -> str:
    ped_abs = abs(ped)
    if ped_abs < 1:
        return "Inelastic demand"
    if ped_abs == 1:
        return "Unit elastic demand"
    return "Elastic demand"

