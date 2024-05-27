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
