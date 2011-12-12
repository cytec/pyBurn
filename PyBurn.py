# -*- coding: utf-8 -*-

"""
    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 3 of the License,
    or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program; if not, see <http://www.gnu.org/licenses/>.
    
    @author: cytec
    @interface-version: 0.1
"""

from os import makedirs
from os import listdir
from os.path import exists
from os.path import join
from os.path import isfile
from shutil import move
import time

from module.plugins.Hook import Hook

class PyBurn(Hook):
    __name__ = "PyBurn"
    __version__ = "0.1"
    __description__ = """Control pyLoad via Twitter and other cool stuff"""
    __config__ = [ ("activated", "bool", "Activated" , "False"),
                   ("folder", "str", "Folder to observe", "container"),
                   ("watch_file", "bool", "Observe link file", "False"),
                   ("keep", "bool", "Keep added containers", "True"),
                   ("file", "str", "Link file", "links.txt")]
    __threaded__ = []
    __author_name__ = ("cytec")
    __author_mail__ = ("iamcytec@googlemail.com")
    
