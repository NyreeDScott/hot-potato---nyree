timer = 0

def on_button_pressed_a():
    global timer
    music.set_volume(255)
    timer = randint(5, 15)
    basic.show_leds("""
        . # # # .
        # # # # #
        # # # # #
        # # # # #
        . # # # .
        """)
    while timer > 0:
        timer += -1
        basic.pause(1000)
    music.play(music.tone_playable(622, music.beat(BeatFraction.BREVE)),
        music.PlaybackMode.UNTIL_DONE)
    basic.show_icon(IconNames.SAD)
input.on_button_pressed(Button.A, on_button_pressed_a)
