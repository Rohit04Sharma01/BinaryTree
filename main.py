import pygame
from sys import exit

# Initializing Pygame
pygame.init()
clock = pygame.time.Clock()


def create_button(x, y, width, height, label):
    # Set up button properties
    button_color = (0, 0, 0)
    font = pygame.font.Font(None, 30)
    text_color = (255, 255, 255)

    # Create button surface and rect
    button_surface = pygame.Surface((width, height))
    button_surface.fill(button_color)
    button_rect = button_surface.get_rect(x=x, y=y)

    # Create text surface and rect
    text_surface = font.render(label, True, text_color)
    text_rect = text_surface.get_rect(center=button_rect.center)

    # Draw button and text on screen
    screen.blit(button_surface, button_rect)
    screen.blit(text_surface, text_rect)

    return button_rect


def create_label(x, y, width, height, text, bg_color=None):
    # Set up label properties
    font = pygame.font.Font(None, 50)
    text_color = (0, 0, 0)

    # Create text surface and rect
    text_surface = font.render(text, True, text_color, bg_color)
    text_rect = text_surface.get_rect(x=x, y=y, width=width, height=height)

    # Draw text on screen
    screen.blit(text_surface, text_rect)
    return text_rect


def draw_square(screen, position, size, color):
    """
    Draws a square block with a given color and position on the screen.
    """
    rect = pygame.Rect(position, size)
    pygame.draw.rect(screen, color, rect)

    return rect


SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1200
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
hex_code = "#6c747e"
rgb_color = pygame.Color(hex_code)
screen.fill(rgb_color)
pygame.display.set_caption('Binary Tree')

# Simulation Screen

# Load image and resize it
image = pygame.image.load("tree_bg.jpg")
image = pygame.transform.scale(image, (800, 650))

# Set image position
image_position = (40, 40)

# Text Box
# Define textbox dimensions and position
textbox_width = 200
textbox_height = 60
textbox_position = (900, 40)

# Define textbox color and border
textbox_color = (255, 255, 255)
textbox_border_color = (0, 0, 0)
textbox_border_width = 2

# Define submit button dimensions and position
button_width = 200
button_height = 60
button_position = (900, 150)

# Define button color and text
button_color = (0, 0, 0)
font = pygame.font.Font(None, 30)
button_text = font.render("Submit", True, (255, 255, 255))
button_text_position = (button_position[0] + (button_width - button_text.get_width()) // 2,
                        button_position[1] + (button_height - button_text.get_height()) // 2)
button_rect = pygame.Rect(button_position[0], button_position[1], button_width, button_height)
textbox_rect = pygame.Rect(textbox_position[0], textbox_position[1], textbox_width, textbox_height)
screen.blit(button_text, button_text_position)

# Create textbox and button rectangles
textbox_rect = pygame.Rect(textbox_position[0], textbox_position[1], textbox_width, textbox_height)
button_rect = pygame.Rect(button_position[0], button_position[1], button_width, button_height)

# Draw textbox and button on screen
pygame.draw.rect(screen, textbox_color, textbox_rect)
pygame.draw.rect(screen, textbox_border_color, textbox_rect, textbox_border_width)
pygame.draw.rect(screen, button_color, button_rect)
screen.blit(button_text, button_text_position)

pygame.display.flip()

# Main loop
text_input = ""

# Search Button
# Define submit button dimensions and position
search_btn_rect = create_button(900, 250, 200, 60, "Search")
Traversal_text_rect = create_label(900, 350, 200, 200, "Traversal", "#6c747e")
preorder_btn_rect = create_button(900, 425, 200, 60, "PreOrder")
inorder_btn_rect = create_button(900, 525, 200, 60, "InOrder")
postorder_btn_rect = create_button(900, 625, 200, 60, "PostOrder")


# Traversal Label
block_rect1 = draw_square(screen, (40, 720), (50, 50), (255, 0, 0))
block_rect2 = draw_square(screen, (150, 720), (50, 50), (255, 0, 0))
block_rect3 = draw_square(screen, (260, 720), (50, 50), (255, 0, 0))
block_rect4 = draw_square(screen, (370, 720), (50, 50), (255, 0, 0))
block_rect5 = draw_square(screen, (480, 720), (50, 50), (255, 0, 0))
block_rect6 = draw_square(screen, (590, 720), (50, 50), (255, 0, 0))
block_rect7 = draw_square(screen, (700, 720), (50, 50), (255, 0, 0))
block_rect8 = draw_square(screen, (810, 720), (50, 50), (255, 0, 0))

create_label(900, 720, 200, 100, "Output")

text = "eerT yraniB"
font = pygame.font.SysFont(None, 50)
text_color = (0, 0, 0)
text_position = (1150, 300)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN and textbox_rect.collidepoint(pygame.mouse.get_pos()):
            if event.unicode.isalnum():
                text_input += event.unicode
            elif event.key == pygame.K_BACKSPACE:
                text_input = text_input[:-1]
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(pygame.mouse.get_pos()):
                print("Submit button clicked with input:", text_input)
                text_input = ""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if search_btn_rect.collidepoint(pygame.mouse.get_pos()):
                print("Search Button Clicked")
        if event.type == pygame.MOUSEBUTTONDOWN:
            # print(pygame.mouse.get_pos())
            if preorder_btn_rect.collidepoint(pygame.mouse.get_pos()):
                print("Preorder Button Clicked")
        if event.type == pygame.MOUSEBUTTONDOWN:
            if inorder_btn_rect.collidepoint(pygame.mouse.get_pos()):
                print("Inorder Button Clicked")
        if event.type == pygame.MOUSEBUTTONDOWN:
            if postorder_btn_rect.collidepoint(pygame.mouse.get_pos()):
                print("Postorder Button Clicked")

    # Binary Tree Background
    screen.blit(image, image_position)
    pygame.draw.rect(screen, textbox_color, textbox_rect)
    pygame.draw.rect(screen, textbox_border_color, textbox_rect, textbox_border_width)
    pygame.draw.rect(screen, button_color, button_rect)
    screen.blit(button_text, button_text_position)

    # Render text inside textbox
    font = pygame.font.Font(None, 24)
    text_surface = font.render(text_input, True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=textbox_rect.center)
    screen.blit(text_surface, text_rect)

    for i, char in enumerate(text):
        char_surface = font.render(char, True, text_color)
        char_rect = char_surface.get_rect()
        char_rect.center = (text_position[0], text_position[1] + i * char_rect.height)
        rotated_surface = pygame.transform.rotate(char_surface, 90)
        screen.blit(rotated_surface, char_rect)
    pygame.display.flip()
    clock.tick(60)
