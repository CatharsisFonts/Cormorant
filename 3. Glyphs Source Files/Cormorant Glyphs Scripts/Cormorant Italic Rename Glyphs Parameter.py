#MenuTitle: Cormorant Italic Rename Glyphs Custom Parameter
# -*- coding: utf-8 -*-
"""Injects and/or updates the Rename Glyphs custom parameters for all upright italics in the .glyphs file."""

import GlyphsApp

# Infant
Font = Glyphs.font

suffix = ".ss03"
allSuffixedGlyphNames = [ g.name for g in Font.glyphs if g.name.endswith(suffix) ]
renameGlyphs1 = [ "%s=%s" % ( x, x.replace(suffix,"") ) for x in allSuffixedGlyphNames ]
renameGlyphsParameterKey = "Rename Glyphs"

suffix = ".lf"
allSuffixedGlyphNames = [ g.name for g in Font.glyphs if g.name.endswith(suffix) ]
renameGlyphs2 = [ "%s=%s" % ( x, x.replace(suffix,"") ) for x in allSuffixedGlyphNames ]


for thisInstance in Font.instances:
	parameterFamilyName = thisInstance.customValueForKey_("familyName")
	if parameterFamilyName:
		familyName = parameterFamilyName
	else:
		familyName = Font.familyName
	if familyName.startswith("Cormorant Infant"):
		thisInstance.removeObjectFromCustomParametersForKey_( renameGlyphsParameterKey )
		thisInstance.setCustomParameter_forKey_( renameGlyphs1+renameGlyphs2, renameGlyphsParameterKey )
		thisInstance.setCustomParameter_forKey_( ["onum", "ss03"], "Remove Features" )


# Garamond
Font = Glyphs.font

suffix = ".ss02"
allSuffixedGlyphNames = [ g.name for g in Font.glyphs if g.name.endswith(suffix) ]
renameGlyphs1 = [ "%s=%s" % ( x, x.replace(suffix,"") ) for x in allSuffixedGlyphNames ]
renameGlyphsParameterKey = "Rename Glyphs"

for thisInstance in Font.instances:
	parameterFamilyName = thisInstance.customValueForKey_("familyName")
	if parameterFamilyName:
		familyName = parameterFamilyName
	else:
		familyName = Font.familyName
	if familyName.startswith("Cormorant Garamond"):
		thisInstance.removeObjectFromCustomParametersForKey_( renameGlyphsParameterKey )
		thisInstance.setCustomParameter_forKey_( renameGlyphs1, renameGlyphsParameterKey )
		thisInstance.setCustomParameter_forKey_( ["ss02"], "Remove Features" )


