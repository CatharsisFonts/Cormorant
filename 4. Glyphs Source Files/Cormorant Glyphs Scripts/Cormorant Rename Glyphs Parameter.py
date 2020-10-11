#MenuTitle: Cormorant Rename Glyphs Custom Parameter
# -*- coding: utf-8 -*-
"""Injects and/or updates the Rename Glyphs custom parameters for all upright italics in the .glyphs file."""

import GlyphsApp


# SC        
Font = Glyphs.font

suffix = ".liga.toBeDeleted"
allSuffixedGlyphNames = [ g.name for g in Font.glyphs if g.name.endswith(suffix) ]
removeGlyphs1 = [ "%s" % x for x in allSuffixedGlyphNames ]
removeGlyphs2 = [ "%s" % x.replace(suffix,".liga") for x in allSuffixedGlyphNames ]
removeGlyphsParameterKey = "Remove Glyphs"

suffix = ".sc"
allSuffixedGlyphNames = [ g.name for g in Font.glyphs if g.name.endswith(suffix) ]
renameGlyphs1 = [ "%s=%s" % ( x, x.replace(suffix,"") ) for x in allSuffixedGlyphNames ]
suffix = ".sc.ss12"
allSuffixedGlyphNames = [ g.name for g in Font.glyphs if g.name.endswith(suffix) ]
renameGlyphs2 = [ "%s=%s" % ( x, x.replace(suffix,".ss12") ) for x in allSuffixedGlyphNames ]
renameGlyphsParameterKey = "Rename Glyphs"

decomposeGlyphs = [g.name for g in Font.glyphs]

for thisInstance in Font.instances:
	parameterFamilyName = thisInstance.customValueForKey_("familyName")
	if parameterFamilyName:
		familyName = parameterFamilyName
	else:
		familyName = Font.familyName
	if familyName.startswith("Cormorant SC"):
		thisInstance.removeObjectFromCustomParametersForKey_( "Decompose Glyphs" )
		thisInstance.removeObjectFromCustomParametersForKey_( removeGlyphsParameterKey )
		thisInstance.removeObjectFromCustomParametersForKey_( renameGlyphsParameterKey )
		thisInstance.setCustomParameter_forKey_( decomposeGlyphs, "Decompose Glyphs" )
		thisInstance.setCustomParameter_forKey_( removeGlyphs1+removeGlyphs2, removeGlyphsParameterKey )
		thisInstance.setCustomParameter_forKey_( renameGlyphs1+renameGlyphs2, renameGlyphsParameterKey )
		thisInstance.setCustomParameter_forKey_( ["sc", "c2sc", "ss01", "ss02", "ss03", "ss04", "ss05", "ss06", "ss09", "ss10", "ss11", "dlig", "liga", "hlig", "onum"], "Remove Features" )




# Unicase
Font = Glyphs.font

suffix = ".liga.toBeDeleted"
allSuffixedGlyphNames = [ g.name for g in Font.glyphs if g.name.endswith(suffix) ]
removeGlyphs1 = [ "%s" % x for x in allSuffixedGlyphNames ]
removeGlyphs2 = [ "%s" % x.replace(suffix,".liga") for x in allSuffixedGlyphNames ]
removeGlyphsParameterKey = "Remove Glyphs"

allSS05GlyphNames = [ g.name for g in Font.glyphs if g.name.endswith(".ss05") ]
allSCGlyphNames = [ g.name for g in Font.glyphs if g.name.endswith(".sc") ]
mundaneSCGlyphNames = [ x for x in allSCGlyphNames if x not in allSS05GlyphNames ]
renameMundaneGlyphs = [ "%s=%s" % ( x, x.replace(".sc","") ) for x in mundaneSCGlyphNames ]
renameSS05Glyphs = [ "%s=%s" % ( x, x.replace(".sc.ss05","") ) for x in allSS05GlyphNames ]
renameGlyphs = renameMundaneGlyphs + renameSS05Glyphs
renameGlyphsParameterKey = "Rename Glyphs"

decomposeGlyphs = [g.name for g in Font.glyphs]

for thisInstance in Font.instances:
	parameterFamilyName = thisInstance.customValueForKey_("familyName")
	if parameterFamilyName:
		familyName = parameterFamilyName
	else:
		familyName = Font.familyName
	if familyName.startswith("Cormorant Unicase"):
		thisInstance.removeObjectFromCustomParametersForKey_( "Decompose Glyphs" )
		thisInstance.removeObjectFromCustomParametersForKey_( removeGlyphsParameterKey )
		thisInstance.removeObjectFromCustomParametersForKey_( renameGlyphsParameterKey )
		thisInstance.setCustomParameter_forKey_( decomposeGlyphs, "Decompose Glyphs" )
		thisInstance.setCustomParameter_forKey_( removeGlyphs1+removeGlyphs2, removeGlyphsParameterKey )
		thisInstance.setCustomParameter_forKey_( renameGlyphs, renameGlyphsParameterKey )
		thisInstance.setCustomParameter_forKey_( ["sc", "c2sc", "ss01", "ss02", "ss03", "ss04", "ss05", "ss06", "ss09", "ss10", "ss11", "dlig", "liga", "hlig", "onum"], "Remove Features" )



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

removeGlyphs = [ g.name for g in Font.glyphs if (g.name.find(".loclBGR") > 0)]

decomposeGlyphs = [g.name for g in Font.glyphs]

for thisInstance in Font.instances:
	parameterFamilyName = thisInstance.customValueForKey_("familyName")
	if parameterFamilyName:
		familyName = parameterFamilyName
	else:
		familyName = Font.familyName
	if familyName.startswith("Cormorant Infant"):
		thisInstance.removeObjectFromCustomParametersForKey_( "Decompose Glyphs" )
		thisInstance.setCustomParameter_forKey_( decomposeGlyphs, "Decompose Glyphs" )
		thisInstance.removeObjectFromCustomParametersForKey_( "Rename Glyphs" )
		thisInstance.setCustomParameter_forKey_( renameGlyphs, "Rename Glyphs" )
		thisInstance.setCustomParameter_forKey_( ["onum", "ss03"], "Remove Features" )
		thisInstance.setCustomParameter_forKey_( removeGlyphs, "Remove Glyphs" )


# Garamond
Font = Glyphs.font

suffix = ".ss02"
allSuffixedGlyphNames = [ g.name for g in Font.glyphs if g.name.endswith(suffix) ]
renameGlyphs1 = [ "%s=%s" % ( x, x.replace(suffix,"") ) for x in allSuffixedGlyphNames ]
renameGlyphsParameterKey = "Rename Glyphs"
#renameGlyphs2 = ["f_f.liga=uniFB00", "f_i.liga=uniFB01", "f_l.liga=uniFB02", "f_f_i.liga=uniFB03", "f_f_l.liga=uniFB04", "longs_t=uniFB05", "s_t=uniFB06"]

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
