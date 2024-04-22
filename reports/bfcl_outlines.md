# Outlines Function Calling Evaluation

## Goal

## Benchmark

## Methodology

- We deployed a [modal function](modal/transformers_outlines.py) to run open-source models using [Transformers](https://github.com/huggingface/transformers) + [Outlines](https://github.com/outlines-dev/outlines).
- We created different [model handlers](evals/bfcl/scripts) to run the [Gorilla BFCL scripts](https://github.com/ShishirPatil/gorilla/tree/c6221060a9d50d0c7e7705f1ac95b9e5c4a95252) [April 6, 2024 version] for the `AST simple` evaluation category.
- We [evaluated](evals/bfcl/score) and reported the [results](evals/bfcl/result) comparing them with the [Leaderboard Website](https://github.com/ShishirPatil/gorilla/tree/bdd9d0ac13b6d61ebe1cbfed3903cd16939f1d5f) [April 14, 2024 version].

## Results

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

### Mistral-7B-Instruct-v0.2

[Code](../evals/bfcl/scripts/mistral_outlines_handler.py) | [Results](../evals/bfcl/result/mistralai_Mistral-7B-Instruct-v0.2/gorilla_openfunctions_v1_test_simple_result.json) | [Score](../evals/bfcl/score/mistralai_Mistral-7B-Instruct-v0.2/simple_score.json)

### Deepseek-v1.5

[Code](../evals/bfcl/scripts/deepseek_outlines_handler.py) | [Results](../evals/bfcl/result/deepseek-ai_deepseek-coder-7b-instruct-v1.5/gorilla_openfunctions_v1_test_simple_result.json) | [Score](../evals/bfcl/score/deepseek-ai_deepseek-coder-7b-instruct-v1.5/simple_score.json)

### Gemma-7b-it

[Code](../evals/bfcl/scripts/gemma_outlines_handler.py) | [Results](../evals/bfcl/result/google_gemma-7b-it/gorilla_openfunctions_v1_test_simple_result.json) | [Score](../evals/bfcl/score/google_gemma-7b-it/simple_score.json)

### Meta-Llama-3-8B-Instruct

[Code](../evals/bfcl/scripts/llama_outlines_handler.py) | [Results](../evals/bfcl/result/meta-llama_Meta-Llama-3-8B-Instruct/gorilla_openfunctions_v1_test_simple_result.json) | [Score](../evals/bfcl/score/meta-llama_Meta-Llama-3-8B-Instruct/simple_score.json)


## Conclusion