import unittest

import seismograph.runnable as runnable


class TestRunnableObject(unittest.TestCase):

    class InnerRunnable(runnable.RunnableObject):

        def __init__(self):
            self._mock_var = False

        def __run__(self, *args, **kwargs):
            self.mock_var = True

        @property
        def mock_var(self):
            return self._mock_var

        @mock_var.setter
        def mock_var(self, value):
            self._mock_var = value

    def setUp(self):
        self.mock_arr = [1, 2, 3]
        self.mock_kwarg = {"test": "mock"}
        self.instance = self.InnerRunnable()

    def tearDown(self):
        self.instance = None

    def test_run(self):
        runnable.run(self.instance, self.mock_arr, self.mock_kwarg)
        self.assertTrue(self.instance.mock_var)


class TestRunnableGroup(unittest.TestCase):
    def setUp(self):
        self.mock_config = {"mock_var": 1}
        self.mock_object = ["some_list"]

    def test_make_instance(self):
        run = runnable.RunnableGroup(self.mock_object, self.mock_config)
        self.assertEqual(run.config, self.mock_config)
        self.assertEqual(run.objects, self.mock_object)

    def test_is_run(self):
        run = runnable.RunnableGroup(self.mock_object, self.mock_config)
        self.assertFalse(run.__is_run__())


if __name__ == '__main__':
    unittest.main()
