def validate_robot_data(data):
    errors = []

    if not data.get('model'):
        errors.append()
    if not data.get('version'):
        errors.append()
    if not data.get('created'):
        errors.append()

    return errors
