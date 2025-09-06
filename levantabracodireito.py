 
import time
 
import hiwonder.ActionGroupControl as AGC

print("Iniciando o programa para levantar o braço direito...")

try:
     
    print("Iniciando na posição de stand...")
    AGC.runActionGroup('stand')
    time.sleep(2)

    # Move o servo do braço direito para cima
    AGC.runActionGroup('levantabraco')
    time.sleep(2)  # Mantém o braço na posição por 2 segundos

    # Retorna o braço para a posição inicial
    AGC.runActionGroup('stand')

    time.sleep(1)

    print("Programa concluído.")

except KeyboardInterrupt:    # Ctrl c para interromper
	 
	 
    AGC.runActionGroup ('stand')

    print("Programa fechado.")


