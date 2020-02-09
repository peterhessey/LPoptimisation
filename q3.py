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