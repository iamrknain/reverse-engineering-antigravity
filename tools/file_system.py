import os

def view_file(path, start_line=1, end_line=None):
    """
    Reads the contents of a file.
    """
    if not os.path.exists(path):
        return f"Error: File {path} does not exist."
    
    try:
        with open(path, 'r') as f:
            lines = f.readlines()
        
        if end_line is None:
            end_line = len(lines)
        
        # Adjust for 0-based indexing
        start_index = max(0, start_line - 1)
        end_index = min(len(lines), end_line)
        
        return "".join(lines[start_index:end_index])
    except Exception as e:
        return f"Error reading file by read_file: {e}"

def write_to_file(path, content, overwrite=False):
    """
    Writes content to a file.
    """
    if os.path.exists(path) and not overwrite:
        return f"Error: File {path} already exists. Set overwrite=True to overwrite."
    
    try:
        with open(path, 'w') as f:
            f.write(content)
        return f"Successfully wrote to {path}"
    except Exception as e:
        return f"Error writing to file: {e}"

def list_dir(path):
    """
    Lists contents of a directory.
    """
    if not os.path.isdir(path):
        return f"Error: {path} is not a directory."
    
    try:
        return os.listdir(path)
    except Exception as e:
        return f"Error listing directory: {e}"

def replace_file_content(path, target_content, replacement_content):
    """
    Replaces target_content with replacement_content in the file at path.
    """
    if not os.path.exists(path):
        return f"Error: File {path} does not exist."
    
    try:
        with open(path, 'r') as f:
            content = f.read()
        
        if target_content not in content:
            return f"Error: Target content not found in {path}."
        
        new_content = content.replace(target_content, replacement_content, 1) # Replace only the first occurrence for safety
        
        with open(path, 'w') as f:
            f.write(new_content)
            
        return f"Successfully replaced content in {path}"
    except Exception as e:
        return f"Error replacing content: {e}"
