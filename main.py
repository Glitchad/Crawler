import sys

import pygame

from music import play_music
from player import Player
from world import World


def run_game():
    pygame.init()  # Initialize all imported pygame modules
    screen = pygame.display.set_mode((1280, 800))  # Set the dimensions of the window
    world = World()  # Create a new World object
    player = Player(
        world.locations["cave"]
    )  # Create a new Player object starting in the "cave" location
    font = pygame.font.Font(None, 36)  # Set the font for the game

    picking_up = (
        False  # Variable to track if the player is in the process of picking up an item
    )
    key_directions = {  # Map the keys to directions
        pygame.K_w: "north",
        pygame.K_s: "south",
        pygame.K_a: "west",
        pygame.K_d: "east",
    }
    item_keys = [pygame.K_1, pygame.K_2, pygame.K_3]  # Keys for picking up items

    while True:  # Main game loop
        play_music()  # Call the play_music function

        for event in pygame.event.get():  # Event handling
            if event.type == pygame.QUIT:  # If the event is QUIT, exit the game
                sys.exit()
            elif event.type == pygame.KEYDOWN:  # If a key is pressed
                if (
                    event.key in key_directions
                    and key_directions[event.key] in player.location.exits
                ):
                    # If the key corresponds to a direction and there is an exit in that direction, move the player
                    player.location = player.location.exits[key_directions[event.key]][
                        "location"
                    ]
                elif (
                    event.key == pygame.K_p
                ):  # If the key is 'p', start the process of picking up an item
                    picking_up = True
                elif (
                    picking_up and event.key in item_keys
                ):  # If the player is picking up an item and presses a number key
                    player.pick_up(
                        player.location.items[int(event.unicode) - 1]
                    )  # Pick up the corresponding item
                    picking_up = False  # End the process of picking up an item

        screen.fill((0, 0, 0))  # Fill the screen with black
        player.location.render(font, screen)  # Render the player's current location
        if picking_up:  # If the player is picking up an item
            for i, item in enumerate(
                player.location.items, start=1
            ):  # For each item in the location
                # Render the item's number and name
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

        pygame.display.flip()  # Update the full display surface to the screen


run_game()
