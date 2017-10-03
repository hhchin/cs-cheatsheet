import subprocess
import yaml

base_fn = "cheatsheet_base.tex"
output_fn = "cheatsheet.tex"
yaml_fn = "master_cheatsheet.yml"

def main():
	with open(base_fn,'r') as fd:
		L = fd.readlines()
	in_dump = [l.rstrip() for l in L]

	with open(yaml_fn,'r') as fd:
		Y = yaml.load(fd)
	results = Y['cheatsheet']
	
	res_dump = []
	for res in results:
		res_dump.append('\\textbf{{{}}}: {}\\\\'.format(res['name'], res['result']))




	
	ind = 0
	for i in range(len(in_dump)):
		if in_dump[i]=='%%MAGIC%%':
			ind = i
			break

	out_dump = in_dump[:i] + res_dump + in_dump[i+1:]

	with open(output_fn,'w') as fd:
		for l in out_dump:
			fd.write(l)
			fd.write('\n')
	subprocess.call(['pdflatex', output_fn])
	

	
if __name__ == '__main__':
	main()