from time import clock
import wit
import classes.character

if __name__ == '__main__':
	wit.init('cards.pcm.default')
	lisa_fsm = classes.character.Lisa()
	while True:
		startTime = clock()
		timeInterval = 1
		while startTime + timeInterval > clock():
			pass
		lisa_fsm.Execute()
		if not lisa_fsm.Exit():
			break
	wit.close()
	print "Bye Bye!"