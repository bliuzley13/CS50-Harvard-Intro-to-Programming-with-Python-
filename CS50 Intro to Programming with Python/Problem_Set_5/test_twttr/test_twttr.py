from twttr import shorten

def main():
    #test case functions
    test_upp_loww_cases()
    test_nums()
    test_punc()

def test_upp_loww_cases():
    #tests the upper and lower cases combinations
    assert shorten('TWITTER') == 'TWTTR'
    assert shorten('twitter') == 'twttr'
    assert shorten('TwItTeR') == 'TwtTR'

def test_nums():
    #tests numbers
    assert shorten('4000') == '4000'

def test_punc():
    #tests punctuation
    assert shorten('.?!') == '.?!'

if __name__ == "__main__":
    main()