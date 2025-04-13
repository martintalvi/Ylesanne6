import pygame
import random

# Pygame initsialiseerimine
pygame.init()

# Ekraani seaded
ekraanX = 640
ekraanY = 480
ekraan = pygame.display.set_mode([ekraanX, ekraanY])
pygame.display.set_caption("Pallimäng")

taustavärv = (173, 216, 230)

# Taustamuusika laadimine ja mängimine
pygame.mixer.music.load("Beyond the Grey Veil.mp3")
pygame.mixer.music.play(-1)

# Palli pildi laadimine ja kiiruse määramine
pallipilt = pygame.image.load("ball.png")
pallipilt = pygame.transform.scale(pallipilt, (20, 20))
pall = pygame.Rect(ekraanX // 2, ekraanY // 2, 20, 20)
kiirusX = 4
kiirusY = 4

# Aluse pildi laadimine ja kiiruse määramine
alusepilt = pygame.image.load("pad.png")
alusepilt = pygame.transform.scale(alusepilt, (120, 20))
alus = pygame.Rect(ekraanX // 2 - 60, ekraanY / 1.5, 120, 20)
alusekiirus = 5

skoor = 0
font = pygame.font.Font(None, 36)

# Mängutsükkel
clock = pygame.time.Clock()

gameover = False
while not gameover:
    clock.tick(60)
    ekraan.fill(taustavärv)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                alusekiirus = -5
            elif event.key == pygame.K_RIGHT:
                alusekiirus = 5
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                alusekiirus = 0

    # Palli liikumine
    pall.x += kiirusX
    pall.y += kiirusY

    # Seinakokkupõrge
    if pall.left <= 0 or pall.right >= ekraanX:
        kiirusX = -kiirusX
    if pall.top <= 0:
        kiirusY = -kiirusY

    # Kui pall puudutab alumist äärt, lõpetame mängu
    if pall.bottom >= ekraanY:
        gameover = True

    # Aluse liikumine
    alus.x += alusekiirus
    if alus.left < 0:
        alus.left = 0
    if alus.right > ekraanX:
        alus.right = ekraanX

    # Kokkupõrge alusega
    if pall.colliderect(alus) and kiirusY > 0:
        kiirusY = -kiirusY
        skoor += 1

    # Objektide joonistamine
    ekraan.blit(alusepilt, alus)
    ekraan.blit(pallipilt, pall)

    # Skoori kuvamine
    skooritekst = font.render(f"Skoor: {skoor}", True, (0, 0, 0))
    ekraan.blit(skooritekst, (10, 10))

    pygame.display.flip()

pygame.quit()
