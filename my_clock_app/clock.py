# clock.py

from turtle import *
from datetime import datetime

class ClockApp:
    def __init__(self):
        self.second_hand = None
        self.minute_hand = None
        self.hour_hand = None
        self.writer = None

    def jump(self, distanz, winkel=0):
        penup()
        right(winkel)
        forward(distanz)
        left(winkel)
        pendown()

    def hand(self, laenge, spitze):
        fd(laenge*1.15)
        rt(90)
        fd(spitze/2.0)
        lt(120)
        fd(spitze)
        lt(120)
        fd(spitze)
        lt(120)
        fd(spitze/2.0)

    def make_hand_shape(self, name, laenge, spitze):
        reset()
        self.jump(-laenge*0.15)
        begin_poly()
        self.hand(laenge, spitze)
        end_poly()
        hand_form = get_poly()
        register_shape(name, hand_form)

    def clockface(self, radius):
        reset()
        pensize(7)
        for i in range(60):
            self.jump(radius)
            if i % 5 == 0:
                fd(25)
                self.jump(-radius-25)
            else:
                dot(3)
                self.jump(-radius)
            rt(6)

    def setup(self):
        mode("logo")
        self.make_hand_shape("second_hand", 125, 25)
        self.make_hand_shape("minute_hand",  130, 25)
        self.make_hand_shape("hour_hand", 90, 25)
        self.clockface(160)
        self.second_hand = Turtle()
        self.second_hand.shape("second_hand")
        self.second_hand.color("gray20", "gray80")
        self.minute_hand = Turtle()
        self.minute_hand.shape("minute_hand")
        self.minute_hand.color("blue1", "red1")
        self.hour_hand = Turtle()
        self.hour_hand.shape("hour_hand")
        self.hour_hand.color("blue3", "red3")
        for hand in self.second_hand, self.minute_hand, self.hour_hand:
            hand.resizemode("user")
            hand.shapesize(1, 1, 3)
            hand.speed(0)
        ht()
        self.writer = Turtle()
        self.writer.ht()
        self.writer.pu()
        self.writer.bk(85)

    def wochentag(self, t):
        wochentag = ["Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"]
        return wochentag[t.weekday()]

    def datum(self, z):
        monat = ["Jan.", "Feb.", "Mar.", "Apr.", "May", "June",
                 "July", "Aug.", "Sep.", "Oct.", "Nov.", "Dec."]
        j = z.year
        m = monat[z.month - 1]
        t = z.day
        return "%s %d %d" % (m, t, j)

    def tick(self):
        t = datetime.today()
        sekunde = t.second + t.microsecond*0.000001
        minute = t.minute + sekunde/60.0
        stunde = t.hour + minute/60.0
        try:
            tracer(False)  # Terminator can occur here
            self.writer.clear()
            self.writer.home()
            self.writer.forward(65)
            self.writer.write(self.wochentag(t),
                         align="center", font=("Courier", 14, "bold"))
            self.writer.back(150)
            self.writer.write(self.datum(t),
                         align="center", font=("Courier", 14, "bold"))
            self.writer.forward(85)
            self.second_hand.setheading(6*sekunde)  # or here
            self.minute_hand.setheading(6*minute)
            self.hour_hand.setheading(30*stunde)
            tracer(True)
            ontimer(self.tick, 100)
        except Terminator:
            pass  # turtledemo user pressed STOP

    def run(self):
        tracer(False)
        self.setup()
        tracer(True)
        self.tick()
        mainloop()

