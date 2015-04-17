# -*- coding: UTF-8 -*-
import yaml
import path_declarations

with open(path_declarations.config("config.yml"), "r") as f:
	config = yaml.safe_load(f)