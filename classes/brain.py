import pkgutil
import path_declarations
import config
import tts

class Brain(object):
	def __init__(self):
		self.modules = self.get_modules()
		self.speaker = tts.GoogleTTS()

	@classmethod
	def get_modules(cls):
		locations = [path_declarations.MODULE_PATH]
		modules = []
		for finder, name, ispkg in pkgutil.walk_packages(locations):
			try:
				loader = finder.find_module(name)
				mod = loader.load_module(name)
				#print mod
			except:
				print("We made a booboo")
			else:
				if hasattr(mod, "WORDS") and config.config['modules'][name] == True:
					modules.append(mod)
				elif hasattr(mod, "WORDS") and config.config['modules'][name] == None:
					modules.append(mod)
				elif mod.__name__ == "default":
					modules.append(mod)
		print modules
		return modules

	def query(self, text):
		for module in self.modules:
			if module.isValid(text):
				try:
					module.handle(text, self.speaker)
				except:
					self.speaker.say("Sorry. Ik heb problemen met het uitvoeren daarvan. " +
							"Probeer het later nog eens.")
				finally:
					return
