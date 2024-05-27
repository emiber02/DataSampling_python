from dataclasses import dataclass
from datetime import datetime, timedelta
from enum import Enum
from typing import List, Dict


class MeasType(Enum):
    SPO2 = 1
    HR = 2
    TEMP = 3


@dataclass
class Measurement:
    measurementTime: datetime = datetime.min
    measurementType: MeasType = MeasType.SPO2
    value: float = 0.0


def sampleMeasurements(startOfSampling: datetime,
                       unsampledMeasurements: List[Measurement]) -> Dict[MeasType, List[Measurement]]:
    # Group measurements by type
    grouped_measurements: Dict[MeasType, List[Measurement]] = {}
    for measurement in unsampledMeasurements:
        if measurement.measurementType not in grouped_measurements:
            grouped_measurements[measurement.measurementType] = []
        grouped_measurements[measurement.measurementType].append(measurement)

    # Sampled measurements dictionary
    sampled_measurements: Dict[MeasType, List[Measurement]] = {}

    for meas_type, measurements in grouped_measurements.items():
        # Sort measurements by time
        measurements.sort(key=lambda x: x.measurementTime)

        # Sampling process
        current_interval_start = startOfSampling
        current_interval_end = current_interval_start + timedelta(minutes=5)
        last_measurement_in_interval = None

        for measurement in measurements:
            while measurement.measurementTime > current_interval_end:
                if last_measurement_in_interval:
                    if meas_type not in sampled_measurements:
                        sampled_measurements[meas_type] = []
                    sampled_measurements[meas_type].append(
                        Measurement(current_interval_end, meas_type, last_measurement_in_interval.value))
                    last_measurement_in_interval = None
                current_interval_start = current_interval_end
                current_interval_end = current_interval_start + timedelta(minutes=5)

            last_measurement_in_interval = measurement

            # If the measurement exactly matches the interval end, treat it as part of the current interval
            if measurement.measurementTime == current_interval_end:
                if meas_type not in sampled_measurements:
                    sampled_measurements[meas_type] = []
                sampled_measurements[meas_type].append(
                    Measurement(current_interval_end, meas_type, measurement.value))
                last_measurement_in_interval = None
                current_interval_start = current_interval_end
                current_interval_end = current_interval_start + timedelta(minutes=5)

        if last_measurement_in_interval:
            if meas_type not in sampled_measurements:
                sampled_measurements[meas_type] = []
            sampled_measurements[meas_type].append(
                Measurement(current_interval_end, meas_type, last_measurement_in_interval.value))

    return sampled_measurements


# Example usage
input_measurements = [
    Measurement(datetime(2017, 1, 3, 10, 4, 45), MeasType.TEMP, 35.79),
    Measurement(datetime(2017, 1, 3, 10, 1, 18), MeasType.SPO2, 98.78),
    Measurement(datetime(2017, 1, 3, 10, 9, 7), MeasType.TEMP, 35.01),
    Measurement(datetime(2017, 1, 3, 10, 3, 34), MeasType.SPO2, 96.49),
    Measurement(datetime(2017, 1, 3, 10, 2, 1), MeasType.TEMP, 35.82),
    Measurement(datetime(2017, 1, 3, 10, 5, 0), MeasType.SPO2, 97.17),
    Measurement(datetime(2017, 1, 3, 10, 5, 1), MeasType.SPO2, 95.08),
]

start_sampling_time = datetime(2017, 1, 3, 10, 0, 0)
sampled_data = sampleMeasurements(start_sampling_time, input_measurements)

# Prepare the output ensuring TEMP measurements come first, then SPO2
output = []

# Collect TEMP measurements
if MeasType.TEMP in sampled_data:
    for measurement in sampled_data[MeasType.TEMP]:
        output.append((measurement.measurementTime, measurement.measurementType, measurement.value))

# Collect SPO2 measurements
if MeasType.SPO2 in sampled_data:
    for measurement in sampled_data[MeasType.SPO2]:
        output.append((measurement.measurementTime, measurement.measurementType, measurement.value))

# Print the formatted output, ensuring TEMP measurements come first, then SPO2
for time, meas_type, value in output:
    print(f"{{{time.isoformat()}, {meas_type.name}, {value}}}")
