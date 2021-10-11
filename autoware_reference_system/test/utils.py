# Copyright 2021 Apex.AI, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import sys

from constants import TRACE_CALLBACK, TRACE_MEMORY, TRACE_UNSUPPORTED

from tracetools_analysis.loading import load_file
from tracetools_analysis.processor.ros2 import Ros2Handler
from tracetools_analysis.utils.ros2 import Ros2DataModelUtil


def initDataModel(path):
    events = load_file(path)
    handler = Ros2Handler.process(events)
    # handler.data.print_data()

    return Ros2DataModelUtil(handler.data)


def checkPath(path: str):
    # make sure directory exists
    if not os.path.isdir(path):
        # make sure given path isnt a file
        if not os.path.isfile(path):
            print('Given path does not exist: ' + path)
            sys.exit()
    # make sure path ends in a `/`
    if (path[-1] != '/'):
        if not (path.find('.txt') >= 0):
            path += '/'
    return path


def getTraceType(path):
    # check if given path is a callback trace
    print(path)
    if path.find(TRACE_CALLBACK) >= 0:
        print('tracing type')
        return TRACE_CALLBACK
    elif path.find(TRACE_MEMORY) >= 0:
        return TRACE_MEMORY
    else:
        return TRACE_UNSUPPORTED


def getPWD(path):
    return os.path.basename(os.path.normpath(path))


def getDirPath(path):
    # given path is a filename, remove filename but keep rest of path
    return os.path.dirname(path) + '/'


def getFileName(path):
    return os.path.splitext(os.path.basename(path))[0]
