from multiprocessing import Process, Array, Value
import time

turno_actual = Value('i',0)

def filosofo(tenedores,indice,turno_actual):
  print(f"Ya llegó el filósofo {indice}")
  n = len(tenedores)
  izq = tenedores[indice]
  der = tenedores[(indice+1)%n]
    
  while turno_actual.value != indice or izq == False or der == False:
     # Empecemos con la sección crítica
     pass
  izq = False
  der = False
  print(f"Comiendo el filósofo {indice} está...")
  time.sleep(5)
  print("Jummy Jummy")

  izq = True
  der = True
  print(f"'Que rico estuvo' dice  el filosofo {indice}")

  turno_actual.value = (turno_actual.value + 1)%n

def main():
  # Creamos los recursos compartidos tenedor y los turnos

  tenedores = Array('b',[True,True,True,True,True])
  n = len(tenedores)
  print(tenedores)

  
  F1 = Process(target = filosofo, args=(tenedores,0,turno_actual))
  F2 = Process(target = filosofo, args=(tenedores,1,turno_actual))
  F3 = Process(target = filosofo, args=(tenedores,2,turno_actual))
  F4 = Process(target = filosofo, args=(tenedores,3,turno_actual))
  F5 = Process(target = filosofo, args=(tenedores,4,turno_actual))
  
  F1.start()
  F3.start()
  F2.start()
  F4.start()
  F5.start()
  
main()
