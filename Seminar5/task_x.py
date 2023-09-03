#code = {1:'222anton456',
#    2:'a1n1t1o1n1',
#    3:'0000a0000n00t00000o000000n',
#    4:'gylfole',
#    5:'richard',
#    6:'ant0n'}
#1 2 3
code = {1:'osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen',
    2:'anton',
    3:'aoooooooooontooooo',
    4:'elelelelelelelelelel',
    5:'ntoneeee',
    6:'tonee',
    7:'253235235a5323352n25235352t253523523235oo235523523523n',
    8:'antooooooooooooooooooooooooooooooooooooooootoooooooooooon',
    9:'unton'}
#1 2 7 8
virus = 'antton'
for k in range(1, len(code) + 1):
    s = code[k]
    res = ''
    for m in virus:
        if m in s:
            res = res + m
            s = s[s.find(m)+1:]
    if res == virus:
        print(k)
