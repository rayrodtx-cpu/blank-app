#!/usr/bin/env python3
"""
Split large CSV file into smaller chunks for GitHub upload.
"""

import csv
import os

def split_csv(input_file, rows_per_file=200000):
    """Split CSV into multiple files."""
    print(f"Splitting {input_file}...")

    file_num = 1
    row_count = 0
    output_file = None
    writer = None
    header = None

    with open(input_file, 'r', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        header = next(reader)  # Save header

        for row in reader:
            # Create new file if needed
            if row_count % rows_per_file == 0:
                if output_file:
                    output_file.close()
                    print(f"  ✓ Created part {file_num-1} with {rows_per_file:,} rows")

                filename = f"corpus_christi_page_titles_part{file_num}.csv"
                output_file = open(filename, 'w', newline='', encoding='utf-8')
                writer = csv.writer(output_file)
                writer.writerow(header)  # Write header to each file
                file_num += 1

            writer.writerow(row)
            row_count += 1

    if output_file:
        output_file.close()
        remaining = row_count % rows_per_file
        if remaining == 0:
            remaining = rows_per_file
        print(f"  ✓ Created part {file_num-1} with {remaining:,} rows")

    print(f"\n✓ Total: Split {row_count:,} rows into {file_num-1} files")
    return file_num - 1

def main():
    input_file = "corpus_christi_page_titles.csv"

    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found!")
        return

    num_files = split_csv(input_file, rows_per_file=200000)

    print(f"\nFiles created:")
    for i in range(1, num_files + 1):
        filename = f"corpus_christi_page_titles_part{i}.csv"
        size_mb = os.path.getsize(filename) / (1024 * 1024)
        print(f"  {filename} ({size_mb:.2f} MB)")

if __name__ == "__main__":
    main()
