function getTVMatrix(m::Integer,n::Integer)
# m,n size of image
# create finite difference matrix for an image
if(m<1||n<1)
error("getH:Image size must be positive")
end
mn              = m*n
# (m x n) size of image
tempv           = speye(m)-circshift(speye(m),[0 1])
i,j,s           = findnz(tempv)
ad              = int(ceil( (1:1:2*mn) / (2*m) ) -1)*m
# create the block diagonal matrix
Dv              = sparse(repeat(i,outer=[n])+ad,repeat(j,outer=[n])+ad,repeat(s,outer=[n]),mn,mn)
Dh1             = speye(mn)
Dh2             = circshift(Dh1,[0 n])
H               = vcat(Dv,Dh1-Dh2)
end

function getTVMatrix(n::Integer)
# method 2 - squared image
# n,n size of image
if(n<1)
error("getH:Image size must be positive")
end
# (m x n) size of image
nn              = n*n
tempv           = speye(n)-circshift(speye(n),[0 1])
i,j,s           = findnz(tempv)
ad              = int(ceil( (1:1:2*nn) / (2*n) ) -1)*n
# create the block diagonal matrix
Dv              = sparse(repeat(i,outer=[n])+ad,repeat(j,outer=[n])+ad,repeat(s,outer=[n]),nn,nn)
Dh1             = speye(mn)
Dh2             = circshift(Dh1,[0 n])
H               = vcat(Dv,Dh1-Dh2)
end