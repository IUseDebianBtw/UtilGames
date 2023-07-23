import concurrent.futures

def calculate_term(i):
    return ((-1) ** i) / (2 * i + 1)

def calculate_pi(num_terms):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        terms = list(executor.map(calculate_term, range(num_terms)))
    return 4 * sum(terms)

# usage
num_terms = int(input("Enter the number of terms to use in the approximation: "))
print(calculate_pi(num_terms))
