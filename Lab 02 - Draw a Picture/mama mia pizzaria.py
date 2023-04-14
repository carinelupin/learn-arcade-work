"""
PIZZA drawing
"""

import arcade

arcade.open_window(600, 600, "PIZZA")

arcade.set_background_color((254, 204, 189))

arcade.start_render()

# drawing code
# shading under pizza
arcade.draw_circle_filled(290, 290, 250, (211,151,155))

# base
arcade.draw_circle_filled(300, 300, 250, (255, 203, 41))

# meat
arcade.draw_circle_filled(340, 130, 30, (237, 28, 37))
arcade.draw_circle_outline(340, 130, 30, (106, 24, 79), 5)

arcade.draw_circle_filled(338, 210, 30, (237, 28, 37))
arcade.draw_circle_outline(338, 210, 30, (106, 24, 79), 5)

# outside of pizza
arcade.draw_circle_outline(300, 300, 250, (240, 159, 33), 30)
arcade.draw_circle_outline(300, 300, 250, (106, 24, 79), 5)
arcade.draw_circle_outline(300, 300, 220, (106, 24, 79), 5)
#shading
arcade.draw_circle_outline(300, 300, 225, (201, 119, 47), 5)

# pizza cut lines
arcade.draw_line(300, 550, 300, 50, (106, 24, 79), 3)
arcade.draw_line(550, 300, 50, 300, (106, 24, 79), 3)
arcade.draw_line(123, 477, 477, 123, (106, 24, 79), 3)
arcade.draw_line(123, 123, 477, 477, (106, 24, 79), 3)


arcade.finish_render()

arcade.run()
