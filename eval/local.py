import outlines

model = outlines.models.transformers(
        "TheBloke/Mistral-7B-v0.1-AWQ", device="cuda"
    )

def generate(
    question: str = "Find the area of a triangle with a base of 10 units and height of 5 units.",
    schema: str = '''{"name": "calculate_triangle_area", "description": "Calculate the area of a triangle given its base and height.", "parameters": {"type": "object", "properties": {"base": {"type": "number", "description": "The base of the triangle."}, "height": {"type": "number", "description": "The height of the triangle."}, "unit": {"type": "string", "description": "The unit of measure (defaults to 'units' if not specified)"}}, "required": ["base", "height"]}}'''
):

    generator = outlines.generate.json(model, schema)

    print(f"Responding to question: {question}")
    function_call = generator(
        f"{question}"
    )
    print(f"Response: {function_call}")
    return function_call