

import logging

logging.basicConfig(level=logging.DEBUG,
                    filename="logger.log")

logging.info('info日志')
logging.debug('debug日志')
logging.warning('warning日志')
logging.critical('critical日志')
