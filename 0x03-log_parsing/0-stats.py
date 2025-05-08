#!/usr/bin/python3
import sys
import re

log_pattern = re.compile(
    r'^'
    r'(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # IP address
    r' - '
    r'\[(?P<date>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+)\]'  # Timestamp
    r' "(?P<request>GET /projects/260 HTTP/1\.1)"'  # Request
    r' (?P<status_code>\d{3})'  # Status code (e.g., 400)
    r' (?P<file_size>\d+)'  # File size (e.g., 585)
    r'$'
)
total_size = 0
conter = 0
register = {
    "200": 0, "301": 0, "400": 0, "401": 0,
    "403": 0, "404": 0, "405": 0, "500": 0
}
try:
    # Read line by line
    for line in sys.stdin:
        conter += 1
        match = log_pattern.match(line)
        if conter % 10 == 0:
            print(f"File size: {total_size}")
            for code in sorted(register):
                if register[code] > 0:
                    print(f"{code}: {register[code]}")
        if match:
            status = match.group('status_code')
            file_size = int(match.group('file_size'))
            total_size += file_size
            if status in register:
                register[status] += 1
except KeyboardInterrupt:
    print(f"\nFile size: {total_size}")
    for code in sorted(register):
        if register[code] > 0:
            print(f"{code}: {register[code]}")
