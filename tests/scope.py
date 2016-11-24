from seismograph import scope
import unittest


class TestCaseContext(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_scope__add_extension__raises_on_wrong_file(self):
        with self.assertRaises(NotImplementedError): scope.add_extension("wrong_extension")

    def test_scope__add_extension__finds_install(self):
        import seismograph.ext.mocker as mockedExtension
        try:
            scope.add_extension(mockedExtension)
        except NotImplementedError:
            self.fail("myFunc() raised NotImplementedError unexpectedly!")


class TestCaseConfigure(unittest.TestCase):
    def setUp(self):
        self.start_message = "Mock"

    def test_configure(self):
        scope.configure(self.start_message)
        self.assertEqual(self.start_message,scope._result.START_MESSAGE)


if __name__ == '__main__':
    unittest.main()