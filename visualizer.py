import networkx as nx
from pyvis.network import Network
from analyzer import DependencyAnalyzer

class DependencyGraphVisualizer:
    def __init__(self, dependencies):
        self.graph = nx.DiGraph()
        self.dependencies = dependencies

    def build_graph(self):
        for file, deps in self.dependencies.items():
            for dep in deps:
                self.graph.add_edge(file, dep)

    def visualize(self, output_file='dependency_graph.html'):
        net = Network(notebook=True, directed=True)
        net.from_nx(self.graph)
        net.show(output_file)

if __name__ == "__main__":
    project_path = 'path/to/your/project'
    analyzer = DependencyAnalyzer(project_path)
    dependencies = analyzer.analyze()
    
    visualizer = DependencyGraphVisualizer(dependencies)
    visualizer.build_graph()
    visualizer.visualize()
