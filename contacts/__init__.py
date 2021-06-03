# -*- coding: utf-8 -*-

"""This module provides the contacts package."""

import os, logging, logging.config

__version__ = "0.1.0"

# create logger
logger = logging.getLogger('contacts')
logger.setLevel(logging.DEBUG)
# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# create file handler and set level to debug
fh = logging.FileHandler('contacts.log')
fh.setLevel(logging.DEBUG)
# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# add formatter to ch
ch.setFormatter(formatter)
# add formatter to fh
fh.setFormatter(formatter)
# add ch to logger
logger.addHandler(ch)
logger.addHandler(fh)
