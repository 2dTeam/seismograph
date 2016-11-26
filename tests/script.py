from seismograph import script
import unittest


class InnerShouldStopClass():
    def __init__(self):
        self._should_stop = False

    @property
    def should_stop(self):
        return self._should_stop


class InnerClassScript():
    def __init__(self):
        self._mock_var = InnerShouldStopClass()

    @property
    def current_state(self):
        return self._mock_var

    def start(self, that_self):
        print "AAAAAA"


class TestScriptRun(unittest.TestCase):

    def test_run(self):
        scriptObj = script.Script("pido","qqq")
        scriptObj.__run__(InnerClassScript())


if __name__ == '__main__':
    unittest.main()
