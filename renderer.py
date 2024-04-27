import pygame


class Renderer:
    @staticmethod
    def render_text(font, screen, text, x, y):
        screen.blit(font.render(text, True, (255, 255, 255)), (x, y))

    @staticmethod
    def render_description(font, screen, description):
        words = description.split()
        for i, word in enumerate(words):
            Renderer.render_text(
                font,
                screen,
                word,
                screen.get_width() // 4,
                screen.get_height() // 2 + i * 20,
            )
        pygame.display.flip()

    @staticmethod
    def render_status(font, screen, player):
        Renderer.render_text(font, screen, f"Inventory: {player.inventory}", 50, 700)
        Renderer.render_text(font, screen, f"Health: {player.health}", 50, 720)

    @staticmethod
    def render_items(font, screen, items):
        for i, item in enumerate(items):
            Renderer.render_text(
                font,
                screen,
                f"There is {item}",
                screen.get_width() // 2,
                screen.get_height() // 4 + i * 20,
            )

    @staticmethod
    def render_exits(font, screen, exits):
        for i, exit in enumerate(exits.values()):
            description = exit.get("description", "an exit")
            Renderer.render_text(
                font,
                screen,
                f"There is a {description}",
                screen.get_width() // 2,
                screen.get_height() // 2 + i * 20,
            )

    @staticmethod
    def render_pick_up_options(screen, font, player):
        for i, item in enumerate(player.location.items, start=1):
            Renderer.render_text(font, screen, f"{i}. {item}", 50, 100 + i * 20)
