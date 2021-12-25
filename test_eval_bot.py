"""Tests for telegram EvalBot"""

def echo_all(message):
    """Evals received message"""

    try:
        result = eval(message) # pylint: disable=eval-used
        return "Expression result is: " + str(result)
    except SyntaxError:
        return "Your message does not satisfy python syntax!"
    except: # pylint: disable=bare-except
        return "Your message has an error in runtime or in 'compilation'!"

def test_echo_all():
    """Test echo_all function"""

    prefix = "Expression result is: "

    assert echo_all("1 + 3") == prefix + "4"
    assert echo_all("test string") == "Your message does not satisfy python syntax!"
    assert echo_all("1 // 0") == "Your message has an error in runtime or in 'compilation'!"
