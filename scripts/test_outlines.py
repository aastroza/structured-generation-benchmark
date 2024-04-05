from eval.runner import stub, generate

@stub.local_entrypoint()
def main():
    questions = ["Find the area of a triangle with a base of 10 units and height of 5 units."]
    schemas = ['''{
               "title": "calculate_triangle_area",
               "type": "object",
               "description": "Calculate the area of a triangle given its base and height.",
               "properties": {
                    "base": {
                        "type": "number",
                        "description": "The base of the triangle."
                    },
                    "height": {
                        "type": "number",
                        "description": "The height of the triangle."
                    },
                    "unit": {
                        "type": "string",
                        "description": "The unit of measure (defaults to 'units' if not specified)"
                    }
                },
               "required": ["base", "height"]
               }'''.strip()]
    for function_call in generate.map(questions, schemas):
        print(function_call)