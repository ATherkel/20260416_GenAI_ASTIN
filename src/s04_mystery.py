from typing import Callable


def newton_raphson(
    func: Callable[[float], float],
    derivative: Callable[[float], float],
    initial_guess: float,
    tolerance: float = 1e-10,
    max_iterations: int = 100,
) -> float:
    x = initial_guess
    for _ in range(max_iterations):
        df_x = derivative(x)
        if df_x == 0:
            raise ZeroDivisionError("Derivative is zero; cannot continue")

        x_next = x - func(x) / df_x
        if abs(x_next - x) < tolerance:
            return x_next
        x = x_next

    return x


if __name__ == "__main__":
    # Find the root of f(x) = x^2 - 2, i.e. sqrt(2)
    root = newton_raphson(
        func=lambda x: x**2 - 2,
        derivative=lambda x: 2 * x,
        initial_guess=1.0,
    )
    print(f"sqrt(2) ≈ {root}")
