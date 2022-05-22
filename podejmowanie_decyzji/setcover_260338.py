import gurobipy as gb


setIndex, elements = gb.multidict({
  0: [{0, 1, 1}],
  1: [{1, 1, 1}],
  2: [{2, 1, 1}],
  3: [{2, 3, 4}],
  4: [{1, 3, 4}],
  5: [{1, 4, 5}],
  6: [{1, 2, 6}],
  7: [{1, 2, 7}],
})


L = setIndex
m = gb.Model()
x = m.addVars(len(setIndex), vtype=gb.GRB.BINARY)
m.addConstrs(gb.quicksum(x[k] for k, i in elements.items() if j in i) >= 1 for j in setIndex)
m.setObjective(gb.quicksum(x[i] for i in setIndex), gb.GRB.MINIMIZE)
m.optimize()


isChosen = {i: x[i].x for i in range(len(L))}
print(isChosen)
chosenSet = [elements[k] for k, v in isChosen.items() if v]
print(chosenSet)
