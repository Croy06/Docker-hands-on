# seqClass.py

This script classifies a given sequence as either DNA or RNA.

## Usage

```bash
python3 seqClass.py -s <sequence> [-m <motif>] [-p <percentage of nucleotide>]
```

## Arguments

- `-s`, `--seq`: The input sequence. This argument is mandatory.
- `-m`, `--motif`: A motif to search for within the sequence. This argument is optional.
- `-p`, `--percentage`: Calculate nucleotide percentage. This argument is optional.

## Examples

```bash
python3 seqClass.py -s ATCG
```

This command will classify the sequence `ATCG` as either DNA or RNA.

```bash
python3 seqClass.py -s AUG -m UG
```

This command will classify the sequence `AUG` as either DNA or RNA and will search for the motif `UG` within the sequence.

```bash
python3 seqClass.py -s AUG -p
```

This command will classify the sequence `AUG` as either DNA or RNA and will calculate the nucleotide percentage.

## Notes

- **Performance**: The performance of this script largely depends on the length of the sequence and the complexity of the motif. For very long sequences or complex motifs, the script may take longer to execute.

- **Nucleotide Percentage**: The -p option calculates the percentage of each nucleotide in the sequence. This can be useful for understanding the composition of the sequence, which can have implications for its structure and function.

- **Motif Search**: The -m option allows you to search for a specific motif within the sequence. Motifs, or recurring patterns in DNA or RNA, can have biological significance. For example, they could indicate binding sites for proteins or be involved in regulatory functions.

- **Sequence Validation**: This script validates that the input sequence only contains valid nucleotide characters (A, C, G, T, U). If the sequence contains any other characters, the script will return an error message.

- **Case Insensitivity**: This script is case-insensitive, meaning it treats lower-case and upper-case letters as the same. This is common in bioinformatics, as DNA and RNA sequences are often represented in upper-case letters, but users may input them in lower-case.