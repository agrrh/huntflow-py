# Info

[![Build Status](https://drone-gh.agrrh.com/api/badges/agrrh/huntflow-py/status.svg)](https://drone-gh.agrrh.com/agrrh/huntflow-py)

## Requirements

To use [Huntflow API](https://github.com/huntflow/api) you need to obtain personal token by asking support via email.

This library also requires you to set proper (at least valid) email to let Huntflow staff contact you in case of emergency.

## Usage

After you're ready, usage is quite simple:

```python
from huntflow_py.api import APIv1 as Huntflow

huntflow = Huntflow(
  token='your-token-here',
  email='your-email-here',
)

print(huntflow.me())
```

For other methods see `api.py`.

Right now I'm not sure how to generate available methods list automatically, feel free to contact and let me know.
