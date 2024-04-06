import json
from pathlib import Path

from eval.config import ROOT_DIR, BATCH_SIZE
from eval.runner import stub, generate

# Load original dataset
with open(Path(ROOT_DIR, "data/processed/gorilla_openfunctions_v1_test_simple_jsonschema.jsonl"), "r") as f:
    data = [json.loads(item) for item in list(f)[0:10]]

@stub.local_entrypoint()
def main():

    with open(Path(ROOT_DIR, "data/results/gorilla_openfunctions_v1_test_simple_outlines.jsonl"), "w") as f:
        for i in range(0, len(data), BATCH_SIZE):
            questions = [item["question"] for item in data[i:i+BATCH_SIZE]]
            schemas = [item["schema"] for item in data[i:i+BATCH_SIZE]]
            for function_call in generate.map(questions, schemas):
                f.write(json.dumps(function_call) + "\n")

