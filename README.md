Read this in [Portuguese](translations/README.pt.md).

<!-- About the Service -->
# Data Lake as a Service

Welcome to our Data Lake as a Service Open Source. Our software is specialized in managing and providing a fully managed Data Lake for your company, offering a robust and scalable solution for data storage and analysis.

With Data Lake as a Service, you don't need to worry about infrastructure, configuration, or environment maintenance. Our code will take care of everything, allowing you to focus on extracting valuable insights from your data.

<!-- Benefits -->
## Benefits of Data Lake as a Service Open Source

- Scalability: Expand your data storage capacity according to your business needs.
- Security: Keep your data secure with advanced security measures and encryption.
- Ease of Use: Intuitive and user-friendly interface for accessing and analyzing your data effortlessly.
- Cost Reduction: Eliminate expenses related to infrastructure and labor for environment maintenance.
- Advanced Data Analysis: Conduct detailed analyses and gain valuable insights for strategic decision-making.

![Data Lake as a Service](https://dataengineer.help/DLaaS/DLaaS.png)

## Project in Miro

https://miro.com/app/board/uXjVMr3ALEo=/?share_link_id=493109150457

<!-- Project Setup -->
## Project Setup

Follow the steps below to set up and run the Data Lake as a Service project in your environment using Poetry.

## Install Poetry

If you don't already have Poetry installed, you can do so using the pip package manager. Open your terminal and run the following command:

```bash
pip install poetry
```

### Install the Dependencies

To install the project dependencies, execute the following command in the project's root directory:

```bash
poetry install
```

This will ensure that all the necessary dependencies are installed in the project's virtual environment.

### Run the Project
To start the project, execute the following command:

```bash
poetry run python -m main
```

Remember to configure the environment variables and any other necessary settings before running the project. Also, be sure to consult the documentation for additional information on how to use the Data Lake as a Service Open Source.

Enjoy using Data Lake as a Service and start exploring the benefits it provides for data storage and analysis in your company!

## Logging System in the Project


The Data Lake as a Service project incorporates a logging system using Python's `logging` library. This logging system has been implemented to assist in tracking code execution and identifying potential issues during processing.

### Basic Operation

The logging systems works as the following:

1. **Logging Setup**: At the beginning of the code, we configure the logging system to direct messages to a file named "init.log" in the "logs" directory. Log messages are recorded with different levels, with the primary level being `INFO`, which is used for informative messages.


2. **Message Logging**: Throughout the code, we use the `logging.info()` function to log informative messages at relevant points during execution. For example, we log information about processed URLs, API requests, and database operations.

3. **Benefits**: The logging system provides several benefits, including:
    - Progress Tracking: Log messages help track what's happening during code execution.
    - Debugging: It facilitates the identification of issues and errors, enabling more effective debugging.
    - Auditing: Log messages can be used for auditing and post-execution analysis.

4. **Location of Records**: All log messages are recorded in the "init.log" file in the "logs" directory. Make sure to create the "logs" folder in the same directory where the script is located or adjust the log file path as needed.


### Recommended Usage

When running the Data Lake as a Service project, it is advisable to refer to the "init.log" log file for information about the progress of execution. If any issues arise, the log messages will provide valuable clues for troubleshooting.

Remember to configure environment variables and any other necessary settings before running the project. Additionally, consult the documentation for further information on using Data Lake as a Service.

Utilizing the logging system helps maintain transparency and visibility during project execution, contributing to a smoother and more reliable experience.