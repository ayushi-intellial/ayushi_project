import os
import pandas as pd
import docx
from PyPDF2 import PdfReader

def parse_file(file_path):
    _, extension = os.path.splitext(file_path)
    extension = extension.lower()

    if extension == '.xlsx':
        return pd.read_excel(file_path)
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
    
    merged_bom = pd.merge(master_bom, target_bom, on='MPN', how='outer', indicator=True, suffixes=('_master', '_target'))

    unchanged = merged_bom[merged_bom['_merge'] == 'both']
    unchanged = unchanged[unchanged.apply(lambda x: x.filter(like='_master').equals(x.filter(like='_target')), axis=1)]

    modified = merged_bom[merged_bom['_merge'] == 'both']
    modified = modified[~modified.index.isin(unchanged.index)]

    added = merged_bom[merged_bom['_merge'] == 'right_only']
    deleted = merged_bom[merged_bom['_merge'] == 'left_only']

    return {
        'unchanged': unchanged,
        'modified': modified,
        'added': added,
        'deleted': deleted
    }
