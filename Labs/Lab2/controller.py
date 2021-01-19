import random
import datetime
import time
from Labs.Lab2.asteroid import Asteroid
from Labs.Lab2.vector import Vector


class Controller:

    asteroid_list = []

    def __init__(self):
        for i in range(100):
            radius = random.randrange(1, 4)
            position = Vector(random.randint(0, 100), random.randint(0, 100), random.randint(0, 100))
            velocity = Vector(random.randint(0, 5), random.randint(0, 5), random.randint(0, 5))
            asteroid = Asteroid(radius, position, velocity)
            self.asteroid_list.append(asteroid)

    def simulate(self, seconds):
        current_time = time.time()
        seconds_to_wait = int(current_time + 1) - current_time
        start_time = current_time + seconds_to_wait
        time.sleep(seconds_to_wait)
        print("Simulation Start Time: ", datetime.datetime.now())
        print("\nMoving Asteroids!")
        print("-----------------")
        while time.time() <= (start_time + seconds):
            for asteroid in self.asteroid_list:
                print(f"Asteroid {asteroid.get_asteroid_id()} Moved! Old Pos: {asteroid.get_position()} -> New Pos: {asteroid.move()}")
                print(f"Asteroid {asteroid.get_asteroid_id()} is currently at {asteroid.get_position()} and moving at {asteroid.get_velocity()} "
                      f"metres per second. It has a circumference of {asteroid.get_circumference()}")
            time.sleep(1)
            print()


if __name__ == "__main__":
    controller = Controller()
    controller.simulate(5)
