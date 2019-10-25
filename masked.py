#!/usr/bin/env python
"""
Masked wordcloud
================

Using a mask you can generate wordclouds in arbitrary shapes.
"""

from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

from wordcloud import WordCloud

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# Read the whole text.
text = 'AI Java CPP Python NodeJs Golang Docker MySQL React Vue Angular MongoDB PostgreSQL Redis Hadoop Spark HBase Storm PHP Nginx SpringBoot Tensorflow Caffe CMake MyBatis LUA Linux Win32 VSCode 薄国宁 孟超 邱玲 邵盛松 孙国平 王增周 王志亮'

# read the mask image
# taken from
# http://www.stencilry.org/stencils/movies/alice%20in%20wonderland/255fk.jpg
mask = np.array(Image.open(path.join(d, "xlab_small.png")))

wc = WordCloud(font_path='c:\\windows\\fonts\\msyh.ttc',max_words=1000, mask=mask, repeat=True, colormap=plt.cm.Pastel1, min_font_size=6, background_color='black', mode="RGBA", scale=4 )

# generate word cloud
wc.generate(text)

# store to file
wc.to_file(path.join(d, "output.png"))

# show
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()
