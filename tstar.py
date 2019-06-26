# Revised version of Python3 Turtle Example from:
# https://docs.python.org/3.3/library/turtle.html
#
# Brython Turtle does not currently support Vec2D so 
# the abs() implementation on position does not work

from brythonserver.turtle import *

def abs(v):
    return (v[0]**2 + v[1]**2)**0.5

color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
