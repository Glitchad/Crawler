import sys

import pygame

from location import World
from music import play_music  # Import the play_music function
from player import Player


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
        # Call the play_music function
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
        player.location.render(font, screen)
        if picking_up:
            for i, item in enumerate(player.location.items, start=1):
                screen.blit(
                    font.render(f"{i}. {item}", True, (255, 255, 255)),
                    (50, 100 + i * 20),
                )

        # Render player's inventory at the bottom left of the screen
        for i, item in enumerate(player.inventory, start=1):
            screen.blit(
                font.render(f"{i}. {item}", True, (255, 255, 255)), (50, 800 - i * 20)
            )

        # Render player's health at the top right of the screen
        health_text = font.render(f"Health: {player.health}", True, (255, 255, 255))
        screen.blit(health_text, (1280 - health_text.get_rect().width - 10, 10))

        pygame.display.flip()


run_game()
