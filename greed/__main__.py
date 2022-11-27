import random

from game.casting.actor import Actor
from game.casting.artifact import Artifact
from game.casting.cast import Cast
from game.casting.score import Score #?

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


FRAME_RATE = 70
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 20
COLS = 60
ROWS = 40
CAPTION = "Greed"
WHITE = Color(255, 255, 255)
RED = Color(255, 0, 0)
DEFAULT_ARTIFACTS = 50 # Test, Original-> 40
ARTIFACTS_SHAPES = ["|*|","O"]
VELOCITY = Point(0, 1)


def main():
    
    # create the cast
    cast = Cast()
    
    # create the banner
    banner = Actor()
    banner.set_text("")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)
    
    # create the robot
    x = int(MAX_X / 2)
    y = int(MAX_Y - CELL_SIZE) # Mod --------------
    position = Point(x, y)

    robot = Actor()
    robot.set_text("#")
    robot.set_font_size(FONT_SIZE)
    robot.set_color(RED)
    robot.set_position(position)
    cast.add_actor("robots", robot)

    # create the artifacts
    for _ in range(DEFAULT_ARTIFACTS): # Mod ---
        text = random.choice(ARTIFACTS_SHAPES) # Mod ----------
        #message = messages[n] # No message

        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 5) # Mod ---------------------
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        artifact = Artifact()
        artifact.set_text(text)
        artifact.set_font_size(FONT_SIZE)
        artifact.set_color(color)
        artifact.set_position(position)
        artifact.set_velocity(VELOCITY)

        # If the artifact is a "rock" the score will be -1 if the robot touches it # Mod ---
        if artifact.get_text() == "O":
            artifact.set_value(-1)
            #artifact.set_message(message)

        cast.add_actor("artifacts", artifact)
        
    
    """
    ##### Hello, I commented this because we already have a score in Director class
    # create initial score    
    score = Score()
    score.set_position(Point(MAX_X // 2, 15))
    score.set_color(RED)
    cast.add_actor("score", score)"""
        
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()
