def blink(coordinates: List[number]):
    led.plot(coordinates[0], coordinates[1])
    basic.pause(500)
    led.unplot(coordinates[0], coordinates[1])
    basic.pause(500)

def on_button_pressed_b():
    if direction == 0:
        basic.show_string("" + str((list2[1])))
        basic.clear_screen()
        update(list2)
        list2[1] = list2[0] - 1
    elif direction == 1:
        pass
    elif direction == 2:
        pass
    else:
        pass
input.on_button_pressed(Button.B, on_button_pressed_b)

def update(coordinates2: List[number]):
    led.unplot(coordinates2[0], coordinates2[1])
    return coordinates2
list2: List[number] = []
direction = 0
direction = 0
list2 = [2, 2]

def on_forever():
    blink(list2)
basic.forever(on_forever)
