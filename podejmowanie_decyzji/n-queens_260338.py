import gurobipy as gp
from gurobipy import GRB


n = 8

m = gp.Model("matrix2")

x = m.addMVar((n, n), vtype=GRB.BINARY, name="x")

m.setObjective(x.sum(), GRB.MAXIMIZE)

for i in range(n):

    m.addConstr(x[i, :].sum() <= 1, name="row"+str(i))

    m.addConstr(x[:, i].sum() <= 1, name="col"+str(i))

for i in range(1, 2*n):

    diagn = (range(max(0, i-n), min(n, i)), range(min(n, i)-1, max(0, i-n)-1, -1))
    m.addConstr(x[diagn].sum() <= 1, name="diag"+str(i))

    adiagn = (range(max(0, i-n), min(n, i)), range(max(0, n-i), min(n, 2*n-i)))
    m.addConstr(x[adiagn].sum() <= 1, name="adiag"+str(i))

m.optimize()

print(x.X)
print('Queens: %g' % m.ObjVal)
