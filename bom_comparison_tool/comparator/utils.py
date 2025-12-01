import os
import re
import pandas as pd
import docx
from PyPDF2 import PdfReader

def normalize_mpn(mpn):
    """Converts to uppercase and removes all non-alphanumeric characters."""
    if not isinstance(mpn, str):
        return ''
    return re.sub(r'[^A-Z0-9]', '', mpn.upper())

def parse_file(file_path):
    _, extension = os.path.splitext(file_path)
    extension = extension.lower()

    if extension == '.xlsx':
        # Use read_only mode for potentially large Excel files
        return pd.read_excel(file_path, engine='openpyxl', engine_kwargs={'read_only': True})
    elif extension == '.csv':
        return pd.read_csv(file_path)
    elif extension == '.docx':
        doc = docx.Document(file_path)
        # This is a simplification. It assumes the first table is the BOM.
        table = doc.tables[0]
        data = [[cell.text for cell in row.cells] for row in table.rows]
        return pd.DataFrame(data[1:], columns=data[0])
    elif extension == '.pdf':
        reader = PdfReader(file_path)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
        # This is a major simplification. It just returns the raw text.
        # A more robust solution would be needed for parsing various PDF layouts.
        return pd.DataFrame([x.split() for x in text.splitlines()])
    elif extension == '.txt':
        # Assumes tab-separated or comma-separated
        return pd.read_csv(file_path, delimiter='t', header=None)
    else:
        return pd.DataFrame()

def compare_boms(master_bom, target_bom):
    if 'MPN' not in master_bom.columns or 'MPN' not in target_bom.columns:
        return {'error': 'MPN column not found in one or both BOMs.'}

    # Convert all columns to string to avoid dtype issues
    master_bom = master_bom.astype(str)
    target_bom = target_bom.astype(str)
    
    master_bom['normalized_MPN'] = master_bom['MPN'].apply(normalize_mpn)
    target_bom['normalized_MPN'] = target_bom['MPN'].apply(normalize_mpn)

    merged_bom = pd.merge(master_bom, target_bom, on='normalized_MPN', how='outer', indicator=True, suffixes=('_master', '_target'))

    both = merged_bom[merged_bom['_merge'] == 'both'].copy()
    
    # This is complex. Let's make it more readable.
    # Get the columns to compare, excluding the original MPN and normalized MPN
    master_cols = [c for c in master_bom.columns if c not in ['MPN', 'normalized_MPN']]
    
    are_equal = pd.Series(True, index=both.index)
    for col in master_cols:
        are_equal &= (both[f'{col}_master'] == both[f'{col}_target'])

    unchanged = both[are_equal]
    modified = both[~are_equal]

    added = merged_bom[merged_bom['_merge'] == 'right_only'].copy()
    deleted = merged_bom[merged_bom['_merge'] == 'left_only'].copy()

    results = {
        'unchanged': unchanged,
        'modified': modified,
        'added': added,
        'deleted': deleted
    }

    for key in results:
        if 'normalized_MPN' in results[key].columns:
            results[key] = results[key].drop(columns=['normalized_MPN'])
        if '_merge' in results[key].columns:
            results[key] = results[key].drop(columns=['_merge'])

    return results
