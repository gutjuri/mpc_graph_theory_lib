## MIT License
from Compiler.types import sint, Array
from Compiler.library import if_then, end_if, print_ln, print_str
T = 99999


def test_print_vector_secret(V):
    [print_str("%s ", v.reveal()) for v in V]
    print_ln(" ")


def ineq(a, b):
    return a < b


def vector_permutation(v, factor):
    return v


def matrix_permutation(u, factor):
    return u


def obtain_random_factor(n):
    return 0


def exchange_elements(c, a, b):
    aux_a = ternary_operator(c, b, a)
    aux_b = ternary_operator(c, a, b)
    return aux_a, aux_b


def exchange_row_matrix(i, j, u):

    for h in range(len(u)):
        c = h == j
        for k in range(len(u[0])):
            u[i][k], u[h][k] = exchange_elements(c, u[i][k], u[h][k])
    return u


def exchange_vector(i, j, v):
    for h in range(len(v)):
        c = h == j
        v[i], v[h] = exchange_elements(c, v[i], v[h])
    return v


def ternary_operator(c, if_true, if_false):
    return c * (if_true - if_false) + if_false


def dijkstra_optimized(weights, source):
    # L1-3
    n = len(weights)
    distance = sint.Array(n)
    alpha = sint.Array(n)
    P = sint.Array(n)

    @for_range(n)
    def f(i):
        distance[i] = ternary_operator(sint(i) == source, sint(0), sint(T))
        alpha[i] = sint(i)
        P[i] = sint(i)
    
    #test_print_vector_secret(distance)

    # L4
    factor = obtain_random_factor(0)
    p_weights = matrix_permutation(weights, factor)
    distance = vector_permutation(distance, factor)
    p_vertex_id = vector_permutation(P, factor)



    test_print_vector_secret([x for xs in weights for x in xs])

    @for_range(n)
    def _(i):
        global d_prime, v
        d_prime = sint(T)
        v = sint(0)
        
        @for_range(n-1, i-1, -1)
        def _(j):
            global d_prime, v
            c = ineq(distance[j], d_prime)
            v = ternary_operator(c, j, v)
            d_prime = ternary_operator(c, distance[j], d_prime)
        v_open = None
        if isinstance(v, sint):            
            v_open = v.reveal()
        else: 
            v_open = v
        exchange_row_matrix(i, v_open, p_weights)
        exchange_vector(i, v_open, distance)
        exchange_vector(i, v_open, p_vertex_id)
        
        @for_range(i+1, n)
        def _(j):
            a = distance[i] + p_weights[i][j]
            c = ineq(a,  distance[j])
            distance[j] = ternary_operator(c, a, distance[j])
            alpha[j] = ternary_operator(c, p_vertex_id[i], alpha[j])
    test_print_vector_secret(p_vertex_id)
    return (alpha, distance)

source = sint.get_input_from(0)

n = 5
weights = sint.Matrix(n, n)
for i in range(n):
    for j in range(n):
        weights[i][j] = sint.get_input_from(1)


(alpha, distance) = dijkstra_optimized(weights, source)
test_print_vector_secret(alpha)
test_print_vector_secret(distance)
