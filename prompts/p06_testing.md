# Prompts — 06 Testing

File: [s06_needs_testing.py](../src/s06_needs_testing.py)

1. > Generate unit tests for this module using pytest.

2. > Add parametrized tests for multiple `(alpha, beta)` combinations.

3. > Add edge-case tests for invalid inputs.

4. > Add property-based tests verifying that `CDF(quantile(p)) ≈ p` and `PDF ≥ 0` for all valid inputs.

5. > Add an integration test that numerically integrates the PDF over `[0, ∞)` and checks the result is 1.

6. > Add a performance benchmark testing 100 000 evaluations of `pareto_pdf`.

7. > Show me code coverage — are there any untested branches?

8. > <details>
   >  <summary>Bonus</summary>
   >  Now write tests for <code>s05_buggy.py</code> — do all the tests pass?
   >  </details>
