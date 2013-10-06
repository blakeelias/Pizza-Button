#!/usr/bin/env python
import sys

import cgi
import cgitb
import ordrin

# Two different servers:
# ordrin.TEST or ordrin.PRODUCTION
server = ordrin.TEST

ordrin_api = ordrin.APIs("jWSw_CthhgY0afo7hMbN7gd3AlPtKLYtDs2Mf_uituM",server)


