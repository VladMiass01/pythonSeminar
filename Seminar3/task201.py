def summa(X, Z):
    point = 0
    for char_text in X:
        for k, v in Z.items():
            if Z[k].find(char_text) >= 0:
                point += k
            else:
                continue
    return point
    
eng = {1:'AEIOULNSTR',
       2:'DG',
	   3:'BCMP',
       4:'FHVWY',
       5:'K',
	   8:'JZ',
       10:'QZ'}
rus = {1:'АВЕИНОРСТ',
       2:'ДКЛМПУ',
       3:'БГЁЬЯ',
       4:'ЙЫ',
       5:'ЖЗХЦЧ',
       8:'ШЭЮ',
       10:'ФЩЪ'}
text = input('input text: ').upper()
print(text)
summa_rus = summa(text, rus)
summa_eng = summa(text, eng)
print(summa_eng + summa_rus)
