class FSM(object):
	def __init__(self, character):
		self.char = character
		self.states = {}
		self.transitions = {}
		self.curState = None
		self.prevState = None
		self.trans = None

	def add_transition(self, transName, transition):
		self.transitions[transName] = transition

	def add_state(self, stateName, state):
		self.states[stateName] = state

	def set_state(self, stateName):
		self.prevState = self.curState
		self.curState = self.states[stateName]

	def to_transition(self, toTrans):
		self.trans = self.transitions[toTrans]

	def execute(self):
		if self.trans:
			self.curState.exit()
			self.trans.execute()
			self.set_state(self.trans.to_state)
			self.curState.enter()
			self.trans = None
		self.curState.execute()