from .chapter_01 import define_thanks_word
from .utils import call_gforth


class TestQuestion01:
    def test_thanks_word(self):
        thanks_word = f'{define_thanks_word()} THANKS'
        expected = 'DEAR STEPHANIE,\n    THANKS FOR THE BOOKENDS.'

        assert call_gforth(thanks_word) == expected
