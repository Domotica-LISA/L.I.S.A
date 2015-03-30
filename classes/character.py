import fsm
import states
import transitions
import brain
import tts

Char = type("Char", (object, ), {})

class Lisa(Char):
	def __init__(self):
		self.FSM = fsm.FSM(self)
		self.brain = brain.Brain(tts.GoogleTTS())
		##print(self.brain.modules)

		## STATES
		self.FSM.AddState("Startup", states.Startup(self.FSM, self.brain))
		self.FSM.AddState("Scanning", states.Scanning(self.FSM, self.brain))
		self.FSM.AddState("Move", states.Move(self.FSM, self.brain))
		self.FSM.AddState("Track", states.Track(self.FSM, self.brain))
		self.FSM.AddState("Shutdown", states.Shutdown(self.FSM, self.brain))

		## TRANSITIONS
		self.FSM.AddTransition("toStartup", transitions.Transition("Startup"))
		self.FSM.AddTransition("toScanning", transitions.Transition("Scanning"))
		self.FSM.AddTransition("toMove", transitions.Transition("Move"))
		self.FSM.AddTransition("toTrack", transitions.Transition("Track"))
		self.FSM.AddTransition("toShutdown", transitions.Transition("Shutdown"))

		self.FSM.SetState("Startup")

	def Execute(self):
		self.FSM.Execute()
