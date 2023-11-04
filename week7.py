import threading
from pyDatalog import pyDatalog

# Define the father fact
pyDatalog.create_terms('father')
father('John', 'Bob')
father('Bob', 'Alice')
father('Bob', 'Charlie')
father('Charlie', 'David')

# Define a rule to find grandfathers
def grandfather(X, Z):
    Y = pyDatalog.Variable()
    father(X, Y) & father(Y, Z)
    
# Define PyDatalog variables for querying
X = pyDatalog.Variable()
Z = pyDatalog.Variable()

# Query for grandfathers
print("Grandfathers:")
print(grandfather(X, Z))
