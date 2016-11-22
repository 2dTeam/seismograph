from seismograph import scope

from .lib.case import (
    BaseTestCase,
)


class TestCaseContext(BaseTestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_scope__add_extension__raises_on_wrong_file(self):
        with self.assertRaises(NotImplementedError) as error: scope.add_extension("wrong_extension")
