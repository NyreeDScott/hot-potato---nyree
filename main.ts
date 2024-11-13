let timer = 0
input.onButtonPressed(Button.A, function () {
    music.setVolume(255)
    timer = randint(5, 15)
    basic.showLeds(`
        . # # # .
        # # # # #
        # # # # #
        # # # # #
        . # # # .
        `)
    while (timer > 0) {
        timer += -1
        basic.pause(1000)
    }
    music.play(music.tonePlayable(622, music.beat(BeatFraction.Breve)), music.PlaybackMode.UntilDone)
    basic.showIcon(IconNames.Sad)
})
