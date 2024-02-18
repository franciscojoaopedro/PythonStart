word="string"

list_word=[]
for w in word:
    list_word.append(w)

list_word=[(w) for w in word]
list_word
y=20
list_2=[(x**2+y) for x in range(50) if x%2==0]
list_2