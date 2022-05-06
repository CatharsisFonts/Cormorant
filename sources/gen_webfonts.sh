set -e

mkdir -p ../fonts/webfonts
fonts=$(ls ../fonts/*/*.ttf)
for font in $fonts
do
   out_filename=$(basename -s ".ttf" $font)
   out_fp="../fonts/webfonts/$out_filename.woff2"
   fontTools ttLib.woff2 compress $font -o $out_fp
done