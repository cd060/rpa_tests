from django.shortcuts import render


def input_view(request):
    last_input = None
    if request.method == 'POST':
        input_str = request.POST.get('input_str')
        last_input = input_str
    return render(request, 'testapp/input.html', {'last_input': last_input})