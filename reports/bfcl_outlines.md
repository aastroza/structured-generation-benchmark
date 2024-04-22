# Outlines Function Calling Evaluation

> [!NOTE]
> This report originates from the [Outlines](https://github.com/outlines-dev/outlines) community's proposal to build a dataset for evaluating structured generation. If you want to participate, join our [Discord](https://discord.gg/ZxBxyWmW5n).

## Goal

The main goal of this evaluation is to show the power of structured generation in the context of Function Calling, which is the ability of Large Language Models (LLMs) to call functions based on natural language instructions. We focus on the case where the LLM is given a single JSON function document and is expected to make a single function call.

To create this evaluation, we use the [Outlines](https://github.com/outlines-dev/outlines) library, which changes the problem of neural text generation into transitions between states of a finite-state machine[^1]. Outlines allows for the creation of reliable interfaces by ensuring the structure of the generated text.

[^1]: [Willard, B. T., & Louf, R. (2023). Efficient Guided Generation for Large Language Models](https://huggingface.co/papers/2307.09702).

We want to explore some interesting questions: Can structured generation work better than fine-tuning for Function Calling? Can this approach allow smaller open-source models to perform as well as larger, state-of-the-art models? The results of this evaluation will give us valuable insights into the abilities and potential of structured generation in improving the performance of LLMs across various model sizes and architectures, potentially reshaping our understanding of how to optimize  for specific tasks.

## Benchmark

There is a dataset generated from real-world data that has been released for the construction of the [**Berkeley Function-Calling Leaderboard**](https://gorilla.cs.berkeley.edu/leaderboard.html#leaderboard). It consists of 2,000 question-function-answer pairs across multiple languages, diverse application domains, and complex use cases. Additionally, it includes the [code to reproduce the benchmark](https://github.com/ShishirPatil/gorilla/tree/main/berkeley-function-call-leaderboard), which serves as a sort of framework for evaluation. If you want to learn more about this outstanding initiative, we recommend reading [this blog post](https://gorilla.cs.berkeley.edu/blogs/8_berkeley_function_calling_leaderboard.html).

In the Outlines community, we decided to start with the 'AST Simple' category, as described by the authors:

> Simple Function: The evaluation of a single function includes the simplest but most commonly seen format, where the user provides a single JSON function document. Only one function call will be invoked.

It's exactly the use case we've been facing in our efforts to integrate LLMs to power software.

## Methodology

- We deployed a [**Modal** function](modal/transformers_outlines.py) to run open-source models using [Transformers](https://github.com/huggingface/transformers) + [Outlines](https://github.com/outlines-dev/outlines). [Modal](https://modal.com/) is an easy-to-use cloud platform useful to run generative AI models. Soon, we will write in more detail about [our experience deploying structured generation there](https://github.com/aastroza/modal-outlines-examples).
- We created different [model handlers](evals/bfcl/scripts) to run the [Gorilla BFCL evaluation framework](https://github.com/ShishirPatil/gorilla/tree/c6221060a9d50d0c7e7705f1ac95b9e5c4a95252) [April 6, 2024 version] for the `AST simple` evaluation category.
- We [evaluated](evals/bfcl/score) and reported the [results](evals/bfcl/result) comparing them with the [Leaderboard Website](https://github.com/ShishirPatil/gorilla/tree/bdd9d0ac13b6d61ebe1cbfed3903cd16939f1d5f) [April 14, 2024 version].

## Results

The **results in bold** are those we added using Outlines. The rest of the rows are the results already reported on the Leaderboard.

| Rank | Model                                            | Simple Function AST |
|------|--------------------------------------------------|---------------------|
| 1    | GPT-4-0125-Preview (Prompt)                      | 88.00%              |
| 2    | Gorilla-OpenFunctions-v2 (FC)                    | 87.64%              |
| **3**    | **Deepseek-v1.5 (Outlines)**                         | **87.00%**              |
| **4**    | **Gorilla-OpenFunctions-v2 (Outlines)**              | **87.00%**              |
| 5    | Claude-3-Opus-20240229 (Prompt)                  | 86.36%              |
| 6    | GPT-4-turbo-2024-04-09 (Prompt)                  | 85.82%              |
| **7**    | **Mistral-7B-Instruct-v0.2 (Outlines)**              | **85.50%**              |
| 8    | Claude-3-Haiku-20240307 (Prompt)                 | 85.45%              |
| 9    | Claude-3-Haiku-20240307 (FC tools-2024-04-04)    | 85.27%              |
| **10**   | **Gemma-7b-it (Outlines)**                           | **84.25%**              |
| **11**   | **Meta-Llama-3-8B-Instruct (Outlines)**              | **84.25%**              |
| 12   | Mistral-large-2402 (FC Any)                      | 82.91%              |
| 13   | GPT-4-1106-Preview (FC)                          | 82.00%              |
| 14   | Claude-3-Sonnet-20240229 (Prompt)                | 81.82%              |
| 15   | Mistral-small-2402 (FC Any)                      | 81.09%              |
| 16   | Claude-3-Opus-20240229 (FC tools-2024-04-04)     | 80.91%              |
| 17   | GPT-4-0125-Preview (FC)                          | 80.00%              |
| 18   | Functionary-Small-v2.4 (FC)                      | 80.00%              |
| 19   | Claude-instant-1.2 (Prompt)                      | 80.00%              |
| 20   | Functionary-Medium-v2.4 (FC)                     | 79.45%              |
| 21   | Mistral-Medium-2312 (Prompt)                     | 79.27%              |
| 22   | Gemini-1.0-Pro (FC)                              | 77.27%              |
| 23   | Claude-3-Sonnet-20240229 (FC tools-2024-04-04)   | 76.73%              |
| 24   | Claude-2.1 (Prompt)                              | 74.36%              |
| 25   | GPT-4-turbo-2024-04-09 (FC)                      | 73.82%              |
| 26   | Hermes-2-Pro-Mistral-7B (FC)                     | 71.45%              |
| 27   | Nexusflow-Raven-v2 (FC)                          | 70.18%              |
| 28   | FireFunction-v1 (FC)                             | 67.27%              |
| 29   | DBRX-Instruct (Prompt)                           | 66.73%              |
| 30   | Mistral-large-2402 (FC Auto)                     | 66.36%              |
| 31   | GPT-4-0613 (FC)                                 | 61.64%              |
| 32   | GPT-3.5-Turbo-0125 (FC)                         | 57.09%              |
| 33   | Mistral-tiny-2312 (Prompt)                       | 49.64%              |
| 34   | Gemma-7b-it (Prompt)                             | 42.18%              |
| 35   | Deepseek-v1.5 (Prompt)                           | 38.91%              |
| 36   | Mistral-Small-2402 (Prompt)                      | 5.64%               |
| 37   | Mistral-small-2402 (FC Auto)                     | 1.64%               |

## Discussion

### Mistral-7B-Instruct-v0.2 (7th, 85.5%)

[Code](../evals/bfcl/scripts/mistral_outlines_handler.py) | [Results](../evals/bfcl/result/mistralai_Mistral-7B-Instruct-v0.2/gorilla_openfunctions_v1_test_simple_result.json) | [Score](../evals/bfcl/score/mistralai_Mistral-7B-Instruct-v0.2/simple_score.json)

Our first intuition was to explore the potential of structured generation in enhancing the performance of a 7B model on the Function Calling task. `Mistral-7B-Instruct-v0.2` achieved an impressive accuracy of 85.5%, securing the 7th position on the leaderboard. Notably, this result stands as the highest score among all Mistral models in the table, suggesting that structured generation may play a significant role in enabling smaller models to tackle complex tasks effectively.

### Gemma-7b-it (from 34th, 42.18% to 10th, 84.25%)

[Code](../evals/bfcl/scripts/gemma_outlines_handler.py) | [Results](../evals/bfcl/result/google_gemma-7b-it/gorilla_openfunctions_v1_test_simple_result.json) | [Score](../evals/bfcl/score/google_gemma-7b-it/simple_score.json)

We wanted to see if a base 7B model could reach the top of the leaderboard by using the power of structured generation. `google/gemma-7b-it` was already the best 7B model on the leaderboard before our tests. However, when we combined it with Outlines, it showed a huge jump in performance. It went from the 34th position with an accuracy of 42.18% to an impressive 10th place, achieving an accuracy of 84.25%. This big improvement highlights the potential of structured generation to boost the performance of base models.

### Deepseek-v1.5 (from 35th, 38.91% to 3rd, 87%)

`deepseek-coder-7b-instruct-v1.5`

[Code](../evals/bfcl/scripts/deepseek_outlines_handler.py) | [Results](../evals/bfcl/result/deepseek-ai_deepseek-coder-7b-instruct-v1.5/gorilla_openfunctions_v1_test_simple_result.json) | [Score](../evals/bfcl/score/deepseek-ai_deepseek-coder-7b-instruct-v1.5/simple_score.json)

### Meta-Llama-3-8B-Instruct (11th, 84.25%)

[Code](../evals/bfcl/scripts/llama_outlines_handler.py) | [Results](../evals/bfcl/result/meta-llama_Meta-Llama-3-8B-Instruct/gorilla_openfunctions_v1_test_simple_result.json) | [Score](../evals/bfcl/score/meta-llama_Meta-Llama-3-8B-Instruct/simple_score.json)

We couldn't resist testing the latest sensation in the world of language models. When combined with structured generation, `Meta-Llama-3-8B-Instruct` achieved an impressive accuracy of 84.25%, securing the 11th position on the leaderboard. 

## Conclusion