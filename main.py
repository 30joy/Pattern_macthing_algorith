def compute_lps(pattern):
    lps = [0] * len(pattern)
    j = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
            i += 1
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def kmp_search(text, pattern):
    m = len(pattern)
    n = len(text)
    lps = compute_lps(pattern)
    i, j, match_count = 0, 0, 0
    positions = []

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

            if j == m:
                match_count += 1
                positions.append(i - j)
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return match_count, positions


def main():
    print("Welcome to Pattern Matching with KMP Algorithm")

    # Prompt the user for the file path containing the text
    file_path = input("Enter the file path to read the input text from: ")

    try:
        with open(file_path, 'r') as file:
            text = file.read()
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return

    pattern = input("Enter the pattern to search for: ")

    match_count, positions = kmp_search(text, pattern)

    if match_count > 0:
        print(f"Pattern matched {match_count} times.")
        print(f"Matching positions: {positions}")
        matching_percentage = (match_count / len(text)) * 100
        print(f"Matching percentage: {matching_percentage:.2f}%")
    else:
        print("Pattern not found in the input text.")


if __name__ == "__main__":
    main()
