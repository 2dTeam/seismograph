import seismograph


suite = seismograph.Suite(__name__)


@suite.register
def my_first_test(case):
    case.assertion.equal(2, 1)


if __name__ == '__main__':
    seismograph.main()