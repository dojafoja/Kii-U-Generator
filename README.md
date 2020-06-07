# Kii-U-Generator

This is my take, a Python implementation, of the Wii U title-key generating algorithm that recently surfaced online.
Title keys are a pbkdf2 hash with sha1 base. A md5 hash of a 'secret' with the title id, minus the prefixed 00 padding, appended to it is used as salt. It needs to be hashed with 20 iterations to produce the correct title key.

Usage:

First, open the ckey.json file and enter the common key as plaintext. This is a json file so keep the structure as is.

Then there are multiple ways to use this tool.
1: You can use the included GUI by running gui.py.
2: You can use this as a CLI tool. Run keygen.py [title_id] [password].
The password argument is optional and will default to mypass if it's not included. This seems correct for all games that it has been tested on. System titles, however, require a different password. The password is used as part of the generation algorithm for producing the pbkdf2 hash.
3: You can include keygen.py in your Python script and use as a library. Please read the source to see the functions available.
