from django.shortcuts import render

# Create your views here.

def square(request):
    a = request.GET.get('a', None)
    b = request.GET.get('b', None)
    c = request.GET.get('c', None)

    if None in (a, b, c):
        result = u'Not the correct input'
    else:
        a = float(a)
        b = float(b)
        c = float(c)
        d = b * b - 4 * a * c
        if d >= 0:
            x1 = (-b - d**(0.5))/(2 * a)
            x2 = (-b + d**(0.5))/(2 * a)
            result = (x1, x2)
        else:
            result = u"The discriminant is less than zero"

    return render(request, 'nine/index.html', {"string" : result})

