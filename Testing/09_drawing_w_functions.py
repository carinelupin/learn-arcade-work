# import the "arcade" library
import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


def draw_grass():
    """draw the ground"""
    arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.GREEN)


def draw_tree_trunk(x):
    """draw tree trunk"""
    arcade.draw_rectangle_filled(x, 320, 20, 60, arcade.csscolor.SIENNA)


def draw_circle_tree(x):
    """draw tree trunk w circle tree top"""
    # tree trunk
    draw_tree_trunk(x)

    # circle top
    arcade.draw_circle_filled(x, 350, 30, arcade.csscolor.DARK_GREEN)


def draw_ellipse_tree(x):
    """draw tree with ellipse top"""
    # tree trunk
    draw_tree_trunk(x)

    # tree top
    arcade.draw_ellipse_filled(x, 370, 60, 80, arcade.csscolor.DARK_GREEN)


def draw_arc_tree(x):
    """draw tree w arc top"""
    # tree trunk
    draw_tree_trunk(x)

    # tree top
    arcade.draw_arc_filled(x, 340, 60, 180, arcade.csscolor.DARK_GREEN, 0, 180)


def draw_triangle_tree():
    """draw tree w triangle top"""
    # tree trunk
    draw_tree_trunk(400)

    # tree top
    arcade.draw_triangle_filled(400, 400, 370, 320, 430, 320, arcade.csscolor.DARK_GREEN)


def draw_polygon_tree():
    """draw tree w polygon top"""
    # tree trunk
    draw_tree_trunk(500)

    # tree top
    arcade.draw_polygon_filled(((500, 400),
                                (480, 360),
                                (470, 320),
                                (530, 320),
                                (520, 360)),
                               arcade.csscolor.DARK_GREEN)


def draw_sun():
    arcade.draw_circle_filled(500, 550, 40, arcade.csscolor.YELLOW)

    # rays left, right, up, down
    arcade.draw_line(500, 550, 400, 550, arcade.csscolor.YELLOW)
    arcade.draw_line(500, 550, 600, 550, arcade.csscolor.YELLOW)
    arcade.draw_line(500, 550, 500, 450, arcade.csscolor.YELLOW)
    arcade.draw_line(500, 550, 500, 650, arcade.csscolor.YELLOW)

    # rays diagonal
    arcade.draw_line(500, 550, 550, 600, arcade.csscolor.YELLOW)
    arcade.draw_line(500, 550, 550, 500, arcade.csscolor.YELLOW)
    arcade.draw_line(500, 550, 450, 600, arcade.csscolor.YELLOW)
    arcade.draw_line(500, 550, 450, 500, arcade.csscolor.YELLOW)


def draw_text(x):
    arcade.draw_text(x,
                     150, 230,
                     arcade.csscolor.BLACK, 24)


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Example")
    arcade.set_background_color(arcade.csscolor.SKY_BLUE)
    arcade.start_render()

    draw_grass()

    # trees
    draw_circle_tree(100)
    draw_ellipse_tree(200)
    draw_arc_tree(300)
    draw_triangle_tree()
    draw_polygon_tree()

    draw_sun()

    draw_text("wow what a view")

    # finish & run
    arcade.finish_render()
    arcade.run()


main()
