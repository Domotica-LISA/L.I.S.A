class Transition(object):
	def __init__(self, toState):
		self.toState = toState

	def Execute(self):
		print "Transitioning..."