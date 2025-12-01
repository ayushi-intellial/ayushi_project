# BOM Comparison Tool

## Description

This project is a Django-based web application that allows users to compare Bill of Materials (BOM) files. Users can upload a master BOM file and one or more target BOM files to identify the differences between them. The comparison highlights parts that are unchanged, modified, added, or deleted.

## Features

-   Upload master and target BOM files in various formats (.xlsx, .csv, .docx, .pdf).
-   Compares BOMs based on the 'MPN' (Manufacturer Part Number) column.
-   Displays a clear comparison report showing:
    -   Unchanged parts
    -   Modified parts
    -   Added parts (present in target BOM but not in master)
    -   Deleted parts (present in master BOM but not in target)
-   Download the comparison results in JSON format.

## Technology Stack

-   **Backend:** Django
-   **Data Processing:** pandas
-   **File Parsing:**
    -   `openpyxl` for `.xlsx` files
    -   `python-docx` for `.docx` files
    -   `PyPDF2` for `.pdf` files

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd bom-comparison-tool
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run database migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```
    The application will be available at `http://127.0.0.1:8000`.

## Usage

1.  Navigate to the upload page (`/`).
2.  Select a "master" BOM file.
3.  Select one or more "target" BOM files.
4.  Click "Upload and Compare".
5.  The comparison results will be displayed on the next page.
6.  You can download the results as a JSON file.

## Project Structure

```
.
├── bom_comparison_tool/      # Django project directory
│   ├── comparator/           # Django app for the comparison logic
│   │   ├── migrations/
│   │   ├── templates/        # HTML templates
│   │   │   ├── compare.html
│   │   │   └── upload.html
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   ├── utils.py          # File parsing and comparison logic
│   │   └── views.py          # Views for file upload and comparison
│   ├── bom_comparison_tool/    # Django project settings
│   │   ├── settings.py
│   │   └── urls.py
│   ├── db.sqlite3            # SQLite database (ignored by git)
│   └── manage.py             # Django's command-line utility
├── media/                    # Uploaded files (ignored by git)
├── requirements.txt          # Project dependencies
├── README.md                 # This file
└── .gitignore                # Files to be ignored by git
```