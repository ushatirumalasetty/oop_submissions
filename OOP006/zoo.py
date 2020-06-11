class animal():
    SOUND=""
    BREATH=""

    def __init__(self,age_in_months, breed, required_food_in_kgs):
        if age_in_months!=1:
            raise ValueError(f"Invalid value for field age_in_months: {age_in_months}")
        else:
            self.age_in_months=age_in_months
        if type(breed)!=str:
            raise ValueError(f"Invalid value for field breed: {breed}")
        else:
            self.breed=breed
        if required_food_in_kgs<=0:
            raise ValueError(f"Invalid value for field age_in_months: {required_food_in_kgs}")
        else:
            self.required_food_in_kgs=required_food_in_kgs
        self.growth=1
        self.food_growth=0

    def grow(self):
        self.age_in_months+=self.growth
        self.required_food_in_kgs+=self.food_growth

    @classmethod
    def make_sound(cls):
        print(cls.SOUND)

    @classmethod
    def breathe(cls):
        print(cls.BREATH)

    def __str__(self):
        return f"{self.age_in_months} {self.breed} {self.required_food_in_kgs}"

class Deer(animal):
    SOUND="Buck Buck"
    BREATH="Breathe in air"

    def __init__(self,age_in_months, breed, required_food_in_kgs):
        super().__init__(age_in_months, breed, required_food_in_kgs)
        self.food_growth=2

class Lion(animal):
    SOUND="Roar Roar"
    BREATH="Breathe in air"

    def __init__(self,age_in_months, breed, required_food_in_kgs):
        super().__init__(age_in_months, breed, required_food_in_kgs)
        self.food_growth=4

    def hunt(self,zoo_obj):
        for i in zoo_obj.animals_list:
            if isinstance(i,Deer):
                zoo_obj.animal_list.remove(i)
                zoo_obj.animals_count-=1
                zoo_obj.count_of_all_animals_in_zoos-=1



class Shark(animal):
    SOUND="Shark Sound"
    BREATH="Breathe oxygen from water"

    def __init__(self,age_in_months, breed, required_food_in_kgs):
        super().__init__(age_in_months, breed, required_food_in_kgs)
        self.food_growth=8

    def hunt(self,zoo_obj):
        for i in zoo_obj.animals_list:
            if isinstance(i,GoldFish):
                zoo_obj.animal_list.remove(i)
                zoo_obj.animals_count-=1
                zoo_obj.count_of_all_animals_in_zoos-=1


class GoldFish(animal):
    SOUND="Hum Hum"
    BREATH="Breathe oxygen from water"

    def __init__(self,age_in_months, breed, required_food_in_kgs):
        super().__init__(age_in_months, breed, required_food_in_kgs)
        self.food_growth=0.2

class Snake(animal):
    SOUND="Hiss Hiss"
    BREATH="Breathe in air"

    def __init__(self,age_in_months, breed, required_food_in_kgs):
        super().__init__(age_in_months, breed, required_food_in_kgs)
        self.food_growth=0.5

    def hunt(self,zoo_obj):
        for i in zoo_obj.animals_list:
            if isinstance(i,Deer):
                zoo_obj.animal_list.remove(i)
                zoo_obj.animals_count-=1
                zoo_obj.count_of_all_animals_in_zoos-=1



class Zoo():
    count_of_all_animals_in_zoos=0
    def __init__(self):
        self.reserved_food_in_kgs=0
        self.animals_list=[]
        self.animals_count=0

    def add_food_to_reserve(self,quantity):
        self.reserved_food_in_kgs+=quantity

    def add_animal(self,details):
        self.animals_list.append(details)
        self.animals_count+=1
        type(self).count_of_all_animals_in_zoos+=1


    @classmethod
    def count_animals_in_all_zoos(cls):
        return cls.count_of_all_animals_in_zoos
    @staticmethod
    def count_animals_in_given_zoos(zoo_obj):
        return sum([i.animals_count for i in zoo_obj])

    def count_animals(self):
        return self.animals_count

    def feed(self,animal_name):
        if self.reserved_food_in_kgs>=animal_name.required_food_in_kgs:
            self.reserved_food_in_kgs-=animal_name.required_food_in_kgs
            animal_name.grow()








