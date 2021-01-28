import json

from lifeguard.controllers import controller, request


@controller("/hello/<name>", methods=["GET", "POST"])
def hello(name):
    print(request.args)
    return json.dumps({"name": name})
