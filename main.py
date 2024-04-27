import sys

import pygame

from music import play_music
from player import Player
from world import World


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1280, 800))
    world = World()
    player = Player(world.locations["cave"])
    font = pygame.font.Font(None, 36)

    picking_up = False
    key_directions = {
        pygame.K_w: "north",
        pygame.K_s: "south",
        pygame.K_a: "west",
        pygame.K_d: "east",
    }
    item_keys = [pygame.K_1, pygame.K_2, pygame.K_3]

    while True:
        play_music()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if (
                    event.key in key_directions
                    and key_directions[event.key] in player.location.exits
                ):
                    player.location = player.location.exits[key_directions[event.key]][
                        "location"
                    ]
                elif event.key == pygame.K_p:
                    picking_up = True
                elif picking_up and event.key in item_keys:
                    player.pick_up(player.location.items[int(event.unicode) - 1])
                    picking_up = False

        screen.fill((0, 0, 0))
        player.location.render(font, screen, player)
        if picking_up:
            for i, item in enumerate(player.location.items, start=1):
                screen.blit(
                    font.render(f"{i}. {item}", True, (255, 255, 255)),
                    (50, 100 + i * 20),
                )

        pygame.display.flip()


run_game()
