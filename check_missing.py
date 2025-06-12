import json
import pandas as pd

# Load submission.json (JSON lines format)
with open("submission.json", "r") as f:
    submission_data = [json.loads(line) for line in f]
submission_indices = set(item["index"] for item in submission_data)

# Load eval.csv (ground truth index file)
eval_df = pd.read_csv("Eval-Data-Label/STask-A(index,label)val.csv")
eval_indices = set(eval_df["index"].tolist())

# Compare
missing = eval_indices - submission_indices
extra = submission_indices - eval_indices

print(f"✅ Submission entries: {len(submission_indices)}")
print(f"✅ Eval entries: {len(eval_indices)}")

if missing:
    print(f"❌ Missing index(es): {missing}")
else:
    print("✅ No missing indices")

if extra:
    print(f"❌ Extra/unexpected index(es): {extra}")
else:
    print("✅ No extra indices")
