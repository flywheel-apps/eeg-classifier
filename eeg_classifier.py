import sys
import os
import re
import zipfile
import json


# Gear basics
input_folder = 'input/file/'
output_folder = 'output/'

# Declare the output path
output_filepath = os.path.join(output_folder, '.metadata.json')

# declare config file path
config_file_path = 'config.json'


# prepare container object for .metadata.json file
container = {
	'acquisition' : {
		'files' : []
	}
}

# prepare eeg file object / attributes to accumulate values from header file
eeg_obj = {
	'name': '',
	'modality': 'EEG',
	'measurements': ['eeg'],
	'info': {}
}

# initialize variables for processing loops
group_key = ''
vhdrfilename = ''


# pattern for identifying the header file in the zip archive file contents
vhdrfile = re.compile('^[^_.]\S+\.vhdr$')

# patterns for use in matching lines in the header file
group = re.compile('\[[\w ]*\]')
value = re.compile('[\w]+=')



print('\n\nStarting Brain Vision EEG Classifier...')


# Read config.json to get eeg filename
with open(config_file_path) as config_data:
    config = json.load(config_data)
    print('Config:', json.dumps(config, separators=(', ', ': '), sort_keys=True, indent=4))
    eeg_obj['name'] = config['inputs']['file']['location']['name']


# open the zip archive, find the headerfile, and read contents to eeg_obj
with zipfile.ZipFile(config['inputs']['file']['location']['path'],'r') as eegfile:
	print('\nopening archive file:' + config['inputs']['file']['location']['path'])
	for item in eegfile.infolist():
		if vhdrfile.search(item.filename):
			vhdrfilename = item.filename
			print('opening header file:' + item.filename)
			header_file = eegfile.read(vhdrfilename)
			header_file = header_file.decode('UTF-8')
			header_file = header_file.split('\n')
			for line in header_file:
				text = line.replace('\r','')
				if text.startswith('Brain Vision'):
					eeg_obj['info']['Header'] = text
					eeg_obj['info']['Vendor'] = 'Brain Vision'

				if group.match(text):
					group_key = text[1:len(text)-1]
					group_key = group_key.replace(' ','_')
					eeg_obj['info'][group_key] = {}

				if value.match(text):
					key,val = text.split('=')
					eeg_obj['info'][group_key][key] = val


container['acquisition']['files'].append(eeg_obj)
print('\npreparing to write container:\n', json.dumps(container, separators=(', ', ': '), sort_keys=True, indent=4))

with open(output_filepath,'w') as outfile:
	print('writing container to file:', output_filepath)
	json.dump(container,outfile, separators=(', ', ': '), sort_keys=True, indent=4)

print('\nJob completed successfully!!\n')
exit(0)




