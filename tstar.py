# Revised version of Python3 Turtle Example from:
# https://docs.python.org/3.3/library/turtle.html
#
# Brython Turtle does not currently support Vec2D so 
# the abs() implementation on position does not work

from brythonserver.turtle import *

color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
