#!/bin/bash

# Ensure the script takes two arguments: video directory and output directory
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <video_directory> <output_directory>"
    exit 1
fi

VIDEO_DIR=$1
OUTPUT_DIR=$2

# Run the Python script
python3 utils/scenecut.py --vid_dir "$VIDEO_DIR" --out_dir "$OUTPUT_DIR"