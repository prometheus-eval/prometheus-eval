# Tool Making

Tasks involving the creation of reusable tools for problem-solving.

**Authors:** FILL IN ME

## Example

A sample query in a zero-shot setting:


Input:
A patient has undergone genetic testing, and their DNA sequence has been obtained. There is a need to analyze this sequence to identify any potential genetic diseases that the patient might be at risk for.
**DNA Sequence of the Patient**: **`\"GCTAGCTCGATCGTAGCTACGTACGATCGAGCTAGCTACG\"`**

**Known Mutation-Disease Mapping**:
- **`\"GCTAGCTC\"`**: Disease X
- **`\"ATCGTAGC\"`**: Disease Y
- **`\"CGTACGAT\"`**: Disease Z

Question: Analyze the patient's DNA sequence. Identify any matches with known mutations and report the potential genetic diseases associated with these mutations.
Existing tool:
```python
def dna_sequence_matcher(dna_sequence, known_mutations):
    matches = []
        for mutation in known_mutations:
            if mutation in dna_sequence:
                matches.append(mutation)
    return matches

```
Example usage:
```python
dna_sequence = "AGTCGATCGCGTAGCTAGTACGATCGA\"
known_mutations = ["AGTCGATCG", "CGTAGCTAG", "TACGATCGA"]
matches = dna_sequence_matcher(dna_sequence, known_mutations)
print(\"Matches:\", matches)
```
New tool:

**Output:**
```python
def genetic_disease_identifier(dna_sequence, mutation_disease_mapping):
    matches = dna_sequence_matcher(dna_sequence, mutation_disease_mapping.keys())
    diseases = [mutation_disease_mapping[match] for match in matches if match in mutation_disease_mapping]
    return diseases
```

## What is the task trying to measure?

The tasks is designed for measuring tool making ability of LMs.

## Motivation

FILL IN ME

## Related work

Large Language Models as Tool Makers (https://arxiv.org/abs/2305.17126)