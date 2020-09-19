def define_thanks_word():
    return """
    : GIFT ." BOOKENDS" ; 
    : GIVER ." STEPHANIE" ;
    : THANKS ." DEAR " GIVER ." ," CR 
      4 SPACES ." THANKS FOR THE " GIFT ." ." ;
    """


def define_ten_less_word():
    return """
    : TEN.LESS ( n -- n-10 )
      -10 + ;
    """
