let coordinates = [2, 2]
let direction = 0
basic.forever(function () {
    led.plot(coordinates[0], coordinates[1])
    basic.pause(500)
    led.unplot(coordinates[0], coordinates[1])
    basic.pause(500)
})
