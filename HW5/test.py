execfile("StrokeHMMbasic.py") ## StrokeHMMbasic.py
x = StrokeLabeler()
	x.trainHMMDir("../trainingFiles/")
x.testHMMDir("../trainingFiles/")