import unittest

from ped import calculate_ped_arc, classify_ped, percent_change_arc


class TestPed(unittest.TestCase):
    def test_percent_change_arc(self):
        self.assertAlmostEqual(percent_change_arc(10, 12), 18.18181818, places=6)

    def test_ped_arc_negative_for_normal_good(self):
        ped = calculate_ped_arc(p1=10, p2=12, q1=100, q2=80)
        self.assertLess(ped, 0)

    def test_classify(self):
        self.assertEqual(classify_ped(-0.8), "Inelastic demand")
        self.assertEqual(classify_ped(1.0), "Unit elastic demand")
        self.assertEqual(classify_ped(-2.0), "Elastic demand")


if __name__ == "__main__":
    unittest.main()

