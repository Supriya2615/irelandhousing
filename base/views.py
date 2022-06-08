from django.shortcuts import render
from pathlib import Path  # Python Standard Library
import pandas as pd
from numpy import int64
from .forms import ReportSearchForm

from .utils import get_chart

import matplotlib.pyplot as plt


# Create your views here.

def home(request):
    chart = None
    chart = get_chart('1975', '2016', '#0', 'None', 'None')
    context = {'chart': chart}
    return render(request, 'base/home.html', context)


def reportForm(request):
    chart = None
    no_data = None
    report_form = ReportSearchForm(request.POST or None)

    if request.method == 'POST':
        year_from = request.POST.get('year_from')
        year_to = request.POST.get('year_to')
        chart_type = request.POST.get('chart_type')
        show_results_of = request.POST.get('show_results_of')
        compare_results_to = request.POST.get('compare_results_to')
        chart = get_chart(year_from, year_to, chart_type, show_results_of, compare_results_to)
    else:
        no_data = 'No data available in this date range'
    context = {'report_form': report_form, 'chart': chart, 'no_data':no_data}

    return render(request, "base/report-form.html", context)
