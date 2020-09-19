from .chapter_01 import define_thanks_word, define_ten_less_word, \
    define_giver_again
from .utils import call_gforth


class TestQuestion01:
    def test_thanks_word(self):
        words = f'{define_thanks_word()} THANKS'
        expected = 'DEAR STEPHANIE,\n    THANKS FOR THE BOOKENDS.'

        assert call_gforth(words) == expected


class TestQuestion02:
    def test_ten_less_word(self):
        words = f'{define_ten_less_word()} 20 TEN.LESS . '
        expected = '10'

        assert call_gforth(words) == expected


class TestQuestion03:
    def test_define_giver_again(self):
        words = f'{define_giver_again()} THANKS'
        expected = 'DEAR FOX,\n    THANKS FOR THE BOOKENDS.'

        assert call_gforth(words) == expected
