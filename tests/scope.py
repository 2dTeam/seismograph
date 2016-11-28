import unittest

from seismograph import scope


class TestCaseContext(unittest.TestCase):

    class InnerMockedExtension:
        def __init__(self):
            pass

        def __install__(self):
            pass

    def setUp(self):
        self.inner_instance = self.InnerMockedExtension()

    def tearDown(self):
        self.inner_instance = None

    def test_scope__add_extension__raises_on_wrong_file(self):
        with self.assertRaises(NotImplementedError): scope.add_extension("wrong_extension")

    def test_scope__add_extension__finds_install(self):
        try:
            scope.add_extension(self.inner_instance)
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
        self.default_test_name = "test"
        self.skip_attr_name = "MockName"
        self.test_name_prefix = "test"
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

    def test_case_config_env_and_max_diff(self):
        scope.configure(config_env_name=self.config_test_name, max_diff=self.max_diff)
        self.assertEqual(scope._program.CONFIG_ENV_NAME, self.config_test_name)
        self.assertEqual(scope._case.assertion.__unittest__.maxDiff, self.max_diff)

    def test_case_default_test_name(self):
        scope.configure(default_test_name=self.default_test_name)
        self.assertEqual(scope._loader.DEFAULT_TEST_NAME, self.default_test_name)

    def test_case_skip_attribute_name(self):
        scope.configure(skip_attribute_name=self.skip_attr_name)
        self.assertEqual(scope._case.SKIP_ATTRIBUTE_NAME, self.skip_attr_name)

    def test_case_name_prefix(self):
        scope.configure(test_name_prefix=self.test_name_prefix)
        self.assertEqual(scope._loader.TEST_NAME_PREFIX, self.test_name_prefix)

    def test_case_skip_why_attr(self):
        scope.configure(skip_why_attribute_name=self.skip_why_attr_name)
        self.assertEqual(scope._case.SKIP_WHY_ATTRIBUTE_NAME, self.skip_why_attr_name)


class TestCaseLayers(unittest.TestCase):
    class InnerListImpl(list):
        def __init__(self):
            pass

    def setUp(self):
        self.inner_layer = self.InnerListImpl()
        self.mock_layers = ["mock", "mock"]

    def test_set_default_program_layers(self):
        scope.set_default_program_layers(self.mock_layers)
        self.assertIn(self.mock_layers, scope._program.DEFAULT_LAYERS)

    def test_match_suite_to_layer(self):
        scope.match_case_to_layer(list, self.inner_layer)

if __name__ == '__main__':
    unittest.main()