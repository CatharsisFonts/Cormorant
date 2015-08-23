#MenuTitle: Cormorant Rename Glyphs Custom Parameter
# -*- coding: utf-8 -*-
"""Injects and/or updates the Rename Glyphs custom parameters for all upright italics in the .glyphs file."""

import GlyphsApp



instanceNamePart = "SC "
Font = Glyphs.font

suffix = ".liga.toBeDeleted"
allSuffixedGlyphNames = [ g.name for g in Font.glyphs if g.name.endswith(suffix) ]
removeGlyphs1 = [ "%s" % x for x in allSuffixedGlyphNames ]
removeGlyphs2 = [ "%s" % x.replace(suffix,".liga") for x in allSuffixedGlyphNames ]
removeGlyphsParameterKey = "Remove Glyphs"

suffix = ".sc"
allSuffixedGlyphNames = [ g.name for g in Font.glyphs if g.name.endswith(suffix) ]
renameGlyphs = [ "%s=%s" % ( x, x.replace(suffix,"") ) for x in allSuffixedGlyphNames ]
renameGlyphsParameterKey = "Rename Glyphs"

for thisInstance in Font.instances:
	if instanceNamePart in thisInstance.name:
		thisInstance.removeObjectFromCustomParametersForKey_( removeGlyphsParameterKey )
		thisInstance.removeObjectFromCustomParametersForKey_( renameGlyphsParameterKey )
		thisInstance.setCustomParameter_forKey_( removeGlyphs1+removeGlyphs2, removeGlyphsParameterKey )
		thisInstance.setCustomParameter_forKey_( renameGlyphs, renameGlyphsParameterKey )



instanceNamePart = "Unicase "
Font = Glyphs.font

suffix = ".liga.toBeDeleted"
allSuffixedGlyphNames = [ g.name for g in Font.glyphs if g.name.endswith(suffix) ]
removeGlyphs1 = [ "%s" % x for x in allSuffixedGlyphNames ]
removeGlyphs2 = [ "%s" % x.replace(suffix,".liga") for x in allSuffixedGlyphNames ]
removeGlyphsParameterKey = "Remove Glyphs"

allSS03GlyphNames = [ g.name for g in Font.glyphs if g.name.endswith(".ss03") ]
allSCGlyphNames = [ g.name for g in Font.glyphs if g.name.endswith(".sc") ]
mundaneSCGlyphNames = [ x for x in allSCGlyphNames if x not in allSS03GlyphNames ]
renameMundaneGlyphs = [ "%s=%s" % ( x, x.replace(".sc","") ) for x in mundaneSCGlyphNames ]
renameSS03Glyphs = [ "%s=%s" % ( x, x.replace(".sc.ss03","") ) for x in allSS03GlyphNames ]
renameGlyphs = renameMundaneGlyphs + renameSS03Glyphs
renameGlyphsParameterKey = "Rename Glyphs"

for thisInstance in Font.instances:
	if instanceNamePart in thisInstance.name:
		thisInstance.removeObjectFromCustomParametersForKey_( removeGlyphsParameterKey )
		thisInstance.removeObjectFromCustomParametersForKey_( renameGlyphsParameterKey )
		thisInstance.setCustomParameter_forKey_( removeGlyphs1+removeGlyphs2, removeGlyphsParameterKey )
		thisInstance.setCustomParameter_forKey_( renameGlyphs, renameGlyphsParameterKey )
		thisInstance.setCustomParameter_forKey_( ["sc", "c2sc", "ss05"], "Remove Features" )



instanceNamePart = "Infant "
Font = Glyphs.font

suffix = ".ss06"
allSuffixedGlyphNames = [ g.name for g in Font.glyphs if g.name.endswith(suffix) ]
renameGlyphs = [ "%s=%s" % ( x, x.replace(suffix,"") ) for x in allSuffixedGlyphNames ]
renameGlyphsParameterKey = "Rename Glyphs"

for thisInstance in Font.instances:
	if instanceNamePart in thisInstance.name:
		thisInstance.removeObjectFromCustomParametersForKey_( renameGlyphsParameterKey )
		thisInstance.setCustomParameter_forKey_( renameGlyphs, renameGlyphsParameterKey )

