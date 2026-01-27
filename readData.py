# Reads a CSV file (Excel saved as CSV) and writes a plain .txt file.
# No `import` statements are used — this script uses only Python builtins.

def try_open_text(path, encodings):
    """Try opening file with a list of encodings; return open file object and used encoding."""
    for enc in encodings:
        try:
            f = open(path, "r", encoding=enc, errors="strict", newline=None)
            return f, enc
        except Exception:
            continue
    # Last-resort: try permissive encoding
    f = open(path, "r", encoding="latin-1", errors="replace", newline=None)
    return f, "latin-1 (replace)"

def main():
    print("This script expects an Excel sheet saved as CSV first.")
    in_path = input("Enter path to CSV file (e.g. sheet.csv): ").strip()
    out_path = input("Enter path for output text file (e.g. out.txt): ").strip()
    if not in_path or not out_path:
        print("Input and output paths are required.")
        return

    encodings_to_try = ["utf-8", "utf-8-sig", "cp1252", "latin-1"]

    try:
        fin, used_enc = try_open_text(in_path, encodings_to_try)
    except Exception as e:
        print("Failed to open input file for reading:", e)
        return

    try:
        # Normalize newlines and write as CRLF so Notepad shows lines correctly on older Windows
        with fin:
            with open(out_path, "w", encoding="utf-8", newline="") as fout:
                for raw_line in fin:
                    # strip all trailing newline characters then write CRLF
                    line = raw_line.rstrip("\r\n")
                    fout.write(line + "\r\n")
    except Exception as e:
        print("Failed to write output file:", e)
        return

    print(f"Wrote {out_path} (read with encoding: {used_enc})")

if __name__ == "__main__":
    main()