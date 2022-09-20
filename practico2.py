#Generamos los grupos 
import random
from operator import itemgetter

paises = ["Argentina","Brasil","Chile","Colombia","Ecuador","Nicaragua","Mexico","Canada",
          "Italia","España","Portugal","Alemania","Francia","Holanda","Suiza","Suecia",
          "China","Japon","Taiwan","Irak","India","Tailandia","Korea del Norte","Korea del Sur",
          "Australia","Nueva Zelanda","Guam","Tonga","Sudafrica","Ghana","Kenia","Kongo"]

cantidadDeGrupos = 8
participantesPorGrupo = 4

grupos = [[["",0] for x in range(participantesPorGrupo)] for y in range(cantidadDeGrupos)]

for g in range(0,cantidadDeGrupos):
  for p in range(0,participantesPorGrupo):
    pais = paises[(g*participantesPorGrupo)+p]    
    grupos[g][p][0]+=pais    
print ("Antes de la ronda de grupos",grupos)

#Calculamos el resultado de cada partido y los puntos por partido

nombre=0
puntos=1
for grupo in range(0,cantidadDeGrupos):
  for equipoA in range(0, participantesPorGrupo - 1):
    for equipoB in range(equipoA + 1, participantesPorGrupo):                  
      golesEquipoA = random.randrange(5)
      golesEquipoB = random.randrange(5)            
      
      if golesEquipoA > golesEquipoB:
        grupos[grupo][equipoA][puntos]+=3      
      elif golesEquipoA < golesEquipoB:
        grupos[grupo][equipoB][puntos]+=3      
      else:
        grupos[grupo][equipoA][puntos]+=1
        grupos[grupo][equipoB][puntos]+=1

print ("Luego de la ronda de grupos",grupos)

gruposOrdenados=[]
for g in range(0,cantidadDeGrupos):
  grupoDesordenado = grupos[g]
  gruposOrdenados.append(sorted(grupoDesordenado,key=itemgetter(1),reverse=True))

print ("Orden de la ronda de grupos",gruposOrdenados)

print ("Pasan a la siguiente ronda:")
for g in range(0,cantidadDeGrupos):
  print("Grupo ",g, " ", gruposOrdenados[g][0][0], "y", gruposOrdenados[g][1][0])
  #octavos de finales
  octavos = []
  for f in range(0,gruposOrdenados):
      gruposOrdenados = octavos[f]
      


    