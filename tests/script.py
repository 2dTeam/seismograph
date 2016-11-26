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

    def add_success(self, msg, msg2):
        pass

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
        def __init__(self, should_stop=False):
            self._STOP = should_stop

        @property
        def STOP(self):
            return self._STOP

        @STOP.setter
        def STOP(self, value):
            self._STOP = value

    def __init__(self, should_stop=False):
        self._config = self.MockClassProgramConfig(should_stop)

    @property
    def config(self):
        return self._config


class TestScriptRun(unittest.TestCase):
    def setUp(self):
        self.program = MockClassProgram()
        self.mock_method_name = "MethodName"
        self.runnable_method_name = "__str__"

    def test_run_raises_debug_error(self):
        script_obj = script.Script(self.program, self.mock_method_name)
        result_instance = MockClassScript(should_stop=False)
        with self.assertRaises(AttributeError): script_obj.__run__(result_instance)

    def test_run_with_should_stop(self):
        program = MockClassProgram(should_stop=True)
        script_obj = script.Script(program, self.mock_method_name)
        result_instance = MockClassScript(should_stop=False)
        with self.assertRaises(AttributeError): script_obj.__run__(result_instance)

    def test_run_with_task(self):
        script_obj = script.Script(self.program, self.runnable_method_name)
        result_instance = MockClassScript(should_stop=False)
        script_obj.__run__(result_instance)

    def test_is_run_returning_method(self):
        script_obj = script.Script(self.program, self.runnable_method_name)
        self.assertEqual(script_obj.__is_run__(), False)


if __name__ == '__main__':
    unittest.main()
