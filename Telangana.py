
import networkx as nx
import matplotlib.pyplot as plt

# ------------------ NEIGHBORS (33 Districts) ------------------
TELANGANA_NEIGHBORS = {
    'Adilabad': ['Kumuram Bheem', 'Nirmal', 'Mancherial'],
    'Kumuram Bheem': ['Adilabad', 'Mancherial', 'Nirmal'],
    'Mancherial': ['Adilabad', 'Kumuram Bheem', 'Nirmal', 'Jagtial', 'Peddapalli'],
    'Nirmal': ['Adilabad', 'Kumuram Bheem', 'Mancherial', 'Nizamabad', 'Jagtial'],
    'Nizamabad': ['Nirmal', 'Jagtial', 'Kamareddy', 'Rajanna Sircilla'],
    'Jagtial': ['Nirmal', 'Mancherial', 'Nizamabad', 'Rajanna Sircilla', 'Karimnagar', 'Peddapalli'],
    'Rajanna Sircilla': ['Nizamabad', 'Jagtial', 'Kamareddy', 'Karimnagar', 'Siddipet'],
    'Kamareddy': ['Nizamabad', 'Rajanna Sircilla', 'Medak', 'Sangareddy', 'Siddipet'],
    'Karimnagar': ['Jagtial', 'Rajanna Sircilla', 'Peddapalli', 'Siddipet', 'Jayashankar', 'Warangal Urban'],
    'Peddapalli': ['Mancherial', 'Jagtial', 'Karimnagar', 'Jayashankar'],
    'Siddipet': ['Kamareddy', 'Rajanna Sircilla', 'Karimnagar', 'Medak', 'Sangareddy', 'Medchal', 'Yadadri', 'Jangaon', 'Warangal Urban'],
    'Medak': ['Kamareddy', 'Siddipet', 'Sangareddy'],
    'Sangareddy': ['Kamareddy', 'Medak', 'Siddipet', 'Medchal', 'Hyderabad'],
    'Medchal': ['Sangareddy', 'Siddipet', 'Hyderabad', 'Rangareddy', 'Yadadri'],
    'Hyderabad': ['Sangareddy', 'Medchal', 'Rangareddy'],
    'Jayashankar': ['Peddapalli', 'Karimnagar', 'Warangal Urban', 'Bhadradri Kothagudem', 'Mulugu'],
    'Warangal Urban': ['Karimnagar', 'Siddipet', 'Jayashankar', 'Jangaon', 'Warangal Rural', 'Mahabubabad'],
    'Warangal Rural': ['Warangal Urban', 'Jangaon', 'Mahabubabad', 'Suryapet'],
    'Jangaon': ['Siddipet', 'Warangal Urban', 'Warangal Rural', 'Yadadri'],
    'Yadadri': ['Medchal', 'Siddipet', 'Jangaon', 'Rangareddy', 'Nalgonda', 'Suryapet'],
    'Rangareddy': ['Medchal', 'Hyderabad', 'Yadadri', 'Nalgonda', 'Mahabubnagar', 'Vikarabad'],
    'Vikarabad': ['Rangareddy', 'Mahabubnagar', 'Sangareddy'],
    'Mahabubnagar': ['Rangareddy', 'Vikarabad', 'Nalgonda', 'Nagarkurnool', 'Wanaparthy', 'Gadwal'],
    'Nalgonda': ['Rangareddy', 'Yadadri', 'Suryapet', 'Mahabubnagar', 'Khammam'],
    'Suryapet': ['Yadadri', 'Warangal Rural', 'Nalgonda', 'Khammam', 'Mahabubabad'],
    'Mahabubabad': ['Warangal Urban', 'Warangal Rural', 'Suryapet', 'Khammam', 'Bhadradri Kothagudem', 'Jayashankar'],
    'Khammam': ['Nalgonda', 'Suryapet', 'Mahabubabad', 'Bhadradri Kothagudem'],
    'Bhadradri Kothagudem': ['Khammam', 'Mahabubabad', 'Jayashankar', 'Mulugu'],
    'Mulugu': ['Jayashankar', 'Bhadradri Kothagudem'],
    'Nagarkurnool': ['Mahabubnagar', 'Nalgonda', 'Wanaparthy', 'Jogulamba Gadwal'],
    'Wanaparthy': ['Mahabubnagar', 'Nagarkurnool', 'Gadwal'],
    'Gadwal': ['Mahabubnagar', 'Wanaparthy', 'Jogulamba Gadwal'],
    'Jogulamba Gadwal': ['Nagarkurnool', 'Gadwal'],
}

COLORS = ['Red', 'Green', 'Blue', 'Yellow']


# ------------------ CSP FUNCTIONS ------------------

def is_consistent(region, color, assignment):
    for neighbor in TELANGANA_NEIGHBORS[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True


def select_unassigned_variable(assignment):
    unassigned = [r for r in TELANGANA_NEIGHBORS if r not in assignment]
    return min(unassigned, key=lambda r: sum(
        1 for c in COLORS if is_consistent(r, c, assignment)
    ))


def backtrack(assignment):
    if len(assignment) == len(TELANGANA_NEIGHBORS):
        return assignment

    region = select_unassigned_variable(assignment)

    for color in COLORS:
        if is_consistent(region, color, assignment):
            assignment[region] = color

            result = backtrack(assignment)
            if result:
                return result

            del assignment[region]

    return None


def verify(solution):
    for r in TELANGANA_NEIGHBORS:
        for n in TELANGANA_NEIGHBORS[r]:
            if solution[r] == solution[n]:
                return False
    return True


# ------------------ GRAPH VISUALIZATION ------------------

def draw_graph(solution):
    G = nx.Graph()

    # nodes
    for region in TELANGANA_NEIGHBORS:
        G.add_node(region)

    # edges
    for region, neigh in TELANGANA_NEIGHBORS.items():
        for n in neigh:
            G.add_edge(region, n)

    # colors
    color_map = []
    for node in G.nodes():
        c = solution[node]
        if c == "Red":
            color_map.append("red")
        elif c == "Green":
            color_map.append("green")
        elif c == "Blue":
            color_map.append("blue")
        else:
            color_map.append("yellow")

    plt.figure(figsize=(14, 10))
    pos = nx.spring_layout(G, seed=42)

    nx.draw(
        G, pos,
        with_labels=True,
        node_color=color_map,
        node_size=1500,
        font_size=7
    )

    plt.title("Telangana Map Coloring (CSP)")
    plt.show()


# ------------------ MAIN ------------------

solution = backtrack({})

print("\nTelangana Map Coloring Solution:\n")

for region, color in solution.items():
    print(f"{region:30} -> {color}")

print("\nValid Solution:", verify(solution))
print("Total Districts:", len(solution))

# Draw Graph
draw_graph(solution)
