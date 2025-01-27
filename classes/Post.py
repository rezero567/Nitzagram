import pygame

from constants import *
from helpers import screen, read_comment_from_user


class Post:
    """
    A class used to represent post on Nitzagram
    """
    def __init__(self, username, location, description):
        self.username = username
        self.location = location
        self.description = description
        self.likes_counter = 0
        self.comments = []
        self.comments_display_index = len(self.comments)

    def add_like(self):
        self.likes_counter += 1

    def add_comment(self, text):
        # TODO: ADD COMMENT OBJECT
        self.comments.append(text)

    def display(self):
        """
        Display the Post image/Text, description, location, likes and comments
        on screen

        :return: None
        """
        font = pygame.font.SysFont('chalkduster.ttf', UI_FONT_SIZE)

        username = font.render(self.username, True, BLACK)
        screen.blit(username, (USER_NAME_X_POS, USER_NAME_Y_POS))

        location = font.render(self.location, True, LIGHT_GRAY)
        screen.blit(location, (LOCATION_TEXT_X_POS, LOCATION_TEXT_Y_POS))

        if self.likes_counter == 1:
            likes = font.render(f"liked by {self.likes_counter} user", True, GREY)
        else:
            likes = font.render(f"liked by {self.likes_counter} users", True, GREY)
        screen.blit(likes, (LIKE_TEXT_X_POS, LIKE_TEXT_Y_POS))

        description = font.render(self.description, True, BLACK)
        screen.blit(description, (DESCRIPTION_TEXT_X_POS, DESCRIPTION_TEXT_Y_POS))

        self.display_comments()

    def display_comments(self):
        """
        Display comments on post. In case there are more than 4
        comments, show only 4 comments chosen by reset_comments_display_index

        :return: None
        """
        position_index = self.comments_display_index
        # If there are more than 4 comments, print "view more comments"
        if len(self.comments) > NUM_OF_COMMENTS_TO_DISPLAY:
            comment_font = pygame.font.SysFont('chalkduster.ttf',
                                               COMMENT_TEXT_SIZE)
            view_more_comments_button = comment_font.render("view more comments",
                                                            True, LIGHT_GRAY)
            screen.blit(view_more_comments_button, (VIEW_MORE_COMMENTS_X_POS,
                                                    VIEW_MORE_COMMENTS_Y_POS))

        # Display 4 comments starting from comments_display_index
        # This doesn't work so commented out to prevent unwanted crashes
        # TODO: Fix
        for i in range(0, len(self.comments)):
            if position_index >= len(self.comments):
                position_index = 0
            self.comments[position_index].display(i)
            position_index += 1
            if i >= NUM_OF_COMMENTS_TO_DISPLAY - 1:
                break


class Comment:
    def __init__(self, text):
        self.text = text


class ImagePost(Post):
    # TODO: write me! load images and override the super().display() method
    def __init__(self, username, location, description, img_path):
        super().__init__(username, location, description)
        self.img_path = img_path

    def display(self):
        super().display()

        image = pygame.image.load(self.img_path)
        # Fix size
        image = pygame.transform.scale(image, (POST_WIDTH, POST_HEIGHT))
        screen.blit(image, (POST_X_POS, POST_Y_POS))
        

class TextPost(Post):
    # TODO: write me! draw background and create text then override the super().display() method
    pass
