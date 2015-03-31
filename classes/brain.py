import pkgutil
import path_declarations
import config

class Brain(object):
	def __init__(self):
		self.modules = self.get_modules()

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
		return modules

	def query(self, text):
		for module in self.modules:
			if module.isValid(text):
				try:
					module.handle(text, tts.GoogleTTS())
				except:
					#self.speaker.say("Sorry. Ik heb problemen met het uitvoeren daarvan. " +
							#"Probeer het later nog eens.")
					print "doei"
				finally:
					return
