import unittest
from datetime import datetime
from typing import List
from main import Measurement, MeasType, sampleMeasurements


class TestSampleMeasurements(unittest.TestCase):

    def setUp(self):
        self.start_sampling_time = datetime(2017, 1, 3, 10, 0, 0)
        self.input_measurements = [
            Measurement(datetime(2017, 1, 3, 10, 4, 45), MeasType.TEMP, 35.79),
            Measurement(datetime(2017, 1, 3, 10, 1, 18), MeasType.SPO2, 98.78),
            Measurement(datetime(2017, 1, 3, 10, 9, 7), MeasType.TEMP, 35.01),
            Measurement(datetime(2017, 1, 3, 10, 3, 34), MeasType.SPO2, 96.49),
            Measurement(datetime(2017, 1, 3, 10, 2, 1), MeasType.TEMP, 35.82),
            Measurement(datetime(2017, 1, 3, 10, 5, 0), MeasType.SPO2, 97.17),
            Measurement(datetime(2017, 1, 3, 10, 5, 1), MeasType.SPO2, 95.08),
        ]

    def test_sampling_basic(self):
        expected_output = {
            MeasType.TEMP: [
                Measurement(datetime(2017, 1, 3, 10, 5, 0), MeasType.TEMP, 35.79),
                Measurement(datetime(2017, 1, 3, 10, 10, 0), MeasType.TEMP, 35.01)
            ],
            MeasType.SPO2: [
                Measurement(datetime(2017, 1, 3, 10, 5, 0), MeasType.SPO2, 97.17),
                Measurement(datetime(2017, 1, 3, 10, 10, 0), MeasType.SPO2, 95.08)
            ]
        }

        sampled_data = sampleMeasurements(self.start_sampling_time, self.input_measurements)

        self.assertEqual(sampled_data, expected_output)

    def test_sampling_empty_input(self):
        input_measurements: List[Measurement] = []
        expected_output = {}

        sampled_data = sampleMeasurements(self.start_sampling_time, input_measurements)

        self.assertEqual(sampled_data, expected_output)

    def test_sampling_exact_interval_boundary(self):
        input_measurements = [
            Measurement(datetime(2017, 1, 3, 10, 0, 0), MeasType.TEMP, 36.00),
            Measurement(datetime(2017, 1, 3, 10, 5, 0), MeasType.TEMP, 36.01),
            Measurement(datetime(2017, 1, 3, 10, 10, 0), MeasType.TEMP, 36.02),
            Measurement(datetime(2017, 1, 3, 10, 0, 0), MeasType.SPO2, 98.0),
            Measurement(datetime(2017, 1, 3, 10, 5, 0), MeasType.SPO2, 97.5),
            Measurement(datetime(2017, 1, 3, 10, 10, 0), MeasType.SPO2, 97.0),
        ]

        expected_output = {
            MeasType.TEMP: [
                Measurement(datetime(2017, 1, 3, 10, 5, 0), MeasType.TEMP, 36.01),
                Measurement(datetime(2017, 1, 3, 10, 10, 0), MeasType.TEMP, 36.02)
            ],
            MeasType.SPO2: [
                Measurement(datetime(2017, 1, 3, 10, 5, 0), MeasType.SPO2, 97.5),
                Measurement(datetime(2017, 1, 3, 10, 10, 0), MeasType.SPO2, 97.0)
            ]
        }

        sampled_data = sampleMeasurements(self.start_sampling_time, input_measurements)

        self.assertEqual(sampled_data, expected_output)

    def test_sampling_single_measurement(self):
        input_measurements = [
            Measurement(datetime(2017, 1, 3, 10, 4, 0), MeasType.TEMP, 36.00),
        ]

        expected_output = {
            MeasType.TEMP: [
                Measurement(datetime(2017, 1, 3, 10, 5, 0), MeasType.TEMP, 36.00)
            ]
        }

        sampled_data = sampleMeasurements(self.start_sampling_time, input_measurements)

        self.assertEqual(sampled_data, expected_output)


if __name__ == "__main__":
    unittest.main()
