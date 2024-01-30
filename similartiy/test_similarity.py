from unittest import TestCase

from similartiy.similarity import _calculate_area_shoelace, _calculate_barycenter, _gen_a_square, calculate


class Test(TestCase):
    def setUp(self):
        self.polygon = [(0, 0), (0, 1), (1, 1), (1, 0)]

    def test_calculate(self):
        distance, _ = calculate(self.polygon)
        assert abs(distance) < 1e-5

    def test__calculate_area_shoelace(self):
        area = _calculate_area_shoelace(self.polygon)
        assert area == 1

    def test__calculate_barycenter(self):
        barycenter = _calculate_barycenter(self.polygon)
        assert barycenter[0] == 0.5
        assert barycenter[1] == 0.5

    def test__gen_a_square(self):
        barycenter = (0.5, 0.5)
        direction = (0.6, 0.8)
        distance = 3
        square = _gen_a_square(barycenter, direction, distance)
        arc_len = (square[0][0] - square[1][0])**2 + (square[0][1] - square[1][1])**2
        assert abs(arc_len - distance**2 * 2) < 1e-5

