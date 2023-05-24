"""
Lifeguard Settings
"""
import lifeguard_mongodb
import lifeguard_notification_google_chat
import lifeguard_rabbitmq
import lifeguard_simple_dashboard

from lifeguard.auth import BASIC_AUTH_METHOD
from lifeguard.validations import VALIDATIONS
from lifeguard.actions.database import save_result_into_database
from lifeguard_rabbitmq import RABBITMQ_PLUGIN_CONTEXT

RABBITMQ_PLUGIN_CONTEXT.consumers_validation_options = {
    "actions": [save_result_into_database],
    "schedule": {"every": {"minutes": 1}},
    "settings": {},
    "queues": {
        "default": [
            {
                "name": "lifeguard.queue.example",
                "min_number_of_consumers": 1,
            }
        ]
    },
}

RABBITMQ_PLUGIN_CONTEXT.messages_increasing_validation_options = {
    "actions": [save_result_into_database],
    "schedule": {"every": {"minutes": 1}},
    "settings": {},
    "queues": {
        "default": [
            {
                "name": "lifeguard.queue.example",
                "count_before_alert": 3,
            }
        ]
    },
}

PLUGINS = [
    lifeguard_mongodb,
    lifeguard_notification_google_chat,
    lifeguard_rabbitmq,
    lifeguard_simple_dashboard,
]


def setup(lifeguard_context):
    lifeguard_context.auth_method = BASIC_AUTH_METHOD
    lifeguard_context.users = [{"username": "test", "password": "pass"}]
    for validation in VALIDATIONS:
        print(validation)
