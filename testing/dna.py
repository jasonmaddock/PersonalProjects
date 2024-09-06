import csv
import sys


def main():
    if not cla():
        return 1
    db = db_reader(sys.argv[1])
    dna = dna_reader(sys.argv[2])
    analysis = match_counter(db, dna)
    matches = db_check(db, analysis)
    print(match_format(matches))
    return


def match_format(matches):
    if len(matches) > 1:
        return "Multiple matches"
    elif len(matches) == 1:
        return matches[0]
    else:
        return "No match"


# Find longest match of each STR in DNA sequence
def match_counter(db, dna):
    results = {}
    for key in db.keys():
        results[key] = longest_match(dna, key)
    return results


# Check database for matching profiles
def db_check(db, results):
    candidates = {}
    matches = {}
    for substring in results.keys():
        for candidate in db[substring].keys():
            matches[candidate] = db[substring][candidate] = results[substring]
    matches = [candidate for candidate in matches.keys() if matches[candidate]]
    return matches



# Read DNA sequence file into a variable
def dna_reader(dna_file):
    with open(dna_file) as file:
        sequence = file.read()
    return sequence


# Read database file into a variable
def db_reader(db_file):
    with open(db_file) as file:
        reader = csv.DictReader(file)
        sequences = reader.fieldnames[1:]
        output = {}
        for sequence in sequences:
            output[sequence] = {}
        for row in reader:
            for sequence in sequences:
                output[sequence][row["name"]] = row[sequence]
    return output


# Check for command-line usage
def cla():
    if len(sys.argv) == 3:
        return True
    else:
        print("Incorrect number of command line arguments.")
        return False


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
