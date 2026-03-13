import json
import sys
import os

def update_json(payload_data):
    file_path = 'transforms.json'
    with open(file_path, 'r') as f:
        data = json.load(f)

    # 1. Define the staging key
    staging_key = "next-release-placeholder"
    
    # 2. Initialize staging block if it doesn't exist
    if staging_key not in data["transformsData"]:
        data["transformsData"][staging_key] = {
            "systemVersion": {"majorVersion": 0, "minorVersion": 0, "patchVersion": 0, "packageDate": "PENDING"},
            "transforms": []
        }

    new_entries = []
    for item in payload_data['new_transforms']:
        # Construct the object (you can add logic for inverse IDs here)
        entry = {
            "transformId": item['id'],
            "userName": item['user'],
            "transformType": "CSC", # Or parse from ID string
            "previousEquivalentTransformIds": [],
            "inverseTransformId": "",
            "transformUrl": f"https://raw.githubusercontent.com/ampas/{payload_data['submodule']}/{payload_data['sha']}/{item['file']}"
        }
        data["transformsData"][staging_key]["transforms"].append(entry)
        new_entries.append(f"- Added `{item['id']}` from {payload_data['submodule']}")

    # 3. Write back to file
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)
    
    # 4. Return changelog text for the PR body
    return "\n".join(new_entries)

if __name__ == "__main__":
    # Payload passed as a JSON string argument from the workflow
    payload = json.loads(sys.argv[1])
    changelog = update_json(payload)
    # Output for GitHub Actions
    with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
        print(f"changelog<<EOF\n{changelog}\nEOF", file=fh)