## Init and test formulas

from matplotlib import mathtext, font_manager
import matplotlib as mpl
mpl.rcParams['savefig.transparent'] = True

texFont = font_manager.FontProperties(size=30, family='serif', math_fontfamily='cm')

mathtext.math_to_image(r"$e = mc^2$", "output.png", prop=texFont, dpi=300, format='png')

!pip install "drawsvg~=2.0"
!pip install "cairosvg"

import drawsvg as draw
import copy
