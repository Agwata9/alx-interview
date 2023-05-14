#!/usr/bin/python3
"""
 a script that reads stdin line by line and computes metrics
"""
import sys


# Initialize variables
total_file_size = 0
status_code_count = {}

try:
    # Read stdin line by line
    for i, line in enumerate(sys.stdin, start=1):
        # Parse the line
        parts = line.strip().split()
        if len(parts) != 7:
            # Skip lines with incorrect format
            continue

        # Extract relevant information
        status_code = parts[5]
        file_size = int(parts[6])

        # Update total file size
        total_file_size += file_size

        # Update status code count
        if status_code.isdigit():
            status_code = int(status_code)
            if status_code in status_code_count:
                status_code_count[status_code] += 1
            else:
                status_code_count[status_code] = 1

        # Print statistics after every 10 lines
        if i % 10 == 0:
            # Print total file size
            print("Total file size:", total_file_size)

            # Print status code count
            sorted_status_codes = sorted(status_code_count.keys())
            for code in sorted_status_codes:
                print(f"{code}: {status_code_count[code]}")

except KeyboardInterrupt:
    # Print statistics when a keyboard interruption occurs
    print("\nTotal file size:", total_file_size)
    sorted_status_codes = sorted(status_code_count.keys())
    for code in sorted_status_codes:
        print(f"{code}: {status_code_count[code]}")

