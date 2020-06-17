"""Takes a test_name, test_score, and invalid_message that validates
    the test_score, asking the user for a valid test score until it is in the range,
    then prints valid input as 'Test name: #"""

def score_input(test_name, test_score=0, invalid_message='Invalid test score, try again!'):
    """Returns
    :param test_name: name of the test
    :param test_score: optional test score
    :param invalid_message: optional invalid message
    # return { test_name: test_score}
    :returns test_name and test_score in a string
    """
    try:
        if test_score < 0 or test_score > 100:
            return invalid_message
        else:
            test_name_and_score = (test_name + ": " + str(test_score))
    except TypeError as err:
        raise TypeError
    else:
        return test_name_and_score


if __name__ == '__main__':
    try:
        print(score_input("math", 100))
    except TypeError as err:
        print("TypeError encountered")
