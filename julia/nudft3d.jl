function nudft3d(tab_u::Array,tab_v::Array,nx::Integer,ny::Integer)
# 3D nudft [number of bases (spatiale frequencies) per wavelength * number of pixels * number of wavelength]
# U and V must be of the form : [number of bases * number of wavelength] in arc second
# If U and V are spatial frequencies in meter
# and field of view (FOd) is in arcsecond
# DegRad      = 2.0*pi/360.0
# RadArcsec   = 3600.0/DegRad
# coef        = FOV/RadArcsec
# println("3D NU DFT matrices")
# (F3D,Fr3D)  = nudft3d(U.* coef,V.* coef,nx,ny)
# nx and ny size of image

if nx<1||ny<1
  error("nudft3d:Image size must be positive")
end
  nfu  	= length(tab_u)
  nfv  	= length(tab_v)
  if(nfu==nfv&&nfu>0&&nfv>0)
    # test if U and V have same size and have same number of wavelength, otherwise PB
    size_tab_u = size(tab_u)
    size_tab_v = size(tab_v)
    if(size_tab_u[2]==size_tab_v[2])
      (nbase,nwvl)= size_tab_u
      F3D = complex(zeros(nbase,nx*ny,nwvl))
      for n      = 1:nwvl
        nudftmat   = non_uniform_dft(tab_u[:,n],tab_v[:,n],nx,ny)
        F3D[:,:,n] = nudftmat
      end
    Fr3D= nudftreim(F3D)
    return(F3D,Fr3D)
    else
    error("nudft3d: U ad V vectors have not of same number of wavelength")
    end
  else
    error("nudft3d: U ad V vectors are not of same size")
  end
end
function nudftreim(mat::Array)
# real valued nudft matrix
vcat(real(mat),imag(mat))
end