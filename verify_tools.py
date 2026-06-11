
import os
import sys

# Add the current directory to sys.path so we can import the tools
sys.path.append(os.getcwd())

from tools.file_system import view_file, write_to_file, list_dir, replace_file_content
from tools.system import run_command
from tools.search import find_by_name, grep_search

def test_file_system():
    print("Testing File System Tools...")
    test_file = "test_file.txt"
    content = "Hello, World!\nThis is a test file."
    
    # Write
    print(f"Writing to {test_file}...")
    result = write_to_file(test_file, content, overwrite=True)
    print(result)
    
    # Read
    print(f"Reading {test_file}...")
    read_content = view_file(test_file)
    print(f"Content: {read_content}")
    assert read_content == content
    
    # Replace
    print("Replacing content...")
    replace_result = replace_file_content(test_file, "World", "Universe")
    print(replace_result)
    
    read_content = view_file(test_file)
    print(f"New Content: {read_content}")
    assert "Universe" in read_content
    
    # List Dir
    print("Listing directory...")
    files = list_dir(".")
    print(f"Files: {files}")
    assert test_file in files
    
    # Clean up
    os.remove(test_file)
    print("File System Tests Passed!")

def test_system():
    print("\nTesting System Tools...")
    # Run Command
    print("Running 'echo Hello'...")
    result = run_command("echo Hello")
    print(result)
    assert result['stdout'].strip() == "Hello"
    print("System Tests Passed!")

def test_search():
    print("\nTesting Search Tools...")
    test_file = "tools/search_test_dummy.py"
    write_to_file(test_file, "def test_func():\n    pass\n", overwrite=True)
    
    # Find By Name
    print("Finding 'search_test_dummy.py'...")
    found = find_by_name(".", "search_test_dummy.py")
    print(f"Found: {found}")
    # Normalize paths for comparison to avoid ./ prefix issues if present
    found_normalized = [os.path.normpath(p) for p in found]
    test_file_normalized = os.path.normpath(f"./{test_file}") 
    # Check if the file is in the list, accounting for relative paths
    assert any(p.endswith("search_test_dummy.py") for p in found_normalized)

    
    # Grep Search
    print("Grepping for 'test_func'...")
    grep_results = grep_search(".", "test_func")
    print(f"Grep Results: {grep_results}")
    assert len(grep_results) > 0
    
    # Clean up
    os.remove(test_file)
    print("Search Tests Passed!")

if __name__ == "__main__":
    try:
        test_file_system()
        test_system()
        test_search()
        print("\nALL TESTS PASSED SUCCESSFULLY!")
    except Exception as e:
        print(f"\nTESTS FAILED: {e}")
        exit(1)
