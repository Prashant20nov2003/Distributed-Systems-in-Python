#    Copyright 2004 Andrew Wilkinson <aw@cs.york.ac.uk>.
#
#    This file is part of PyLinda (http://www-users.cs.york.ac.uk/~aw/pylinda)
#
#    PyLinda is free software; you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published by
#    the Free Software Foundation; either version 2.1 of the License, or
#    (at your option) any later version.
#
#    PyLinda is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with PyLinda; if not, write to the Free Software
#    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

def pack(ts):
    return "linda.TupleSpace(%s)" % (ts.__getstate__()[0])

def unpack(s):
    assert s[:16] == "linda.TupleSpace"

    id = s[s.index("(")+1:s.index(")")]
    ts = kernel.TupleSpace(True)
    ts.__setstate__([id])
    return ts

import typeconvert
from . import kernel
typeconvert.registerType(kernel.TupleSpace, "linda.TupleSpace", pack, unpack)
