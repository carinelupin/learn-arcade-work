"""
PIZZZZZAAAAAA
"""

import arcade

arcade.open_window(600, 600, "PIZZZZAAAAAA")

arcade.set_background_color(arcade.csscolor.SKY_BLUE)

arcade.start_render()

# drawing code
# all about that base
arcade.draw_circle_filled(300, 300, 250, arcade.csscolor.SADDLE_BROWN)

arcade.finish_render()

arcade.run()
