from django.shortcuts import render
from django.shortcuts import redirect

from .forms import SevenForm

UP_TO = 7


def _get_pairs(number_list):
    """
    Get unique pairs that can add up to 7
    :param number_list: string Comma separated string of integers
    :return: pairs:list
    """
    # Filter numbers and remove duplicates
    numbers = [int(number) for number in number_list.split(',') if int(number) < UP_TO]
    numbers = set(numbers)

    # Get unique pairs
    pairs = []
    for number_x in numbers:
        print(number_x)
        for number_y in numbers:
            if number_x + number_y == UP_TO \
                    and ((number_x, number_y) not in pairs
                         and (number_y, number_x) not in pairs):
                pairs.append((number_x, number_y))

    return pairs


def index(request):
    """
    Just redirects to main route
    :param request:
    :return:
    """
    return redirect('seven')


def seven(request):
    """
    Show form or find a list of unique number that can add up to 7
    :param request:
    :return:
    """
    if request.method == 'POST':
        form = SevenForm(request.POST)
        if form.is_valid():
            return render(request, 'seven/result.html', {'pairs': _get_pairs(form.cleaned_data['numbers'])})
    else:
        form = SevenForm()

    return render(request, 'seven/index.html', {'form': form})
