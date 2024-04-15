import os
import pathlib

from inputs import AwsParameter, parse_input_params
from common.aws_clients import get_client


def run(aws_parameters: dict[str, AwsParameter]):
    print(aws_parameters)
    for n, p in aws_parameters.items():
        print(f"{n}: {p.value}")
    ssm_client = get_client(service_name='ssm',
                            region_name=os.getenv('AWS_REGION'),
                            aws_access_key=os.getenv('AWS_ACCESS_KEY'),
                            aws_secret_key=os.getenv('AWS_SECRET_KEY'),
                            )
    for name, param in aws_parameters.items():
        ssm_client.put_parameter(Name=param.name, Value=param.value, Type=param.param_type, Overwrite=param.overwrite)


if __name__ == '__main__':
    print("test")
    input_params = os.getenv('INPUT_PARAMS')
    params_inline = parse_input_params(input_params) if input_params is not None else {}
    params_from_file = {}
    params_file_path = os.getenv('INPUT_PARAMS_FILE_PATH')
    print(f"params_file_path: {params_file_path}")
    print(params_file_path)
    print(f"workspace: {os.getenv('GITHUB_WORKSPACE')}")
    if params_file_path is not None and params_file_path != "":
        path = pathlib.PurePath(os.getenv('GITHUB_WORKSPACE'), params_file_path)
        with open(path, 'r') as f:
            params_from_file = parse_input_params(f.read())
    params = {**params_from_file, **params_inline}.items()
