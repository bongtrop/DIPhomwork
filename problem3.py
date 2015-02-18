import dip
import view
import cal
import opener

r = opener.pgm2mat('dataset/SanFranPeak_red.pgm')
g = opener.pgm2mat('dataset/SanFranPeak_green.pgm')
b = opener.pgm2mat('dataset/SanFranPeak_blue.pgm')

excess_green = 2*g - r - b
excess_blue = 2*b - g - r
redblue_diff = r - b
gray = (r + g + b)/3

view.mat(excess_green, " Excess Green")
view.mat(redblue_diff, " Red-Blue Different")
view.mat(gray, " Gray Scale")
view.mat(excess_blue, "Excess Blue")
view.show()

opener.mat2pgm('report/excess_green_p3.pgm', excess_green)
opener.mat2pgm('report/redblue_diff_p3.pgm', redblue_diff)
opener.mat2pgm('report/excess_blue_p3.pgm', excess_blue)
opener.mat2pgm('report/gray_p3.pgm', gray)
