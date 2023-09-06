import pygame


class Button:
    def __init__(
        self, text, width, height, pos, elevation, font, color="#475F77", event=None
    ):
        # Core attributes
        self.color = color
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.original_y_pos = pos[1]

        # top rectangle
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = self.color
        # bottom rectangle
        self.bottom_rect = pygame.Rect(pos, (width, height))
        self.bottom_color = "#354B5E"
        # text
        self.text = text
        self.text_surf = font.render(text, True, "#FFFFFF")
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)
        #        buttons.append(self)
        # events
        self.event = event

    def draw(self, screen):
        # elevation logic
        self.top_rect.y = self.original_y_pos - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

        pygame.draw.rect(screen, self.bottom_color, self.bottom_rect, border_radius=12)
        pygame.draw.rect(screen, self.top_color, self.top_rect, border_radius=12)
        screen.blit(self.text_surf, self.text_rect)
        return self.check_click()

    def check_click(self):
        action = False
        mouse_pos = pygame.mouse.get_pos()

        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = "#D74B4B"
            if pygame.mouse.get_pressed()[0] == 1 and self.pressed == False:
                self.dynamic_elevation = 0
                self.pressed = True
                if self.event is not None:
                    pygame.event.post(self.event)
            if pygame.mouse.get_pressed()[0] == 0:
                self.dynamic_elevation = self.elevation
                if self.pressed == True:
                    action = True
                self.pressed = False
                self.dynamic_elevation = self.elevation
                self.top_color = self.color

        return action
