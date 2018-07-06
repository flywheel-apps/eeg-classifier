[![Docker Pulls](https://img.shields.io/docker/pulls/flywheel/eeg-classifier.svg)](https://hub.docker.com/r/flywheel/eeg-classifier/)
[![Docker Stars](https://img.shields.io/docker/stars/flywheel/eeg-classifier.svg)](https://hub.docker.com/r/flywheel/eeg-classifier/)

# flywheel/eeg-classifier
Build context for a [Flywheel Gear](https://github.com/flywheel-io/gears/tree/master/spec) that classifies Brain Vision EEG data. This tool appends metadata attributes to the file's custom info structure within Flywheel. 

Input to this gear are Brain Vision EEG data files. 

Output is a JSON file (.metadata.json) containing metadata that will be used by the Flywheel platform to populate the input file's custom info fields.
