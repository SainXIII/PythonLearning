#! /usr/bin/env python
# coding: utf-8
# authod: Adrian.Cui
# E-mail: cuiqinsain@gmail.com
# file  : filelogconf.py

import logging
import logging.config


logging.config.fileConfig('logging.conf')

#create logger
logger = logging.getLogger('simpleExample')

#create formatter
formatter = logging.Formatter('%(asctime)s %(name)s %(levelname) %(message)')

#add formatter
logger.setFormatter(formatter)


#example code
logger.debug('debug')
logger.info('info')
logger.warn('warning')
logger.error('error')
logger.critical('critical')
