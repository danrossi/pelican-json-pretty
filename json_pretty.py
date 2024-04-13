from pelican import signals
import json
import yaml

def to_pretty_json(value):
	#print(value)
	try:
		return json.dumps(value, sort_keys=True, indent=4)
	except Exception as e:
		print(value)
		print(e)


def to_json(value):
	#print(value)
	try:
		return yaml.safe_load(value)
		#return json.loads(value)
	except Exception as e:
		#print(value)
		print(e)

def to_json_pretty(value):
	#print(value)
	return to_pretty_json(json.loads(value))

def unescape_functions(value):
	return value.replace('"tokenService"','tokenService')

def add_filter(pelican):
    pelican.env.filters.update({'json_pretty': to_pretty_json })
    pelican.env.filters.update({'to_json': to_json })
    pelican.env.filters.update({'to_json_pretty': to_json_pretty })
    pelican.env.filters.update({'unescape_functions': unescape_functions })

def register():
    """Plugin registration."""
    signals.generator_init.connect(add_filter)