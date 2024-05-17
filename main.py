drone = ''
controle = '' 
statuscontrole = ''
statusdrone = ''

def status():
  print('Status do controle:')
  global statuscontrole
  global statusdrone
  global controle
  if controle is True:
    statuscontrole = True
    print('Ligado')
  else:
    statuscontrole = False
    print('Desligado')
  print('Status do drone:')
  if drone is True:
    statusdrone = True
    print('Ligado')
  else:
    statusdrone = False
    print('Desligado')

def ligarcontrole():
  global controle
  controle = input('Deseja ligar o controle? (S/N): ')
  if controle.lower() == 's':
    controle = True
    print('Controle ligado')
  def ligardrone():
    global drone
    if controle is True:
      drone = input('Deseja ligar o drone? (S/N): ')
      if drone.lower() == 's':
        drone = True
        print('Ligando drone')
      else:
        drone = False
        print('Drone desligado')
    else:
      print('Controle desligado')
  ligardrone()
  print('')
  status()
  print('')

def desligardrone():
  global drone
  global statusdrone
  global controle
  if drone is True:
    controle = True
  desligar = ''
  if controle is True and drone is True:
    desligar = input('Deseja desligar o drone? (S/N): ')
    if desligar.lower() == 's':
      drone = False
      print('Desligando drone')
    else: 
      drone = True
  
  
  def desligarcontrole():
    global controle
    if controle is True:
      controle = input('Deseja desligar o controle? (S/N): ')
      if controle.lower() == 's':
        controle = False
        drone = False
        print('Desligando controle')
      else: 
        controle = True
        drone = True

  desligarcontrole()
  print('')
  status()
  print('')

ligarcontrole()
desligardrone()


import movimentação

print(movimentação.movimentacao())
print(movimentação.camera())
print(movimentação.acao())