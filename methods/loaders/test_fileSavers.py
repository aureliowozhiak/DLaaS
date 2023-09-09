from unittest import TestCase
from unittest.mock import mock_open, patch

from .fileSavers import FileSavers


class FileSaversTestSuite(TestCase):
    def setUp(self):
        self.fileSavers = FileSavers()
        self.content = "1,2,3\n4,5,6\n,7,8,9"

    @patch('builtins.open', new_callable=mock_open)
    def test_can_write_simple_files(self, m):
        filename = "test_file.txt"
        self.fileSavers.save_content(self.content, filename)
        m.assert_called_with(f"output/{filename}", "w", encoding='utf-8')

    @patch('builtins.open', new_callable=mock_open)
    def test_can_write_csv(self, m):
        filename = "test_file.csv"
        columns = ['A', 'B', 'C']
        self.fileSavers.save_content(self.content, filename, columns=columns)
        m.assert_called_with(f"output/{filename}", "w", encoding='utf-8')
