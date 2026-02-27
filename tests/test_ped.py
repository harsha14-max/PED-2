import unittest

from ped import (
    calculate_ped_arc,
    calculate_ped_proportionate,
    classify_ped,
    percent_change_arc,
)


class TestPed(unittest.TestCase):
    def test_percent_change_arc(self):
        self.assertAlmostEqual(percent_change_arc(10, 12), 18.18181818, places=6)

    def test_ped_methods_match_hand_formula(self):
        # Example values
        p1, p2, q1, q2 = 10.0, 12.0, 100.0, 80.0

        # Proportionate: abs((ΔQ/ΔP) * (P1/Q1)) = 1.0
        ped_prop = calculate_ped_proportionate(p1, p2, q1, q2)
        self.assertAlmostEqual(abs(ped_prop), 1.0, places=6)

        # Arc: abs((ΔQ/ΔP) * (P1/Q1 + P2/Q2)) ≈ 2.5
        ped_arc = calculate_ped_arc(p1, p2, q1, q2)
        self.assertAlmostEqual(abs(ped_arc), 2.5, places=6)

    def test_classify(self):
        self.assertEqual(classify_ped(-0.8), "Inelastic demand")
        self.assertEqual(classify_ped(1.0), "Unit elastic demand")
        self.assertEqual(classify_ped(-2.0), "Elastic demand")


if __name__ == "__main__":
    unittest.main()

