#Criar movimentação do drone

direcao = ''
visao = ''
turn = ''
vis = ''

def mapeamento(d, v):
  global direcao
  global visao
  global turn
  direcao = d
  visao = v
  d = {'left', 'right', 'front', 'back'}
  v = {'left', 'right', 'up', 'down'}

direct = ''

def movimentacao():
  global direct
  global turn
  direct = input('Diga para onde deseja acelerar? (left, right, front, back): ')
  if direct == 'left':
    turn = 'Acelerando para esquerda'
    return turn
  elif direcao == 'right':
    turn = 'Acelrando para direita'
    return turn
  elif direct == 'front':
    turn = 'Acelerando para frente'
    return turn
  elif direct == 'back':
    turn = 'Acelerando para trás'
    return turn
  else:
    print('Não foi possível acelerar')

cam = ''
def camera():
  global cam
  global vis
  cam = input('Diga para onde deseja olhar? (left, right, up, down): ')
  if cam == 'left':
    vis = 'Olhando para esquerda'
    return vis
  elif cam == 'right':
    vis = 'Olhando para direita'
    return vis
  elif cam == 'up':
    vis = 'Olhando para cima'
    return vis
  elif cam == 'down':
    vis = 'Olhando para baixo'
    return vis
  else:
    print('Não foi possível olhar')

def acao():
  global turn
  global vis
  print('')
  return turn + " e " + vis 
  
  
  