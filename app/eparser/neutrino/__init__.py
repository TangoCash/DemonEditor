# -*- coding: utf-8 -*-
#
# The MIT License (MIT)
#
# Copyright (c) 2018-2021 Dmitriy Yefremov
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# Author: Dmitriy Yefremov
#

SP = "_:::_"
KSP = "_::_"
API_VER = "4"


def get_attributes(data):
    return {el[0]: el[1] for el in (e.split(KSP) for e in data.split(SP))}


def get_xml_attributes(attr):
    attrs = attr.attributes
    return {t: attrs[t].value for t in attrs.keys()}

# Override _write_data function to escape correctly
import xml.dom.minidom as md
def wd(writer, data):
    "Writes datachars to writer."
    if data:
        data = data.replace("&", "&amp;").replace("'", "&apos;"). \
                    replace('"',"&quot;").replace("<","&lt;"). \
                    replace(">","&gt;")
        writer.write(data)

md._write_data = wd
