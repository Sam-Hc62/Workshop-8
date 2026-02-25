from calculator import square
def main():
    test_square()
def test_square():
    try:
        assert square(-2) == 4
    except AssertionError:
        print('untrue')
    try:
        assert square(0) == 0
    except AssertionError:
        print('untrue')
if __name__ == "__main__":
    main()