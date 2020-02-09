import pulp as lp

problem =  lp.LpProblem('q3', lp.LpMaximize)

# variables for objective function
red = lp.LpVariable('Red paint', lowBound=0)
green = lp.LpVariable('Green paint', lowBound=0)
blue = lp.LpVariable('Blue paint', lowBound=0)
black = lp.LpVariable('Black paint', lowBound=0)

# constraint variables
y_red = lp.LpVariable('Yellow paint used to make red paint', lowBound=0)
y_green = lp.LpVariable('Yellow paint used to make green paint', lowBound=0)
y_black = lp.LpVariable('Yellow paint used to make black paint', lowBound=0)

m_red = lp.LpVariable('Magenta paint used to make red paint', lowBound=0)
m_blue = lp.LpVariable('Magenta paint used to make blue paint', lowBound=0)
m_black = lp.LpVariable('Magenta paint used to make black paint', lowBound=0)

c_green = lp.LpVariable('Cyan paint used to make green paint', lowBound=0)
c_blue = lp.LpVariable('Cyan paint used to make blue paint', lowBound=0)
c_black = lp.LpVariable('Cyan paint used to make black paint', lowBound=0)


# objective function
problem += 10 * red + 15 * green + 25 * blue + 25 * black

# constraints
problem += red == y_red + m_red
problem += green == y_green + c_green
problem += blue == m_blue + c_blue
problem += black == y_black + m_black + c_black

problem += y_red + y_green + y_black <= 11
problem += m_red + m_blue + m_black <= 5
problem += c_green + c_blue + c_black <= 10

problem += y_red == m_red
problem += y_green == c_green
problem += m_blue == c_blue
problem += y_black == m_black
problem += m_black == c_black

# solve problem
problem.solve()

for variable in problem.variables():
    print('%s = %s' % (variable.name, variable.varValue))


print('Total income: %s' % lp.value(problem.objective))
print('Problem status: %s' % lp.LpStatus[problem.status])