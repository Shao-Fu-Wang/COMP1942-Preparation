a = [1, 1, 1, 0]
b = [1, 1, 0, 0]
c = [0, 0, 1, 1]
d = [0, 0, 0, 0, 0, 0]

ab = []
ac = []
ad = []
bc = []
bd = []
cd = []


tempsuma = 0
tempsumb = 0
tempsumc = 0
tempsumd = 0
tempsumx2 = 0

for i in range(len(a)):
    if(a[i] == b[i] == 1):
        tempsuma+=1
    if(a[i] == 0 and b[i] == 1):
        tempsumb+=1
    if(a[i] == 1 and b[i] == 0):
        tempsumc+=1
    if(a[i] == 0 and b[i] == 0):
        tempsumd+=1
tempsumx2 = pow(tempsuma*tempsumd-tempsumb*tempsumc, 2)*len(a)/((tempsuma+tempsumb)*(tempsuma+tempsumc)*(tempsumb+tempsumd)*(tempsumc+tempsumd)+0.000000000000000000000000000001)
ab.append(tempsuma)
ab.append(tempsumb)
ab.append(tempsumc)
ab.append(tempsumd)
ab.append(tempsumx2)
print('ab: ', ab)

#-------------------------------
tempsuma = 0
tempsumb = 0
tempsumc = 0
tempsumd = 0
tempsumx2 = 0
for i in range(len(a)):
    if(a[i] == c[i] == 1):
        tempsuma+=1
    if(a[i] == 0 and c[i] == 1):
        tempsumb+=1
    if(a[i] == 1 and c[i] == 0):
        tempsumc+=1
    if(a[i] == 0 and c[i] == 0):
        tempsumd+=1
tempsumx2 = pow(tempsuma*tempsumd-tempsumb*tempsumc, 2)*len(a)/((tempsuma+tempsumb)*(tempsuma+tempsumc)*(tempsumb+tempsumd)*(tempsumc+tempsumd)+0.00000000000000000001)
ac.append(tempsuma)
ac.append(tempsumb)
ac.append(tempsumc)
ac.append(tempsumd)
ac.append(tempsumx2)
print('ac: ', ac)

#-------------------------------
tempsuma = 0
tempsumb = 0
tempsumc = 0
tempsumd = 0
tempsumx2 = 0
for i in range(len(a)):
    if(a[i] == d[i] == 1):
        tempsuma+=1
    if(a[i] == 0 and d[i] == 1):
        tempsumb+=1
    if(a[i] == 1 and d[i] == 0):
        tempsumc+=1
    if(a[i] == 0 and d[i] == 0):
        tempsumd+=1
tempsumx2 = pow(tempsuma*tempsumd-tempsumb*tempsumc, 2)*len(a)/((tempsuma+tempsumb)*(tempsuma+tempsumc)*(tempsumb+tempsumd)*(tempsumc+tempsumd)+0.00000000000000000001)
ad.append(tempsuma)
ad.append(tempsumb)
ad.append(tempsumc)
ad.append(tempsumd)
ad.append(tempsumx2)
print('ad: ', ad)

#-------------------------------
tempsuma = 0
tempsumb = 0
tempsumc = 0
tempsumd = 0
tempsumx2 = 0
for i in range(len(a)):
    if(b[i] == d[i] == 1):
        tempsuma+=1
    if(b[i] == 0 and d[i] == 1):
        tempsumb+=1
    if(b[i] == 1 and d[i] == 0):
        tempsumc+=1
    if(b[i] == 0 and d[i] == 0):
        tempsumd+=1
tempsumx2 = pow(tempsuma*tempsumd-tempsumb*tempsumc, 2)*len(a)/((tempsuma+tempsumb)*(tempsuma+tempsumc)*(tempsumb+tempsumd)*(tempsumc+tempsumd)+0.00000000000000000001)
bd.append(tempsuma)
bd.append(tempsumb)
bd.append(tempsumc)
bd.append(tempsumd)
bd.append(tempsumx2)
print('bd: ', bd)
#-------------------------------
tempsuma = 0
tempsumb = 0
tempsumc = 0
tempsumd = 0
tempsumx2 = 0
for i in range(len(a)):
    if(b[i] == c[i] == 1):
        tempsuma+=1
    if(b[i] == 0 and c[i] == 1):
        tempsumb+=1
    if(b[i] == 1 and c[i] == 0):
        tempsumc+=1
    if(b[i] == 0 and c[i] == 0):
        tempsumd+=1
tempsumx2 = pow(tempsuma*tempsumd-tempsumb*tempsumc, 2)*len(a)/((tempsuma+tempsumb)*(tempsuma+tempsumc)*(tempsumb+tempsumd)*(tempsumc+tempsumd)+0.00000000000000000001)
bc.append(tempsuma)
bc.append(tempsumb)
bc.append(tempsumc)
bc.append(tempsumd)
bc.append(tempsumx2)
print('bc: ', bc)

#-------------------------------
tempsuma = 0
tempsumb = 0
tempsumc = 0
tempsumd = 0
tempsumx2 = 0
for i in range(len(a)):
    if(c[i] == d[i] == 1):
        tempsuma+=1
    if(c[i] == 0 and d[i] == 1):
        tempsumb+=1
    if(c[i] == 1 and d[i] == 0):
        tempsumc+=1
    if(c[i] == 0 and d[i] == 0):
        tempsumd+=1
tempsumx2 = pow(tempsuma*tempsumd-tempsumb*tempsumc, 2)*len(a)/((tempsuma+tempsumb)*(tempsuma+tempsumc)*(tempsumb+tempsumd)*(tempsumc+tempsumd)+0.00000000000000000001)
cd.append(tempsuma)
cd.append(tempsumb)
cd.append(tempsumc)
cd.append(tempsumd)
cd.append(tempsumx2)
print('cd: ', cd)




        