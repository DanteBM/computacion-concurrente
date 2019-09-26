from multiprocessing import Process, Value
import time



def filosofo(tenedores, indice):
  print(f"Ya llegó el filósofo {indice}")
  
  while tenedores.value < 2:
     # Empecemos con la sección crítica
     pass
  tenedores.value -= 2
  print(f"Comiendo el filósofo {indice} está...")
  time.sleep(5)
  print("Jummy Jummy")

  print(f"'Que rico estuvo' dice  el filosofo {indice}")
  tenedores.value += 2
  
def main():
  tenedores = Value('i', 5) 
  F1 = Process(target = filosofo, args=(tenedores,0))
  F2 = Process(target = filosofo, args=(tenedores,1))
  F3 = Process(target = filosofo, args=(tenedores,2))
  F4 = Process(target = filosofo, args=(tenedores,3))
  F5 = Process(target = filosofo, args=(tenedores,4))
  
  F1.start()
  F3.start()
  F2.start()
  F4.start()
  F5.start()

main()



