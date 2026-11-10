# Version 1: fixed 100 steps with for
x = 10
learning_rate = 0.1

for epoch in range(1, 101):
    gradient = 2 * x + 3
    x = x - learning_rate * gradient
    func = x ** 2 + 3 * x
    if epoch % 10 == 0:
        print(f"Epoch: {epoch} | X: {x:.4f} | Gradient: {gradient:.4f} | f(x): {func:.4f}")

# Version 2: 
x = 10
learning_rate = 0.1

gradient = 2 * x + 3

epoch = 0
while abs(gradient) >= 0.000001 and epoch < 10000:
    epoch += 1
    gradient = 2 * x + 3
    x = x - learning_rate * gradient
    func = x ** 2 + 3 * x
    if epoch % 10 == 0:
        print(f"Epoch: {epoch} | X: {x:.4f} | f(x): {func:.4f}")

print(f"Program stopped at: {epoch} epoch.")

# Experiment on the learning rate parameter:
# learning rate = 0.01 => 841 epoch
# learning rate = 0.1 => 77 epoch
# learning rate = 0.5 => 2 epoch
# learning rate = 1 => 10000 epoch
# learning rate = 1.1 => OverflowError: (34, 'Result too large'), Because our function was getting the square of x.