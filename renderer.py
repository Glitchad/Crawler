class Renderer:
    @staticmethod
    def render_text(font, screen, text, x, y):
        screen.blit(font.render(text, True, (255, 255, 255)), (x, y))

    @staticmethod
    def render_description(font, screen, description):
        for i, word in enumerate(description.split()):
            Renderer.render_text(font, screen, word, 50, 50 + i * 20)

    @staticmethod
    def render_status(font, screen, player):
        Renderer.render_text(font, screen, f"Inventory: {player.inventory}", 50, 700)
        Renderer.render_text(font, screen, f"Health: {player.health}", 50, 720)

    @staticmethod
    def render_items(font, screen, items):
        Renderer.render_text(font, screen, f"Items: {items}", 1130, 700)

    @staticmethod
    def render_exits(font, screen, exits):
        for i, exit in enumerate(exits.values()):
            Renderer.render_text(
                font, screen, f"There is a {exit['description']}", 1130, 720 + i * 20
            )
