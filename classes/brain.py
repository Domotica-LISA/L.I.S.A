# -*- coding: UTF-8 -*-
import pkgutil
import path_declarations
import config
from tts import GoogleTTS
from stt import WitAiSTT
from mic import Mic

class Brain(object):
	def __init__(self):
		self.modules = self.get_modules()
		self.speaker = GoogleTTS()
		self.mic = Mic(WitAiSTT(config.config['wit_ai_token']))
		self.ledRingColor = {
			"red": 30,
			"green": 0,
			"blue": 30}

	@classmethod
	def get_modules(cls):
		locations = [path_declarations.modulePath]
		modules = []
		for finder, name, ispkg in pkgutil.walk_packages(locations):
			try:
				loader = finder.find_module(name)
				mod = loader.load_module(name)
				#print mod
			except:
				print("We made a booboo")
			else:
				if hasattr(mod, "WORDS") and name not in config.config['modules']:
					modules.append(mod)
				elif hasattr(mod, "WORDS") and config.config['modules'][name] == True:
					modules.append(mod)
			modules.sort(key=lambda mod: mod.PRIORITY if hasattr(mod, 'PRIORITY')
                     else 0, reverse=True)
		#print modules
		return modules

	def query(self, text):
		for module in self.modules:
			if module.is_valid(text):
				try:
					module.handle(text, self.speaker, self.mic, config.config)
				except:
					self.speaker.say("Sorry. Ik heb problemen met het uitvoeren daarvan. " +
							"Probeer het later nog eens.")
				finally:
					return
