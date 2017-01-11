#MenuTitle: Cormorant Batch Generate Fonts
# -*- coding: utf-8 -*-
__doc__="""
Cormorant Batch Generate Fonts.
"""


fileFolder = "~/Documents/Typography/Cormorant/GitHub/4. Glyphs Source Files"

otf_path = "~/Documents/Typography/Cormorant/GitHub/2. OpenType Files"
ttf_path = "~/Documents/Typography/Cormorant/GitHub/1. TrueType Font Files"
ufo_path = "~/Documents/Typography/Cormorant/GitHub/6. UFO Files"
web_path = "~/Documents/Typography/Cormorant/GitHub/3. Webfont Files"

OTF_AutoHint = True
TTF_AutoHint = True
RemoveOverlap = True
UseSubroutines = True
UseProductionNames = True


import os

fileFolder = os.path.expanduser(fileFolder)
fileNames = os.listdir(fileFolder)

for fileName in fileNames:
	if os.path.splitext(fileName)[1] == ".glyphs":
		font = GSFont(os.path.join(fileFolder, fileName))
		print font.familyName
		for instance in font.instances:
			print "== Exporting OTF =="
			print instance.generate(Format = "OTF", FontPath = os.path.expanduser(otf_path), AutoHint = OTF_AutoHint, RemoveOverlap = RemoveOverlap, UseSubroutines = UseSubroutines, UseProductionNames = UseProductionNames)
		print
		for instance in font.instances:
			print "== Exporting TTF =="
			print instance.generate(Format = "TTF", FontPath = os.path.expanduser(ttf_path), AutoHint = TTF_AutoHint, RemoveOverlap = RemoveOverlap, UseProductionNames = UseProductionNames)
		print
		#for instance in font.instances:
		#	print "== Exporting WOFF =="
		#	print instance.generate(Format = "WOFF", FontPath = os.path.expanduser(web_path), AutoHint = TTF_AutoHint, RemoveOverlap = RemoveOverlap, UseSubroutines = UseSubroutines, UseProductionNames = UseProductionNames)
		#print