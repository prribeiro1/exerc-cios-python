from time import sleep

print('\033[34m'+'Olá, eu sou o\033[0;0m \033[94m'+'DDT1-V\033[0;0m')

print('''


  .OOOOOOOOOOOOOOO @@                                   @@ OOOOOOOOOOOOOOOO.
  OOOOOOOOOOOOOOOO @@                                    @@ OOOOOOOOOOOOOOOO
  OOOOOOOOOO'''''' @@                                    @@ ```````OOOOOOOOO
  OOOOO'' aaa@@@@@@@@@@@@@@@@@@@@"""                   """""""""@@aaaa `OOOO
  OOOOO,""""@@@@@@@@@@@@@@""""                                     a@"" OOOA
  OOOOOOOOOoooooo,                                            |OOoooooOOOOOS
  OOOOOOOOOOOOOOOOo,                                          |OOOOOOOOOOOOC
  OOOOOOOOOOOOOOOOOO                                         ,|OOOOOOOOOOOOI
  OOOOOOOOOOOOOOOOOO @                                       |OOOOOOOOOOOOOI
  OOOOOOOOOOOOOOOOO'@                                        OOOOOOOOOOOOOOb
  OOOOOOOOOOOOOOO'a'                                         |OOOOOOOOOOOOOy
  OOOOOOOOOOOOOO''                                         aa`OOOOOOOOOOOP
  OOOOOOOOOOOOOOb,..                                          `@aa``OOOOOOOh
  OOOOOOOOOOOOOOOOOOo                                           `@@@aa OOOOo
  OOOOOOOOOOOOOOOOOOO|                                             @@@ OOOOe
  OOOOOOOOOOOOOOOOOOO@                               aaaaaaa       @@',OOOOn
  OOOOOOOOOOOOOOOOOOO@                        aaa@@@@@@@@""        @@ OOOOOi
  OOOOOOOOOO~~ aaaaaa"a                 aaa@@@@@@@@@@""            @@ OOOOOx
  OOOOOO aaaa@"""""""" ""            @@@@@@@@@@@@""               @@@|`OOOO'
  OOOOOOOo`@@a                  aa@@  @@@@@@@""         a@        @@@@ OOOO9
  OOOOOOO'  `@@a               @@a@@   @@""           a@@   a     |@@@ OOOO3
  `OOOO'       `@    aa@@       aaa"""          @a        a@     a@@@',OOOO'
''')


print('\033[34m'+'sou o detetive encarregado desse caso e conto com sua colaboração para solucioná-lo\033[0;0m\n')
sleep(1)
print('\033[91m'+'Vamos às perguntas então:\033[0;0m')
sleep(1)
print('\033[94m'+'PROCESSANDO...\033[0;0m\n\n')
sleep(2)




p1 = input('Você telefonou para a vítima? [sim/não] ').lower().strip()
p2 = input('Você esteve no local do crime? [sim/não] ').lower().strip()
p3 = input('Você mora perto da vítima? [sim/não] ').lower().strip()
p4 = input('Você devia para a vítima? [sim/não] ').lower().strip()
p5 = input('Você já trabalhou com a vítima? [sim/não] ').lower().strip()

count = 0

if p1 == 'sim':
  count += 1
if p2 == 'sim':
  count += 1
if p3 == 'sim':
  count +=  1
if p4 == 'sim':
  count += 1
if p5 == 'sim':
  count += 1

if count == 2:
  print('\033[33m'+'Suspeita\033[0;0m')
elif count == 3 or count == 4:
    print('\033[31m'+'Cúmplice\033[0;0m')
elif count == 5:
    print('\033[91m'+'Assassino\n\nVocê está preso!!\033[0;0m')
    print('''     ___________________
     ||   ||     ||   ||
     ||   ||, , ,||   ||
     ||  (||/|/(\||/  ||
     ||  ||| _'_`|||  ||
     ||   || o o ||   ||
     ||  (||  - `||)  ||
     ||   ||  =  ||   ||
     ||   ||\___/||   ||
     ||___||) , (||___||
    /||---||-\_/-||---||''')
else:
    print('\033[34m'+'inocente\033[0;0m')