from auto_gptq import exllama_set_max_input_length
import outlines

model_name = "TheBloke/Mistral-7B-Instruct-v0.2-GPTQ"
model = outlines.models.transformers(model_name, device='cuda')
model.model = exllama_set_max_input_length(model.model, max_input_length=4000)
# model = outlines.models.transformers(
#         "TheBloke/Mistral-7B-v0.1-AWQ", device="cuda"
#     )

def generate(
    question: str = "Find the area of a triangle with a base of 10 units and height of 5 units.",
    schema: str = '''{"name": "calculate_triangle_area", "description": "Calculate the area of a triangle given its base and height.", "parameters": {"type": "object", "properties": {"base": {"type": "number", "description": "The base of the triangle."}, "height": {"type": "number", "description": "The height of the triangle."}, "unit": {"type": "string", "description": "The unit of measure (defaults to 'units' if not specified)"}}, "required": ["base", "height"]}}'''
):

    generator = outlines.generate.json(model, schema.strip(), whitespace_pattern="")

    print(f"Responding to question: {question}")
    function_call = generator(
        f""""
    You are an expert in composing functions. You are given a question and a set of possible functions. 
    Based on the question, you will need to make one or more function/tool calls to achieve the purpose. 
    If none of the function can be used, point it out. If the given question lacks the parameters required by the function,
    also point it out. You should only return the function call in tools call sections.
    Question: {question}
    """
    )
    print(f"Response: {function_call}")
    return function_call