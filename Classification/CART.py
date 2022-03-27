import math

err = 0.000000000000000000000000000000001

while(1):
    totalInfo = float(input("The Target split: "))
    firstInfo = float(input("T_one: "))
    secondInfo = float(input("T_two: "))
    attrSplit = float(input("The attribute split(T_one_portion): "))
    totalInfo = 1 - pow(totalInfo, 2) - pow(1-totalInfo, 2)
    firstInfo = 1 - pow(firstInfo, 2) - pow(1-firstInfo, 2)
    secondInfo = 1 - pow(secondInfo, 2) - pow(1-secondInfo, 2)
    attrInfo = attrSplit*firstInfo + (1-attrSplit)*secondInfo
    Cartgain = totalInfo - attrInfo
    print("\ntotalInfo: ", totalInfo)
    print("firstInfo: ",  firstInfo)
    print("secondInfo: ", secondInfo)
    print("attrInfo: ", attrInfo)
    print("CART gain: ", Cartgain)
    print()