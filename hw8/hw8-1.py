from random import randrange

class Animal:
	
	def __init__(self, name):
		self.name = name

	def guess_who_am_i(self):
		e_hints = ["I have exceptional memory.", 
                      "I am the largest land-living mammal in the world.",
                      "I have a trunk."]
		t_hints = ["I am the biggest cat.",
                      "I come in black and white or orange and black.",
                      "I like Frosted Flakes."]
		b_hints = ["I use echo-location.",
                      "I can fly.",
                      "I see well in the dark."]
		
           # Create a dictionary to hold the proper list of hints
		d = {"elephant":e_hints, "tiger":t_hints, "bat":b_hints}
  
		for i in range(0,3):
                  print(d[self.name][i])
                  answer = input("Who am i? ")
                  if (answer == self.name):
                      print("You guessed it! The animal is " + self.name + ".")
                      break
                  else:
                      if (i == 2):
                          print("Nope! I am out of hints. The answer is " + self.name + ".")
                      else:
                          print("Nope! Guess again.")
                  
print("Animal Guessing Game")
print("I will give you up to three hints, and you try to guess the animal.")
print("Here goes...\n")
# Randomly select an animal from a list
animal_list = ["elephant", "tiger", "bat"]
an = Animal(animal_list[randrange(3)])
an.guess_who_am_i()

              

