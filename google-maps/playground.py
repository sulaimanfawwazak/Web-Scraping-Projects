from dataclasses import dataclass

# Define a class without `@dataclass` decorator
class RegularRectangle:
  def __init__(self, height, width):
    self.height = height
    self.width = width

@dataclass
class ModernRectangle:
  width: float
  height: float

# Define a class with `@dataclass` decorator, inherited fgrom `RegularRectangle` class
@dataclass
class RegularSquare(RegularRectangle):
  side: float

  def __post_init__(self):
    super().__init__(self.side, self.side)

# Define a class with `@dataclass` decorator, inherited fgrom `ModernRectangle` class
@dataclass
class ModernSquare(ModernRectangle):
  color: str

regular_square = RegularSquare(5)
modern_square = ModernSquare(5, 5, 'yellow') # We need to dfine the attributes, starting from the parent class

halo = 'tes a'
print(halo.strip('a'))

