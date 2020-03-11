import ast


def read_cli(testdata):
    """

    :param testdata:
    :return:
    """
    testdatadict = ast.literal_eval(testdata)

    return testdatadict
