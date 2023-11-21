import argparse
import re
from datetime import datetime

def custom_parse_datetime(datetime_str):
    # Splitting the datetime string into date and time components
    date_str, time_str = datetime_str.split('T')
    year, month, day = map(int, date_str.split('-'))
    hms_str, frac_str = time_str.split('.')
    hour, minute, second = map(int, hms_str.split(':'))
    frac_second = int((frac_str.rstrip('Z') + '000000')[:6])  # Normalizing to microseconds

    # Creating a datetime object with the parsed components
    return datetime(year, month, day, hour, minute, second, frac_second)

def parse_task_durations(log_lines):
    task_start_pattern = re.compile(r'(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d+Z) TASK \[.*\]')
    tasks = []
    start_time = None
    last_task = None

    for line in log_lines:
        match = task_start_pattern.match(line)
        if match:
            task_start_str = match.group(1)
            task_start_dt = custom_parse_datetime(task_start_str)

            if start_time:
                # Calculate duration of the previous task
                duration = task_start_dt - start_time
                tasks.append((last_task, duration))

            # Update the start time for the new task
            start_time = task_start_dt
            last_task = line.strip().split("TASK [")[-1].split("]")[0]
    
    return tasks

def colored(text, color):
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'end': '\033[0m',
    }
    return f"{colors.get(color, '')}{text}{colors['end']}"

# Set up argument parsing
parser = argparse.ArgumentParser(description="Parse task durations from a log file.")
parser.add_argument("file_path", help="Path to the log file.")
args = parser.parse_args()

# Reading the log file
with open(args.file_path, 'r') as file:
    ansible_log_content = file.readlines()

# Rest of your code
task_durations = parse_task_durations(ansible_log_content)
for task, duration in task_durations:
    task_colored = colored(task, 'red')
    duration_seconds = duration.total_seconds()
    duration_colored = colored(f"{duration_seconds:.2f} seconds", 'green')
    print(f"{task_colored}: {duration_colored}")
