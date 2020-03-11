import os


def findNewest(path):
    """
    Find the newest file in the absolute path given
    :param path: Absolute path that you would like to find the newest file in.
    :return:
    """

    my_dir = os.path.expanduser(path)
    print(my_dir)
    files = os.listdir(my_dir)
    paths = [os.path.join(my_dir, basename) for basename in files]
    return max(paths, key=os.path.getctime)
