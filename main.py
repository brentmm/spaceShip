import random #importing random for warp method

class spaceShip(): #defining ship characteristics
  def __init__(self, shipName, shipLocation = 0, shipFuel = 100):
    self.name = shipName
    self.location = shipLocation
    self.fuel = shipFuel

  def fly(self): #fly method
    if self.location < 62843036:
      self.location += 10000000
      self.fuel -= 1
    else:
      self.location = 62843036

  def __str__(self): #returns ships information
    return "The spaceship " + str(self.name)  + " is " + str(self.location) + " km from Earth and has " + str(self.fuel) + "% of its fuel remaining."

class warpShip(spaceShip): #defining warp ship characteristics
  def __init__(self, shipName, shipLocation = 0, shipFuel = 100):
    super().__init__(shipName, shipLocation, shipFuel)
    self.warps = 5
    
  def warp(self): #warp method
    if self.warps > 0:
      self.location += random.randint(0, 60000000) #generates random warp distance
      self.fuel -=3
      self.warps -= 1
    else:
      print("No warps remain.")

  def __str__(self): #returns warp ship info
    return "The spaceship " + str(self.name)  + " is " + str(self.location) + " km from Earth and has " + str(self.fuel) + "% of its fuel remaining." + " There are " + str(self.warps) + " warps remaining."

#assigning variables and names to classes
shipOne = spaceShip("Patriot I")
shipTwo = warpShip("Patriot II")
launch = 1 #setting launch value

while launch == 1: #running ship launch
  if shipOne.location < 62843036:
    shipOne.fly() 
  else:
    shipOne.location = 62843036
    print("Patriot I has landed on Jupiter")
    launch +=1
  print(shipOne)
  print()

while launch == 2: #running warp ship launch
  if shipTwo.warps > 0:
    shipTwo.warp()
  elif shipTwo.location < 62843036:
    shipTwo.fly() 
  else:
    shipTwo.location = 62843036
    print("Patriot II has landed on Jupiter")
    launch +=1
  print(shipTwo)
  print()