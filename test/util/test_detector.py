import pytest
from unittest.mock import patch, Mock
from src.util.detector import detect_duplicates

# add your test case implementation here
@patch('src.util.parser.Article.parse', autospec=True)
class TestSolution:

    @pytest.fixture
    def sut(self):
        return detect_duplicates(items_dao=Mock())

    @pytest.mark.unit
    def tc_1(self, mocked_parse, sut):

        mocked_parse.return_value =  [1]
        return_value = sut.detect_duplicates(mocked_parse)
        assert ValueError

    @pytest.mark.unit
    def tc_2(self, mocked_parse, sut):

        mocked_parse.return_value =  [1, 2]
        return_value = sut.detect_duplicates(mocked_parse)
        assert return_value == list

    @pytest.mark.unit
    def tc_3(self, mocked_parse, sut):
        mocked_parse.return_value =  [1, 2, 3]
        return_value = sut.detect_duplicates(mocked_parse)
        assert return_value == list