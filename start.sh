#!/bin/bash

export LIFEGUARD_DIRECTORY="."
export LIFEGUARD_VALIDATION_REPOSITORY_IMPLEMENTATION="lifeguard_mongodb.MongoDBValidationRepository"
export LIFEGUARD_NOTIFICATION_IMPLEMENTATIONS="lifeguard_notification_google_chat.GoogleNotificationBase"

lifeguard