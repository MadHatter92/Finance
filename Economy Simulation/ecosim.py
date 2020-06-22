import random
import matplotlib.pyplot as plt

N  = 50000 # Default size of the population
MU = 1000 # Default mean of the population
SIGMA = 200

population = [random.gauss(mu=MU, sigma=SIGMA) for _ in range(N)]

def gini(y):
    "Compute the Gini coefficient (a measure of equality/inequality) in a population, y."
    y = sorted(y)
    n = len(y)
    numer = 2 * sum((i+1) * y[i] for i in range(n))
    denom = n * sum(y)
    return (numer / denom) - (n + 1) / n

print gini(population)

def hist(population, label='pop', **kwargs):
    "A custom version of `hist` with better defaults."
    label = label + ': G=' + str(round(gini(population), 2))
    h = plt.hist(list(population), bins=30, alpha=0.5, label=label, **kwargs)
    plt.xlabel('wealth'); plt.ylabel('count'); plt.grid(True)
    plt.legend()
    plt.show()

hist(population)