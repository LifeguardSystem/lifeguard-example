import json

from lifeguard.controllers import controller


@controller("/hello/<name>")
def hello(name):
    return json.dumps({"name": name})
