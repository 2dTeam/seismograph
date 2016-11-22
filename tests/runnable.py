import unittest
import seismograph.runnable as runnable


class TestRunnableGroup(unittest.TestCase):
    def test_make_instance(self):
        mock_config = {"mock_var": 1}
        mock_object = ["some_list"]
        run = runnable.RunnableGroup(mock_object, mock_config)
        self.assertEqual(run.config, mock_config)

if __name__ == '__main__':
    unittest.main()