def mystery(f, df, x0, t=1e-10, m_iter=100):
    x = x0
    for _ in range(m_iter):
        dfx = df(x)
        if dfx == 0:
            raise ZeroDivisionError("Derivative is zero; cannot continue")

        x_next = x - f(x) / dfx
        if abs(x_next - x) < t:
            return x_next
        x = x_next

    return x


