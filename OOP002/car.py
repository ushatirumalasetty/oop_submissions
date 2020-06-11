import math
class Car:


    def __init__(self, acceleration,max_speed, tyre_friction,color=None):
        self._color=color
        self.acc(acceleration)
        self.tyre(tyre_friction)
        self.max(max_speed)
        self._is_engine_started=False
        self._current_speed=0
        self._horn='"Beep Beep"'




    def max(self,ace):
        if ace>=0:
            self._max_speed=ace
        else:
            #print("ValueError: Invalid value for max_speed")
            raise ValueError("Invalid value for max_speed")

    def tyre(self,ace):
        if ace>=0:
            self._tyre_friction=ace
        else:
            #print("ValueError: Invalid value for tyre_friction")
            raise ValueError("Invalid value for tyre_friction")

    def acc(self,ace):
        if ace>=0:
            self._acceleration=ace
        else:
            raise ValueError("Invalid value for acceleration")
            #raise ValueError: Invalid value for acceleration



    def start_engine(self):
        self._is_engine_started=True



    def accelerate(self):
        if self._is_engine_started==True:
             self._current_speed+=self._acceleration
             if self._current_speed>=self._max_speed:
                   self._current_speed=self._max_speed
        else:
            print("Start the engine to accelerate")


    def apply_brakes(self):
        if self._tyre_friction>self._current_speed:
            self._current_speed=0
        else:
            self._current_speed-=self._tyre_friction


    def sound_horn(self):
        if self._is_engine_started==True:
             print(self._horn)
        else:
            print("Start the engine to sound_horn")

    def stop_engine(self):
        if self.current_speed == 0 :
            self._is_engine_started=False
        else :
            raise ValueError("can't stop engine while in motion")


    @property
    def current_speed(self):
        return self._current_speed
    @property
    def max_speed(self):
        return self._max_speed
    @property
    def tyre_friction(self):
        return self._tyre_friction
    @property
    def color(self):
        return self._color
    @property
    def horn(self):
        return self._horn
    @property
    def is_engine_started(self):
        return self._is_engine_started

    @property
    def acceleration(self):
        return self._acceleration






class Truck(Car):

    def __init__(self,color, max_speed, acceleration, tyre_friction, max_cargo_weight):
         super().__init__( acceleration,max_speed, tyre_friction,color)

         self._horn="Honk Honk"
         self._max_cargo_weight=max_cargo_weight
         self._loads=0

    @property
    def max_cargo_weight(self):
        return self._max_cargo_weight

    @property
    def loads(self):
        return self._loads




    def load(self,weight):
        if self._current_speed==0:
            if weight<0:
               print("ValueError: Invalid value for cargo_weight")
               #ValueError: Invalid value for cargo_weight
            else:
               if (self._loads+weight)>self._max_cargo_weight:
                   print(f"Cannot load cargo more than max limit: {self._max_cargo_weight}")
               else:
                   self._loads+=weight
        else:
            print("Cannot load cargo during motion")



    def unload(self,weight):
        if self._current_speed==0:
            if weight<0:
               print("ValueError: Invalid value for cargo_weight")
               #ValueError: Invalid value for cargo_weight
            else:
               if (self._loads-weight)<0:
                   self._loads=0
                   print(f"Cannot unload cargo more than max limit: {self._max_cargo_weight}")
               else:
                   self._loads-=weight
        else:
            print("Cannot unload cargo during motion")


class RaceCar(Car):
    def __init__(self,color, max_speed, acceleration, tyre_friction):
        super().__init__(acceleration,max_speed, tyre_friction,color=None)
        self._horn="Peep Peep\nBeep Beep"
        self._nitro=0

    @property
    def nitro(self):
        return self._nitro


    def accelerate(self):
            if self._nitro:
               self._current_speed+=(math.ceil(130//100*(self._acceleration)))
               self._nitro-=10
            else:
                super._acceleration()

    def apply_brakes(self):
        if self._current_speed>(self._max_speed/2):
            self._nitro+=10
        else:
            super.apply_brakes()
# truck = Truck(color="Red", max_speed=250, acceleration=10, tyre_friction=3, max_cargo_weight=100)
# print(truck.color)