# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 Infinity Online Solutions
"""Regression tests for the maintained fork's yoga 155 count handling."""
import unittest
from unittest.mock import patch

from jhora import const
from jhora.horoscope.chart import yoga


class Yoga155Tests(unittest.TestCase):
    def calculate(self, lord_count, jupiter_count, venus_count,
                  in_kendra=True, deeply_exalted=True):
        # Isolate the score contract from astronomical prerequisites. The real
        # producer returns [count, divisional_chart_names, weighted_score].
        lord = const.SUN_ID
        scores = {
            lord: [lord_count, 'D1/D9', 99],
            const.JUPITER_ID: [jupiter_count, 'D1/D9', 99],
            const.VENUS_ID: [venus_count, 'D1/D9', 99],
        }
        with patch.object(yoga.utils, 'get_planet_to_house_dict_from_chart',
                          return_value={const._ascendant_symbol: 0, lord: 0}), \
             patch.object(yoga.house, 'house_owner_from_planet_positions', return_value=lord), \
             patch.object(yoga, 'quadrants_of_the_house', return_value=[0] if in_kendra else [3]), \
             patch.object(yoga.utils, 'is_planet_in_exalation', return_value=deeply_exalted):
            return yoga._yukthi_samanwithavagmi_yoga_155_calculation(
                chart_1d=[''] * 12, vaiseshikamsa_scores=scores)

    def test_jupiter_at_threshold(self):
        self.assertIs(self.calculate(6, 5, 0), True)

    def test_venus_at_threshold(self):
        self.assertIs(self.calculate(6, 0, 5), True)

    def test_above_threshold(self):
        self.assertIs(self.calculate(7, 6, 6), True)

    def test_lord_below_threshold_ignores_weighted_score(self):
        self.assertIs(self.calculate(5, 5, 5), False)

    def test_both_benefics_below_threshold(self):
        self.assertIs(self.calculate(6, 4, 4), False)

    def test_requires_kendra(self):
        self.assertIs(self.calculate(6, 5, 5, in_kendra=False), False)

    def test_requires_deep_exaltation(self):
        self.assertIs(self.calculate(6, 5, 5, deeply_exalted=False), False)


if __name__ == '__main__':
    unittest.main()
