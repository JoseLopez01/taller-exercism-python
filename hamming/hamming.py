def distance(strand_a, strand_b):
    if len(strand_a) == len(strand_b):
        return len([value for key, value in zip(strand_a, strand_b) if key != value])
    else:
        raise ValueError("DNA strands are not the same length")
