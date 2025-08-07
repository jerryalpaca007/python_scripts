print("finding longest word and no of pallindromes using functions")
print("-----------------------------------------------------------\n")
def analyse(words):
    longest=""
    for word in words:
        if len(word)>len(longest):
            longest=word
    return longest
print("Input Data")
print("----------\n")
sentence=input('enter a sentence:')

def slist(sentence):
    words = []
    word = ""
    for char in sentence:
        if char.isalnum():
            word += char
        elif char.isspace() or char in ".,?!":
            if word != "":
                words.append(word)
                word = ""
    if word != "":
        words.append(word)
    return words
def cntpal(w_list):
    pcnt=0
    for word in word_list:
        is_pallindrome=True
        i=0
        j=len(word)-1
        while i<j:
            if word[i]!=word[j]:
                is_pallindrome=False
                break
            i+=1
            j-=1
        if is_pallindrome==True:
            pcnt+=1
    return pcnt
print('\nOutput Data')
print('-----------\n')
word_list=slist(sentence)
result=analyse(word_list)
pallindrome=cntpal(word_list)
print('Word list:',word_list)
print('The Longest word in the sentence is:',result)
print('Number of Pallindromes present in the sentence:',pallindrome)
