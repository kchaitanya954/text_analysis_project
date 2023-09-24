from django.shortcuts import render
from analyze_suggestions import analyze_text, standardized_phrases  # Replace with the actual module where you have the analysis code

def text_analysis_view(request):
    if request.method == 'POST':
        input_text = request.POST.get('input_text', '')

        # Perform text analysis
        suggestions = analyze_text(input_text, standardized_phrases)  # Make sure standardized_phrases is defined

        return render(request, 'text_analyzer/analysis_result.html', {'input_text': input_text, 'suggestions': suggestions})

    return render(request, 'text_analyzer/input.html')


def analysis_result_view(request):
    # This view will be used to display the results
    input_text = request.POST.get('input_text', '')
    
    # Perform text analysis (you might need to call your analysis function here)
    suggestions = analyze_text(input_text, standardized_phrases)
    return render(request, 'text_analyzer/analysis_result.html', {'input_text': input_text, 'suggestions': suggestions})
