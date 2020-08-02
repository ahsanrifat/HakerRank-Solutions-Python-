def split(word): 
    return [char for char in word]  
      
def merge_the_tools(string, k):
    n=len(string)
    each_word_length=k
    number_of_words=int(n/each_word_length)
    ti=list()
    start=0
    end=each_word_length
    for i in range(number_of_words):
        word=string[start:end]
        word=split(word)
        fword=list()
        match=dict()
        for c in word:
            if c not in match:
                match[c]=True
                fword.append(c)
        print(''.join(fword))
        start=end
        end=end+each_word_length

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)