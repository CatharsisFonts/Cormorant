# The Cormorant Typeface Project

**☞ NEW: The Cormorant font family is now available on [Google Fonts][12]! ☜**

Cormorant is a free display type family developed by Christian Thalmann ([Catharsis Fonts][1]).  It comprises a total of 45 font files spanning 9 different styles (Roman, Italic, Infant, Infant Italic, Garamond, Garamond Italic, Upright Cursive, Small Caps, Unicase) and 5 weights (Light, Regular, Medium, Semibold, Bold).  For an illustrated presentation and description of the family, **please visit [its Bēhance page][3]**.

Cormorant is open source, and all its working files (in [Glyphs][2] format) are available from this repository. If you wish to work with Cormorant in a different font editor (which I wouldn't recommend), I can provide you with UFO versions of those files instead.

Any feedback, bug reports, test results, and suggestions for additions are very welcome. You can contact me using the [Cormorant issue tracker][4]. 

If you like Cormorant, please help spread the word via the social media of your choice. You might also be interested in my other typefaces on [MyFonts][1].

### Installation

If you wish to use the Cormorant type family on your computer, simply download the "Cormorant_Install" ZIP file from the [latest release][5], unpack it, and install the TrueType font files (.ttf) as appropriate for your operating system.

If you wish to use the Cormorant type family on your website, it is now offered as part of the free webfonts service at [Google Fonts][12]. 

### License
 
The Cormorant typeface and all its associated font files are free software under the [SIL Open Font License][10]. Essentially, this gives you the right to download, use, and redistribute the fonts as you like, provided that 

1. you retain my copyright notices;
2. you do not redistribute this software without this license information; and 
3. you do not redistribute the fonts by themselves for a fee (though you are allowed to sell them as part of a bundle containing other items.)

### Building fonts

The variable fonts are built using the [gftools builder](https://github.com/googlefonts/gftools). To install gftools you will need to have Python3.7+. Once you have Python installed you will need to use the command line and enter the following commands from the repo's current working directory:

```
pwd # this command will return our current working directory. Make sure it's the project's main directory!
python3 -m venv venv
```

We then need to activate this virtual environment

```
source venv/bin/activate
```

We are now ready to install gftools. Enter the following command:

```
pip install -r requirements.txt
```

This will install all the dependencies needed in order to build the fonts.

We can now build the variable fonts by entering the commands:

```
cd sources/
gftools builder build.yaml
```

We now need to generate the static fonts. Due to the complexity of renaming/swapping glyphs etc for the static fonts, we need to use Glyphsapp because the gftools builder currently doesn't support these features.

Inside glyphsapp, load the glyphs source files found in sources/ then hit command+e and generate the static ttfs to sources/ttf and static otfs to sources/otf.

We now need to post process the static fonts so they pass our internal QA tools. Please run the following command:

```
sh fix_statics.sh
```

The final step is to generate the webfonts. This can be done by running the command:

```
sh gen_webfonts.sh
```

### Acknowledgements
 
Cormorant was conceived, drawn, spaced, kerned, programmed, interpolated, and produced in its entirety by myself (Christian Thalmann, [Catharsis Fonts][1]). I did all the work with [Glyphs][2], which I consider the world's best font editing software. It's not free, but it's worth every penny ten times over; I cannot recommend it enough. I used the public beta version of the RMX Harmonizer plug-in to ensure curve quality.
 
While this project was heavily inspired by [Claude Garamont][6]'s immortal legacy, I did not use any specific font as a starting point or direct reference for my designs. Most glyphs were drawn from scratch; when I needed guidance on a specific character, I searched [MyFonts](https://www.myfonts.com/) for the term «Garamond» and skimmed through the results for a general impression.
 
I am very grateful to the creative souls on the [TypeDrawers][7] forum, the [Typografie.info][11] forum, and the (late?) [Typophile][8] forum for teaching me all I know about type design in the first place, and for providing me with a large amount of excellent feedback on Cormorant in particular. Likewise, my gratitude goes to the tireless folks at [Glyphs][2] — in particular Rainer Erich Scheichelbauer (Mekka Blue, [Schriftlabor][9]) and Georg Seifert — for the creation and support of their magnificent engine. Special thanks go to Dave Crossland and [Google Fonts][12] for making the libre release of this font family possible through generous funding of the development process. 

[1]: https://www.myfonts.com/foundry/Catharsis_Fonts
[2]: https://glyphsapp.com
[3]: https://www.behance.net/gallery/28579883/Cormorant-an-open-source-display-font-family
[4]: https://github.com/CatharsisFonts/Cormorant/issues/
[5]: https://github.com/CatharsisFonts/Cormorant/releases/latest
[6]: https://en.wikipedia.org/wiki/Claude_Garamond
[7]: http://typedrawers.com
[8]: http://typophile.com
[9]: http://schriftlabor.at
[10]: http://scripts.sil.org/OFL
[11]: http://typografie.info
[12]: https://fonts.google.com/?query=cormorant
