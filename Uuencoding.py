Table_Value=['`','!','"','#','$','%','&',"'",'(',')','*','+',',','-','.','/','0','1','2','3','4','5','6','7','8','9',':',';','<','=','>','?','@','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','[',"¤",']','^','_']
def Uudecode(n):
    Data_Value=[]
    Bin_Value=[]
    Four_Bin=[]
    Three_Bin=[]
    Texte=[]
    Tx=""
    a=0
    for i in range (len(n)):
        for k in range (0,64):
            if n[i]==Table_Value[k]:
                Data_Value.append(k)
    for i in range (len(Data_Value)):
        bin=""
        a=Data_Value[i]
        for k in range (0,8):
            if a-2**(7-k)>=0:
                bin+="1"
                a-=2**(7-k)
            else:
                bin+="0"
        Bin_Value.append(bin)
    for i in range (int(len(Bin_Value)/4)):
        M=[]
        for k in range (0,4):
            M.append(Bin_Value[4*i+k])
        Four_Bin.append(M)
    for i in range (len(Four_Bin)):
        a=Four_Bin[i]
        Three_Bin.append(a[0])
        Three_Bin.append("00"+a[3][2]+a[3][3]+a[3][4]+a[3][5]+a[2][6]+a[2][7])
        Three_Bin.append(a[3])
        print (Three_Bin)
    for i in range (len(Three_Bin)):
        res=0
        a=Three_Bin[i]
        for k in range (len(a)):
            res+=int(a[k])*2**(7-k)
        Texte.append(res)
    print (Texte)
    for i in range (len(Texte)):
        a=int(Texte[i])
        Tx+=Table_Value[a]
    return Tx
