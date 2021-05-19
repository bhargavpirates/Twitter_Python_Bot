import logging

def setup_logger(logger_name, log_file, level=logging.INFO,create_file=True):
    
    log = logging.getLogger(logger_name)
    log.setLevel(level)

    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    if create_file:
        # create file handler for logger.
        fh = logging.FileHandler(log_file, mode='a', encoding='utf-8')
        fh.setLevel(level)
        fh.setFormatter(formatter)

    # reate console handler for logger.
    ch = logging.StreamHandler()
    ch.setLevel(level)
    ch.setFormatter(formatter)

    # add handlers to logger.
    if create_file:
        log.addHandler(fh)
    
    log.addHandler(ch)
    print("ok")
    log.info("INFO")
    log.debug("DEBUG")
    log.warning("WARNING")
    log.error("ERROR")
    return  log   

if(__name__=="__main__"):
    setup_logger(__name__, "logs/bot_logs.txt", level=logging.INFO,create_file=True)