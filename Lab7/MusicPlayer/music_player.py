import pygame
import os
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((300, 200))
pygame.display.set_caption("Music Player")
MUSIC_FOLDER = "."
tracks = [f for f in os.listdir(MUSIC_FOLDER) if f.endswith(".mp3")]
tracks.sort()  
current_track = tracks.index("secret song.mp3") if "secret song.mp3" in tracks else 0
pygame.mixer.music.load(os.path.join(MUSIC_FOLDER, tracks[current_track]))
pygame.mixer.music.play()
print(f"Now: {tracks[current_track]}")
print("Control: [SPACE] - Pause, [S] - Stop, [N] - Next, [P] - Previous")

running = True
while running:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                    print("Music is paused")
                else:
                    pygame.mixer.music.unpause()
                    print("Continue")
            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()
                print("Music is paused")
            elif event.key == pygame.K_n:
                current_track = (current_track + 1) % len(tracks)
                pygame.mixer.music.load(os.path.join(MUSIC_FOLDER, tracks[current_track]))
                pygame.mixer.music.play()
                print(f"Now: {tracks[current_track]}")
            elif event.key == pygame.K_p:
                current_track = (current_track - 1) % len(tracks)
                pygame.mixer.music.load(os.path.join(MUSIC_FOLDER, tracks[current_track]))
                pygame.mixer.music.play()
                print(f"Now: {tracks[current_track]}")
pygame.quit()