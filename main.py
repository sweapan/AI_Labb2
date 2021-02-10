import pygame, sys, mapreader, pathfinder
from pygame.locals import *

pygame.init()

FPS = 60
clock = pygame.time.Clock()

maprows = mapreader.ReadMap("Map1.txt") #display based on amount of tiles in map
displaySize = (len(maprows)*(len(maprows[0])-1))
display = pygame.display.set_mode((displaySize, displaySize))
display.fill((255,255,255))
pygame.display.set_caption("Path Finding")


rectSize = displaySize / (len(maprows[0])-1)
for i in range(len(maprows)):
    for j in range(len(maprows[0])-1):
        if(maprows[i][j] == "X"):
            pygame.draw.rect(display, (0,0,0), (j*rectSize, i*rectSize, rectSize, rectSize))
            pathfinder.paths.pathBlocks.append(pathfinder.PathBlock(i*100+j, [(i-1)*100+j, i*100+j+1, (i+1)*100+j, i*100+j-1], False, False, False))
        if(maprows[i][j] == "0"):
            pygame.draw.rect(display, (0,0,0), (j*rectSize, i*rectSize, rectSize, rectSize), 1)
            pathfinder.paths.pathBlocks.append(pathfinder.PathBlock(i*100+j, [(i-1)*100+j, i*100+j+1, (i+1)*100+j, i*100+j-1], True, False, False))
        if(maprows[i][j] == "S"):
            pygame.draw.rect(display, (0,255,0), (j*rectSize, i*rectSize, rectSize, rectSize))
            pathfinder.paths.pathBlocks.append(pathfinder.PathBlock(i*100+j, [(i-1)*100+j, i*100+j+1, (i+1)*100+j, i*100+j-1], True, False, True))
        if(maprows[i][j] == "G"):
            pygame.draw.rect(display, (255,0,0), (j*rectSize, i*rectSize, rectSize, rectSize))
            pathfinder.paths.pathBlocks.append(pathfinder.PathBlock(i*100+j, [(i-1)*100+j, i*100+j+1, (i+1)*100+j, i*100+j-1], True, True, False))

pygame.display.update()
pathfinder.pf.dfs(pathfinder.paths.GetStart())
print(pathfinder.pf.path)

#for i in pathfinder.pf.path:
#    print(i.id)
#    pygame.draw.circle(display, (150,0,150), ((i.id%100 + 1)*(rectSize) - rectSize/2, (i.id/100 + 1)*(rectSize) - rectSize/2), 3)

for i in range(len(pathfinder.pf.path)-1):
    startPoint = (pathfinder.pf.path[i].id%100 + 1)*(rectSize) - rectSize/2, (pathfinder.pf.path[i].id/100 + 1)*(rectSize) - rectSize/2
    endPoint = (pathfinder.pf.path[i+1].id%100 + 1)*(rectSize) - rectSize/2, (pathfinder.pf.path[i+1].id/100 + 1)*(rectSize) - rectSize/2
    pygame.draw.line(display, (0,0,255), startPoint, endPoint, 3)
    print(i)

pygame.display.update()
while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(FPS)
