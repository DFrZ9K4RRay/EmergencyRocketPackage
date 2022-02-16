'''
The MIT License (MIT)

Copyright (c) 2015 Patrick Olsen

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

Author: Patrick Olsen
Email: patrick.olsen@sysforensics.org
Twitter: @patrickrolsen
'''
import os
import struct
import argparse
from stat import *

def main():
    parser = argparse.ArgumentParser(description='Parse the RecentFileCache.bcf file on Windows 7.')
    parser.add_argument('-f', '--infile', help='Path to the RecentFileCache.bcf file.')
    args = parser.parse_args()

    if args.infile:
        input_file = args.infile
    else:
        print "You need to specify the RecentFileCache.bcf file."
        exit(0)

    with open(input_file, "rb") as f:
        #Offset
        offset = 0x14       
        # File Size
        file_size = os.stat(input_file)[6]
        # Go to beginning of file.
        f.seek(0)
        # Read forward 0x14 (20).
        f.seek(offset)
        while (offset < file_size):
            try:
                rl = struct.unpack('>B',f.read(4)[0])[0]
                fnlen = (rl + 1) * 2
                print f.read(fnlen).replace('\x00', '')
                file_size = offset + fnlen
            
            except IndexError as e:
                exit(0)

if __name__ == "__main__":
    main()