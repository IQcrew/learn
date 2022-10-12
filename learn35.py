myARR = {"a" : 23, "Y" : 2, "idk" : ["AA", "AAA", "AAAA", "AAAAA"], "T" : 5}




def idkARR(arr):
    for key in myARR:
        if True:
            try:
                for i in myARR[key]:
                    print(f"subitem - {i}")
            except:
                print(f"normal item - {key}  {myARR[key]}")
        else:
            print(f"normal item - {key}  {myARR[key]}")


idkARR(myARR)