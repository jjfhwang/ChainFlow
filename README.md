# ChainFlow: Streamlining Data Pipelines with Python

ChainFlow is a Python library designed to simplify the creation, execution, and management of complex data processing pipelines. It offers a declarative approach to pipeline definition, allowing developers to focus on the logic of their data transformations rather than the intricacies of workflow management. ChainFlow provides a robust framework for building scalable and maintainable data workflows, making it an ideal solution for data scientists, engineers, and analysts alike.

ChainFlow addresses the challenges of building and maintaining data pipelines, such as managing dependencies between tasks, handling errors gracefully, and ensuring data consistency. It introduces a graph-based execution model, enabling parallel processing and efficient resource utilization. The library abstracts away the complexities of underlying execution engines, allowing users to easily switch between different environments, such as local machines, distributed clusters, or cloud platforms. By providing a unified API for defining and executing pipelines, ChainFlow significantly reduces the development time and effort required to build and deploy data-intensive applications.

The library excels at orchestrating data transformations, data loading, feature engineering, and model training processes. It provides built-in support for various data sources, including relational databases, NoSQL databases, cloud storage, and streaming platforms. ChainFlow further empowers developers with capabilities for data validation, monitoring, and alerting, allowing them to ensure the quality and reliability of their data pipelines. With its extensible architecture, ChainFlow can be easily adapted to meet the specific requirements of any data processing workflow.

ChainFlow not only simplifies data pipeline creation but also greatly improves the maintainability and scalability of these pipelines. By abstracting the implementation details and providing a clear, declarative syntax for pipeline definition, the library allows developers to easily understand, modify, and extend existing workflows. The modular architecture makes it simple to add new data sources, transformation functions, and execution environments. This ensures that ChainFlow remains a valuable tool as data processing needs evolve.

## Key Features

*   **Declarative Pipeline Definition:** Define pipelines using a simple, Pythonic syntax, focusing on the logical flow of data transformations. Pipelines are defined as directed acyclic graphs (DAGs), where nodes represent tasks and edges represent dependencies.
*   **Automatic Dependency Resolution:** ChainFlow automatically resolves dependencies between tasks, ensuring that tasks are executed in the correct order. The library leverages topological sorting algorithms to determine the optimal execution sequence.
*   **Parallel Execution:** Execute tasks in parallel to maximize resource utilization and reduce overall execution time. ChainFlow automatically manages the scheduling and distribution of tasks across available resources.
*   **Error Handling and Recovery:** Implement robust error handling mechanisms to gracefully handle failures and ensure data consistency. ChainFlow provides support for retries, rollbacks, and custom error handling logic.
*   **Data Validation:** Integrate data validation steps into your pipelines to ensure data quality. ChainFlow supports various validation techniques, including schema validation, data type checking, and custom validation rules.
*   **Extensible Architecture:** Easily extend ChainFlow to support new data sources, transformation functions, and execution environments. The library provides a plugin-based architecture that allows developers to add custom functionality.
*   **Monitoring and Logging:** Monitor the execution of your pipelines and track key metrics. ChainFlow provides integration with logging frameworks and monitoring tools, allowing you to easily track the performance and health of your workflows.

## Technology Stack

*   **Python:** The core programming language for ChainFlow.
*   **NetworkX:** A Python library for creating, manipulating, and studying the structure, dynamics, and functions of complex networks. Used for representing and processing the pipeline's DAG.
*   **Dask:** A flexible parallel computing library for Python. Can be used as an optional execution engine for distributed processing.
*   **SQLAlchemy:** A Python SQL toolkit and Object-Relational Mapper. Used for interacting with relational databases.
*   **Pandas:** A Python data analysis library. Provides data structures and tools for data manipulation and analysis.

## Installation

1.  **Clone the repository:**

    git clone https://github.com/jjfhwang/ChainFlow.git
    cd ChainFlow

2.  **Create a virtual environment:**

    python3 -m venv venv
    source venv/bin/activate  (or venv\Scripts\activate on Windows)

3.  **Install the required dependencies:**

    pip install -r requirements.txt

## Configuration

ChainFlow relies on environment variables for configuration. The following environment variables are supported:

*   `CHAINFLOW_LOG_LEVEL`: Sets the logging level (e.g., `DEBUG`, `INFO`, `WARNING`, `ERROR`). Defaults to `INFO`.
*   `CHAINFLOW_DATA_DIR`: Specifies the directory for storing temporary data files. Defaults to `./data`.

You can set these environment variables using the following command:

export CHAINFLOW_LOG_LEVEL=DEBUG
export CHAINFLOW_DATA_DIR=/path/to/data

Or, set them directly within your Python script before using ChainFlow:

import os
os.environ['CHAINFLOW_LOG_LEVEL'] = 'DEBUG'
os.environ['CHAINFLOW_DATA_DIR'] = '/path/to/data'

## Usage

Here's a simple example of how to define and execute a pipeline using ChainFlow:

from chainflow import Pipeline, Task

def task_one(data):
  # Your data transformation logic here
  processed_data = data * 2
  return processed_data

def task_two(data):
  # Your data transformation logic here
  final_data = data + 10
  return final_data

pipeline = Pipeline()
pipeline.add_task(Task(task_one, name="TaskOne"))
pipeline.add_task(Task(task_two, name="TaskTwo", dependencies=["TaskOne"]))

data = 5
result = pipeline.execute(data)
print(result)

This example defines a pipeline with two tasks: `task_one` and `task_two`. `task_two` depends on `task_one`, so it will be executed after `task_one` completes. The `execute` method runs the pipeline and returns the final result.

## Contributing

We welcome contributions to ChainFlow! To contribute, please follow these guidelines:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Implement your changes and write unit tests.
4.  Submit a pull request with a clear description of your changes.
5.  Ensure all tests pass before submitting the pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/jjfhwang/ChainFlow/blob/main/LICENSE) file for details.

## Acknowledgements

We would like to thank the developers of NetworkX, Dask, SQLAlchemy, and Pandas for creating the powerful open-source libraries that ChainFlow relies on.