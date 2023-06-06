from lifeguard.actions.notifications import notify_in_thread
from lifeguard.http_client import post
from lifeguard.validations import validation

from lifeguard_openai.actions.errors import explain_error


@validation(
    "This validation will ever return a error. The objective is to test the actions on error",
    actions=[notify_in_thread],
    actions_on_error=[explain_error, notify_in_thread],
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

*explanation*
```
{{explanation}}
```
""",
        }
    },
)
def on_error_example():
    a_not_imported_function()
