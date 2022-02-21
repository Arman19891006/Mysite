from django.http import HttpResponse,JsonResponse

def http_test(request):
    return HttpResponse('Hi ArmanRizan')


def json_test(request):
    return JsonResponse({'Name':'ArmanRizan'})