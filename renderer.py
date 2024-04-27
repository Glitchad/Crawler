import pygame


class Renderer:
    @staticmethod
    def render_text(font, screen, text, x, y):
        screen.blit(font.render(text, True, (255, 255, 255)), (x, y))

    @staticmethod
    def render_words(font, screen, words, start_x, start_y):
        for i, word in enumerate(words):
            text = font.render(word, True, (255, 255, 255))
            x = start_x
            y = start_y + i * 20
            Renderer.render_text(font, screen, word, x, y)
            pygame.display.flip()
            pygame.time.wait(500)

    @staticmethod
    def render_description(font, screen, description):
        start_x = (screen.get_width() // 2 - font.size(description)[0]) // 2
        start_y = screen.get_height() // 2
        Renderer.render_words(font, screen, description.split(), start_x, start_y)

    @staticmethod
    def render_status(font, screen, player):
        Renderer.render_text(font, screen, f"Inventory: {player.inventory}", 50, 700)
        Renderer.render_text(font, screen, f"Health: {player.health}", 50, 720)

    @staticmethod
    def render_items(font, screen, items):
        start_x = screen.get_width() // 2
        start_y = screen.get_height() // 4
        for item in items:
            Renderer.render_words(
                font, screen, f"There is {item}".split(), start_x, start_y
            )
            start_y += 20  # Move to the next line for the next item

    @staticmethod
    def render_exits(font, screen, exits):
        start_x = screen.get_width() // 2
        start_y = screen.get_height() // 2
        for exit in exits.values():
            Renderer.render_words(
                font,
                screen,
                f"There is a {exit['description']}".split(),
                start_x,
                start_y,
            )
