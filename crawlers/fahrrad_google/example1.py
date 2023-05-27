from gurobipy import *

model = Model("Rein & Sauber I")

x1 = model.addVar(lb=0, obj=1, vtype=GRB.CONTINUOUS, name="x1")
x2 = model.addVar(lb=0, ub=45, obj=2, vtype=GRB.CONTINUOUS, name="x2")

model.addConstr(3*x1 + 4*x2 <= 240)
model.addConstr(3*x1 + 2*x2 <= 180)

model.setAttr("ModelSense", GRB.MAXIMIZE)

model.update()
model.optimize()

print(model.objVal)
print(f"x = {x1.X}")
print(f"y = {x2.X}")
