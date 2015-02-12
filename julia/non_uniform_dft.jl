function non_uniform_dft(u_in::Array,v_in::Array,nx::Integer,ny::Integer)
# Non Uniform DFT Matrix:
# for a nx*ny pixels image
# u, v vector of normalized spatial frequencies (between -0.5 and 0.5)
nf    = length(u_in)
u 		= vec(u_in)
v 		= vec(v_in)
kx 		= [-nx/2:-1+nx/2]
ky 		= [-ny/2:-1+ny/2]
k1  	= repmat(kx,1,ny)
k2  	= repmat(ky',nx,1)
k1v 	= vec(k1)'/nx
k2v 	= vec(k2)'/ny
um 		= repmat(u,1,nx*ny)
vm 		= repmat(v,1,nx*ny)
k1m 	= repmat(k1v,nf,1)
k2m 	= repmat(k2v,nf,1)
F    	= exp(-2im*pi*(k1m.*um+k2m.*vm))./sqrt(nx*ny)
end