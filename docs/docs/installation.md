---
layout: default
title: Installation
nav_order: 2
has_children: false
---

## 2. Installation

### 2.1. Prerequisites

Before installing PrometheusEval, ensure that you have the following prerequisites:

- Python 3.11 or higher
- pip package installer

2.2. Installing the Package

To install PrometheusEval, follow these steps:

1. Open a terminal or command prompt.

2. Run the following command to install PrometheusEval using pip:
   ```shell
   pip install prometheus-eval
   ```

   This command will download and install the latest version of the package along with its dependencies.

   For efficient inference, we strongly encourage you to install flash-attention as well.

   ```shell
   pip install flash-attn --no-build-isolation
   ```

3. Once the installation is complete, you can verify that PrometheusEval is installed correctly by running the following command:
   ```
   python -c "import prometheus_eval; print(prometheus_eval.__version__)"
   ```

   If the installation was successful, it will print the version number of the installed package.


That's it! You have now successfully installed PrometheusEval. You're ready to start using the package to evaluate and grade AI-generated responses.

If you encounter any issues during the installation process or have any questions, please refer to the Troubleshooting section of the documentation or reach out to our support team for assistance.

Note: It is recommended to use a virtual environment to isolate the package dependencies and avoid conflicts with other packages in your Python environment. You can create a virtual environment using tools like `virtualenv`, `poetry` or `conda` before installing PrometheusEval.