from django.shortcuts import render

def calculator(request):
    result = ''
    if request.method == 'POST':
        expression = request.POST.get('expression')
        try:
            result = eval(expression)
        except:
            result = 'Error'
    return render(request, 'index.html', {'result': result})
