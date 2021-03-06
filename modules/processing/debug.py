# Copyright (C) 2010-2012 Cuckoo Sandbox Developers.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file 'docs/LICENSE' for copying permission.

import os
import codecs

from lib.cuckoo.common.abstracts import Processing
from lib.cuckoo.common.exceptions import CuckooProcessingError


class Debug(Processing):
    """Analysis debug information."""

    def run(self):
        """Run debug analysis.
        @return: debug information dict.
        """
        self.key = "debug"
        debug = {}

        if os.path.exists(self.log_path):
            try:
                debug["log"] = codecs.open(self.log_path, "rb", "utf-8").read()
            except ValueError as e:
                raise CuckooProcessingError("Error decoding %s: %s" % (self.log_path, e))
            except (IOError, OSError):
                raise CuckooProcessingError("Error opening %s: %s" % (self.log_path, e))
        else:
            debug["log"] = ""

        return debug
