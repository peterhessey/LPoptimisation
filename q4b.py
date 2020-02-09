import pulp as lp

problem = lp.LpProblem('q4a', lp.LpMaximize)

# objective function variables
A = lp.LpVariable('A_object', lowBound=0, upBound=1, cat=lp.LpInteger)
B = lp.LpVariable('B_object', lowBound=0, upBound=1, cat=lp.LpInteger)
C = lp.LpVariable('C_object', lowBound=0, upBound=1, cat=lp.LpInteger)
D = lp.LpVariable('D_object', lowBound=0, upBound=1, cat=lp.LpInteger)
E = lp.LpVariable('E_object', lowBound=0, upBound=1, cat=lp.LpInteger)
F = lp.LpVariable('F_object', lowBound=0, upBound=1, cat=lp.LpInteger)

# objective function
problem += 60*A + 70*B + 40*C + 70*D + 16*E + 100*F

# constraints
problem += 6*A + 7*B + 4*C + 9*D + 3*E + 8*F <= 20
problem += D - C >= 0

# solve problem
problem.solve()

for variable in problem.variables():
    print('%s = %s' % (variable.name, variable.varValue))

print('Total value of items: %s' % lp.value(problem.objective))
print('Problem status: %s' % lp.LpStatus[problem.status])