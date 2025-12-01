import json
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

        for target_path in target_file_paths:
            target_data = parse_file(target_path)
            comparison = compare_boms(master_bom_data, target_data)

            comparison_for_template = {
                'filename': os.path.basename(target_path),
                'comparison': {
                    'unchanged': comparison.get('unchanged', pd.DataFrame()).to_html(classes='table table-success', index=False),
                    'modified': comparison.get('modified', pd.DataFrame()).to_html(classes='table table-warning', index=False),
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
