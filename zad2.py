# Poissonov problem u 2D, P1 elementi
# -(u_xx + u_yy) = xy, na 1<x<2, 2<y<3 
# u_D = 0, na rubu
# Koristene varijable
# mesh = diskretizacija domene
# V = prostor konacnih elemenata
# u_R = rubni uvjet za rjesenje
# bc = rubni uvjet interpoliran u prostor konacnih elemenata
# a = lijeva strana slabe formulacije
# A = sastavljena matrica lijeve strane
# L = desna strana slabe formulacije
# b = sastavljen vektor desne strane
# u = funkcija rjesenja
import fenics as fn
import matplotlib.pyplot as plt


# Diskretizacija jedinicnog intervala i definiranje 
# prostora konacnih elemenata na diskretizaciji:

mesh = fn.RectangleMesh(fn.Point(1,2), fn.Point(2,3), 10, 10)        
# u mesh je spremljena diskretizacija jediničnog intervala 
# koji je podijeljen na 10 i 10 jednakih dijelova

V = fn.FunctionSpace(mesh, 'CG', 1)
# formiramo prostor konačnih elemenata V, funkciji prostor izgraden je na 
# postojećoj diskretizaciji koja je prvi argument prethodne funkcije. 
# Drugi argument odreduje vrstu korištenih elemenata. Oznaka CG je oznaka 
# za Continuous Galerkin ili Lagrange elemente. Riječ je o aproksimaciji 
# neprekidnim funkcijama. Treći argument je red elemenata.

# Bazne funkcije za definiranje rubnih uvjeta
u_D = fn.Expression('0', degree=1)

def boundary(x, on_boundary):   #tražimo rub domene funkcijom koja ispituje je li točka x na rubu domene
    return on_boundary          #ima vrijednost True ako je x na rubu domene diskretizacije

bc = fn.DirichletBC(V, u_D, boundary)
# Rubni uvjet u kojemu definiramo vrijednost funkcije na rubu zove se 
# Dirichletov rubni uvjet pa se i ova klasa zove DirichletBC

# Slaba formulacija
u = fn.TrialFunction(V) 
v = fn.TestFunction(V)
f = fn.Expression('x[0]*x[1]', degree=1)                #funkcija desne strane
a = fn.dot(fn.grad(u), fn.grad(v))*fn.dx              
# Dot je funkcija skalarnog produkta, grad je standardni gradijent koji je 
# u jednoj dimenziji jednak derivaciji, a dx je oznaka za integral po domeni. 
L = f*v*fn.dx

# Kreiranje matrice sustava i vektora desne strane
A = fn.assemble(a)
b = fn.assemble(L)
bc.apply(A, b)                            #primjenjujemo rubni uvjet

# Rjesavanje sustava linearnih jednadzbi
u = fn.Function(V)
U = u.vector()
fn.solve(A, U, b)

# Grafovi
fig1 = plt.figure()
fn.plot(mesh) 
plt.savefig('mesh2D.png')
fig2 = plt.figure()
fn.plot(u)
plt.savefig('poisson2D.png')

# File za paraview
vtkfile = fn.File('poisson2D.pvd')
vtkfile << u