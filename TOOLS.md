# Antigravity Tools Reference

This document details the capabilities and usage of the Antigravity agent's toolset.

## File System Tools

### `view_file`
Reads the contents of a file.
- **Arguments**:
  - `AbsolutePath` (string): Full path to the file.
  - `StartLine` (int, optional): 1-indexed start line.
  - `EndLine` (int, optional): 1-indexed end line.
- **Usage**: Reading code, configuration files, or documentation.

### `write_to_file`
Creates or overwrites a file with new content.
- **Arguments**:
  - `TargetFile` (string): absolute path.
  - `CodeContent` (string): content to write.
  - `Overwrite` (boolean): must be explicitly true to overwrite.
- **Usage**: Creating new modules, scripts, or artifacts.

### `list_dir`
Lists contents of a directory.
- **Arguments**:
  - `DirectoryPath` (string): absolute path.
- **Usage**: Exploring project structure.

### `replace_file_content`
Replaces a single contiguous block of text in a file.
- **Arguments**:
  - `TargetFile` (string)
  - `TargetContent` (string): Exact text to find.
  - `ReplacementContent` (string): New text.
- **Usage**: Small, precise code edits.

## System Tools

### `run_command`
Executes a shell command.
- **Arguments**:
  - `CommandLine` (string): Command to run.
  - `SafeToAutoRun` (boolean): User safety flag.
- **Usage**: Running tests, installing dependencies, file operations.

### `command_status`
Checks the status/output of a background command.
- **Arguments**:
  - `CommandId` (string).
- **Usage**: Monitoring long-running processes.

## Search Tools

### `find_by_name`
Finds files by filename pattern.
- **Arguments**:
  - `SearchDirectory` (string).
  - `Pattern` (string): Glob pattern (e.g., `*.py`).
- **Usage**: Locating specific files.

### `grep_search`
Searches for text patterns within files.
- **Arguments**:
  - `SearchPath` (string).
  - `Query` (string): Text or regex to find.
- **Usage**: Finding function definitions, usages, or specific strings.

## Specialized Tools

- **`browser_subagent`**: Controls a browser for web tasks.
- **`codebase_search`**: Semantic search for code concepts.
- **`task_boundary`**: Manage task state.
- **`notify_user`**: Communicate with the user.
