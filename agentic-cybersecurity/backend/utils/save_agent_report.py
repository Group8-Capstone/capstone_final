import json


def save_agent_report(
    report_data,
    report_name
):

    save_path = (
        f'outputs/reports/investigation/'
        f'{report_name}.json'
    )

    with open(save_path, 'w') as file:

        json.dump(
            report_data,
            file,
            indent=4
        )

    print(f'Agent report saved: {save_path}')