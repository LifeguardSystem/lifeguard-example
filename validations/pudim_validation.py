"""
Check if pudim is alive
"""
import requests

from lifeguard import NORMAL, PROBLEM, change_status
from lifeguard.actions.database import save_result_into_database
from lifeguard.logger import lifeguard_logger as logger
from lifeguard.validations import validation, ValidationResponse


@validation(
    "check if pudim is alive",
    actions=[save_result_into_database],
    schedule={"every": {"minutes": 1}},
)
def pudim_is_alive():
    status = NORMAL
    result = requests.get("http://pudim.com.br")
    logger.info("pudim status code: %s", result.status_code)

    if result.status_code != 200:
        status = change_status(status, PROBLEM)
    return ValidationResponse("pudim_is_alive", NORMAL, {status: result.status_code})
