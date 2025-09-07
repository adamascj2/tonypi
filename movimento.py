import hiwonder.ActionGroupControl as AGC
import time
import readchar

texto = '''
Use as teclas
    w: Frente
    s: Tras
    a: Virar a esquerda
    d: Virar a direita
    ctrl+c: Sair
'''

def titulo():
    print("\033[H\033[J",end='')  # para limpar a tela
    print(texto)

try:
       
        
        titulo()
        while True:
            key = readchar.readkey()
            key = key.lower()
            if key in('wsad'):
                if 'w' == key:
                    AGC.runActionGroup('passofrente')

                elif 's' == key:
                   AGC.runActionGroup('passotras')

                elif 'a' == key:
                   AGC.runActionGroup('curvaesquerda')

                elif 'd' == key:
                   AGC.runActionGroup('curvadireita')

                 
                 
                titulo()
                time.sleep(0.5)
                AGC.runActionGroup('stand')
 

            elif key == readchar.key.CTRL_C:
                print("\n Sair")
                break

    except KeyboardInterrupt:    # Ctrl c para interromper
     	 AGC.runActionGroup('stand')
