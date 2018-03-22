import logging

logging.basicConfig(level=logging.INFO,filename='myLog.log')
logging.info('Starting program')
logging.info('Trying to divide 1 by 0.')

print(1/0)

logging.info('Succeeded')
logging.info('Ending program')