import logging
import logging.config
import json
import os

# DEBUG < INFO << WARNING < ERROR < CRITICAL

if __name__ == '__main__':

    with open('logger.json', 'rt') as f:
        config = json.load(f)

    logging.config.dictConfig(config)

    logger = logging.getLogger("my_module")
    logger.error("error test!!!")
    logger.info("info test!!!")
    logger.debug("debug test!!!")