import sympy as sp

# Define symbols
x, y = sp.symbols('x y')

# Define the function
f = sp.exp(x) * sp.sin(y) + y**3

# Compute partial derivatives
df_dx = sp.diff(f, x)
df_dy = sp.diff(f, y)

print("Partial derivative of f with respect to x:", df_dx)
print("Partial derivative of f with respect to y:", df_dy)
# Define the function g
g = x**2 * y + x * y**2

# Compute gradient vector
gradient_g = [sp.diff(g, var) for var in (x, y)]

# Evaluate the gradient vector at the point (1, -1)
gradient_at_point = [gradient_g[0].subs({x: 1, y: -1}), gradient_g[1].subs({x: 1, y: -1})]

# Compute magnitude of the gradient vector
magnitude_gradient = sp.sqrt(sum(component**2 for component in gradient_at_point))

print("Gradient vector of g:", gradient_g)
print("Magnitude of the gradient vector at (1, -1):", magnitude_gradient)
# Define the function h
h = sp.ln(x**2 + y**2)

# Compute second partial derivatives
d2h_dx2 = sp.diff(h, x, x)
d2h_dy2 = sp.diff(h, y, y)
d2h_dxdy = sp.diff(h, x, y)

print("Second partial derivative of h with respect to x:", d2h_dx2)
print("Second partial derivative of h with respect to y:", d2h_dy2)
print("Second partial derivative of h with respect to x and y:", d2h_dxdy)

# Discuss the symmetry of mixed partial derivatives
# Since h is defined in terms of ln(x^2 + y^2), which is symmetric with respect to x and y,
# we expect the mixed partial derivatives to be equal, i.e., ∂^2h/∂x∂y = ∂^2h/∂y∂x

# Define the function k
k = x**2 + y**2

# Convert the SymPy expression to a numerical function
k_func = sp.lambdify((x, y), k, 'numpy')

# Create a grid of x and y values and evaluate k on this grid
x_vals = np.linspace(-3, 3, 400)
y_vals = np.linspace(-3, 3, 400)
X, Y = np.meshgrid(x_vals, y_vals)
Z = k_func(X, Y)

# Plot the contour
plt.contourf(X, Y, Z, levels=50, cmap='viridis')
plt.colorbar()
plt.title('Contour plot of $k(x, y) = x^2 + y^2$')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.show()

