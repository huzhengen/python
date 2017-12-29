import logging

logging.basicConfig(level=logging.DEBUG,
	format = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
	datefmt = '%a, %d %b %Y %H:%M:%S',
	filename = 'learn-logging.log',
	filemode = 'w'
	)
logging.debug('this is debug message')
logging.info('this is info message')
logging.warning('this is warning message')