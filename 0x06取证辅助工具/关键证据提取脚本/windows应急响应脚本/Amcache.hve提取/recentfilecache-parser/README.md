RecentFileCache.bcf (RFC) Parser
=================================

Reference: journeyintoir.blogspot.com/2013/12/revealing-recentfilecachebcf-file.html

Help:
				python rfcparse.py -h
				
				usage: rfcparse.py [-h] [-f RECENTFILECACHE]
				
				Parse the RecentFileCache.bcf file on Windows 7.
				
				optional arguments:
				  -h, --help            show this help message and exit
				  -f RECENTFILECACHE, --recentfilecache RECENTFILECACHE
				                        Path to the RecentFileCache.bcf file.
				                        
Output:
				python rfcparse.py -f RecentFileCache.bcf
				
				c:\windows\system32\w32tm.exe
				c:\program files\vmware\vmware tools\tpautoconnsvc.exe
				c:\program files\vmware\vmware tools\tpvcgateway.exe
				c:\program files\vmware\vmware tools\vmtoolsd.exe
				c:\program files\common files\vmware\drivers\vss\comreg.exe
				c:\program files\vmware\vmware tools\poweron-vm-default.bat
				c:\program files\vmware\vmware tools\tpautoconnect.exe
				c:\program files\vmware\vmware tools\vmwareresolutionset.exe
