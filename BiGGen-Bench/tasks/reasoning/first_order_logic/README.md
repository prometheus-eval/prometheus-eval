# First Order Logic

Tasks that require to utilize first-order-logic to reason.

**Authors:** Juyoung Suk (juyoung@lklab.io)

## Example

A sample query in a zero-shot setting:

```
Input:
"Translate the below natural language statement into a first-order logic formula. Use the following predicates for your translation:

[Predicates]
City(x): x is a city.
HasMuseum(x): City x has a museum.
Tourist(y, x): y is a tourist in city x.

[Statement]
Every city that has a museum has at least one tourist.

Output:
The translation process involves formulating a logic formula that combines these predicates with logical connectors. The phrase ""Every city that has a museum..."" suggests a universal condition applying to all such cities, leading us to use a universal quantifier (∀x). This is combined with a conditional statement that links city and museum predicates. The phrase ""...has at least one tourist"" implies the existence of at least one tourist in these cities, which is expressed using an existential quantifier (∃y). Putting it all together, the first-order logic formula that represents the given statement is: ∀x (City(x) ∧ HasMuseum(x) → ∃y (Tourist(y, x))). This formula succinctly captures the essence of the original statement, stating that for every entity x, if x is a city and has a museum, then there exists an entity y such that y is a tourist in x.
```

## What is the task trying to measure?

FILL IN ME

## Motivation

FILL IN ME

## Related work

FILL IN ME