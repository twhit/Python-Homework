from tkinter import *
from tkinter import messagebox

class Puzzle:
	wordlist = [] # Answer key
     #foundlist determines which words have been found
	foundlist = [False,False,False,False,False,False,False,False,False,False]
	def __init__(self, letters, wordlist):
		self.letters = letters # The letters in the grid
		self.drawn = 0 # Used to make unique tags for each drawn oval
		for word in wordlist:
			self.wordlist.append(word)
	
	@classmethod
	def checkword(cls, word):
		found = False
            # Check both forwards...
		if(word in Puzzle.wordlist):
			c.delete("w" + str(cls.wordlist.index(word)+1))
			cls.foundlist[cls.wordlist.index(word)] = True
			found = True
            # And backwards
		elif(word[::-1] in wordlist):
			c.delete("w" + str(cls.wordlist.index(word[::-1])+1))
			cls.foundlist[cls.wordlist.index(word[::-1])] = True
			found = True
		if (False not in cls.foundlist): # No Falses left -- you win!
			messagebox.showinfo("Winner", "You found all the words!")
		return found

base = Tk()
base.resizable(0,0)

points = [] # Full list of drawn points
ptsx = [] # X-coordinates
ptsy = [] # Y-coordinates

#Puzzle fields are hard coded for now. Should come from DB.
str1 = "AHJAVAKJFHPNFQTRMOZTBSSCUGHAWMLYIJVEBKOLRNXQWURXYPEOLCNMVYBCPHXOREUWUXATGBCSHARPLYXOVFGEHTYPXLZAHPML"
wordlist = ["JAVA","HTML","CSS","PERL","PYTHON","RUBY","PHP","COBOL","CSHARP","JQUERY"]
p = Puzzle(str1, wordlist)

def surround():
	word = ""
     #Read column by column
	for x in range(1,11):
		incol = []
		ct = 0
		for ptx in ptsx:
          # If there are points in this column, add their Y-coords to incol
			if (ptx > x*60-10 and ptx < x*60+10):
				incol.append(ptsy[ct])
			ct += 1
		if (len(incol) > 0):
			for y in range(1,11):
                 # Now go down the column and determine which letters are circled
				if (y*60 > min(incol) and y*60 < max(incol)):
					word += str1[(y-1)*10+(x-1)]
	return word
					
def point(event):
    # Draw a series of points
	c.create_oval(event.x, event.y, event.x+1, event.y+1, fill="black", tags="drawn" + str(p.drawn))
	points.append(event.x)
     # Separate X and Y coords
	ptsx.append(event.x)
	points.append(event.y)	
	ptsy.append(event.y)
	return points

def fill(event):
    # This function fills lines between the points, to make a smoother looking oval.
	p.drawn += 1 # To mark unique tags
	try:
		c.create_line(points, tags="drawn" + str(p.drawn))
		del points[0:]
		if(not p.checkword(surround())):
          # If the circled letters don't form one of the words, delete the lines...
			c.delete("drawn" + str(p.drawn))
          # ...and the points.
			c.delete("drawn" + str(p.drawn - 1))
		del ptsx[0:] #clear lists
		del ptsy[0:] 
	except:
		print("Drawing Error!")

c = Canvas(base, bg="white", width=1000, height= 660)
c.configure(cursor="pencil")
c.pack()

c.bind("<B1-Motion>", point)
c.bind("<ButtonRelease-1>", fill)

ctr = 0
# Create the letter grid, and add the word list to the side.
for yval in range(1,11):
	c.create_text(750, yval*60, font=("Purisa",24), text=p.wordlist[yval-1], anchor="center", tag="w" + str(yval))
	for xval in range(1,11):
		c.create_text(xval*60, yval*60, font=("Purisa",24), text=str1[ctr], anchor="center")
		ctr += 1

base.mainloop()

