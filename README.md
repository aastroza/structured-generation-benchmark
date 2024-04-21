# structured-generation-benchmark

To use Large Language Models (LLMs) effectively and reliably, it's essential to include structured generation techniques. Being able to get outputs like regular expressions, JSON, or a Pydantic data model is key for making useful software.

But what's the real effect of using libraries like [Outlines](https://github.com/outlines-dev/outlines) or [Instructor](https://github.com/jxnl/instructor/)?

The goal of this repository is to put together evaluations to answer this question.

## Function Calling

The ability of the LLM to call functions.

### Datasets

- [Berkeley Function Calling Leaderboard](https://huggingface.co/datasets/gorilla-llm/Berkeley-Function-Calling-Leaderboard/tree/64d44ccd13f3351d17c33951af5ef1bd6e10153c) [April 16, 2024 update]

### Evaluation

- We deployed a [modal function](modal/transformers_outlines.py) to run open-source models using [Transfomers](https://github.com/huggingface/transformers) + [Outlines](https://github.com/outlines-dev/outlines).
- We created different [model handlers](evals/bfcl/scripts) to run the [Gorilla BFCL scripts](https://github.com/ShishirPatil/gorilla/tree/c6221060a9d50d0c7e7705f1ac95b9e5c4a95252) [April 6, 2024 version] for the `AST simple` evaluation category.
- We [evaluated](evals/bfcl/score) and reported the [results](evals/bfcl/result) comparing them with the [Leaderboard Website](https://github.com/ShishirPatil/gorilla/tree/bdd9d0ac13b6d61ebe1cbfed3903cd16939f1d5f) [April 14, 2024 version].

### Reports

- [Outlines Function Calling Evaluation](reports/bfcl_outlines.md)
- [Instructor Function Calling Evaluation](reports/instructor_outlines.md)