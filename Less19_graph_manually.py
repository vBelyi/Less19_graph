import csv #для імпорту даних з csv
import networkx as nx #для візуалізації графу
import matplotlib.pyplot as plt #для візуалізації графу
import math #для встановлення нескінченності для шляхів до вершин, які ще не були оброблені
import queue #для встановлення черги, при якій знаходиться найоптимальніший маршрут

with open('cities.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)
    my_list = []
    for lists in data:
        for data in lists:
            parts = data.split(';')
            parts[2] = int(parts[2])
            my_list.append(parts)

my_graph = {}
for city1, city2, distance in my_list:
    if city1 not in my_graph:
        my_graph[city1] = {}
    if city2 not in my_graph:
        my_graph[city2] = {}

    my_graph[city1][city2] = distance
    my_graph[city2][city1] = distance
#print(my_graph)
#print(len(my_graph))

g = nx.DiGraph(my_graph)
pos = nx.spring_layout(g)

plt.figure(figsize=(15,15))
nx.draw_networkx(g, pos, node_size=200, font_size=10, with_labels=True, node_color='Green')
plt.title('Graph visualisation', fontsize=25)
plt.show()

def find_route(graph, city1, city2):
    dist = {city: math.inf for city in graph}
    prev = {city: None for city in graph}
    dist[city1] = 0
    my_queue = queue.PriorityQueue()
    my_queue.put((0, city1))
    while not my_queue.empty():
        curr_dist, curr_city = my_queue.get()
        if curr_city == city2:
            route = []
            while curr_city is not None:
                route.insert(0, curr_city)
                curr_city = prev[curr_city]
            return f"Route: {' -> '.join(route)}.\nDistance: {curr_dist}"
        for neighbor, distance in graph[curr_city].items():
            new_dist = dist[curr_city] + distance
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                prev[neighbor] = curr_city
                my_queue.put((new_dist, neighbor))
    return None

print(find_route(my_graph, 'Kamianka', 'Mykolaiv'))








