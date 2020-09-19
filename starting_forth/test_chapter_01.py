from .chapter_01 import define_thanks_word, define_ten_less_word
from .utils import call_gforth


class TestQuestion01:
    def test_thanks_word(self):
        word = f'{define_thanks_word()} THANKS'
        expected = 'DEAR STEPHANIE,\n    THANKS FOR THE BOOKENDS.'

        assert call_gforth(word) == expected


class TestQuestion02:
    def test_ten_less_word(self):
        word = f'{define_ten_less_word()} 20 TEN.LESS . '
        expected = '10'

        assert call_gforth(word) == expected
