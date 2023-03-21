import csv
import matplotlib.pyplot as plt
import networkx as nx

with open('cities.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)
    my_list = []
    for lists in data:
        for data in lists:
            parts = data.split(';')
            parts[2] = int(parts[2])
            my_list.append(parts)
#print(my_list)

g = nx.DiGraph()
for edge in my_list:
    g.add_edge(edge[0], edge[1], weight=edge[2])
#print(g)

pos = nx.spring_layout(g)

plt.figure(figsize=(15,15))
nx.draw_networkx(g, pos, node_size=200, font_size=10, with_labels=True)
plt.title('Graph visualisation', fontsize=25)
plt.show()


def find_route(graph, city1, city2):
    shortest_path = nx.shortest_path(graph, source=city1, target=city2)
    shortest_weight = nx.shortest_path_length(graph, source=city1, target=city2, weight='weight')
    print(f'Your route: {shortest_path}.\nDistance: {shortest_weight}')

find_route(g, 'Kamianka', 'Sumy')


