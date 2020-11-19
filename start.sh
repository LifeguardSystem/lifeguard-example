#!/bin/bash

export LIFEGUARD_DIRECTORY="."
export LIFEGUARD_VALIDATION_REPOSITORY_IMPLEMENTATION="lifeguard_mongodb.repositories.MongoDBValidationRepository"

lifeguard-scheduler
