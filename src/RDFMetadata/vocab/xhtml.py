# vocab - definitions and human-readable names for metadata terms
#
# Copyright 2013 Commons Machinery http://commonsmachinery.se/
#
# Authors: Artem Popov <artfwo@commonsmachinery.se>
#
# Distributed under an GPLv2 license, please see LICENSE in the top dir.
import sys
from . import Term

NS_URI = "http://www.w3.org/1999/xhtml/vocab#"

license = Term(
    uri=NS_URI + "license",
    label="License",
    desc="license refers to a resource that defines the associated license."
)