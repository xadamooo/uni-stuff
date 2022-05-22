import math
import random
from itertools import combinations
import gurobipy as gp
from gurobipy import GRB


#przygotowywanie danych

n = 10
random.seed(2)
points = [(random.randint(0, 100), random.randint(0, 100)) for i in range(n)]
dist = {(i, j):
        math.sqrt(sum((points[i][k]-points[j][k])**2 for k in range(2)))
        for i in range(n) for j in range(i)}
m = gp.Model()


#ograniczenia modelu(najkrotsza droga przy kazdej iteracji i droga do
#nastepnego wierzcholka musi byc conajmnniej dlugosci 1 (wykluczenie samego siebie))


def subtourelim(model, where):
    if where == GRB.Callback.MIPSOL:
        vals = model.cbGetSolution(model._vars)
        selected = gp.tuplelist((i, j) for i, j in model._vars.keys()
                                if vals[i, j] > 0.5)
        tour = subtour(selected)
        if len(tour) < n:
            model.cbLazy(gp.quicksum(model._vars[i, j]
                                     for i, j in combinations(tour, 2))
                         <= len(tour)-1)


def subtour(edges):
    unvisited = list(range(n))
    cycle = range(n+1)
    while unvisited:
        thiscycle = []
        neighbors = unvisited
        while neighbors:
            current = neighbors[0]
            thiscycle.append(current)
            unvisited.remove(current)
            neighbors = [j for i, j in edges.select(current, '*')
                         if j in unvisited]
        if len(cycle) > len(thiscycle):
            cycle = thiscycle
    return cycle


#krawedz ma 2 zwroty co trzeba uwzglednic

vars = m.addVars(dist.keys(), obj=dist, vtype=GRB.BINARY, name='e')
for i, j in vars.keys():
    vars[j, i] = vars[i, j]
m.addConstrs(vars.sum(i, '*') == 2 for i in range(n))


#optymalizacja
m._vars = vars
m.Params.lazyConstraints = 1
m.optimize(subtourelim)

vals = m.getAttr('x', vars)
selected = gp.tuplelist((i, j) for i, j in vals.keys() if vals[i, j] > 0.5)

tour = subtour(selected)
#sprawdzenie czy przeszlismy wszystkie wierzcholki
assert len(tour) == n

print('')
print('Optimal tour: %s' % str(tour))
print('Optimal cost: %g' % m.objVal)
print('')
