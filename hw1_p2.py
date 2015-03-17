import dip
# import view
import cal
import opener

mat = opener.pgm2mat('dataset/Cameraman.pgm')
# view.mat(mat, "Cameraman Original")
opener.mat2pgm('report/cameraman_ori_p2.pgm', mat)

nmat = dip.histeq(mat)
# view.mat(nmat, "Cameraman Edited")
opener.mat2pgm('report/cameraman_edi_p2.pgm', nmat)

mat = opener.pgm2mat('dataset/SEM256_256.pgm')
# view.mat(mat, "SEM256_256 Original")
opener.mat2pgm('report/SEM256_256_ori_p2.pgm', mat)
nmat = dip.histeq(mat)
# view.mat(nmat, "SEM256_256 Edited")
opener.mat2pgm('report/SEM256_256_edi_p2.pgm', nmat)

# view.show()
