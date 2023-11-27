import pygame

# def dbscan(points):
#     eps = 30
#     minPts = 5
#     dbScan = DBSCAN(eps, min_samples=minPts.fit(points))

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((600,400))
    screen.fill(color='#FFFFFF')
    pygame.display.update()
    flag = True
    while(flag):
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                flag = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    coords = event.pos
                    pygame.draw.circle(screen, color="#000000", center=coords, radius=2)
                    pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN:
                is_down = True
            if (is_down):
                coords = event.pos
                pygame.draw.circle(screen, color="#000000", center=coords, radius=2)
            if event.type == pygame.KEYDOWN:
                if event.key == 98:
                    pygame.draw.circle(screen, color='black', center= (10,10), radius=5)
            pygame.display.update()
