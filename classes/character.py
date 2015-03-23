import fsm
import states
import transitions
import brain

Char = type("Char", (object, ), {})

class Lisa(Char):
	def __init__(self):
		self.FSM = fsm.FSM(self)
		self.brain = brain.Brain()
		##print(self.brain.modules)

		## STATES
		self.FSM.AddState("Wait", states.Wait(self.FSM))
		self.FSM.AddState("Scanning", states.Scanning(self.FSM))
		self.FSM.AddState("Move", states.Move(self.FSM))
		self.FSM.AddState("Track", states.Track(self.FSM))
		self.FSM.AddState("ShutDown", states.Track(self.FSM))

		## TRANSITIONS
		self.FSM.AddTransition("toWait", transitions.Transition("Wait"))
		self.FSM.AddTransition("toScanning", transitions.Transition("Scanning"))
		self.FSM.AddTransition("toMove", transitions.Transition("Move"))
		self.FSM.AddTransition("toTrack", transitions.Transition("Track"))
		self.FSM.AddTransition("toShutDown", transitions.Transition("ShutDown"))

		self.FSM.SetState("Wait")

	def Execute(self):
		self.FSM.Execute()

	def ShutDown(self):
		return self.FSM.ShutDown()