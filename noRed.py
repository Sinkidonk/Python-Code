## Chapter 6
## remove red
## Alex Parys
## 3/1/2019
from PIL import Image
def noRed(infile,outfile):
    im = Image.open(infile).convert("RGB")

    source = im.split()
    R, G, B = 0, 1, 2

    out = source[R].point(lambda i: i*0)

    source[R].paste(out, None, None)
    im = Image.merge(im.mode, source)

    im.save(outfile)
    
