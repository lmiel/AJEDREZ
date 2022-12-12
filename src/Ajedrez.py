file = open("Partida_ajedrez.txt","w+",encoding='UTF-8')

fichas=     [['♜',	'♞',	'♝',	'♛',   '♚', 	'♝', 	'♞', 	'♜'],
            ['♟',	'♟',	'♟',	'♟',   '♟', 	'♟', 	'♟', 	'♟'],
            [' ',	' ',	' ',	' ',   ' ', 	' ', 	' ', 	' '],
            [' ',	' ',	' ',	' ',   ' ', 	' ', 	' ', 	' '],
            [' ',	' ',	' ',	' ',   ' ', 	' ', 	' ', 	' '],
            [' ',	' ',	' ',	' ',   ' ', 	' ', 	' ', 	' '],
            ['♙',	'♙',	'♙',	'♙',   '♙', 	'♙', 	'♙', 	'♙'],
            ['♖',	'♘',	'♗',	'♕',   '♔', 	'♗', 	'♘', 	'♖']]

def draw_tablero():
    for fila in fichas:
        print(fila)


def save_tablero():
    for fila in fichas:
        filastr = ""
        for element in fila:
            filastr=filastr+element
        filastr=filastr+'\n'
        file.write(filastr)
    file.write('\n'+'----------------'+'\n'+'\n')
    

def move_ficha(posact_ficha, posnext_ficha):
    #borro lo q haya en la posnext (sobreescribirlo) y pongo la pieza de posact en esa posnext, luego borro la pieza que haya en posact    
    #coordenada horizontal: A,B,C,D,E,F,G,H y coordenada vertical: 1,2,3,4,5,6,7,8
    columna = {"A" : 0, "B" : 1, "C" : 2, "D" : 3, "E" : 4, "F" : 5, "G" : 6, "H" : 7}
    fichas[8-int(posnext_ficha[1])][columna.get(posnext_ficha[0])]=fichas[8-int(posact_ficha[1])][columna.get(posact_ficha[0])]
    fichas[8-int(posact_ficha[1])][columna.get(posact_ficha[0])]=" "

def bucle_game():
    while input("Quieres seguir jugando? (s/n): ") == "s":
        draw_tablero()
        save_tablero()
        posincial_ficha = input("Introduzca la posicion de la pieza que quiere mover (EJ:A2): ")
        posfinal_ficha = input("Introduzca la posicion donde quiere mover la pieza (EJ:A4): ")
        move_ficha(posincial_ficha,posfinal_ficha)
        draw_tablero()
        save_tablero()
    file.close()


