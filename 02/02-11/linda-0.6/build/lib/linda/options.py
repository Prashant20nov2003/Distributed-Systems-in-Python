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

## \namespace options
## \brief Handles command line options for linda_server
##
## \author Andrew Wilkinson <aw@cs.york.ac.uk>

from optparse import OptionParser
import sys

def getOptions():
    """\internal
    Handles commandline options for the linda_server
    """
    parser = OptionParser(version="%prog 0.2")
    parser.add_option("-c", "--connect", type="string", dest="connect", default="",
                      help="IP Address or DNS name of a computer connected to the Linda system")

    parser.add_option("-p", "--connect-port", type="int", dest="connectport", default=2102,
                      help="The port of to connect to of the destination computer")

    parser.add_option("-s", "--server-port", type="int", dest="port", default=2102,
                      help="The port to run the server from. (default: 2102)")

    parser.add_option("-l", "--localbind",
                      default="",
                      dest="bindaddress",
                      action="store_const",
                      const="127.0.0.1",
                      help="bind the server process to the loopback device")

    parser.add_option("--peer",
                      default=[],
                      dest="peer",
                      action="append",
                      help="allow connects from the IP address PEER. "\
                           "Supports n.n.n.n[/r] network notation or dnsname[/r]. "\
                           "Default: allow all.")

    parser.add_option("-d", "--disable-domain", default=True, action="store_false", dest="use_domain",
                      help="Disable the use of Unix Domain Sockets")

    parser.add_option("-D", "--daemon", default=False, action="store_true", dest="daemon",
                      help="Disable the interactive shell for the server. Default: Enabled.")

    parser.add_option("-v", "--verbose",
                      action="store_false", dest="verbose")

    (options, args) = parser.parse_args()

    if len(args) != 0:
        parser.print_help()
        sys.exit(0)

    return options
