#!/usr/bin/env python3

import os

import jinja2

loader = jinja2.FileSystemLoader('templates')
jinja_env = jinja2.Environment(loader=loader, auto_reload=False)
for template_name in jinja_env.list_templates():
	if template_name == 'base.jinja2':
		continue
	template = jinja_env.get_template(template_name)
	output_path = template_name.replace('.jinja2', '.html')
	print(template_name, '→', output_path)

	depth = template_name.count('/')
	prefix = '../' * depth
	active_nav = template_name.split('/', 1)[0].replace('.jinja2', '')
	with open(output_path, 'w') as f:
		f.write(template.render(prefix=prefix, active_nav=active_nav))
