from flask import Flask, render_template
from analyzer import DependencyAnalyzer
from visualizer import DependencyGraphVisualizer

app = Flask(__name__)

@app.route('/')
def index():
    project_path = 'path/to/your/project'
    analyzer = DependencyAnalyzer(project_path)
    dependencies = analyzer.analyze()

    visualizer = DependencyGraphVisualizer(dependencies)
    visualizer.build_graph()
    visualizer.visualize('static/dependency_graph.html')

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
