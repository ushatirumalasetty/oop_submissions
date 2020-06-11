import math
class Car:
    HORN="Beep Beep"
    def __init__(self, max_speed, acceleration, tyre_friction,color=None):
        self.check_is_positive(max_speed,"max_speed")
        self.check_is_positive(acceleration,"acceleration")
        self.check_is_positive(tyre_friction,"tyre_friction")
        self._max_speed=max_speed
        self._acceleration=acceleration
        self._tyre_friction=tyre_friction
        self._color=color
        self._is_engine_started=False
        self._current_speed=0

    @property
    def max_speed(self):
        return self._max_speed
    @property
    def acceleration(self):
        return self._acceleration
    @property
    def tyre_friction(self):
        return self._tyre_friction
    @property
    def color(self):
        return self._color
    @property
    def is_engine_started(self):
        return self._is_engine_started
    @property
    def current_speed(self):
        return self._current_speed


    @ staticmethod
    def check_is_positive(check_item,check_item_name):
        if check_item<=0:
            raise ValueError(f"Invalid value for {check_item_name}")

    def start_engine(self):
        self._is_engine_started=True

    def accelerate(self):
        if self._is_engine_started==True:
            self._current_speed+=self._acceleration
            if self._current_speed>self._max_speed:
                self._current_speed=self._max_speed
        else:
            print("Start the engine to accelerate")

    def apply_brakes(self):
        self._current_speed-=self._tyre_friction
        if self._current_speed<0:
            self._current_speed=0

    def sound_horn(self):
        if self._is_engine_started==True:
            print(self.HORN)
        else:
            print("Start the engine to sound_horn")

    def stop_engine(self):
            self._is_engine_started=False

class Truck(Car):
    HORN="Honk Honk"

    def __init__(self,color,max_speed, acceleration, tyre_friction, max_cargo_weight):
        super().__init__( max_speed, acceleration, tyre_friction,color)
        self.check_is_positive(max_cargo_weight,"max_cargo_weight")
        self._max_cargo_weight=max_cargo_weight
        self._cargo_weight=0

    @property
    def max_cargo_weight(self):
        return self._max_cargo_weight
    @property
    def cargo_weight(self):
        return self._cargo_weight


    def load(self,weight):
        if weight<0:
            raise ValueError("Invalid value for cargo_weight")
        else:
            if self._current_speed==0:
                if self._cargo_weight+weight>self._max_cargo_weight:
                    print(f"Cannot load cargo more than max limit: {self._max_cargo_weight}")
                else:
                    self._cargo_weight+=weight
            else:
                print("Cannot load cargo during motion")

    def unload(self,weight):
        if weight<0:
            raise ValueError("Invalid value for cargo_weight")
        else:
            if self._current_speed==0:
                if self._cargo_weight-weight<0:
                    print("Cannot unload cargo less than min limit: 0")
                else:
                    self._cargo_weight-=weight
            else:
                print("Cannot unload cargo during motion")

class RaceCar(Car):
    HORN="Peep Peep\nBeep Beep"
    def __init__(self,color, max_speed, acceleration, tyre_friction):
        super().__init__( max_speed, acceleration, tyre_friction,color)
        self._nitro=0

    @property
    def nitro(self):
        return self._nitro


    def apply_brakes(self):
        if self._current_speed>(self._max_speed/2):
            self._nitro+=10
            super().apply_brakes()
        else:
            super().apply_brakes()

    def accelerate(self):
        if self._nitro:
            if self._is_engine_started==True:
                if self._current_speed!=self._max_speed:
                     self._current_speed+=(math.ceil((130/100)*self._acceleration))
                     if self._current_speed>self._max_speed:
                         self._current_speed=self._max_speed
                else:
                    self._current_speed=self._max_speed
                self._nitro-=10
            else:
               print("Start the engine to accelerate")
        else:
            super().accelerate()