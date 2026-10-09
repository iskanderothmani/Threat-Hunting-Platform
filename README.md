# Threat Hunting Platform

A local-first hunt runner for normalized synthetic event records. Executes simple, documented hypotheses against supplied JSON; it does not connect to telemetry systems.

## Run
Python 3.11+; standard library only.

```bash
python app.py
python -m unittest discover -s tests -v
```

## Safety
Use synthetic or authorized event data. Do not commit production logs, credentials, or personal data. Matching rules are examples, not a detection guarantee.

## License
MIT
