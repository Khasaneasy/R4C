from django.http import HttpResponse

from orders.reports.excel_generator import excel_generate


def production_dowload_report(request):
    wb = excel_generate()

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    response['Content-Disposition'] = 'attachment; filename="production_report.xlsx"'

    wb.save(response)
    return response
