class FSM(object):
	def __init__(self, character):
		self.char = character
		self.states = {}
		self.transitions = {}
		self.curState = None
		self.prevState = None
		self.trans = None

	def AddTransition(self, transName, transition):
		self.transitions[transName] = transition

	def AddState(self, stateName, state):
		self.states[stateName] = state

	def SetState(self, stateName):
		self.prevState = self.curState
		self.curState = self.states[stateName]

	def ToTransition(self, toTrans):
		self.trans = self.transitions[toTrans]

	def Execute(self):
		if self.trans:
			self.curState.Exit()
			self.trans.Execute()
			self.SetState(self.trans.toState)
			self.curState.Enter()
			self.trans = None
		self.curState.Execute()

	def ShutDown(self):
		return self.curState.Enter()
		#if self.curState == classes.states.ShutDown:
			#return True