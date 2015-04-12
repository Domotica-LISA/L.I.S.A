class Transition(object):
	def __init__(self, toState):
		self.toState = toState

	def execute(self):
		print "Transitioning..."