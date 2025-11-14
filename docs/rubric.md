# Rubric

Use this project rubric to understand and assess the project criteria.

## Agent Pattern Implementation

| Criteria                                                                                   | Submission Requirements                                                                                                                                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Validate and correct malformed SWIFT messages using the Evaluator-Optimizer pattern.       | * The `EvaluatorOptimizerAgent` calls the `evaluator_agent` to assess message validity.* If invalid, the message is passed to `optimizer_agent` for correction.* The final output is a valid SWIFT message object (original or corrected).* Implementation is located in `evaluator_optimizer.py`. |
| Concurrently detect different types of fraudulent activity using multiple agents           | * At least three fraud detection agents are implemented, including a custom third agent.* All fraud detection agents run in parallel using `ThreadPoolExecutor`.* Fraud results are aggregated using a dedicated aggregation agent.* Implementation is located in `parallelization.py`.                |
| Perform multi-step fraud analysis using chained agents with distinct roles                 | * The conversation chain includes a Junior Analyst → Technical Analyst → Compliance Officer.* Each step uses the result of the previous agent to inform its own reasoning.* Output is a structured log of all steps in the chain.* Implementation is located in `prompt_chaining.py`.                  |
| Structure finalized transactions using an orchestrator that delegates subtasks to workers. | * Orchestrator agent proposes a valid grouping plan (e.g., by bank, currency).* Worker agent formats and returns final reports based on the orchestrator’s plan.* Outputs are coherent, structured, and match the proposed grouping.* Implementation is located in `orchestrator_worker.py`.            |

## Main System Integration and Workflow

| Criteria                                                                         | Submission Requirements                                                                                                                                                                                                                                                                  |
| -------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Sequentially invoke all agent patterns to analyze and report SWIFT transactions. | * The system calls all four agent patterns in sequence within `main.py`.* Outputs from one stage feed directly into the next.* At least two distinct reports are generated based on different message filters.* System runs end-to-end without errors and logs agent activity clearly. |

## Industry Best Practices

| Criteria                                                                            | Submission Requirements                                                                                                                                                                                                                                               |
| ----------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Follow clean coding practices and include documentation for implemented components. | * Clear function names and consistent formatting (PEP8 style).* All custom agent classes and key methods include docstrings.* Includes evidence of testing: print statements, logs, or screenshots of output.* No syntax errors, missing imports, or hardcoded paths. |

## Suggestions to Make Your Project Stand Out

* Additional fraud detection logic (e.g., AI-driven anomaly detection)
* Performance optimizations (e.g., caching, batching)
* Comprehensive error handling (e.g., fallback logic, retry strategies)
* Unit tests for any agent or system component

---
