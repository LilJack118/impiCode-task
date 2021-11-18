import sys


def create_cycle(cycles,permutation):
    element = list(permutation.items())[0]
    cycle = []
    cycle.append(element[0])
    element = element[1]
    iterate = True
    while iterate:
        cycle.append(element) if element not in cycle else cycle
        element = permutation[element]
        iterate = False if element in cycle else True
    for x in set(cycle):
        del permutation[x]
        
    cycles.append(cycle)
    
    if permutation:
        create_cycle(cycles,permutation)
        


def sort_elephants(weights,order,director_order):
    # permutation
    permutation = dict(zip(order,director_order))
    cycles = []
            
    create_cycle(cycles,permutation)
    print('created_cycle')
        
    weights_cycle = [[weights[element-1] for element in cycle] for cycle in cycles]
    metoda_1 = sum([sum(weights_c)+(len(weights_c)-2)*min(weights_c) for weights_c in weights_cycle])
    metoda_2 = sum([sum(weights_c) + min(weights_c) + (len(weights_c) - 1)*min(weights) for weights_c in weights_cycle if len(weights_c) > 1])
    min_effort = min(metoda_1,metoda_2)
    print(min_effort)
        
    
if len(sys.argv) == 1:
    print('No file specified')
    data = []
else:
    output_path = (sys.argv[1].split('.'))[0]+'.out'
    output = open(output_path, 'r')
    
    file = open(sys.argv[1], 'r')
    lines = [line.split(' ') for line in file.read().splitlines()]
    data = [int(x) for line in lines for x in line]
    n = data[0]
    weights = data[1:n+1]
    order = data[n+1:2*n+1]
    director_order = data[2*n+1:]
    file.close()
    print('opened')

    effort = sort_elephants(weights,order,director_order)
    if int(output.read()) == effort:
        print(effort)
    




