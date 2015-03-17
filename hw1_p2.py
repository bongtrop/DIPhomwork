import dip
# import view
import cal
import opener

mat = opener.pgm2mat('dataset/Cameraman.pgm')
hist = dip.mat2hist(mat)
im = dip.hist2im(hist)
# view.mat(mat, "Cameraman Original")
opener.mat2pgm('report/cameraman_ori_p2.pgm', mat)
opener.mat2pgm('report/cameraman_ori_hist_p2.pgm', im)

nmat = dip.histeq(mat)
hist = dip.mat2hist(nmat)
im = dip.hist2im(hist)
# view.mat(nmat, "Cameraman Edited")
opener.mat2pgm('report/cameraman_edi_p2.pgm', nmat)
opener.mat2pgm('report/cameraman_edi_hist_p2.pgm', im)

mat = opener.pgm2mat('dataset/SEM256_256.pgm')
hist = dip.mat2hist(mat)
im = dip.hist2im(hist)
# view.mat(mat, "SEM256_256 Original")
opener.mat2pgm('report/SEM256_256_ori_p2.pgm', mat)
opener.mat2pgm('report/SEM256_256_ori_hist_p2.pgm', im)

nmat = dip.histeq(mat)
hist = dip.mat2hist(nmat)
im = dip.hist2im(hist)
# view.mat(nmat, "SEM256_256 Edited")
opener.mat2pgm('report/SEM256_256_edi_p2.pgm', nmat)
opener.mat2pgm('report/SEM256_256_edi_hist_p2.pgm', im)

# view.show()
