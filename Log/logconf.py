#! /usr/bin/env python
# coding: utf-8
# author: Adrian.Cui
# E-mail: cuiqinsain@gmail.com
# file  : logconf.py

import logging

#create logger
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

#create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

#create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

#add formatter to ch
ch.setFormatter(formatter)

#add ch to logger
logger.addHandler(ch)

#example code
logger.debug('debug')
logger.info('info')
logger.warn('warning')
logger.error('error')
logger.critical('critical')
