import ast
from glusto.core import Glusto as g

def read_cli(testdata):
    """

    :param testdata:
    :return:
    """
    testdatadict = ast.literal_eval(testdata)

    return testdatadict