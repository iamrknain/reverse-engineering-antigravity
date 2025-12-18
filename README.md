# Reverse Engineering Antigravity

## Knowledge Base

-   [**Identity & Core Mission**](IDENTITY.md) - Who it is and how it operates.
-   [**Tools Reference**](TOOLS.md) - A guide to its capabilities and toolset.
-   [**Workflow & Agentic Mode**](WORKFLOW.md) - Understanding the "Task View" and artifacts.
-   [**Browser Automation**](BROWSER_AUTOMATION.md) - Details on the browser subagent.

## Goals

1.  Reverse engineer Antigravity and learn things in reverse order.
2.  Explore agent communication and implementation details.
3.  Explore browser automation.

---

# Identity: Antigravity

## Who is Antigravity?
**Antigravity** is an agentic AI coding assistant designed by the **Google Deepmind team** and released on 18th November 2025.

## Operational Constraints
-   **Workspace**: It can only access files in the specified active workspaces (e.g., `/home/ravi/Desktop/antigravity`).
-   **Internal Memory**: It uses `/home/ravi/.gemini` for internal state and artifacts, but avoids writing project code there.
-   **Communication**: When in "Agentic Mode" (focusing on a task), it communicates primarily through `notify_user` to minimize noise, only surfacing for reviews or critical questions.

---

# Tools

Antigravity possesses a suite of tools to interact with the file system, terminal, and browser.

## File System Operations
-   `view_file` / `view_file_outline`: Read file contents and structure.
-   `write_to_file`: Create new files.
-   `replace_file_content` / `multi_replace_file_content`: Precise editing of existing files.
-   `list_dir`: Explore directory contents.
-   `find_by_name` / `grep_search`: Innovative search capabilities.

## System & Terminal
-   `run_command`: Execute shell commands (requires user approval).
-   `command_status` / `read_terminal`: Monitor command output.
-   `send_command_input`: Interact with running processes.

## Analysis & Communication
-   `codebase_search`: Semantic search for code snippets.
-   `notify_user`: The primary channel for updates and review requests during active tasks.
-   `task_boundary`: Manages the "task view" UI to group related actions.

## Web & Browser
-   `read_url_content`: Fetch static web content.
-   `browser_subagent`: Full browser control for complex interactions.

---

# Workflow & Agentic Mode

Antigravity operates in a structured "Agentic Mode" to handle complex tasks without overwhelming the user.

## The Loop
1.  **Task Boundary**: Defines a high-level task using `task_boundary`. This creates a UI block in the chat.
2.  **Iterative Work**: Performs file edits, command runs, and analysis.
3.  **Updates**: Periodically updates the task status to reflect progress.
4.  **Completion**: Uses `notify_user` to exit the task mode and return control to the user.

## Artifacts
It maintains persistent documents to track state across the conversation. These live in a dedicated "brain" directory (`/home/ravi/.gemini/antigravity/brain/...`).

-   **`task.md`**: A living checklist of the current mission.
-   **`implementation_plan.md`**: Design documents created during the PLANNING phase.
-   **`walkthrough.md`**: Proof-of-work documents created during the VERIFICATION phase to show what was tested.

## Modes
-   **PLANNING**: Researching and designing. Output: `implementation_plan.md`.
-   **EXECUTION**: Writing code. Output: Source code changes.
-   **VERIFICATION**: Testing changes. Output: `walkthrough.md`.

---

# Browser Automation

For tasks involving web interaction, Antigravity can deploy a specialized **Browser Subagent**.

## Capabilities
-   **Navigation**: Open URLs, click links, navigate usage.
-   **Interaction**: Click buttons, type text, fill forms.
-   **Observation**: Read the DOM, capture screenshots.
-   **Recording**: All sessions are recorded as videos (saved as artifacts).

## Usage
It uses the `browser_subagent` tool. This agent has its own limited set of tools specifically for browser control.

## Limitations
-   The subagent is a separate entity; Antigravity provides it with a high-level task.
-   It is best for verification (e.g., "Login and check if the dashboard loads") or data extraction.
