import random

def dibujar(tablero):
	print('   |   |')
	print(' ' + tablero[7] + ' | ' + tablero[8] + ' | ' + tablero[9])
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(' ' + tablero[4] + ' | ' + tablero[5] + ' | ' + tablero[6])
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(' ' + tablero[1] + ' | ' + tablero[2] + ' | ' + tablero[3])
	print('   |   |')

def ingresaLetraJugador():
	letra = ''
	while not (letra == 'X' or letra == 'O'):
		print('¿Jugar con X o O?')
		letra = input().upper()
	if letra == 'X':
		return ['X', 'O']
	else:
		return ['O', 'X']

def quienComienza():
	# Elije al azar que jugador comienza.
	if random.randint(0, 1) == 0:
		return 'La computadora'
	else:
		return 'El jugador'

def jugarDeNuevo():
	print('¿Jugar de nuevo? (sí/no)?')
	return input().lower().startswith('s')

def hacerJugada(tablero, letra, jugada):
	tablero[jugada] = letra

def esGanador(ta, le):
	return ((ta[7] == le and ta[8] == le and ta[9] == le) or
		(ta[4] == le and ta[5] == le and ta[6] == le) or
		(ta[1] == le and ta[2] == le and ta[3] == le) or
		(ta[7] == le and ta[4] == le and ta[1] == le) or
		(ta[8] == le and ta[5] == le and ta[2] == le) or
		(ta[9] == le and ta[6] == le and ta[3] == le) or
		(ta[7] == le and ta[5] == le and ta[3] == le) or
		(ta[9] == le and ta[5] == le and ta[1] == le))

def obtenerDuplicadoTablero(tablero):
	lista = []
	for i in tablero:
		lista.append(i)
	return lista

def hayEspacioLibre(tablero, jugada):
	return tablero[jugada] == ' '

def obtenerJugadaJugador(tablero):
	jugada = ' '
	while jugada not in '1 2 3 4 5 6 7 8 9'.split() or not hayEspacioLibre(tablero, int(jugada)):
		print('¿Proximo movimiento? (1-9)')
		jugada = input()
	return int(jugada)

def elegirAzarDeLista(tablero, listaJugada):
	listaJugadasPosibles = []
	for i in listaJugada:
		if hayEspacioLibre(tablero, i):
			listaJugadasPosibles.append(i)
	if len(listaJugadasPosibles) != 0:
		return random.choice(listaJugadasPosibles)
	else:
		return None

def obtenerJugadaComputadora(tablero, letraComputadora):
	if letraComputadora == 'X':
		letraJugador = 'O'
	else:
		letraJugador = 'X'
	for i in range(1, 10):
		copia = obtenerDuplicadoTablero(tablero)
		if hayEspacioLibre(copia, i):
			hacerJugada(copia, letraComputadora, i)
			if esGanador(copia, letraComputadora):
				return i

	for i in range(1, 10):
		copia = obtenerDuplicadoTablero(tablero)
		if hayEspacioLibre(copia, i):
			hacerJugada(copia, letraJugador, i)
			if esGanador(copia, letraJugador):
				return i
	jugada = elegirAzarDeLista(tablero, [1, 3, 7, 9])
	if jugada != None:
		return jugada
	if hayEspacioLibre(tablero, 5):
		return 5
	return elegirAzarDeLista(tablero, [2, 4, 6, 8])

def Completo(tablero):
	for i in range(1, 10):
		if hayEspacioLibre(tablero, i):
			return False
	return True

print('¡Ta Te Ti!')
while True:
	panel = [' '] * 10
	letraJug, letraPc = ingresaLetraJugador()
	turno = quienComienza()
	print(turno + ' irá primero.')
	juegoEnCurso = True

	while juegoEnCurso:
		if turno == 'El jugador':
			# Turno del jugador
			dibujar(panel)
			jugada = obtenerJugadaJugador(panel)
			hacerJugada(panel, letraJug, jugada)

			if esGanador(panel, letraJug):
				dibujar(panel)
				print('¡Ganaste!')
				juegoEnCurso = False
			else:
				if Completo(panel):
					dibujar(panel)
					print('¡Empataron!')
					break
				else:
					turno = 'La computadora'
		else:
			# Turno de la computadora
			jugada = obtenerJugadaComputadora(panel, letraPc)
			hacerJugada(panel, letraPc, jugada)
			if esGanador(panel, letraPc):
				dibujar(panel)
				print('Perdiste, la maquina gana!')
				juegoEnCurso = False
			else:
				if Completo(panel):
					dibujar(panel)
					print('Empate!')
					break
				else:
					turno = 'El jugador'
	if not jugarDeNuevo():
		break
