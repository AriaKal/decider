# Help you make important decisions foolishly :P

import random

INTRO = "\nHello, I'm Decider. Your very own super smart decision maker. Just think of a decision you can't make and let me do my magic to help you out."
ANSWERS = ["Go for it!","Forget about it!", "Better off without it.", "Go for the healthier option!", "Yes, Yes, Yes!", "Never do that." , "Think about it, really deeply." ,"Sure, why not?",
		"No Way Jose", "A thousand times yes", "I think yes","Hell Yeah!","Never say never","Why not?","Definitely, positively, yes!","It's a big no-no","Y-E-S","Nah"]
MISTAKE = "\nDidn't catch that. My vocabulary is limited to 'decide' and 'exit.'"
HELP = "Type 'Decide' for a decision or 'Exit' to quit.\n"
OUTRO = "\nSee ya later!"

print(INTRO)
while(True):
	print(HELP)
	response = input()
	if(response.lower() == "decide"):
		print("\n"+random.choice(ANSWERS)+"\n")
	elif(response == "exit"):
		print(OUTRO)
		break
	else:
		print(MISTAKE)