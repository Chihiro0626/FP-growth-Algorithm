import fpgrowth
import time


#simple data

simDat = fpgrowth.loadSimpDat()
initSet = fpgrowth.createInitSet(simDat)
myFPtree, myHeaderTab = fpgrowth.createFPtree(initSet, 3)
myFPtree.disp()        #FP树

print(fpgrowth.findPrefixPath('z', myHeaderTab))
print(fpgrowth.findPrefixPath('r', myHeaderTab))
print(fpgrowth.findPrefixPath('x', myHeaderTab))

freqItems = []
fpgrowth.mineFPtree(myFPtree, myHeaderTab, 3, set([]), freqItems)
for x in freqItems:
     print(x)

     



#kosarak data
'''
start = time.time()
n = 100000
with open("H:/data/kosarak.dat/kosarak.dat", "rb") as f:
    parsedDat = [line.split() for line in f.readlines()]
initSet = fpgrowth.createInitSet(parsedDat)
myFPtree, myHeaderTab = fpgrowth.createFPtree(initSet, n)
myFPtree.disp()
freqItems = []
fpgrowth.mineFPtree(myFPtree, myHeaderTab, n,set([]), freqItems)
for x in freqItems:
    print(x)
print(time.time()-start, 'sec')
'''


'''
# compute support values of freqItems
suppData = fpgrowth.calSuppData(myHeaderTab, freqItems, len(parsedDat))
suppData[frozenset([])] = 1.0
for x,v in suppData.iteritems():
    print(x,v)

freqItems = [frozenset(x) for x in freqItems]
fpgrowth.generateRules(freqItems, suppData)
'''