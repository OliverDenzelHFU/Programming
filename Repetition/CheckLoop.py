def grade(b,cell):
	if cell.stdout.startswith('0\n1\n2\n') and cell.stdout.endswith("10\n"):
		b.button_style = 'success'
	else:
		b.button_style = 'danger'