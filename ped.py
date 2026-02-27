def percent_change_arc(v1: float, v2: float) -> float:
    avg = (v1 + v2) / 2.0
    if avg == 0:
        raise ValueError("Average value is 0; percent change is undefined.")
    return ((v2 - v1) / avg) * 100.0


def calculate_ped_arc(p1: float, p2: float, q1: float, q2: float) -> float:
    delta_q = q2 - q1
    delta_p = p2 - p1

    if delta_p == 0:
        raise ValueError("Price change (ΔP) must be non-zero.")

    # User-specified arc method: abs((ΔQ/ΔP) * (P1/Q1 + P2/Q2))
    return (delta_q / delta_p) * ((p1 / q1) + (p2 / q2))


def calculate_ped_proportionate(p1: float, p2: float, q1: float, q2: float) -> float:
    delta_q = q2 - q1
    delta_p = p2 - p1

    if delta_p == 0:
        raise ValueError("Price change (ΔP) must be non-zero.")
    if q1 == 0:
        raise ValueError("Initial quantity (Q1) must be non-zero.")

    # Proportionate method: abs((ΔQ/ΔP) * (P1/Q1))
    return (delta_q / delta_p) * (p1 / q1)


def classify_ped(ped: float) -> str:
    ped_abs = abs(ped)
    if ped_abs < 1:
        return "Inelastic demand"
    if ped_abs == 1:
        return "Unit elastic demand"
    return "Elastic demand"

