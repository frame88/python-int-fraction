n = int(input('inserisci un numeratore: '))
d = int(input('inserisci un denominatore: '))

if n < d:
    print('frazione propria')

if n % d == 0:
    print ('frazione apparente')

if n>d and n%d!=0:
    print('frazione impropria')