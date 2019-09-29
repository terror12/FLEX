import os
from glusto.core import Glusto as g

def findNewest(path):
    """

    :param path:
    :return:
    """

    my_dir = os.path.expanduser(path)
    print(my_dir)
    files = os.listdir(my_dir)
    paths = [os.path.join(my_dir, basename) for basename in files]
    return max(paths, key=os.path.getctime)