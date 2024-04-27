import sys

import pygame

from music import play_music
from player import Player
from renderer import Renderer
from world import World


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1280, 800))
    world = World()
    player = Player(world.locations["cave"])
    font = pygame.font.Font(None, 36)

    key_directions = {
        pygame.K_w: "north",
        pygame.K_s: "south",
        pygame.K_a: "west",
        pygame.K_d: "east",
    }

    play_music(player.location.song)

    clock = pygame.time.Clock()

    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if (
                    event.key in key_directions
                    and key_directions[event.key] in player.location.exits
                ):
                    player.move(
                        player.location.exits[key_directions[event.key]]["location"]
                    )
                elif event.key == pygame.K_p:
                    player.picking_up = True
                elif player.picking_up and event.key in range(pygame.K_1, pygame.K_4):
                    player.pick_up(player.location.items[event.key - pygame.K_1])
                    player.picking_up = False

        player.location.render(font, screen, player)
        if player.picking_up:
            Renderer.render_pick_up_options(screen, font, player)

        pygame.display.flip()


if __name__ == "__main__":
    run_game()
