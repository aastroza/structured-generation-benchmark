import os
from modal import App, Secret, gpu, method, Image

app = App(name="outlines-app")

outlines_image = Image.debian_slim(python_version="3.11").pip_install(
    "outlines==0.0.39",
    "transformers==4.38.2",
    "datasets==2.18.0",
    "accelerate==0.27.2",
    "einops==0.7.0"
)

@app.cls(image=outlines_image, secrets=[Secret.from_dotenv()], gpu=gpu.H100(), timeout=300)
class Model:
    def __init__(self, model_name: str) -> None:
        import outlines

        self.model = outlines.models.transformers(
            model_name,
            device="cuda",
            model_kwargs={
                "token": os.environ["HF_TOKEN"],
                "trust_remote_code": True,
            },
        )

    @method()
    def generate(self, schema: str, prompt: str, whitespace_pattern: str = None):
        import outlines

        if whitespace_pattern:
            generator = outlines.generate.json(self.model, schema.strip(), whitespace_pattern=whitespace_pattern)
        else:
            generator = outlines.generate.json(self.model, schema.strip())

        result = generator(prompt)

        return result