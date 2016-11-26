from seismograph import scope
import unittest


class TestCaseContext(unittest.TestCase):

    # I am doing it wrong
    class MockedExtension:
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
        mocked_extension = self.MockedExtension()
        try:
            scope.add_extension(mocked_extension)
        except NotImplementedError:
            self.fail("myFunc() raised NotImplementedError unexpectedly!")


class TestCaseConfigure(unittest.TestCase):
    def setUp(self):
        self.start_message = "Mock"
        self.round_time = "one"
        self.real_round_time = 1
        self.mock_group_class = object
        self.config_test_name = "MockName"
        self.max_diff = 1.5
        self.default_test_name = "MockDefaultName"
        self.skip_attr_name = "MockName"
        self.use_static_test_functions = True
        self.test_name_prefix = "MockPrefix"
        self.skip_why_attr_name = "MockAttrName"

    def test_configure_start_message(self):
        scope.configure(self.start_message)
        self.assertEqual(self.start_message, scope._result.START_MESSAGE)

    def test_configure_with_bad_round_time(self):
        with self.assertRaises(AssertionError): scope.configure(round_runtime=self.round_time)

    def test_configure_round_time(self):
        scope.configure(round_runtime=self.real_round_time)
        self.assertEqual(scope._xunit.ROUND_RUNTIME, self.real_round_time)

    def test_case_group_class(self):
        with self.assertRaises(AssertionError): scope.configure(case_group_class=self.mock_group_class)

    def test_case_suite_group_class(self):
        with self.assertRaises(AssertionError): scope.configure(suite_group_class=self.mock_group_class)

    def test_case_of_init(self):
        scope.configure(config_env_name=self.config_test_name, max_diff=self.max_diff,
                        default_test_name=self.default_test_name, skip_attribute_name=self.skip_attr_name,
                        use_static_test_functions=self.use_static_test_functions, test_name_prefix=self.test_name_prefix,
                        skip_why_attribute_name=self.skip_why_attr_name)

        self.assertEqual(scope._case.Case.__static__, self.use_static_test_functions)
        self.assertEqual(scope._program.CONFIG_ENV_NAME, self.config_test_name)
        self.assertEqual(scope._case.assertion.__unittest__.maxDiff, self.max_diff)
        self.assertEqual(scope._loader.TEST_NAME_PREFIX, self.test_name_prefix)
        self.assertEqual(scope._loader.DEFAULT_TEST_NAME, self.default_test_name)
        self.assertEqual(scope._case.SKIP_ATTRIBUTE_NAME, self.skip_attr_name)
        self.assertEqual(scope._case.SKIP_WHY_ATTRIBUTE_NAME, self.skip_why_attr_name)


if __name__ == '__main__':
    unittest.main()