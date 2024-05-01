from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def calculate(request):
    if request.method == 'POST':
        num1 = request.POST['number1']
        num2 = request.POST['number2']

        i = True

        if 'add' in request.POST:
            ans = int(num1) + int(num2)
        elif 'subtract' in request.POST:
            ans = int(num1) - int(num2)
        elif 'multiply' in request.POST:
            ans = int(num1) * int(num2)
        elif 'divide' in request.POST:
            ans = int(num1) / int(num2)

    return render(request, 'index.html', {'ans':ans})
    
    