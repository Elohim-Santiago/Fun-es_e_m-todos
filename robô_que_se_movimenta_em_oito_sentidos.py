
def linha():
    print("_"*30)
while True:

    coord_x = input("Informe a coordenada X: ")
    coord_y = input("Informe a coordenada y: ")    
    coord_x2 = int (coord_x)
    coord_y2 = int (coord_y)
    cont = 0
    continuar = "sim"
    linha()
    
    while True:
        print("Para Cima -> U")
        print("Para Baixo -> D")
        print("para Direta -> R")
        print("Para Esquerda -> L")
        linha()
        robo =  input("")
        if (robo == "r")or(robo=="R"):
            coord_x2 +=1
            coord_y2 = coord_y2
        elif (robo == "l")or(robo == "L"):
            coord_x2 -=1
            coord_y2= coord_y2
        elif (robo=="D")or(robo=="d"):
            coord_y2-=1
            coord_x2=coord_x2
        elif (robo=="u")or(robo=="U"):
            coord_y2+=1
            coord_x2=coord_x2
            cont+=1
        print("eixo de x: ", coord_x2, "eixo de y: ", coord_y2)
        linha()
    
        print("Digite sim ou não para continuar")
        continuar = input("Continuar?")
        if continuar=='Sim' or continuar=='sim': 
            continue
        elif continuar=='Não' or continuar=='não': 
            break
    break
# plano cartesiano e quadrante
pc_quadrante = ""
if coord_x > 0 & coord_y > 0:
  pc_quadrante = "1º"
elif coord_x > 0 & coord_y < 0:
  pc_quadrante = "4º"
elif coord_x < 0 & coord_y > 0:
  pc_quadrante = "2º"
elif coord_x < 0 & coord_y < 0:
  pc_quadrante = "3º"
# Quadrante secundário
pc_2 = ""
if coord_x2 > 0 & coord_y2 > 0:
    pc_2 = "1º"
elif coord_x2 > 0 & coord_y2 < 0:
    pc_2 = "4º"
elif coord_x2 < 0 & coord_y2 > 0:
    pc_2 = "2º"
elif coord_x2 < 0 & coord_y2 < 0:
    pc_2 = "3º"
print(" Inicio: eixo x: {0}, | eixo y: {1})".format(coord_x, coord_y))
linha()
print("Fim: eixo x: {0},| eixo y: {1}".format(coord_x2, coord_y2))
linha()
print("Quais são os movimentos que são válidos?", cont)
linha()
print("inicio: {0}, final: {1}".format(pc_quadrante, pc_2))
