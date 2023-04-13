"""
drawing a landscape
"""

import arcade

arcade.open_window(600, 600, "Landscape Drawing")

arcade.set_background_color(arcade.csscolor.SKY_BLUE)

arcade.start_render()

# drawing code
arcade.draw_lrtb_rectangle_filled(0, 599, 100, 0, arcade.csscolor.SADDLE_BROWN)

# pine tree w 3 triangles + stump
arcade.draw_rectangle_filled(360, 120, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_triangle_filled(300, 220, 360, 260, 420, 220, arcade.csscolor.DARK_GREEN)
arcade.draw_triangle_filled(300, 180, 360, 240, 420, 180, arcade.csscolor.DARK_GREEN)
arcade.draw_triangle_filled(300, 140, 360, 220, 420, 140, arcade.csscolor.DARK_GREEN)

# the SUN
arcade.draw_circle_filled(580, 580, 40, arcade.csscolor.YELLOW)

arcade.finish_render()

arcade.run()
