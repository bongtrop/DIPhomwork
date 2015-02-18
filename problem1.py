import dip
import view
import cal
import opener

mat = opener.pgm2mat('dataset/scaled_shapes.pgm')
hist = dip.mat2hist(mat)
im = dip.hist2im(hist)
view.mat(im, "histogram")
opener.mat2pgm('report/histogram_p1.pgm', mat)

obj1 = dip.mat2bw(mat, [0])
opener.mat2pgm('report/obj1_p1.pgm', mat)
obj2 = dip.mat2bw(mat, [80])
opener.mat2pgm('report/obj1_p2.pgm', mat)
obj3 = dip.mat2bw(mat, [120])
opener.mat2pgm('report/obj1_p3.pgm', mat)
obj4 = dip.mat2bw(mat, [160])
opener.mat2pgm('report/obj1_p4.pgm', mat)
obj5 = dip.mat2bw(mat, [200])
opener.mat2pgm('report/obj1_p5.pgm', mat)

view.mat(obj1, "OBJ 1")
view.mat(obj2, "OBJ 2")
view.mat(obj3, "OBJ 3")
view.mat(obj4, "OBJ 4")
view.mat(obj5, "OBJ 5")
view.show()


print "\nObject 1"
M00 = dip.moment(obj1, 0, 0)
M01 = dip.moment(obj1, 0, 1)
M10 = dip.moment(obj1, 1, 0)
ctm_x = M01/M00
ctm_y = M10/M00
print "Center of Mess: " + str(ctm_x) + ", " + str(ctm_y)

print "\nObject 2"
M00 = dip.moment(obj2, 0, 0)
M01 = dip.moment(obj2, 0, 1)
M10 = dip.moment(obj2, 1, 0)
ctm_x = M01/M00
ctm_y = M10/M00
print "Center of Mess: " + str(ctm_x) + ", " + str(ctm_y)

print "\nObject 3"
M00 = dip.moment(obj3, 0, 0)
M01 = dip.moment(obj3, 0, 1)
M10 = dip.moment(obj3, 1, 0)
ctm_x = M01/M00
ctm_y = M10/M00
print "Center of Mess: " + str(ctm_x) + ", " + str(ctm_y)

print "\nObject 4"
M00 = dip.moment(obj4, 0, 0)
M01 = dip.moment(obj4, 0, 1)
M10 = dip.moment(obj4, 1, 0)
ctm_x = M01/M00
ctm_y = M10/M00
print "Center of Mess: " + str(ctm_x) + ", " + str(ctm_y)

print "\nObject 5"
M00 = dip.moment(obj5, 0, 0)
M01 = dip.moment(obj5, 0, 1)
M10 = dip.moment(obj5, 1, 0)
ctm_x = M01/M00
ctm_y = M10/M00
print "Center of Mess: " + str(ctm_x) + ", " + str(ctm_y)

print "\nQuantity"
print "Obj1 is " + str(dip.norm_moment(obj1, 2, 0) + dip.norm_moment(obj1, 0, 2))
print "Obj2 is " + str(dip.norm_moment(obj2, 2, 0) + dip.norm_moment(obj2, 0, 2))
print "Obj3 is " + str(dip.norm_moment(obj3, 2, 0) + dip.norm_moment(obj3, 0, 2))
print "Obj4 is " + str(dip.norm_moment(obj4, 2, 0) + dip.norm_moment(obj4, 0, 2))
print "Obj5 is " + str(dip.norm_moment(obj5, 2, 0) + dip.norm_moment(obj5, 0, 2))
