import argparse
from logging import getLogger, FileHandler
from logging import Formatter, DEBUG


def start_logger(filepath, logger_name='logger'):
    logger = getLogger(logger_name)
    logger.setLevel(DEBUG)
    file_handler = FileHandler(filepath)
    file_handler.setLevel(DEBUG)
    fmt_ = '[%(asctime)s: %(levelname)s] - %(funcName)s - %(message)s'
    file_log_formatter = Formatter(fmt=fmt_)
    file_handler.setFormatter(file_log_formatter)
    logger.addHandler(file_handler)
    return logger


def create_parser(arg1):
    parser = argparse.ArgumentParser()
    parser.add_argument('arg1', nargs='?', default=arg1)
    return parser
