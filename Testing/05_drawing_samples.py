"""
SAmple program to show how to draw using Python
and arcade library
"""

# import the "arcade" library
import arcade

# open up a window
# from the "arcade" library, use a function called "open_window"
# set the dimensions (width & height)
# set the window title
arcade.open_window(600, 600, "Drawing Example")

# set background colour
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

# Get ready to draw
arcade.start_render()

# drawing code (always between 'start render' & 'finish render')
# draw a rectangle
# left of 0 , right of 599
# top of 300, bottom of 0
arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.GREEN)

# tree trunk
# center of 100, 320
# width of 20
# height of 60
arcade.draw_rectangle_filled(100, 320, 20, 60, arcade.csscolor.SIENNA)

# tree top
arcade.draw_circle_filled(100, 350, 30, arcade.csscolor.DARK_GREEN)

# another tree, w/ trunk and ellipse top
arcade.draw_rectangle_filled(200, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_ellipse_filled(200, 370, 60, 80, arcade.csscolor.DARK_GREEN)

# more tree w trunk & arc top
# arc is centered at  (300, 340) w/ width of 60 & height of 180
# starting angle 0 & ending angle is 180
arcade.draw_rectangle_filled(300, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_arc_filled(300, 340, 60, 180, arcade.csscolor.DARK_GREEN, 0, 180)

# tree w/ trunk & triangle top
arcade.draw_rectangle_filled(400, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_triangle_filled(400, 400, 370, 320, 430, 320, arcade.csscolor.DARK_GREEN)

# tree w trunk + polygon top
arcade.draw_rectangle_filled(500, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_polygon_filled(((500, 400),
                            (480, 360),
                            (470, 320),
                            (530, 320),
                            (520, 360)),
                           arcade.csscolor.DARK_GREEN)

# draw sun
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

# text
arcade.draw_text("arbor day - plant a tree!",
                 150, 230,
                 arcade.csscolor.BLACK, 24)

# finish drawing
arcade.finish_render()

# Keep window up until someone closes it
arcade.run()
