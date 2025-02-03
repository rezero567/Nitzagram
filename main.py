import pygame
from pygame.examples.cursors import image

from helpers import screen
from constants import *
from class_module import Post, ImagePost, TextPost, Comment


def main():
    # Set up the game display, clock and headline
    pygame.init()

    # Change the title of the window
    pygame.display.set_caption('Nitzagram')

    clock = pygame.time.Clock()

    # Set up background image
    background = pygame.image.load('Images/background.png')
    background = pygame.transform.scale(background,
                                        (WINDOW_WIDTH, WINDOW_HEIGHT))

    # TODO: add a post here
    # ----- ↓↓↓ POST LIST!!! ↓↓↓ -----
    posts_list = []

    # ----- ↓↓↓ EMPTY TEST POST!!! ↓↓↓ -----
    noa_img = "Images\\noa_kirel.jpg"
    test_post = ImagePost("daniel", "beer", "yay", noa_img)
    like_rect = pygame.Rect(LIKE_BUTTON_X_POS, LIKE_BUTTON_Y_POS, LIKE_BUTTON_WIDTH, LIKE_BUTTON_HEIGHT)
    posts_list.append(test_post)

    # ----- ↓↓↓ Shrekxy IMAGE TEST POST!!! ↓↓↓ -----
    shrekxy_img = "Images\\shrekxy_img.jpg"
    image_post = ImagePost("Ron", "North Korea", "Long live Kim Jong Un", shrekxy_img)
    like_rect = pygame.Rect(LIKE_BUTTON_X_POS, LIKE_BUTTON_Y_POS, LIKE_BUTTON_WIDTH, LIKE_BUTTON_HEIGHT)
    post_rect = pygame.Rect(POST_X_POS, POST_Y_POS, POST_WIDTH, POST_HEIGHT)
    comment_rect = pygame.Rect(COMMENT_BUTTON_X_POST, COMMENT_BUTTON_Y_POS, COMMENT_BUTTON_WIDTH, COMMENT_BUTTON_HEIGHT)
    posts_list.append(image_post)
    
    ronaldo_img = "Images\\ronaldo.jpg"
    sec_post = ImagePost("Itay", "Portugal", "Long live Ronaldo", ronaldo_img)
    like_rect = pygame.Rect(LIKE_BUTTON_X_POS, LIKE_BUTTON_Y_POS, LIKE_BUTTON_WIDTH, LIKE_BUTTON_HEIGHT)
    posts_list.append(sec_post)

    masts_img = "Images\\masts_img.jpg"
    tre_post = ImagePost("daniel", "Isral", "sus", masts_img)
    like_rect = pygame.Rect(LIKE_BUTTON_X_POS, LIKE_BUTTON_Y_POS, LIKE_BUTTON_WIDTH, LIKE_BUTTON_HEIGHT)
    posts_list.append(tre_post)

    man_img = "Images\\man_img.jpg"
    four_post = ImagePost("Ron", "?", "my man", man_img)
    like_rect = pygame.Rect(LIKE_BUTTON_X_POS, LIKE_BUTTON_Y_POS, LIKE_BUTTON_WIDTH, LIKE_BUTTON_HEIGHT)
    posts_list.append(four_post)

    text_post = TextPost("Itay", "Tel Aviv", "best nitzagram")
    like_rect = pygame.Rect(LIKE_BUTTON_X_POS, LIKE_BUTTON_Y_POS, LIKE_BUTTON_WIDTH, LIKE_BUTTON_HEIGHT)
    posts_list.append(text_post)

    work_img = "Images\\work_img.jpg"
    four_post = ImagePost("Itamer", "Isral", "its me in work", work_img)
    like_rect = pygame.Rect(LIKE_BUTTON_X_POS, LIKE_BUTTON_Y_POS, LIKE_BUTTON_WIDTH, LIKE_BUTTON_HEIGHT)
    posts_list.append(work_img)

    post_index_to_display = 0
    running = True
    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:  # check for mouse events
                mouse_pos = event.pos  # Get mouse position

                if like_rect.collidepoint(mouse_pos):  # check if mouse click like
                     posts_list[post_index_to_display].add_like()
                     
                if post_rect.collidepoint(mouse_pos):
                    # Check if the user clicked on the view more comments button and advances to the next post in a loop
                    if post_index_to_display == len(posts_list) - 1:
                        post_index_to_display = 0
                    else:
                        post_index_to_display += 1
                if comment_rect.collidepoint(mouse_pos):
                    posts_list[post_index_to_display].add_comment()

        # Display the background, presented Image, likes, comments, tags and location(on the Image)
        screen.fill(BLACK)
        screen.blit(background, (0, 0))

        # Shows the next post according to the post index
        posts_list[post_index_to_display].display()

        # Update display - without input update everything
        pygame.display.update()

        # Set the clock tick to be 60 times per second. 60 frames for second.
        clock.tick(60)
    pygame.quit()
    quit()


main()
