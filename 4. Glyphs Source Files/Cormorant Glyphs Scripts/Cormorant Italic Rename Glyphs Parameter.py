#MenuTitle: Cormorant Italic Rename Glyphs Custom Parameter
# -*- coding: utf-8 -*-
"""Injects and/or updates the Rename Glyphs custom parameters for all upright italics in the .glyphs file."""

import GlyphsApp

# Infant
Font = Glyphs.font

all02names = [ g.name for g in Font.glyphs if (g.name.find(".ss02") > 0) ]
all03names = [ g.name for g in Font.glyphs if (g.name.find(".ss03") > 0) ]
all10names = [ g.name for g in Font.glyphs if (g.name.find(".ss10") > 0) ]
allLFnames = [ g.name for g in Font.glyphs if (g.name.find(".lf") > 0) ]

badones = [ name for name in all02names if ((name.replace(".ss02",".ss03") in all03names) or (name.replace(".ss02",".lf") in allLFnames)) ]
for b in badones: all02names.remove( b )

rename02 = [ "%s=%s" % ( x, x.replace(".ss02","") ) for x in all02names ]
rename03 = [ "%s=%s" % ( x, x.replace(".ss03","") ) for x in all03names ]
rename10 = [ "%s=%s" % ( x, x.replace(".ss10","") ) for x in all10names ]
renameLF = [ "%s=%s" % ( x, x.replace(".lf","") ) for x in allLFnames ]

renameGlyphs = rename02 + rename03 + rename10 + renameLF

decomposeGlyphs = [g.name for g in Font.glyphs]

#removeGlyphs = [ g.name for g in Font.glyphs if (g.name.find(".loclBGR") > 0)]

for thisInstance in Font.instances:
	parameterFamilyName = thisInstance.customValueForKey_("familyName")
	if parameterFamilyName:
		familyName = parameterFamilyName
	else:
		familyName = Font.familyName
	if familyName.startswith("Cormorant Infant"):
		thisInstance.removeObjectFromCustomParametersForKey_( "Decompose Glyphs" )
		thisInstance.removeObjectFromCustomParametersForKey_( "Rename Glyphs" )
		thisInstance.setCustomParameter_forKey_( decomposeGlyphs, "Decompose Glyphs" )
		thisInstance.setCustomParameter_forKey_( renameGlyphs, "Rename Glyphs" )
		thisInstance.setCustomParameter_forKey_( ["onum", "ss02", "ss03"], "Remove Features" )
#		thisInstance.setCustomParameter_forKey_( removeGlyphs, "Remove Glyphs" )


# Garamond
Font = Glyphs.font

suffix = ".ss02"
allSuffixedGlyphNames = [ g.name for g in Font.glyphs if g.name.endswith(suffix) ]
renameGlyphs1 = [ "%s=%s" % ( x, x.replace(suffix,"") ) for x in allSuffixedGlyphNames ]
renameGlyphsParameterKey = "Rename Glyphs"

decomposeGlyphs = [g.name for g in Font.glyphs]

for thisInstance in Font.instances:
	parameterFamilyName = thisInstance.customValueForKey_("familyName")
	if parameterFamilyName:
		familyName = parameterFamilyName
	else:
		familyName = Font.familyName
	if familyName.startswith("Cormorant Garamond"):
		thisInstance.removeObjectFromCustomParametersForKey_( "Decompose Glyphs" )
		thisInstance.removeObjectFromCustomParametersForKey_( renameGlyphsParameterKey )
		thisInstance.setCustomParameter_forKey_( decomposeGlyphs, "Decompose Glyphs" )
		thisInstance.setCustomParameter_forKey_( renameGlyphs1, renameGlyphsParameterKey )
		thisInstance.setCustomParameter_forKey_( ["ss02"], "Remove Features" )


