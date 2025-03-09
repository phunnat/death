import sys
import yaml
import re
from glob import glob

def validate_file(file_path):
    with open(file_path, 'r') as f:
        data = yaml.safe_load(f)

    errors = []

    # Check 1: qualifiedSearch starts with "search index="
    if 'qualifiedSearch' in data:
        if not data['qualifiedSearch'].strip().startswith('search index='):
            errors.append(f"{file_path}: 'qualifiedSearch' must start with 'search index='")
    else:
        errors.append(f"{file_path}: 'qualifiedSearch' is missing")

    # Check 2: description contains a MITRE ATT&CK ID (e.g., Txxxx.xxx)
    if 'description' in data:
        if not re.search(r'T\d{4}\.\d{3}', data['description']):
            errors.append(f"{file_path}: 'description' must include a MITRE ATT&CK ID (e.g., T1204.002)")

    return errors

def main():
    files = sys.argv[1:]  # Get file paths from command line
    all_errors = []

    for file in files:
        all_errors.extend(validate_file(file))

    if all_errors:
        for error in all_errors:
            print(error)
        sys.exit(1)  # Exit with failure if errors found
    else:
        print("All detections comply with the guide!")
        sys.exit(0)

if __name__ == "__main__":
    main()