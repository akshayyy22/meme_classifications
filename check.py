import json

# Read JSON Lines format (one object per line)
with open("submission.json", "r") as f:
    data = [json.loads(line) for line in f]

print(f"✅ Number of entries in submission.json: {len(data)}")

# Check if indices are sorted
indices = [item["index"] for item in data]
if indices != sorted(indices):
    print("⚠️ Indices are NOT in ascending order.")
else:
    print("✅ Indices are in ascending order.")
