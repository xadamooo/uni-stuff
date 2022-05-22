import gurobipy as gb
import random


n = 20
c = [random.randint(1, 32) for _ in range(0, n)]
a = [random.randint(1, 16) for _ in range(0, n)]
b = sum(a) / 2
model = gb.Model()
x = model.addVars(range(0, n), vtype=gb.GRB.BINARY, name='x')
model.setObjective(x.prod(c), gb.GRB.MAXIMIZE)
model.addConstr(x.prod(a) <= b, name='k')
model.optimize()
bp = {}
cost = 0
for i in range(0, len(c)):
    if model.x[i] == 1:
        isPacked = True
        cost += a[i]
    else:
        isPacked = False
    bp[f'item no.{i}'] = f'cost: {a[i]}, is packed: {isPacked}'
print("Optimal value:", model.ObjVal, "Cost:", cost, "Maximum allowed cost:", b)
#print(bp)
