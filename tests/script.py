import unittest

from seismograph import script


class MockShouldStopClass:
    def __init__(self):
        self.should_stop = False

    def should_stop(self):
        return self.should_stop


class MockClassScript:
    def __init__(self):
        self._that_self = None
        self._mock_var = MockShouldStopClass()

    @property
    def current_state(self):
        return self._mock_var

    @property
    def that_self(self):
        return self._that_self

    def start(self, that_self):
        self.that_self = that_self

    @that_self.setter
    def that_self(self, value):
        self._that_self = value


class MockClassProgram:
    class MockClassProgramConfig:
        def __init__(self):
            self.STOP = False

        @property
        def STOP(self):
            return self.STOP

    def __init__(self):
        self._config = self.MockClassProgramConfig()

    @property
    def config(self):
        return self._config


class TestScriptRun(unittest.TestCase):
    def setUp(self):
        self.program = MockClassProgram()
        self.methodName = "MethodName"

    def test_run(self):
        script_obj = script.Script(self.program, self.methodName)
        inner_instance = MockClassScript()
        with self.assertRaises(AttributeError): script_obj.__run__(inner_instance)


if __name__ == '__main__':
    unittest.main()
