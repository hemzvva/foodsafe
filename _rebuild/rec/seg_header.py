#!/usr/bin/env python3
"""FoodSafe rule oracle: the business rules B-01..B-27 as pure Python, with hand-checked tests and the golden test vectors.

This file is the single source of truth for every rule that has a number, a sort order or a piece of text in it. The Swift
implementation (FoodSafeCore) must give the same answer for every vector in 03-ENGINEERING/fixtures/rules-vectors.json.
To change a rule: change this file and its hand-checked cases first, regenerate the fixtures, then change the Swift.

Usage (always with `python3 -I`; standard library only; Python 3.9 or newer):
  python3 -I tools/rules_reference.py                       run the hand-checked self-test
  python3 -I tools/rules_reference.py --emit DIR            self-test, then write the fixture files into DIR
  python3 -I tools/rules_reference.py --check DIR           self-test, then compare DIR and the generated document blocks with a fresh run
  python3 -I tools/rules_reference.py --update-docs         rewrite the generated blocks of the engineering documents
  python3 -I tools/rules_reference.py --print-fixtures      print the fixture tables (markdown)
  python3 -I tools/rules_reference.py --print-event-codes   print the table of event codes (markdown)

Conventions the Swift twin follows (CORE-API.md, C-1..C-13): exact rational arithmetic (here `Fraction`, there `Decimal`), one
rounding rule (half up), no clock or locale reads, total orders, no traps.
"""
import base64
import json
import math
import os
import re
import sys
from dataclasses import dataclass, replace
from datetime import date, datetime, timedelta, timezone
from fractions import Fraction as F
from typing import Dict, List, Optional, Tuple

HERE = os.path.dirname(os.path.abspath(__file__))
KIT = os.path.dirname(HERE)
TODAY = date(2026, 4, 18)  # the fixed test date of BUSINESS-RULES.md

# B-02: the policy numbers (days left)
EXPIRING_SOON_CARD_MAX_DAYS = 1
ALERT_MAX_DAYS = 2
SOON_BADGE_MAX_DAYS = 3
K_MISSING = 1  # B-08: the number of missing required lines an "Almost Ready" recipe may have
QUERY_TRIM = " \t\n\r"  # B-12, B-27: the four characters trimmed from both ends of a typed query
