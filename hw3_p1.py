import opener
import dip
import numpy as np

print "Process Flower_Snack.pgm"
gt = 2.60
mat = opener.pgm2mat('dataset/Flower_Snack.pgm')
fmat = np.fft.fft2(mat)

idmark = dip.filterdesign(fmat.shape, 'gaussian', [40])
imat = np.fft.ifft2(dip.filter(fmat, idmark))
inmat = dip.norm(np.abs(imat))

bw_obj = dip.mat2bw(inmat,range(225,256))
bw_bg = 255 - dip.mat2bw(inmat, range(0,80))

area_obj = dip.moment(bw_obj, 0, 0)
area_bg = dip.moment(bw_bg, 0, 0)
print "Area Object: "+ str(area_obj)+" px"
print "Area Background: "+ str(area_bg)+" px"
print "Area Groundtruth Background: "+ str(gt)+" cm^2"
print "Area Cal Object: "+ str((1.0*area_obj/area_bg)*gt)+" cm^2"

opener.mat2pgm('report/h3_p1_Flower_Snack_blur.pgm',dip.norm(inmat))
opener.mat2pgm('report/h3_p1_Flower_Snack_obj.pgm',dip.norm(bw_obj))
opener.mat2pgm('report/h3_p1_Flower_Snack_bg.pgm',dip.norm(bw_bg))

#####################################################################

print "Process Crab.pgm"
gt = 2.766
mat = opener.pgm2mat('dataset/Crab.pgm')
fmat = np.fft.fft2(mat)

idmark = dip.filterdesign(fmat.shape, 'gaussian', [40])
imat = np.fft.ifft2(dip.filter(fmat, idmark))
inmat = dip.norm(np.abs(imat))

bw_obj = dip.mat2bw(inmat,range(225,256))
bw_bg = 255 - dip.mat2bw(inmat, range(0,80))

area_obj = dip.moment(bw_obj, 0, 0)
area_bg = dip.moment(bw_bg, 0, 0)
print "Area Object: "+ str(area_obj)+" px"
print "Area Background: "+ str(area_bg)+" px"
print "Area Groundtruth Background: "+ str(gt)+" cm^2"
print "Area Cal Object: "+ str((1.0*area_obj/area_bg)*gt)+" cm^2"

opener.mat2pgm('report/h3_p1_Crab_blur.pgm',dip.norm(inmat))
opener.mat2pgm('report/h3_p1_Crab_obj.pgm',dip.norm(bw_obj))
opener.mat2pgm('report/h3_p1_Crab_bg.pgm',dip.norm(bw_bg))


