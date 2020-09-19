from starting_forth import chapter_02


class TestPostfixPracticeProblem:
    def test_ppp1(self):
        # c(a + b)
        words = chapter_02.define_ppp1()
        expected = 'a b + c *'

        assert words == expected

    def test_ppp2(self):
        # (3a - b)/4 + c
        words = chapter_02.define_ppp2()
        expected = '3 a * b - 4 / c +'

        assert words == expected

    def test_ppp3(self):
        # 0.5ab/100
        words = chapter_02.define_ppp3()
        expected = 'a b * 2 / 100 /'

        assert words == expected

    def test_ppp4(self):
        # (n + 1)/n
        words = chapter_02.define_ppp4()
        expected = 'n 1 + n /'

        assert words == expected

    def test_ppp5(self):
        # x(7x + 5)
        words = chapter_02.define_ppp5()
        expected = '7 x * 5 + x *'

        assert words == expected

    def test_ppp6(self):
        # a b - b a +/
        words = chapter_02.define_ppp6()
        expected = '(a - b)/(b + a)'

        assert words == expected

    def test_ppp7(self):
        # a b 10 * /
        words = chapter_02.define_ppp7()
        expected = 'a/(10b)'

        assert words == expected
