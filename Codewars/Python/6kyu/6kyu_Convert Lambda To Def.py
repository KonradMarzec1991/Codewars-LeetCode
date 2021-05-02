def convert_lambda_to_def(string):
    anno, body = tuple(string.split(':', 1))
    name, lamb = tuple(anno.split('='))
    _, var = tuple(lamb.strip().split(' '))

    return f"""def {name.strip()}({var}):\n    return {body.strip()}"""