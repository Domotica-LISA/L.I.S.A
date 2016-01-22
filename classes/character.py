# -*- coding: UTF-8 -*-
import fsm
import states
import transitions
import brain

Char = type("Char", (object, ), {})

class Lisa(Char):
	def __init__(self):
		self.fSM = fsm.FSM(self)
		self.brain = brain.Brain()
		##print(self.brain)

		## STATES
		self.fSM.add_state("Startup", states.Startup(self.fSM, self.brain))
		self.fSM.add_state("Scanning", states.Scanning(self.fSM, self.brain))
		self.fSM.add_state("Move", states.Move(self.fSM, self.brain))
		self.fSM.add_state("Track", states.Track(self.fSM, self.brain))
		self.fSM.add_state("Shutdown", states.Shutdown(self.fSM, self.brain))
		self.fSM.add_state("DemoStartup", states.DemoStartup(self.fSM, self.brain))
		self.fSM.add_state("Demo", states.Demo(self.fSM, self.brain))

		## TRANSITIONS
		self.fSM.add_transition("toStartup", transitions.Transition("Startup"))
		self.fSM.add_transition("toScanning", transitions.Transition("Scanning"))
		self.fSM.add_transition("toMove", transitions.Transition("Move"))
		self.fSM.add_transition("toTrack", transitions.Transition("Track"))
		self.fSM.add_transition("toShutdown", transitions.Transition("Shutdown"))
		self.fSM.add_transition("toDemoStartup", transitions.Transition("DemoStartup"))
		self.fSM.add_transition("toDemo", transitions.Transition("Demo"))

		self.fSM.set_state("DemoStartup")

	def execute(self):
		self.fSM.execute()
