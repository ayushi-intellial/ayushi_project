# Conversation Prompts and Instructions

This document compiles all the prompts and instructions provided during the interaction.

---
## 2. Django File Upload Error

**User Prompt:**
Hey you are doing well now i am giving you a role scientist in prgramming in all versatile perspective in all fields such as ai/ml, software engineering and etc. now i want to create a project based on the aim given below and also please provide the detailed cinformation in file that which type of configuration, package and the requirements project needed and also create a project in a very advance way. Rules for creating a project: make the code is optimize and provide a detailed workflow that how the project is work. now I'm providing you an aim please refer it, aim: Software Requirement: BOM Comparison Tool
1. Purpose
The tool will compare a Master Bill of Materials (BOM) with one or more revised BOM files and
visually show the differences.
2. Input Requirements
The user must upload a Master BOM in XLSX format (this is the source file).
The user can then select 1 to 5 target files to compare against the Master BOM.
Target files may be in any of the following formats: CSV, XLSX, DOCX, PDF, TXT.
The tool must parse and process all supported formats.
3. Comparison Process
When the user clicks the Compare button:
The software will read the source and target files.
It will compare fields such as MPN, Quantity, Reference Designator (Ref Des),
Description, etc.
Differences will be detected between the Master BOM and each target file.

4. User Interface Requirements
Show a side-by-side table view of the Master BOM and each selected target BOM.
Highlight differences using color coding for easy visual identification.
Each comparison should be clearly separated and readable.
5. Output Requirements
The user must be able to save the comparison result.
The saved result should be downloadable in JSON format.
The JSON file should contain all comparison details and must be readable later by the
user.

---

## 2. Initial Setup and Context

**User Prompt:**
This is the Gemini CLI. We are setting up the context for our chat.
Today's date is Monday, 1 December 2025 (formatted according to the user's locale).
My operating system is: win32
The project's temporary directory is: C:\Users\Admin\.gemini\tmp\bae509806ee0ef13756ac85b081a3287e0e339f85d0e2ffcf1a865650ecf6263
I'm currently working in the directory: D:\ayushi_project
Here is the folder structure of the current working directories:

Showing up to 200 items (files + folders). Folders or files indicated with ... contain more items not shown, were ignored, or the display limit (200 items) was reached.

D:\ayushi_project\
├───bom.csv
├───bom.docx
├───bom.pdf
├───bom.xlsx
├───README.md
├───requirements.txt
├───bom_comparison_tool\
│   ├───db.sqlite3
│   ├───manage.py
│   ├───bom_comparison_tool\
│   │   ├───__init__.py
│   │   ├───asgi.py
│   │   ├───settings.py
│   │   ├───urls.py
│   │   ├───wsgi.py
│   │   └───__pycache__\
│   │       ├───__init__.cpython-313.pyc
│   │       ├───settings.cpython-313.pyc
│   │       ├───urls.cpython-313.pyc
│   │       └───wsgi.cpython-313.pyc
│   ├───comparator\
│   │   ├───__init__.py
│   │   ├───admin.py
│   │   ├───apps.py
│   │   ├───models.py
│   │   ├───tests.py
│   │   ├───urls.py
│   │   ├───utils.py
│   │   ├───views.py
│   │   ├───__pycache__\
│   │   │   ├───__init__.cpython-313.pyc
│   │   │   ├───admin.cpython-313.pyc
│   │   │   ├───apps.cpython-313.pyc
│   │   │   ├───models.cpython-313.pyc
│   │   │   ├───urls.cpython-313.pyc
│   │   │   ├───utils.cpython-313.pyc
│   │   │   └───views.cpython-313.pyc
│   │   └───migrations\
│   │       ├───__init__.py
│   │       └───__pycache__\
│   │           └───__init__.cpython-313.pyc
│   ├───media\
│   ├───static\
│   └───templates\
│       ├───compare.html
│       └───upload.html
└───venv\
    ├───.gitignore
    ├───pyvenv.cfg
    ├───Include\
    ├───Lib\
    │   └───site-packages\
    │       ├───pip\
    │       │   ├───__init__.py
    │       │   ├───__main__.py
    │       │   ├───__pip-runner__.py
    │       │   ├───py.typed
    │       │   ├───__pycache__\
    │       │   │   ├───__init__.cpython-313.pyc
│       │   │   │   ├───__main__.cpython-313.pyc
│       │   │   │   └───__pip-runner__.cpython-313.pyc
│       │   │   ├───_internal\
│       │   │   │   ├───__init__.py
│       │   │   │   ├───build_env.py
│       │   │   │   ├───cache.py
│       │   │   │   ├───configuration.py
│       │   │   │   ├───exceptions.py
│       │   │   │   ├───main.py
│       │   │   │   ├───pyproject.py
│       │   │   │   ├───self_outdated_check.py
│       │   │   │   ├───wheel_builder.py
│       │   │   │   ├───__pycache__\
│       │   │   │   │   ├───__init__.cpython-313.pyc
│       │   │   │   │   ├───build_env.cpython-313.pyc
│       │   │   │   │   ├───cache.cpython-313.pyc
│       │   │   │   │   ├───configuration.cpython-313.pyc
│       │   │   │   │   ├───exceptions.cpython-313.pyc
│       │   │   │   │   ├───main.cpython-313.pyc
│       │   │   │   │   ├───pyproject.cpython-313.pyc
│       │   │   │   │   ├───self_outdated_check.cpython-313.pyc
│       │   │   │   │   └───wheel_builder.cpython-313.pyc
│       │   │   │   ├───cli\
│       │   │   │   │   ├───__init__.py
│       │   │   │   │   ├───autocompletion.py
│       │   │   │   │   ├───base_command.py
│       │   │   │   │   ├───cmdoptions.py
│       │   │   │   │   ├───command_context.py
│       │   │   │   │   ├───index_command.py
│       │   │   │   │   ├───main_parser.py
│       │   │   │   │   ├───main.py
│       │   │   │   │   ├───parser.py
│       │   │   │   │   ├───progress_bars.py
│       │   │   │   │   ├───req_command.py
│       │   │   │   │   ├───spinners.py
│       │   │   │   │   ├───status_codes.py
│       │   │   │   │   └───__pycache__\
│       │   │   │   ├───commands\
│       │   │   │   │   ├───__init__.py
│       │   │   │   │   ├───cache.py
│       │   │   │   │   ├───check.py
│       │   │   │   │   ├───completion.py
│       │   │   │   │   ├───configuration.py
│       │   │   │   │   ├───debug.py
│       │   │   │   │   ├───download.py
│       │   │   │   │   ├───freeze.py
│       │   │   │   │   ├───hash.py
│       │   │   │   │   ├───help.py
│       │   │   │   │   ├───index.py
│       │   │   │   │   ├───inspect.py
│       │   │   │   │   ├───install.py
│       │   │   │   │   ├───list.py
│       │   │   │   │   ├───lock.py
│       │   │   │   │   ├───search.py
│       │   │   │   │   ├───show.py
│       │   │   │   │   ├───uninstall.py
│       │   │   │   │   ├───wheel.py
│       │   │   │   │   └───__pycache__\
│       │   │   │   ├───distributions\
│       │   │   │   │   ├───__init__.py
│       │   │   │   │   ├───base.py
│       │   │   │   │   ├───installed.py
│       │   │   │   │   ├───sdist.py
│       │   │   │   │   ├───wheel.py
│       │   │   │   │   └───__pycache__\
│       │   │   │   ├───index\
│       │   │   │   │   ├───__init__.py
│       │   │   │   │   ├───collector.py
│       │   │   │   │   ├───package_finder.py
│       │   │   │   │   ├───sources.py
│       │   │   │   │   └───__pycache__\
│       │   │   │   ├───locations\
│       │   │   │   │   ├───__init__.py
│       │   │   │   │   ├───_distutils.py
│       │   │   │   │   ├───_sysconfig.py
│       │   │   │   │   ├───base.py
│       │   │   │   │   └───__pycache__\
│       │   │   │   ├───metadata\
│       │   │   │   │   ├───__init__.py
│       │   │   │   │   ├───_json.py
│       │   │   │   │   ├───base.py
│       │   │   │   │   ├───pkg_resources.py
│       │   │   │   │   ├───__pycache__\
│       │   │   │   │   └───importlib\
│       │   │   │   ├───models\
│       │   │   │   │   ├───__init__.py
│       │   │   │   │   ├───candidate.py
│       │   │   │   │   ├───direct_url.py
│       │   │   │   │   ├───format_control.py
│       │   │   │   │   ├───... 
│       │   │   │   │   └───... 
│       │   │   │   ├───network\
│       │   │   │   ├───operations\
│       │   │   │   ├───req\
│       │   │   │   ├───resolution\
│       │   │   │   ├───utils\
│       │   │   │   └───vcs\
│       │   │   └───_vendor\
│       │   │       ├───__init__.py
│       │   │       ├───typing_extensions.py
│       │   │       ├───vendor.txt
│       │   │       ├───__pycache__\
│       │   │       ├───cachecontrol\
│       │   │       ├───certifi\
│       │   │       ├───dependency_groups\
│       │   │       ├───distlib\
│       │   │       ├───distro\
│       │   │       ├───idna\
│       │   │       ├───msgpack\
│       │   │       ├───packaging\
│       │   │       ├───pkg_resources\
│       │   │       ├───platformdirs\
│       │   │       ├───pygments\
│       │   │       ├───pyproject_hooks\
│       │   │       ├───requests\
│       │   │       ├───resolvelib\
│       │   │       ├───rich\
│       │   │       ├───tomli\
│       │   │       ├───tomli_w\
│       │   │       ├───truststore\
│       │   │       └───urllib3\
│       └───pip-25.1.1.dist-info\
│           ├───entry_points.txt
│           ├───INSTALLER
│           ├───METADATA
│           ├───RECORD
│           ├───REQUESTED
│           ├───top_level.txt
│           ├───WHEEL
│           └───licenses\
│               ├───AUTHORS.txt
│               └───LICENSE.txt
└───Scripts\
    ├───activate
    ├───activate.bat
    ├───activate.fish
    ├───Activate.ps1
    ├───deactivate.bat
    ├───pip.exe
    ├───pip3.13.exe
    ├───pip3.exe
    ├───python.exe
    └───pythonw.exe

Reminder: Do not return an empty response when a tool call is required.
My setup is complete. I will provide my first command in the next turn.

---

## 3. Django File Upload Error

**User Prompt:**
master_bom_file = request.files.get('master_bom') showing this error

---

## 4. Request for `agents_prompt.md` (Initial)

**User Prompt:**
ok give agents_prompt.md file all the prompts i had provided you for this porject from very starting point

---

## 5. Agent-related Code and Text (from initial `agents_prompt.md` creation)

This section contains code snippets and descriptions provided by the user in the context of creating `agents_prompt.md` initially.

### PromptAgent Class

```python
class PromptAgent(Agent):
    """prompt-based agent that emits action given the history"""

    @beartype
    def __init__(
        self,
        action_set_tag: str,
        lm_config: lm_config.LMConfig,
        prompt_constructor: PromptConstructor,
    ) -> None:
        super().__init__()
        self.lm_config = lm_config
        self.prompt_constructor = prompt_constructor
        self.action_set_tag = action_set_tag

    def set_action_set_tag(self, tag: str) -> None:
        self.action_set_tag = tag

    @beartype
    def next_action(
        self, trajectory: Trajectory, intent: str, meta_data: dict[str, Any]
    ) -> Action:
        prompt = self.prompt_constructor.construct(
            trajectory, intent, meta_data
        )
        lm_config = self.lm_config
        n = 0
        while True:
            response = call_llm(lm_config, prompt)
            force_prefix = self.prompt_constructor.instruction[
                "meta_data"
            ].get("force_prefix", "")
            response = f"{force_prefix}{response}"
            n += 1
            try:
                parsed_response = self.prompt_constructor.extract_action(
                    response
                )
                if self.action_set_tag == "id_accessibility_tree":
                    action = create_id_based_action(parsed_response)
                elif self.action_set_tag == "playwright":
                    action = create_playwright_action(parsed_response)
                else:
                    raise ValueError(
                        f"Unknown action type {self.action_set_tag}"
                    )
                action["raw_prediction"] = response
                break
            except ActionParsingError as e:
                if n >= lm_config.gen_config["max_retry"]:
                    action = create_none_action()
                    action["raw_prediction"] = response
                    break

        return action

    def reset(self, test_config_file: str) -> None:
        pass
```

### run_agent_prompt Function

```python
async def run_agent_prompt(session: Session, prompt_text: str):
    content = types.Content(
        role="user", parts=[types.Part.from_text(text=prompt_text)]
    )
    print(f"\n>>>> Agent Prompt: {prompt_text}")
    final_agent_response_parts = []
    async for event in runner.run_async(
        user_id=user_id_1,
        session_id=session.id,
        new_message=content,
        run_config=RunConfig(save_input_blobs_as_artifacts=False),
    ):
      if event.content.parts and event.content.parts[0].text:
        print(f"** {event.author} (ADK): {event.content.parts[0].text}")
        if event.author == agent.root_agent.name:
          final_agent_response_parts.append(event.content.parts[0].text)
    print(f"<<<< Agent Final Output: {"".join(final_agent_response_parts)}\n")
```

### get_prompt_instructions Function

```python
def get_prompt_instructions(self):
        return "These are tool instructions."
```

### inspect_ecs_prompt Function

```python
def inspect_ecs_prompt():
        """User wants to inspect ECS resources"""
        return ["ecs_resource_management"]
```

### prompt_string Function (1)

```python
def prompt_string(
        prefix: str = "",
        suffix: str = "AGENT:",
        user_format: str = "USER: {content}\n\n",
        agent_format: str = "AGENT: {content}\n\n",
        prompt_key: str = "prompt",
    ):
        def prompter(messages: List[Dict[str, str]]):
            nonlocal prefix, suffix, user_format, agent_format, prompt_key
            prompt = prefix
            for item in messages:
                if item["role"] == "user":
                    prompt += user_format.format(content=item["content"])
                else:
                    prompt += agent_format.format(content=item["content"])
            prompt += suffix
            print(prompt)
            return {prompt_key: prompt}

        return prompter
```

### prompt_string Function (2)

```python
def prompt_string(
        prefix: str = "",
        suffix: str = "AGENT:",
        user_format: str = "USER: {content}\n\n",
        agent_format: str = "AGENT: {content}\n\n",
        prompt_key: str = "prompt",
    ):
        def prompter(messages: List[Dict[str, str]]):
            nonlocal prefix, suffix, user_format, agent_format, prompt_key
            prompt = prefix
            for item in messages:
                if item["role"] == "user":
                    prompt += user_format.format(content=item["content"])
                else:
                    prompt += agent_format.format(content=item["content"])
            prompt += suffix
            return {prompt_key: prompt}

        return prompter
```

### show_running_containers_prompt Function

```python
def show_running_containers_prompt():
        """User wants to see running containers in ECS"""
        return ["ecs_resource_management"]
```

### make_live_prompt Function

```python
def make_live_prompt():
        """User wants to make an application live"""
        return ["containerize_app", "create_ecs_infrastructure"]
```

### Description of Agent Interfaces

[Title] : Heading
Defines agent interfaces and concrete implementations for interacting with a web environment. Supports teacher-forcing and prompt-based agents for action generation. Facilitates agent creation based on configuration arguments. This file defines the Agent base class with next_action and reset methods. The TeacherForcingAgent follows a predefined action sequence, useful for evaluating fixed strategies. The PromptAgent leverages a language model and a PromptConstructor to generate actions based on trajectory history and intent. Key functions include construct_agent which instantiates agents based on agent_type ('teacher_forcing' or 'prompt'), action_set_tag, and LLM configurations. Actions are parsed into structured formats (id_accessibility_tree or playwright) using helper functions from browser_env.actions. The PromptAgent includes retry logic for LLM calls to handle parsing errors.

### Description of Agent Project Creation Utilities Tests

[Title] : Heading
Tests utilities for creating new agent projects. Verifies file generation, environment variable setup for different backends (API key vs. GCP), and command execution logic. Includes tests for user prompts and handling of existing directories. This file unit tests the cli_create module\'s agent creation utilities. Key functions tested include _generate_files which creates agent project files and .env configurations based on provided backend parameters (API key or GCP project/region), and run_cmd which handles the command-line execution flow including user confirmation for overwrites. Helper functions like _prompt_for_google_cloud, _prompt_for_google_api_key, and _prompt_to_choose_backend are tested for their interactive prompting behavior. Tests also cover fallback mechanisms for retrieving GCP project/region from gcloud commands, ensuring robustness even when these commands are not found or fail. The _mute_click fixture silences Click\'s output during tests, and agent_folder provides a temporary directory for file operations.

---

## 6. GitHub Upload Request (Initial)

**User Prompt:**
also upload this project on github and provide documentation like it conatins what was the url, repository name and all the required documents that needed

---

## 7. Clarification for GitHub Upload

**User Prompt:**
prepare the bom_repository_tool to upload on github in my account whole project you have to upload also provide some that contains detailed informartion about project contains which package you had installed, etc

---

## 8. Confirmation to Keep BOM Files

**User Prompt:**
yes keep it.

---

## 9. UI Improvement Request

**User Prompt:**
now please provide the proper ui for the project for file input and highlighting the difference in the comparison table using css

---

## 10. Multiple Target BOM Files Request

**User Prompt:**
now allow multiple target bom files to be enter to compare with single master bom file

---

## 11. How to Upload Updated Files to GitHub

**User Prompt:**
now i want to upload updated files in github how i?

---

## 12. Advanced Features and Optimization Request

**User Prompt:**
update my project with more advanced features and make code optimize
  Advanced Features:
   1. Export to Excel: Download comparison results as an Excel file, with unchanged, modified, added, and deleted items
      on separate sheets.
   2. Fuzzy Matching: Make the MPN comparison more intelligent, catching minor typos and variations.
   3. Improved PDF Parsing: Enhance the PDF reader\'s ability to handle various table layouts, though this might require
      additional system tools.

  Code Optimizations:
   4. Code Refactoring: Improve the structure and readability of the code.
   5. Large File Handling: Optimize the application to process very large BOM files more efficiently.
---

## 13. Feature Selection

**User Prompt:**
1,2,5

---

## 14. Fuzzy Matching Implementation Confirmation

**User Prompt:**
implement fuzzy matching

## 15. ML models

**User Prompt:**
can i create a ml model for that to comparing data sets and then train on them
