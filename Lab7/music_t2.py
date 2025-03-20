import pygame as pg
import sys

pg.init()
pg.mixer.init()


playlist = ["Engelbert Humperdinck - A Man Without Love.mp3","Frank Ocean - Thinkin Bout You.mp3","Kanye West feat. Dwele - Flash Lights.mp3"]
current_track_index = 0


def play_track(index):
    pg.mixer.music.load(playlist[index])
    pg.mixer.music.play()

play_track(current_track_index)

screen = pg.display.set_mode((550, 200))
pg.display.set_caption("Music Player")

font = pg.font.SysFont("Arial", 24)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        elif event.type == pg.KEYDOWN:
            #(Space-Plays the music)
            if event.key == pg.K_SPACE:
                if not pg.mixer.music.get_busy():
                    pg.mixer.music.play()
            # (S-stop the music)
            elif event.key == pg.K_s:
                pg.mixer.music.stop()
            #  (Right-next mus)
            elif event.key == pg.K_RIGHT:
                current_track_index = (current_track_index + 1) % len(playlist)
                play_track(current_track_index)
            # (Left-previous music)
            elif event.key == pg.K_LEFT:
                current_track_index = (current_track_index - 1) % len(playlist)
                play_track(current_track_index)

    screen.fill((30, 30, 30))


    text_surface = font.render(
        f"Playing: {playlist[current_track_index]}",
        True, (255, 255, 255)
    )
    screen.blit(text_surface, (20, 80))

    pg.display.flip()
    pg.time.Clock().tick(30)

pg.quit()
sys.exit()
