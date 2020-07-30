# OOP 복습!

개의 속성과 행위를 정의하는 Doggy 클래스 만들기

``` python
class Doggy:
    num_of_dog = 0
    birth_of_dog = 0
    def __init__(self, name, species):
        self.name = name
        self.species = species
        Doggy.num_of_dog += 1
        Doggy.birth_of_dog += 1
        
    def __def__(self):
        Doggy.num_of_dog -= 1
        
    def bark(self):
        return '왈왈!'
    
    @classmethod
    def get_status(cls):
        return f'Birth : {cls.birth_of_dog}, Current : {cls.num_of_dog}'
```

