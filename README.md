# DepGraphViz

DepGraphViz is a Python tool that analyzes and visualizes the dependencies in a Python project. It creates an interactive dependency graph to help developers understand the relationships between modules and packages.

## Features

- **Dependency Analysis**: Scans a Python project and identifies all dependencies.
- **Graph Visualization**: Generates an interactive dependency graph.
- **Web Interface**: Provides a simple web interface to display the graph.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/wasserpuncher/DepGraphViz.git
    cd DepGraphViz
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask server:
    ```bash
    python app.py
    ```

2. Open your browser and navigate to `http://127.0.0.1:5000/` to view the interactive dependency graph.

## License

This project is licensed under the MIT License.
