from lifeguard.validations import validation, ValidationResponse
from lifeguard.actions.notifications import notify_in_thread


@validation(
    "This validation will ever return a error. The objective is to test the actions on error",
    actions=[notify_in_thread],
    actions_on_error=[notify_in_thread],
    schedule={"every": {"minutes": 1}},
    settings={
        "notification": {
            "update_thread_interval": 60,
            "template": "sucesso",
            "template_error": """
*exception*: {{exception}}

*traceback*
```
{{traceback}}
```
""",
        }
    },
)
def validate_on_error():
    return ValidationResponse("validate_on_error", "NORMAL", {})
    # raise Exception("error")
