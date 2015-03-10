__author__ = 'Ghany'
import Orange.orange as orange
import Orange.statistics as statistics
import random
data = orange.ExampleTable("bridges")

# parametrisation
EXAMPLE_INSTANCES_CNT = 5
EXAMPLE_VARIABLE = 'PURPOSE'
SAMPLE_SIZE_PERCENTAGE = 8

# print some random Instances
print 'some random Instances:'
grCnt = len(data)/EXAMPLE_INSTANCES_CNT
for i in range(0, EXAMPLE_INSTANCES_CNT):
    print data[random.randrange(grCnt*i, grCnt*(i+1))]

# PURPOSE variable
#   possible values
for a in data.domain.attributes:
    if a.name == EXAMPLE_VARIABLE:
        print EXAMPLE_VARIABLE + ' values:'
        for val in a.values:
            print '- ', val

#   print distribution
distribution = data.domain[EXAMPLE_VARIABLE]
dist = statistics.distribution.Distribution(EXAMPLE_VARIABLE, data)
print EXAMPLE_VARIABLE + ' distribution:'
for i in range(len(distribution.values)):
    print '%s: %5.3f' % (distribution.values[i], dist[i])

# total number, name, mean and missing attributes grouped by VarType
nDisc = 0
nCont = 0
discList = []
contList = []
for a in data.domain.attributes:
    if a.varType == orange.VarTypes.Discrete:
        discList.append(a)
        nDisc += 1
    else:
        contList.append(a)
        nCont += 1
print 'total number of attributes: ', nDisc + nCont
print 'number of discrete: ', nDisc
print 'number of continuous: ', nCont

print 'Discrete:'
for disc in discList:
    d = [0] * 10
    missing = 0
    for e in data:
        if not e[disc].isSpecial():
            for a in data.domain.attributes:
                if a.name == disc.name:
                    i = 0
                    for find in a:
                        if find == e[disc]:
                            d[i] += 1
                            break
                        else:
                            i += 1
        else:
            missing += 1
    count = max(d)
    d = d.index(max(d))
    print "-  %s, mode = %s (%1.0f times), missing = %1.0f" % (disc.name, disc.values[d], count, missing)

print 'Continuous:'
for cont in contList:
    d = 0.
    n = 0
    for e in data:
        if not e[cont].isSpecial():
            d += e[cont]
            n += 1
        else:
            missing += 1
    print "-  %s, mean = %3.2f, missing = %1.0f" % (cont.name, d/n, missing)

# small sample
selection = orange.MakeRandomIndices2(data, SAMPLE_SIZE_PERCENTAGE/100.0)
sample = data.select(selection, 0)
print 'sample - %1.0f' % SAMPLE_SIZE_PERCENTAGE, '% of total'
for s in sample:
    print s