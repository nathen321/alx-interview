#!/usr/bin/python3
import sys
import re

log_pattern = re.compile(
    r'^'
    r'(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
    r' - '
    r'\[(?P<date>[^\]]+)\]'
    r' "GET /projects/260 HTTP/1\.1"'
    r' (?P<status_code>\d{3})'
    r' (?P<file_size>\d+)'
    r'$'
)

total_size = 0
line_count = 0
status_counts = {
    '200': 0, '301': 0, '400': 0, '401': 0,
    '403': 0, '404': 0, '405': 0, '500': 0
}

def print_stats():
    print(f"File size: {total_size}")
    for code in sorted(status_counts):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")

try:
    for line in sys.stdin:
        line = line.strip()
        match = log_pattern.match(line)
        if not match:
            continue
            
        try:
            status = match.group('status_code')
            file_size = int(match.group('file_size'))
            
            total_size += file_size
            if status in status_counts:
                status_counts[status] += 1
                
            line_count += 1
            
            if line_count % 10 == 0:
                print_stats()
                
        except (ValueError, AttributeError):
            continue

except KeyboardInterrupt:
    print_stats()
    raise

print_stats()
