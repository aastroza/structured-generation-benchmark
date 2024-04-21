# Structured Generation of Function Calls using Outlines ( https://github.com/outlines-dev/outlines )
# PoC Code: Connesson, Rémi. (Apr 2024). Outlines Function Call Gorilla Leaderboard Experiment. GitHub.
# https://github.com/remiconnesson/outlines-func-call-gorilla-leaderboard-experiment/tree/main.

from modal import Cls
import os, json
from textwrap import dedent

from model_handler.constant import GORILLA_TO_OPENAPI
from model_handler.model_style import ModelStyle
from model_handler.utils import (
    _cast_to_openai_type,
    ast_parse,
)



class GemmaOutlinesHandler:
    model_name: str
    model_style: ModelStyle

    def __init__(self, model_name, temperature=0.7, top_p=1, max_tokens=1000) -> None:
        self.model_name = model_name
        self.model_style = ModelStyle.Outlines
    
    def format_result(self, function_name, result):
        # This method is used to format the result in a standard way.
        args_string = ', '.join([f"{key}='{value}'" if isinstance(value, str) else f"{key}={value}" for key, value in result.items()])
        # Creating the output string with the function name and arguments
        output_string = f'[{function_name}({args_string})]'
        return output_string

    
    def inference(self, prompt, functions, test_category):
        # IMPORTANT: Only works for 'simple' test_category.
        

        if type(functions) is not list:
                functions = [functions]
        
        schema = json.dumps({
            "title": functions[0]["name"],
            "type": "object",
            "description": functions[0]["description"],
            "properties": _cast_to_openai_type(functions[0]["parameters"]["properties"], GORILLA_TO_OPENAPI, test_category),
            "required": functions[0]["parameters"]["required"]
        })
        try:
            
            # This method is used to retrive model response for each model.

            prompt_template = dedent(
                                    """
                                <bos><start_of_turn>user\n
                                A user is gonna ask you a question, you need to extract the arguments to be passed to the function that can answer the question.
                                You must answer the user's question by replying VALID JSON that matches the schema below:\n
                                ```json\n
                                {schema}\n
                                ```\n
                                The user's question below:\n
                                ```text\n
                                {question}\n
                                ```\n
                                <end_of_turn>\n
                                <start_of_turn>model\n
                                """)
            Model = Cls.lookup("outlines-app", "Model")
            m = Model(model_name=self.model_name)
            result = m.generate.remote(schema.strip(),
                                       prompt_template.format(schema=schema.strip(), question=prompt))
            result = self.format_result(functions[0]["name"], result)

        except:
            result = '[error.message(error="Error occurred")]'

        
        return result, {"input_tokens": 0, "output_tokens": 0, "latency": 0}


    def decode_ast(self, result, language="Python"):
        decoded_output = ast_parse(result,language)
        return decoded_output

    def decode_execute(self, result):
        # This method takes raw model output and convert it to standard execute checker input.
        pass

    def write(self, result, file_to_open):
        # This method is used to write the result to the file.
        if not os.path.exists("./result"):
            os.mkdir("./result")
        if not os.path.exists("./result/" + self.model_name.replace("/", "_")):
            os.mkdir("./result/" + self.model_name.replace("/", "_"))
        with open(
            "./result/"
            + self.model_name.replace("/", "_")
            + "/"
            + file_to_open.replace(".json", "_result.json"),
            "a+",
        ) as f:
            f.write(json.dumps(result) + "\n")

    def load_result(self, test_category):
        # This method is used to load the result from the file.
        result_list = []
        with open(
            f"./result/{self.model_name.replace('/', '_')}/gorilla_openfunctions_v1_test_{test_category}_result.json"
        ) as f:
            for line in f:
                result_list.append(json.loads(line))
        return result_list
