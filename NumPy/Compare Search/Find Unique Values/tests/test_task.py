import unittest
import numpy as np

from task import *

test_csv = np.genfromtxt('data.csv', delimiter=',', skip_header=1)
test_data, test_labels = test_csv[:, 1:], np.array(test_csv[:, 0], dtype=np.int64)
test_classes = np.unique(test_labels)
test_unique_measurements, test_unique_data_counts = np.unique(test_data, return_counts=True)
test_most_frequent_index = np.argmax(test_unique_data_counts)
test_most_frequent_measurement = test_unique_measurements.flatten()[test_most_frequent_index]


class TestCase(unittest.TestCase):
    def test_data(self):
        np.testing.assert_array_equal(csv, test_csv, err_msg='Dataset is imported improperly.')
        np.testing.assert_array_equal(data, test_data, err_msg='Array of measurements is off.')
        np.testing.assert_array_equal(labels, test_labels, err_msg='Labels array is off.')

    def test_unique(self):
        np.testing.assert_array_equal(classes, test_classes,
                                      err_msg='The set of classes is wrong.')
        np.testing.assert_array_equal(unique_measurements, test_unique_measurements,
                                      err_msg='The set of unique measurements is wrong.')
        np.testing.assert_array_equal(unique_data_counts, test_unique_data_counts,
                                      err_msg='The set containing the number of occurrences of the unique values is wrong.')

    def test_most_frequent(self):
        self.assertEqual(most_frequent_index, test_most_frequent_index,
                         msg="The index of the most frequent value is incorrect.")
        self.assertEqual(most_frequent_measurement, test_most_frequent_measurement,
                        msg="The most frequent value is identified incorrectly.")
