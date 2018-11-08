import random

# toppings, when randomizing  pepperoni = 0, mushrooms = 1, olives = 2, peppers = 3
pepperoni = 0
mushrooms = 0
olives = 0
peppers = 0
pizza = [pepperoni, mushrooms, olives, peppers]

def new_game():
	pepperoni = 0
	mushrooms = 0
	olives = 0
	peppers = 0

def topping_type():
	return random.randint(0,3)

def topping_action():
	# if even toppings will be added, if odd toppings will be removed 
	action =  random.randint(0,10)

	if action%2 == 0:
		action = 1
	else:
		action = -1
	return action

def add_toppings(action, number, topping):
	pizza[topping] = pizza[topping] + (action * number)


def make_pizza():
	for turn in xrange(0, 19):
		# get all things needed during turn
		action = topping_action() # add/remove
		number = random.randint(1,3) # number of that toppings added to pizza 
		topping = topping_type() # type of topping added to pizza

		# check that there are enough toppings of that type on pizza to remove
		if (action < 1) and (pizza[topping] < number):
			action = 1
			
		# check to make sure there are not too many toppings aleady on pizza or if adding the toppings will exceed max (6)
		if pizza[topping] >= 6 or (pizza[topping]+number) >=6:
			action = -1

		add_toppings(action, number, topping)

		# get topping type as a string
		if topping == 0:
			topping_str = "PEPPERONI"
		elif topping == 1:
			topping_str = "MUSHROOMS"	
		elif topping == 2:
			topping_str = "OLIVES"
		elif topping == 3:
			topping_str = "PEPPERS"
		else:
			topping_str = "ERROR: Topping type."

		# print instructions
		if action > 0:
			print "Add", number, topping_str, "to your pizza."
		elif action < 0:
			print "Remove", number, topping_str, "from your pizza."
		else:
			print "ERROR: Action"
	return


def main():
	make_pizza()
	print "You should have", pizza[0], "pepperoni,", pizza[1], "mushrooms,", pizza[2], "olives and", pizza[3], "peppers."
	return

if __name__== "__main__":
    main()