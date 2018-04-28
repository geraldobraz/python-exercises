import math
class Sphere(object):
    def __init__(self, raio, massa):
        self.radius = raio
        self.mass = massa
    def get_radius(self):
        return self.radius
    def get_mass(self):
        return self.mass
    def get_volume(self):
        return round(((4.0/3.0)*(math.pi*(self.radius**3))),5)
    def get_surface_area(self):
        return round(4*math.pi*(self.radius**2),5)
    def get_density(self):
        return round(self.mass/self.get_volume(),6)

ball = Sphere(2,50)

print(ball.get_radius())
print(ball.get_mass())
print(ball.get_volume())
print(ball.get_surface_area())
print(ball.get_density())