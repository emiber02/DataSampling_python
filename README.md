# Measurement Sampling

This project contains a Python implementation for sampling time-based measurement data received from a medical device. The data is sampled into 5-minute intervals according to specified rules and tested using the `unittest` framework.

## Features

- Separate sampling for each type of measurement.
- Only the last measurement in each 5-minute interval is considered.
- Measurements matching the interval border exactly are included in the current interval.
- Input values are not required to be sorted by time.
- Output is sorted first by measurement type (`TEMP` first, then `SPO2`).

## Installation

To run this project, you need to have Python installed on your system.

## Usage

You can run the sampling script by executing: python main.py

## Running tests

The project uses the unittest framework for testing. To run the tests, execute: python unittests.py

## Explanation of Tests

The unittests.py file contains several test cases to ensure the sampleMeasurements function works correctly:

- test_sampling_basic: Verifies the basic functionality with a set of sample input measurements.
- test_sampling_empty_input: Ensures that the function handles empty input correctly.
- test_sampling_exact_interval_boundary: Checks the function's handling of measurements that exactly match the interval boundaries.
- test_sampling_single_measurement: Ensures correct sampling when there is only a single measurement.
