import pygame

class Minesweeper():
    def __init__(self):
        pygame.init()
        self.WIDTH, self.HEIGHT = 320, 400
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Minesweeper")
        self.clock = pygame.time.Clock()
        self.running = True

        self.game_loop()

    def game_loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.game_logic()

            pygame.display.flip()
            self.clock.tick(60)

    pygame.quit()

    def game_logic(self):
        WHITE = (255, 255, 255)
        GREY_LIGHT = (192, 192, 192)
        GREY_DARK = (128, 128, 128)
        BLACK = (0, 0, 0)
        RED_LIGHT = (255, 0, 0)
        RED_DARK = (128, 0, 0)
        YELLOW = (255, 255, 0)

        self.screen.fill(GREY_LIGHT)

        hdr_x, hdr_y, hdr_w, hdr_h = 10, 8, 300, 74

        # pygame.draw.rect(self.screen, GREY_DARK, (hdr_x, hdr_y, hdr_w, hdr_h))
        pygame.draw.rect(self.screen, GREY_DARK, (hdr_x, hdr_y, hdr_w - 2, 4))
        pygame.draw.rect(self.screen, GREY_DARK, (hdr_x, hdr_y, 4, hdr_h + 2))
        pygame.draw.rect(self.screen, WHITE, (hdr_x + 2, hdr_y + hdr_h, hdr_w - 2, 4))
        pygame.draw.rect(self.screen, WHITE, (hdr_x + hdr_w - 4, hdr_y + 2, 4, hdr_h - 2))

if __name__ == "__main__":
    minesweeper = Minesweeper()
