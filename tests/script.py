import unittest

from seismograph import script


class MockShouldStopClass:
    def __init__(self, should_stop=False):
        self._should_stop = should_stop

    @property
    def should_stop(self):
        return self._should_stop

    @should_stop.setter
    def should_stop(self, value):
        self._should_stop = value


class MockClassScript:
    def __init__(self, should_stop=False):
        self._that_self = None
        self._mock_var = MockShouldStopClass(should_stop=should_stop)

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
            self._STOP = False

        @property
        def STOP(self):
            return self._STOP

        @STOP.setter
        def STOP(self, value):
            self._STOP = value

    def __init__(self):
        self._config = self.MockClassProgramConfig()

    @property
    def config(self):
        return self._config


class TestScriptRun(unittest.TestCase):
    def setUp(self):
        self.program = MockClassProgram()
        self.methodName = "MethodName"

    def test_run_raises_debug_error(self):
        script_obj = script.Script(self.program, self.methodName)
        inner_instance = MockClassScript(should_stop=False)
        with self.assertRaises(AttributeError): script_obj.__run__(inner_instance)

    def test_run_with_should_stop(self):
        script_obj = script.Script(self.program, self.methodName)
        inner_instance = MockClassScript(should_stop=True)
        script_obj.__run__(inner_instance)
        self.assertEqual(inner_instance.current_state.should_stop, True)

if __name__ == '__main__':
    unittest.main()
