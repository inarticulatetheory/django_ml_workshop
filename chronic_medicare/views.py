from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def results_list(request):
    results = ChronicConditionRegression.objects.all()
    return render(request, 'chronic_medicare/results_list.html', {'results': results})

def results_detail(request, pk):
    result = get_object_or_404(ChronicConditionRegression, pk=pk)
    return render(request, 'chronic_medicare/results_detail.html', {'result': result})