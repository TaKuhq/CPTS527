import os
def question1():
    str_raw = input("Please enter the Ciphertext：")
    k = int(input("Please enter the Shift："))
    str_change = str_raw.lower()
    str_list = list(str_change)
    str_list_decry = str_list
    i = 0
    while i < len(str_list):
        if ord(str_list[i]) >= 97+k:
            str_list_decry[i] = chr(ord(str_list[i]) - k)
        else:
            str_list_decry[i] = chr(ord(str_list[i]) + 26 - k)
        i = i+1
    print ("Answer is "+"".join(str_list_decry))




def question2():
    # statistical frequency
    c_file = open('question2.txt') 
    c_text = c_file.read().replace('?',' ')
    char_list = list(c_text)

    tempSet = set(char_list)

    # Save as a dictionary, key: letter, value: number of occurrences
    tempDict = {}
    for i in tempSet:
        tempDict[i] = char_list.count(i)

    # List sorting, in the form of tuples
    dict_sorted = sorted(tempDict.items(), key=lambda x: x[1], reverse=True)
    # print(dict_sorted)
    frequency_list = []
    print("Letter", "Times", "Frequency")
    for i in dict_sorted:
        print(i[0], "\t", i[1], "\t", i[1] / len(c_text))
        frequency_list.append(i[0]) 

    fp = open('question2new.txt','w')
    table = {'A':'i','B':'j','C':'k','D':'d','E':'g','F':'l','G':'m','H':'n','I':'e','J':'o','K':'p','L':'z','M':'r','N':'c','O':'s','P':'t','Q':'u','R':'h','S':'a','T':'v','U':'b','V':'f','W':'w','X':'x','Y':'y','Z':'q'}
    for key,value in table.items():
        c_text =  c_text.replace(key,value)
    fp.write(c_text)
    fp.close()


def question3():
    # the alphabet
    letter_list='ABCDEFGHIJKLMNOPQRSTUVWXYZ'    
    # Generate a list of keys based on the keys you entered
    key_list=[]
    key=input("Please enter key:")
    for ch in key:
        key_list.append(ord(ch.upper())-65)

    plaintext=""
    ciphertext=input("Please enter the ciphertext:")
    i=0
    for ch in ciphertext: #Traverse the ciphertext
        if 0==i%len(key_list):
            i=0
        if ch.isalpha():
            if ch.isupper():
                plaintext+=letter_list[(ord(ch)-65-key_list[i]) % 26]
                i+=1
            else:
                plaintext+=letter_list[(ord(ch)-97-key_list[i]) % 26].lower()
                i+=1
        else:
            plaintext+=ch
    print("Plaintext:%s" % plaintext)



if __name__ == "__main__":
    question1()
    question2()      
    question3()