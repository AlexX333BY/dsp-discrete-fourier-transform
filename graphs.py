from matplotlib import pyplot
from collections import namedtuple

Graph = namedtuple('Graph', ['ox', 'oy', 'name'])


class GraphDrawer:
    def __init__(self):
        self.__graphs = []

    def add_graph(self, graph):
        self.__graphs.append(graph)

    def draw(self):
        graphs_count = len(self.__graphs)
        new_figure = pyplot.figure()

        for i, graph in enumerate(self.__graphs):
            new_axes = new_figure.add_subplot(1, graphs_count, i + 1)
            pyplot.title(graph.name)
            new_axes.plot(graph.ox, graph.oy)

    @staticmethod
    def show():
        pyplot.show()
