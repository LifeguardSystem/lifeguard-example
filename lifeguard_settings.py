"""
Lifeguard Settings
"""
import lifeguard_mongodb
import lifeguard_notification_google_chat
import lifeguard_rabbitmq
import lifeguard_simple_dashboard

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
    lifeguard_simple_dashboard,
    lifeguard_rabbitmq,
]


def setup(_lifeguard_context):
    for validation in VALIDATIONS:
        print(validation)
