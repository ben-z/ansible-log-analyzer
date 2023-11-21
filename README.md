# Ansible log analyzer

Analyzes the runtime of Ansible steps.

## Getting Started

```bash
python3 print_durations.py <path_to_ansible_log>
```

Example output:
```
Gathering Facts: 3.35 seconds
users : Create a temporary build directory: 0.32 seconds
users : debug: 0.06 seconds
users : Import the dirctory config: 0.05 seconds
users : debug: 0.16 seconds
users : Get a list of users currently on the system: 2.32 seconds
users : parse existing users: 0.65 seconds
users : Get a list of ansible-managed groups currently on the system: 0.50 seconds
users : parse managed groups: 0.40 seconds
users : Generate directory updates: 3.33 seconds
users : Remove users: 0.14 seconds
users : Remove groups: 0.14 seconds
users : Configure groups: 235.51 seconds
users : Configure users: 201.27 seconds
users : Create user SSH key base directory: 0.90 seconds
users : Create user SSH directories: 201.44 seconds
users : Populate user SSH keys: 399.59 seconds
users : Create a directory on the host to store build configs: 0.27 seconds
```
