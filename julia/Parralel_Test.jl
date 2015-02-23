# size of the pb
nx = 256
nw = 50

# function to eval
function CalFx2(x)
  eigvecs(x)
end
# Function to eval in pmap
@everywhere function CalFx(x)
  eigvecs(x)
end


# generate: random data
X   = rand(nx,nx,nw)
println("###################################")
println("Array Initialization as SharedArray(T::Type,(size))")
prinln(" julia -p nprocs")
println("###################################")

Fp  = SharedArray(Complex{Float64},(nx,nx,nw))
Fx  = SharedArray(Complex{Float64},(nx,nx,nw))
Fm  = SharedArray(Complex{Float64},(nx,nx,nw))
Fx2 = zeros(Complex,nx,nx,nw)
println("")
println("###################################")
println("serial: classical 'for' loop")
println("###################################")
tic()
for n = 1:nw
  Fx2[:,:,n] = CalFx2(X[:,:,n])
end
toc()

println("")
println("###################################")
println("@sync @parralel 'for' loop")
println("###################################")
tic()
@sync @parallel for n = 1:nw
  Fp[:,:,n] = CalFx(X[:,:,n])
end
toc()

println("")
println("###################################")
println("Pmap+serial Array filling")
println("###################################")
tic()
tmp = pmap(CalFx,{(X[:,:,i]) for i =1:nw})
a = toq()
tic()
for n = 1:nw
  Fx[:,:,n] = tmp[n]
end
b = toq()
println("pmap")
println(a)
println("Array filling")
println(b)
println("total")
println(a+b)
println("")

println("###################################")
println("Pmap+@synch@parralel Array filling")
tic()
tmp = pmap(CalFx,{(X[:,:,i]) for i =1:nw})
a = toq()
tic()
@sync @parallel for n = 1:nw
  Fm[:,:,n] = tmp[n]
end
b = toq()
println("###################################")
println("pmap")
println(a)
println("@synch@parralel Array filling")
println(b)
println("total")
println(a+b)

println("")
println("###################################")
println("Erreur Estim pmap")
println(sum( Fx[:]-Fx2[:]))
println("Erreur sync parralel")
println(sum( Fp[:]-Fx2[:]))
println("Erreur pmap+synch")
println(sum( Fm[:]-Fx2[:]))

