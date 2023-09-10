from unittest import TestCase

import pandas as pd

from ...methods.transformers.dataCleaners import DataCleaner


class DataCleanerTestSuite(TestCase):
    def setUp(self):
        self.df = pd.DataFrame(
            [[1, 2, 3], [4, 5, 6], [1, 2, 3], [None, 0, None]]
        )  # noqa: E501
        self.cleaner = DataCleaner(self.df)

    def test_can_return_dataframe(self):
        df = self.cleaner.get_cleaned_dataframe()
        self.assertIsNone(pd.testing.assert_frame_equal(df, self.df))

    def test_can_remove_duplicates(self):
        self.cleaner.remove_duplicates()
        df = self.cleaner.get_cleaned_dataframe()
        self.assertEqual((3, 3), df.shape)

    def test_can_clean_data(self):
        self.cleaner.clean_data()
        df = self.cleaner.get_cleaned_dataframe()
        expected = pd.DataFrame(
            [[1, 2, 3], [4, 5, 6], [2.5, 0, 4.5]], index=[0, 1, 3]
        )  # noqa: E501
        self.assertIsNone(pd.testing.assert_frame_equal(df, expected))

    def test_handle_missing_values_drop_as_default(self):
        self.cleaner.handle_missing_values()
        df = self.cleaner.get_cleaned_dataframe()
        expected = pd.DataFrame([[1, 2, 3], [4, 5, 6], [1, 2, 3]])
        self.assertIsNone(
            pd.testing.assert_frame_equal(df, expected, check_dtype=False)
        )

    def test_handle_missing_values_drop(self):
        self.cleaner.handle_missing_values(method="drop")
        df = self.cleaner.get_cleaned_dataframe()
        expected = pd.DataFrame([[1, 2, 3], [4, 5, 6], [1, 2, 3]])
        self.assertIsNone(
            pd.testing.assert_frame_equal(df, expected, check_dtype=False)
        )

    def test_handle_missing_values_fill(self):
        self.cleaner.handle_missing_values(method="fill")
        df = self.cleaner.get_cleaned_dataframe()
        expected = pd.DataFrame([[1, 2, 3], [4, 5, 6], [1, 2, 3], [0, 0, 0]])
        self.assertIsNone(
            pd.testing.assert_frame_equal(df, expected, check_dtype=False)
        )

    def test_no_modifications_if_method_is_invalid(self):
        self.cleaner.handle_missing_values(method="invalid_method")
        df = self.cleaner.get_cleaned_dataframe()
        self.assertIsNone(
            pd.testing.assert_frame_equal(df, self.df, check_dtype=False)
        )  # noqa: E501
