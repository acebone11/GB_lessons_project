import time


class TrafficLight:
    __color = ['red', 'yellow', 'green']


    def running(self):
        i = 0
        while i < 3:
            if i == 0:
                print(TrafficLight.__color[i])
                time.sleep(7)
            if i == 1 :
                print(TrafficLight.__color[i])
                time.sleep(2)
            if i == 2 :
                print(TrafficLight.__color[i])
                time.sleep(7)
            i += 1


f = TrafficLight()
f.running()
