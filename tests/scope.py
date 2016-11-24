from seismograph import scope
import unittest
#from mock import MagickMock


class TestCaseContext(unittest.TestCase):

    # I am doing it wrong
    class MockedExtension():
        def __init__(self):
            pass

        def __install__(self):
            pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_scope__add_extension__raises_on_wrong_file(self):
        with self.assertRaises(NotImplementedError): scope.add_extension("wrong_extension")

    def test_scope__add_extension__finds_install(self):
        mockedExtension = self.MockedExtension()
        try:
            scope.add_extension(mockedExtension)
        except NotImplementedError:
            self.fail("myFunc() raised NotImplementedError unexpectedly!")


class TestCaseConfigure(unittest.TestCase):
    def setUp(self):
        self.start_message = "Mock"
        self.round_time = "one"
        self.real_round_time = 1
        self.mock_group_class = object

    def test_configure_start_message(self):
        scope.configure(self.start_message)
        self.assertEqual(self.start_message,scope._result.START_MESSAGE)

    def test_configure_with_bad_round_time(self):
        try:
            scope.configure(None, self.round_time)
        except AssertionError:
            self.assertEqual(True, True)

    def test_configure_round_time(self):
        scope.configure(None, self.real_round_time)
        self.assertEqual(scope._xunit.ROUND_RUNTIME, self.real_round_time)

    def test_case_group_class(self):
        try:
            scope.configure(None, None, None, None, None, self.mock_group_class)
        except AssertionError:
            self.assertEqual(True, True)

    def test_case_suite_group_class(self):
        try:
            scope.configure(None, None, None, None, None, None, self.mock_group_class)
        except AssertionError:
            self.assertEqual(True, True)



if __name__ == '__main__':
    unittest.main()