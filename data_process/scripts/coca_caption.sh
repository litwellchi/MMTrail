#!/bin/bash

# Ensure the script takes two arguments: video directory and output directory
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <video_directory> <output_directory>"
    exit 1
fi

INPUT_JSON=$1
OUTPUT_JSON=$2

python3 utils/coca.py --input_json "$INPUT_JSON" --output_json "$OUTPUT_JSON"