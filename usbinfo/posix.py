# Copyright 2015 Google Inc. All Rights Reserved.
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

"""
Definitions common to all POSIX-compliant systems.
"""

import re
import subprocess


def get_mounts():
    """Return a dictionary of mounted partitions"""
    mounts = dict()

    pat = re.compile(r'([^\s]*) on (.*?) (?:\(|type)')
    for line in subprocess.check_output(['mount'], universal_newlines=True).split('\n'):
        match = pat.match(line)
        if match:
            mounts[match.group(1)] = match.group(2)

    return mounts
