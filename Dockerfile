# EEG-Classifier

FROM python:slim
MAINTAINER Flywheel <support@flywheel.io>

# Make directory for flywheel spec (v0)
WORKDIR /flywheel/v0
COPY eeg_classifier.py ./run
COPY manifest.json  .
RUN chmod +x run manifest.json

# Set the entrypoint
ENTRYPOINT ["/flywheel/v0/run"]
