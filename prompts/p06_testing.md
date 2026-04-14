# Prompts — 06 Testing

File: [s06_needs_testing.py](../src/s06_needs_testing.py)

1. > Generate one unit test for this module using pytest.

2. > Add one parametrized test for multiple `(alpha, beta)` combinations.

3. > Add one edge-case test for invalid inputs.

4. > ``Add one property-based test verifying that `CDF(quantile(p)) \approx p` and `PDF ≥ 0` for all valid inputs.``

6. > Add a performance benchmark testing 100 000 evaluations of `pareto_pdf`.

7. > Show me code coverage — are there any untested branches?

8. > <details>
   >  <summary>Bonus</summary>
   >  Now write tests for <code>s05_buggy.py</code> — do all the tests pass?
   >  </details>
