import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from robots.models import Robot
from robots.validators import validate_robot_data


@csrf_exempt
def add_robot(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Неверный метод запроса'}, status=405)

    try:
        data = json.loads(request.body)

        validation_erros = validate_robot_data(data)
        if validation_erros:
            return JsonResponse()

        robot = Robot.objects.create(
            serial='',
            model=data['model'],
            version=data['version'],
            created=data['created']
        )

        return JsonResponse(
            {'message': f'Robot {robot.model}--{robot.version} created {robot.created}.'}
        )
    except json.JSONDecodeError:
        return JsonResponse()
