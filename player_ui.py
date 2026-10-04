import pygame

class PlayerUI:
    def __init__(self, max_health, screen):
        self.max_health = max_health
        self.current_health = max_health
        self.screen = screen
        self.difficulty = None
        self.health_bar_image = pygame.image.load("assets/ui_assets/baseHealthBG.png")
        self.play_btn_image = pygame.image.load("assets/ui_assets/play.png")
        self.win_image = pygame.image.load("assets/ui_assets/win_ui.png")
        self.loss_image = pygame.image.load("assets/ui_assets/loss_ui.png")
        self.easy_btn = pygame.image.load("assets/ui_assets/easy_unselected.png")
        self.med_btn = pygame.image.load("assets/ui_assets/med_unselected.png")
        self.hard_btn = pygame.image.load("assets/ui_assets/hard_unselected.png")
        self.easy_selected_btn = pygame.image.load("assets/ui_assets/easy_selected.png")
        self.med_selected_btn = pygame.image.load("assets/ui_assets/med_selected.png")
        self.hard_selected_btn = pygame.image.load("assets/ui_assets/hard_selected.png")

    def draw_health_bar(self):
        self.screen.blit(self.health_bar_image, (0, 0))
        text_surface = pygame.font.Font(None, 36).render(f"{self.current_health}/{self.max_health}", True, (255, 255, 255))
        self.screen.blit(text_surface, (50, 5))

    def take_damage(self, damage):
        self.current_health -= damage
        if self.current_health < 0:
            self.current_health = 0

        self.draw_health_bar()
        return self.current_health
    
    def draw_play_button(self):
        self.screen.blit(self.play_btn_image, (125, 200))

    def clicked_play_button(self):
        pos = pygame.mouse.get_pos()
        play_button_rect = self.play_btn_image.get_rect(topleft=(100, 200))
        if play_button_rect.collidepoint(pos):
            return play_button_rect.collidepoint(pos)
    
    def display_win_message(self):
        self.screen.blit(self.win_image, (20,20))

    def display_lose_message(self):
        self.screen.blit(self.loss_image, (20,20))

    def clicked_again_button(self):
        pos = pygame.mouse.get_pos()
        again_button_rect = self.loss_image.get_rect(topleft=(20, 20))
        return again_button_rect.collidepoint(pos)
    
    def difficulty_selection(self):
        pos = pygame.mouse.get_pos()
        easy_button_rect = self.easy_btn.get_rect(topleft=(50, 100))
        medium_button_rect = self.med_btn.get_rect(topleft=(200, 100))
        hard_button_rect = self.hard_btn.get_rect(topleft=(350, 100))

        if self.difficulty is None:
            self.screen.blit(self.easy_btn, (50, 100))
            self.screen.blit(self.med_btn, (200, 100))
            self.screen.blit(self.hard_btn, (350, 100))
        elif self.difficulty == "easy":
            self.screen.blit(self.easy_selected_btn, (50, 100))
            self.screen.blit(self.med_btn, (200, 100))
            self.screen.blit(self.hard_btn, (350, 100))
        elif self.difficulty == "medium":
            self.screen.blit(self.easy_btn, (50, 100))
            self.screen.blit(self.med_selected_btn, (200, 100))
            self.screen.blit(self.hard_btn, (350, 100))
        elif self.difficulty == "hard":
            self.screen.blit(self.easy_btn, (50, 100))
            self.screen.blit(self.med_btn, (200, 100))
            self.screen.blit(self.hard_selected_btn, (350, 100))

        if easy_button_rect.collidepoint(pos):
            self.screen.blit(self.easy_selected_btn, (50, 100))
            return "easy"
        elif medium_button_rect.collidepoint(pos):
            self.screen.blit(self.med_selected_btn, (200, 100))
            return "medium"
        elif hard_button_rect.collidepoint(pos):
            self.screen.blit(self.hard_selected_btn, (350, 100))
            return "hard"
        else:
            return None
        
    def clicked_difficulty(self):
        pos = pygame.mouse.get_pos()
        easy_button_rect = self.easy_btn.get_rect(topleft=(50, 100))
        medium_button_rect = self.med_btn.get_rect(topleft=(200, 100))
        hard_button_rect = self.hard_btn.get_rect(topleft=(350, 100))

        if easy_button_rect.collidepoint(pos):
            self.screen.blit(self.easy_selected_btn, (50, 100))
            self.difficulty = "easy"
            return "easy"
        elif medium_button_rect.collidepoint(pos):
            self.screen.blit(self.med_selected_btn, (200, 100))
            self.difficulty = "medium"
            return "medium"
        elif hard_button_rect.collidepoint(pos):
            self.screen.blit(self.hard_selected_btn, (350, 100))
            self.difficulty = "hard"
            return "hard"
        else:
            return None