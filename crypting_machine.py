import random
from functools import reduce

def encrypt(input_str: str, key = None) -> str:
    """
    Return encrypt given string\n
    [ hasKey ] is option for generate encrypt key
    """
    temp_lst = [ ord(i)-32 for i in list(input_str)]
    if key != None:   
        key = [random.randrange(1,95) for i in range(21)] if key==True else key
        temp_key = int(reduce(lambda x,y : x*y, key[8:12])%10000+5000)
        temp_key = temp_key if temp_key%2==0 else temp_key+1
        for i in range(len(temp_lst)):
            temp_lst[i] = ( temp_lst[i] + ((i%(((key[0]*key[1])%99+1)+(key[2]*key[3]) %99+1))**(i%((key[4]*key[5])%99+1)+(key[6]*key[7])%99+1))%(temp_key-temp_key/2)+9500)%95
        index_shift = key[12]%11+1
        i = 1
        while True:
            temp_rand = random.randrange(95)
            temp_lst.insert(i,temp_rand)
            i += 1 
            while temp_rand % 2 == 0:
                temp_rand = random.randrange(95)
                temp_lst.insert(i,temp_rand)
                i += 1
            i += index_shift
            if i > len(temp_lst):
                break

        for i in range(len(temp_lst)): 
            for x in [-2,-1,1,2]:
                try:
                    if i+x<1:
                        raise
                    temp_lst[i+x] =  (temp_lst[i+x]+((i%(((key[13]*key[14])%99+1)+(key[15]*key[16]) %99+1))**(i%((key[17]*key[18])%99+1)+(key[19]*key[20])%99+1))%(temp_key-temp_key/2)+9500)%95
                except:
                    pass


        return ["".join(map(lambda x : chr(x+32), key)), "".join(map(lambda x : chr(int(x)+32), temp_lst))]
        
    else:
        for i in range(len(temp_lst)):
            temp_lst[i] = (temp_lst[i]+(((i%20)**(i%30))%10000-5000)+9500)%95
        rand_char = random.randrange(95)
        temp_lst.insert(0, rand_char)
        index_shift = reduce(lambda x,y: int(x)+int(y), [0]+list(str(rand_char)))%11+1
        i = 1
        while True:
            temp_rand = random.randrange(95)
            temp_lst.insert(i,temp_rand)
            i += 1
            while temp_rand % 2 == 0:
                temp_rand = random.randrange(95)
                temp_lst.insert(i,temp_rand)
                i += 1
            i += index_shift
            if i > len(temp_lst):
                break
        for i in range(len(temp_lst)): 
            for x in [-2,-1,1,2]:
                try:
                    if i+x<1:
                        raise
                    temp_lst[i+x] =  (temp_lst[i+x]+((i%40)**(abs(x)*i%20)+temp_lst[i-3]))%95
                except:
                    pass

        
    return "".join(map(lambda x : chr(x+32), temp_lst))
        # 33 - 126
        #  0 - 94


def decrypt(input_str: str, decrypt_key: str = "") -> str:
    """
    decrypt given string
    """
    temp_lst = [ ord(i)-32 for i in list(input_str)]
    
    if decrypt_key != "":
        key = [ord(i)-32 for i in decrypt_key]
        temp_key = (reduce(lambda x,y : x*y, key[8:12])%10000+5000)
        temp_key = temp_key if temp_key%2==0 else temp_key+1
        for i in range(len(temp_lst)-1, -1, -1): 
            for x in [2,1,-1,-2]:
                try:
                    if i+x<1:
                        raise
                    temp_lst[i+x] = (temp_lst[i+x]-((i%(((key[13]*key[14])%99+1)+(key[15]*key[16]) %99+1))**(i%((key[17]*key[18])%99+1)+(key[19]*key[20])%99+1))%(temp_key-temp_key/2)+9500)%95
                except:
                    pass
        index_shift = key[12]%11+1
        i = 1
        while True:
            try:
                temp_rand = temp_lst.pop(i)
                while temp_rand % 2 == 0:
                    temp_rand = temp_lst.pop(i)
                i += index_shift
            except:
                break
        for i in range(len(temp_lst)):
            temp_lst[i] = ( temp_lst[i] - ((i%(((key[0]*key[1])%99+1)+(key[2]*key[3]) %99+1))**(i%((key[4]*key[5])%99+1)+(key[6]*key[7])%99+1))%(temp_key-temp_key/2)+9500)%95
        return "".join(map(lambda x : chr(int(x)+32), temp_lst))
    else:
        for i in range(len(temp_lst)-1, -1, -1):
            for x in [2,1,-1,-2]:
                try:
                    if i+x<1:
                        raise
                    temp_lst[i+x] = (temp_lst[i+x]-((i%40)**(abs(x)*i%20)+temp_lst[i-3]))%95
                except:
                    pass

        index_shift = reduce(lambda x,y: int(x)+int(y), [0]+list(str(temp_lst.pop(0))))%11+1
        i = 0
        while True:
            try:
                temp_rand = temp_lst.pop(i)
                while temp_rand % 2 == 0:
                    temp_rand = temp_lst.pop(i)
                i += index_shift
            except:
                break
            
        for i in range(len(temp_lst)):
            temp_lst[i] = (temp_lst[i]-(((i%20)**(i%30))%10000-5000)+9500)%95


    return "".join(map(lambda x : chr(x+32), temp_lst))


if __name__ == "__main__":
    user_input = input('Enter string to crypt: ')
    print("encrypted: ÷")
    print(encrypt(user_input))
    print("÷decrypted: ")
    print(decrypt(user_input))