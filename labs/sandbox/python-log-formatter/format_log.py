from pathlib import Path
import sys

if len(sys.argv) != 2:
    print("usage: python format_log.py <log_file>", file=sys.stderr)
    sys.exit(1)

log_path = Path(sys.argv[1])

if not log_path.exists():
    print(f"error: file not found: {log_path}", file=sys.stderr)
    sys.exit(1)

text = log_path.read_text(encoding="utf-8")

print("| time | command | result | note |")
print("| --- | --- | --- | --- |")
for line in text.splitlines():
    parts = line.split()
    time = parts[0]
    fields = {}

    for item in parts[1:]:
        key, value = item.split("=",1)
        fields[key] = value

    print(f"| {time} | {fields['command']} | {fields['result']} | {fields['note']} |")
