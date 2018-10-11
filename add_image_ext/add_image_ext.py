#!/usr/bin/env python

import subprocess
import sys

args = sys.argv
image_path = args[1]
print(image_path)

identify_process = subprocess.run(
    [
        'identify',
        '-format',
        '%m',
        image_path
    ],
    stdout=subprocess.PIPE
)
ext = identify_process.stdout.decode('utf-8').lower()

mv_process = subprocess.run(
    [
        'mv',
        image_path,
        './{}.{}'.format(image_path.split('.')[0], ext)
    ]
)
