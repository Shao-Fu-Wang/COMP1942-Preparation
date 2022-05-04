import math

err = 0.000000000000000000000000000000001

while(1):
    totalInfo = float(input("The Target split: "))
    firstInfo = float(input("T_one: "))
    secondInfo = float(input("T_two: "))
    attrSplit = float(input("The attribute split(T_one_portion): "))
    totalInfo = totalInfo*-math.log2(totalInfo+err)-(1-totalInfo)*math.log2(1-totalInfo+err)
    firstInfo = firstInfo*-math.log2(firstInfo+err)-(1-firstInfo)*math.log2(1-firstInfo+err)
    secondInfo = secondInfo*-math.log2(secondInfo+err)-(1-secondInfo)*math.log2(1-secondInfo+err)
    attrInfo = attrSplit*firstInfo + (1-attrSplit)*secondInfo
    splitInfo = attrSplit*-math.log2(attrSplit+err)-(1-attrSplit)*math.log2(1-attrSplit+err)
    ID3gain = totalInfo - attrInfo
    C45gain = ID3gain/(splitInfo+err)
    print()
    print("totalInfo: ", totalInfo)
    print("firstInfo: ",  firstInfo)
    print("secondInfo: ", secondInfo)
    print("attrInfo: ", attrInfo)
    print("ID3 gain: ", ID3gain)
    print("splitInfo: ", splitInfo)
    print("C4.5 gain: ", C45gain)
    print()