# Copyright (C) 2003-2008 Beda Kosata <beda@zirael.org>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>


"""Abstract parent class for all converters."""


class ConverterBase(object):
    """This is a base class for all converters."""

    STATUS_OK = 1
    STATUS_CRITICAL_ERROR = 2

    # standard converter attrs
    reads_text = False
    writes_text = False
    reads_files = False
    writes_files = False

    default_configuration = {}

    def __init__(self):
        """Initializes the converter class."""
        self.configuration = {}
        self.warnings = []
        self.errors = []
        for key, value in list(self.default_configuration.items()):
            self.configuration[key] = value
        self.cleanup()

    def clean_logs(self):
        # here all warnings for the last run should be stored
        self.warnings = []
        # here error messages for the last run will be stored
        self.errors = []

    def mols_to_text(self, structures):
        self.clean_logs()

    def read_text(self, text):
        self.clean_logs()

    def mols_to_file(self, structures, filename):
        self.clean_logs()

    def read_file(self, filename):
        self.clean_logs()

    def cleanup(self):
        self.clean_logs()
        self.result = []
        self.last_status = None
