# AIMA-style CSP for Australia

variables = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']

domains = {v: ['Red', 'Green', 'Blue'] for v in variables}

neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW'],
    'T': []
}

def is_consistent(var, value, assignment):
    for neighbor in neighbors[var]:
        if neighbor in assignment and assignment[neighbor] == value:
            return False
    return True


def backtrack(assignment):
    if len(assignment) == len(variables):
        return assignment

    var = [v for v in variables if v not in assignment][0]

    for value in domains[var]:
        if is_consistent(var, value, assignment):
            assignment[var] = value
            result = backtrack(assignment)
            if result:
                return result
            del assignment[var]

    return None


solution = backtrack({})
print("Australia Solution:", solution)
