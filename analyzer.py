import os
import ast

class DependencyAnalyzer:
    def __init__(self, project_path):
        self.project_path = project_path
        self.dependencies = {}

    def analyze(self):
        for root, _, files in os.walk(self.project_path):
            for file in files:
                if file.endswith('.py'):
                    self._analyze_file(os.path.join(root, file))
        return self.dependencies

    def _analyze_file(self, file_path):
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read(), filename=file_path)
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        self._add_dependency(file_path, alias.name)
                elif isinstance(node, ast.ImportFrom):
                    self._add_dependency(file_path, node.module)

    def _add_dependency(self, file_path, module_name):
        if file_path not in self.dependencies:
            self.dependencies[file_path] = []
        self.dependencies[file_path].append(module_name)

if __name__ == "__main__":
    project_path = 'path/to/your/project'
    analyzer = DependencyAnalyzer(project_path)
    dependencies = analyzer.analyze()
    print(dependencies)
