# -*- coding: utf-8 -*-
#
#    Copyright 2017 Andrew Pong
#
#    Permission is hereby granted, free of charge, to any person obtaining a
#    copy of this software and associated documentation files (the "Software"),
#    to deal in the Software without restriction, including without limitation
#    the rights to use, copy, modify, merge, publish, distribute, sublicense,
#    and/or sell copies of the Software, and to permit persons to whom the
#    Software is furnished to do so, subject to the following conditions:
#
#    The above copyright notice and this permission notice shall be included in
#    all copies or substantial portions of the Software.
#
#    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#    FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
#    IN THE SOFTWARE.
#
"""
NewFireBeardLambdaFunction.run
~~~~~~~~~~~~

Sample POST request body:

    {
        "name": "Tom Bombadil"
    }

Sample POST response:

    {
        "gender":"female",
        "race":"dwarf",
        "isalive":true,
        "name":"Tom Bombadil"
    }

"""

import os
import json
import random

REQ = json.loads(open(os.environ['req']).read())
GENDERS = ('male', 'female')
RACES = ('human', 'dwarf', 'elf')

DWARF = {
    'name': REQ['name'],
    'gender': random.choice(GENDERS),
    'race': random.choice(RACES),
    'isalive': True
}

with open(os.environ['res'], 'w') as output:
    json.dump(DWARF, output)
