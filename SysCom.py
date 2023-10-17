import sys

def compare_hashes(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        for line1 in f1:
            parts = line1.strip().split(':')
            hash_to_check = parts[-1]

            f2.seek(0)  # Reset file pointer to the beginning for each line in file1

            for line2 in f2:
                parts2 = line2.strip().split(':')
                if parts2[0] == hash_to_check:
                    print(line1.strip() + ':' + parts2[1])
                    break
            else:
                print(line1.strip())

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python SisCom.py Combined-DC.txt cracked.txt")
        sys.exit(1)

    file1_path = sys.argv[1]
    file2_path = sys.argv[2]

    compare_hashes(file1_path, file2_path)
