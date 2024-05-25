import matplotlib.pyplot as plt

# Function to read polygon data from the file
def read_polygon_data(filename):
    vertices = {}
    edges = []
    with open(filename, 'r') as file:
        lines = file.readlines()

        # Skip the first line "Polygonization"
        line_index = 1
        while True:
            line = lines[line_index].strip()
            if line.startswith("Polygon:"):
                line_index += 1
                break
            print(
                line
            )
            x, y = map(int, line.split())
            vertices[(x, y)] = len(vertices)
            line_index += 1

        # Read the edges
        while line_index < len(lines):
            line = lines[line_index].strip()
            if line == "":
                line_index += 1
                continue
            if line.startswith("Algorithm:"):
                break
            edge = list(map(int, line.split()))
            edges.append(((edge[0], edge[1]), (edge[2], edge[3])))
            line_index += 1

    return vertices.keys(), edges

# Function to plot the polygon
def plot_polygon(vertices, edges):
    fig, ax = plt.subplots()

    for edge in edges:
        x_values = [edge[0][0], edge[1][0]]
        y_values = [edge[0][1], edge[1][1]]
        ax.plot(x_values, y_values, 'b-')

    # Plotting the vertices
    for vertex in vertices:
        ax.plot(vertex[0], vertex[1], 'ro')
        ax.text(vertex[0], vertex[1], '({},{})'.format(vertex[0], vertex[1]), fontsize=12, ha='right')

    plt.title('Polygon Plot')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.axis('equal')  # Equal scaling for both axes
    plt.show()

# Main script
filename = './test/ouput.txt'
vertices, edges = read_polygon_data(filename)
plot_polygon(vertices, edges)
