from datetime import datetime

now = datetime.now()

now_without_microseconds = now.replace(microsecond=0)

print(now_without_microseconds)
