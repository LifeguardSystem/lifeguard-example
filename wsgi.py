import sys

sys.path.append(".")

from lifeguard import setup
from lifeguard.context import LIFEGUARD_CONTEXT

setup(LIFEGUARD_CONTEXT)

from lifeguard.logger import lifeguard_logger as logger
from lifeguard.server import APP as application


def start_server():
    application.run()


if __name__ == "__main__":
    logger.info("starting server")
    application.run()
