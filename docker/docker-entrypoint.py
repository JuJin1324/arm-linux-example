import os

WORK_DIR = os.environ['WORK_DIR']


def main():
    build_type = os.environ['BUILD_TYPE']
    build_output_path = os.environ['BUILD_OUTPUT_PATH']

    if not os.path.isdir(f'{WORK_DIR}/{build_output_path}'):
        os.system(f'mkdir {build_output_path}')

    os.system(f'cmake -DCMAKE_BUILD_TYPE={build_type} -B {build_output_path}')
    os.system(f'cd {build_output_path}; make')


if __name__ == '__main__':
    main()
