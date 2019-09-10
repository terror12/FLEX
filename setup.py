#
# Copyright(C) 2019 Adam Scerra
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.If not, see < https://www.gnu.org/licenses/>.

import os
from os import walk
from os.path import join
from setuptools import setup, find_packages
from flex import __version__

def package_files(directory):
    paths = []
    for (path, directories, filenames) in walk(directory):
        for filename in filenames:
            paths.append((path, [join(path, filename)]))
    return paths

extra_files = package_files("flex")

setup(
    name="flex",
    version=__version__,
    author="Adam Scerra",
    author_email="acterror12@gmail.com",
    description="Package for all FLEXproject code",
    url="https://github.com/terror12/FLEX.git",
    packages=find_packages(),
    data_files=extra_files,
    install_requires=[
        "glusto@git+git://github.com/loadtheaccumulator/glusto.git"
        "@python3_port4#egg-glusto"
        'httplib2',
        'numba',
        'tqdm',
        'apiclient',
        'google-api-python-client',
        'oauth2client',
        'pandas',
        'schema',
        'google_auth_oauthlib'
    ],
    classifiers=[
        "Programming Language :: Python :: 3"
    ]
)