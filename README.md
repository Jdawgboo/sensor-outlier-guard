# Sensor Outlier Guard

Flag numeric samples outside rolling median/MAD bounds.

```bash
cat values.json | python tool.py
python -m unittest -v
```

This is a local rule-based signal. Tune windows and thresholds for each sensor; it does not identify root cause.
