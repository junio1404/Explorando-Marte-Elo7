import sys
import math
class Cords():
    pos=[]
    direcao=0
    limX=0
    limY=0
    pos_finalX=[]
    pos_finalY=[]
    dir_final=[]
cord = Cords()
direcoes = {'E': 360, 'W': 180, 'N': 90, 'S': 270}
ang = 0
x = 0
y = 0
def movimentoSonda( string ):
    for caractere in string:
        if caractere.upper() == 'L':
            cord.direcao += 90
        elif caractere.upper() == 'R':
            cord.direcao -= 90

        elif caractere.upper() == 'M':
            ang = cord.direcao
            ang = (ang * 2 * math.pi)/360
            cord.pos[0] += int(math.cos(ang))
            if cord.pos[0] > cord.limX:
                cord.pos[0] = cord.limX
            elif cord.pos[0] < 0:
                cord.pos[0] = 0

            cord.pos[1] += int(math.sin(ang))
            if cord.pos[1] > cord.limY:
                cord.pos[1] = cord.limY
            if cord.pos[1] < 0:
                cord.pos[1] = 0
        cord.direcao %= 360
        if cord.direcao < 0:
            cord.direcao += 360
def exibipos():
    dirName = ("E", "N", "W", "S")
    print(" ")
    for i in range(0, numsondas):
        print("%d %d %s" %(cord.pos_finalX.pop(0), cord.pos_finalY.pop(0), dirName[ int((cord.dir_final.pop(0))/90)]))
    input("\nENTER para sair")
    return True
def sondas():
    global numsondas
    numsondas = 2
    for n in range(0, numsondas):
        x, y, d = input("X[%d] Y[%d] D[%d]:  " %((n+1),(n+1),(n+1))).split(" ")
        try:
            int(x)
            int(y)
            cord.direcao = direcoes[d]
            cord.pos = [int(x),int(y)]
            if ((cord.pos[0] > cord.limX) or (cord.pos[1] > cord.limY)):
                print("\nInválida, há algo fora do esperado!")
                input("\nPENTER para sair")
                return False
        except:
            print("\nInválida")
            input("\nPENTER para sair")
            return False
        string = input("Direções da %d Sonda: " %(n+1))
        movimentoSonda(string)
        cord.pos_finalX.insert(n, cord.pos[0])
        cord.pos_finalY.insert(n, cord.pos[1])
        cord.dir_final.insert(n, cord.direcao)
    exibipos()
def main():
    print(" \n\n ")
    print("Exploração Marte Elo 7")
    print(" \n\n ")
    limX, limY = input("Coordenada do ponto superior direito: ").split(" ")
    try:
        int(limX)
        int(limY)
        cord.limX = int( limX )
        cord.limY = int( limY )
    except:
        print("\nEntrada inválida")
        input("\nPressione ENTER para sair")
        return False
    sondas()
if __name__ == '__main__': main()