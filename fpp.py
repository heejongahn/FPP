def fpp(nodes, edges):
    l = len(nodes)
    all_tours = []

    for i in range(l):
        all_tours += find_tour_with_length(nodes, edges, i+1)

    all_tours = simplyfy(all_tours)
    return make_tours_prime(all_tours)

def find_tour_with_length(nodes, edges, l):
    if l == 1:
        return nodes

    prev_tours = find_tour_with_length(nodes, edges, l-1)
    tours = []

    for tour in prev_tours:
        for next_node in edges[tour[-1]]:
            tours.append("".join([tour, next_node]))
    return tours

def simplyfy(tours):
    simple_tours = []
    for tour in tours:
        l = len(tour)
        okay = True

        for i in range(l):
            n = tour[i]
            if n in tour[i+1:]:
                if i==0 and n not in tour[i+1:-1]:
                    pass
                else:
                    okay = False
        if okay:
            simple_tours.append(tour)

    return simple_tours

def make_tours_prime(tours):
    tours = sorted(tours, key = lambda tours:len(tours))

    refined_tours = []
    l = len(tours)

    for i in range(l):
        tour = tours[i]
        redundant = False

        for j in range(i+1, l):
            if tour in tours[j]:
                redundant = True
                break

        if not redundant:
            refined_tours.append(tour)

    return refined_tours

if __name__ == '__main__':
    nodes = input('노드들을 입력해주세요: ').strip('\n').split(' ')
    edges = {}
    for node in nodes:
        current_edges = input('노드 {}에서의 outgoing edge들을 입력해주세요: '.format(node))
        current_edges = current_edges.strip('\n').split(' ')
        edges[node] = current_edges

    pps = fpp(nodes, edges)
    print ('총 {}개의 prime path가 존재합니다.'.format(len(pps)))
    for pp in pps:
        print (pp)
