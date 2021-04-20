import machine
led = machine.Pin(2, machine.Pin.OUT)
led.high()


print("hello world")
for i in range(1, 11):
    print(i)

