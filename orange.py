__author__ = 'Ghany'
import Orange.orange as orange
import Orange
import random
data = orange.ExampleTable("bridges")

# parametrisation
EXAMPLE_INSTANCES_CNT = 5
EXAMPLE_VARIABLE = 'PURPOSE'

# print some random Instances
grCnt = len(data)/EXAMPLE_INSTANCES_CNT
for i in range(0,EXAMPLE_INSTANCES_CNT):
    print data[random.randrange(grCnt*i, grCnt*(i+1))]

# PURPOSE variable
## possible values
for a in data.domain.attributes:
    if a.name == EXAMPLE_VARIABLE:
        print EXAMPLE_VARIABLE + ' values:'
        for val in a.values:
            print "- " + val

## print distribution
distribution = data.domain[EXAMPLE_VARIABLE]
disc = Orange.statistics.distribution.Distribution(EXAMPLE_VARIABLE, data)
print EXAMPLE_VARIABLE + ' distribution:'
for i in range(len(distribution.values)):
    print "%s: %5.3f" % (distribution.values[i], disc[i])