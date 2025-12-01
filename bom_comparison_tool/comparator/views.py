import json
import io
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.files.storage import FileSystemStorage
import os
import pandas as pd
from .utils import parse_file, compare_boms

def upload_view(request):
    if request.method == 'POST':
        master_bom_file = request.FILES.get('master_bom')
        target_files = request.FILES.getlist('target_files')

        if not master_bom_file:
            return HttpResponse("Master BOM file is required.")

        fs = FileSystemStorage()
        master_bom_filename = fs.save(master_bom_file.name, master_bom_file)
        master_bom_path = fs.path(master_bom_filename)

        target_file_paths = []
        for target_file in target_files:
            filename = fs.save(target_file.name, target_file)
            target_file_paths.append(fs.path(filename))

        master_bom_data = parse_file(master_bom_path)
        comparison_results_for_template = []
        comparison_results_for_json = []

        def highlight_diff_row(row):
            style = pd.Series('', index=row.index)
            master_cols = [c for c in row.index if '_master' in c]
            for master_col in master_cols:
                col_name = master_col.replace('_master', '')
                target_col = f'{col_name}_target'
                if target_col in row.index:
                    # Convert to string to avoid dtype mismatches
                    if str(row[master_col]) != str(row[target_col]):
                        style[master_col] = 'background-color: #ffc107'
                        style[target_col] = 'background-color: #ffc107'
            return style

        for target_path in target_file_paths:
            target_data = parse_file(target_path)
            comparison = compare_boms(master_bom_data, target_data)

            modified_df = comparison.get('modified', pd.DataFrame())
            if not modified_df.empty:
                modified_html = modified_df.style.apply(highlight_diff_row, axis=1).to_html(classes='table table-bordered', index=False)
            else:
                modified_html = "<p>No modified items.</p>"

            comparison_for_template = {
                'filename': os.path.basename(target_path),
                'comparison': {
                    'unchanged': comparison.get('unchanged', pd.DataFrame()).to_html(classes='table table-success', index=False),
                    'modified': modified_html,
                    'added': comparison.get('added', pd.DataFrame()).to_html(classes='table table-info', index=False),
                    'deleted': comparison.get('deleted', pd.DataFrame()).to_html(classes='table table-danger', index=False),
                }
            }
            comparison_results_for_template.append(comparison_for_template)
            
            comparison_for_json = {
                'filename': os.path.basename(target_path),
                'comparison': {
                    'unchanged': comparison.get('unchanged', pd.DataFrame()).to_dict('records'),
                    'modified': comparison.get('modified', pd.DataFrame()).to_dict('records'),
                    'added': comparison.get('added', pd.DataFrame()).to_dict('records'),
                    'deleted': comparison.get('deleted', pd.DataFrame()).to_dict('records'),
                }
            }
            comparison_results_for_json.append(comparison_for_json)


        # Storing comparison_results in session to be accessible by download_json
        request.session['comparison_results'] = comparison_results_for_json

        return render(request, 'compare.html', {
            'master_bom_filename': os.path.basename(master_bom_path),
            'master_bom_data': master_bom_data.to_html(classes='table table-striped', index=False),
            'comparison_results': comparison_results_for_template,
        })

    return render(request, 'upload.html')

def download_json(request):
    comparison_results = request.session.get('comparison_results')
    if comparison_results:
        response = JsonResponse(comparison_results, safe=False)
        response['Content-Disposition'] = 'attachment; filename="comparison_results.json"'
        return response
    else:
        return HttpResponse("No comparison results found.")

def download_excel(request):
    comparison_results = request.session.get('comparison_results')
    if not comparison_results:
        return HttpResponse("No comparison results found.")

    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        for i, result in enumerate(comparison_results):
            filename = result.get('filename', f'target_{i+1}')
            # Keep sheet names under 31 characters
            short_filename = (filename[:20] + '...') if len(filename) > 23 else filename

            unchanged_df = pd.DataFrame(result['comparison']['unchanged'])
            modified_df = pd.DataFrame(result['comparison']['modified'])
            added_df = pd.DataFrame(result['comparison']['added'])
            deleted_df = pd.DataFrame(result['comparison']['deleted'])

            if not unchanged_df.empty:
                unchanged_df.to_excel(writer, sheet_name=f"{short_filename}_unchanged", index=False)
            if not modified_df.empty:
                modified_df.to_excel(writer, sheet_name=f"{short_filename}_modified", index=False)
            if not added_df.empty:
                added_df.to_excel(writer, sheet_name=f"{short_filename}_added", index=False)
            if not deleted_df.empty:
                deleted_df.to_excel(writer, sheet_name=f"{short_filename}_deleted", index=False)

    output.seek(0)
    response = HttpResponse(
        output,
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename="bom_comparison_results.xlsx"'
    return response
