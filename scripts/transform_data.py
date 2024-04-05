import sys
sys.path.append('..')

import json
from pathlib import Path

from eval.config import ROOT_DIR

# Load original dataset
with open(Path(ROOT_DIR, "data/raw/gorilla_openfunctions_v1_test_simple.jsonl"), "r") as f:
    data = [json.loads(item) for item in list(f)]

# Transform to follow JSON Schema format
transformed_data = []
for item in data:
    transformed_item = {
        "question": item["question"],
        "schema": json.dumps({
            "title": item["function"]["name"],
            "type": "object",
            "description": item["function"]["description"],
            "properties": item["function"]["parameters"]["properties"],
            "required": item["function"]["parameters"]["required"]
        }),
        "human_eval_answer": item["human_eval_answer"]
    }
    transformed_data.append(transformed_item)

# Save transformed data
with open(Path(ROOT_DIR, "data/processed/gorilla_openfunctions_v1_test_simple_jsonschema.jsonl"), "w") as f:
    for item in transformed_data:
        f.write(json.dumps(item) + "\n")