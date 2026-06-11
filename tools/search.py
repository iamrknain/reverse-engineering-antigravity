import os
import glob
import re

def find_by_name(search_directory, pattern):
    """
    Finds files by filename pattern.
    """
    if not os.path.isdir(search_directory):
        return f"Error: {search_directory} is not a directory."
    
    try:
        # Recursive search using glob
        results = glob.glob(os.path.join(search_directory, "**", pattern), recursive=True)
        return results
    except Exception as e:
        return f"Error searching for files: {e}"

def grep_search(search_path, query):
    """
    Searches for text patterns within files.
    """
    results = []
    
    if os.path.isfile(search_path):
        files_to_search = [search_path]
    elif os.path.isdir(search_path):
        files_to_search = glob.glob(os.path.join(search_path, "**", "*"), recursive=True)
    else:
        return f"Error: {search_path} does not exist."
        
    try:
        for file_path in files_to_search:
            if os.path.isfile(file_path):
                try:
                    with open(file_path, 'r', errors='ignore') as f:
                        for i, line in enumerate(f, 1):
                            if re.search(query, line):
                                results.append({
                                    "file": file_path,
                                    "line_number": i,
                                    "content": line.strip()
                                })
                except Exception:
                    # Skip files that cannot be read (e.g., binary)
                    continue
        return results
    except Exception as e:
        return f"Error grep searching: {e}"
