# Inspired by the outlines-app example from Modal's GitHub repository:
# https://github.com/modal-labs/modal-examples/blob/11316522b678759526e7cc93d910bbd438436fe4/06_gpu_and_ml/llm-structured/outlines_generate.py
# This code adapts the approach for loading and using models with the outlines and transformers libraries.

from modal import Image, Stub, gpu

stub = Stub(name="outlines-app")

outlines_image = Image.debian_slim(python_version="3.11").pip_install(
    "outlines==0.0.34",
    "transformers==4.38.2",
    "datasets==2.18.0",
    "accelerate==0.27.2",
)

def import_model():
    import outlines

    outlines.models.transformers("mistralai/Mistral-7B-v0.1")


outlines_image = outlines_image.run_function(import_model)

@stub.function(image=outlines_image, gpu=gpu.A100(memory=80), timeout=120)
def generate(
    question: str = "Find the area of a triangle with a base of 10 units and height of 5 units.",
    schema: str = '''{"name": "calculate_triangle_area", "description": "Calculate the area of a triangle given its base and height.", "parameters": {"type": "object", "properties": {"base": {"type": "number", "description": "The base of the triangle."}, "height": {"type": "number", "description": "The height of the triangle."}, "unit": {"type": "string", "description": "The unit of measure (defaults to 'units' if not specified)"}}, "required": ["base", "height"]}}'''
):
    import outlines

    model = outlines.models.transformers(
        "mistralai/Mistral-7B-v0.1", device="cuda"
    )

    generator = outlines.generate.json(model, schema)

    print(f"Responding to question: {question}")
    function_call = generator(
        f"{question}"
    )
    print(f"Response: {function_call}")
    return function_call