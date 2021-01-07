"""
Lifeguard Settings
"""
import lifeguard_mongodb
import lifeguard_notification_google_chat

PLUGINS = [lifeguard_mongodb, lifeguard_notification_google_chat]


def setup(_lifeguard_context):
    print("in custom setup")
