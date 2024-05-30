from config.config import conf as config
import vjoule_handler
import pandas as pd

builtin_list = [
    'sum',
#    'hex',
    'abs',
    'len',
#   'divmod',
    'enumerate',
    'map',
    'map_build_list',
    'map_genexp',
    'map_list_comp',
    'filter',
    'filter_build_list',
    'filter_genexp',
    'filter_list_comp',
]


def main():
    for builtin in builtin_list:
        results = {
            # "cpu_original": [],
            # "cpu_custom": [],
            # "ram_original": [],
            # "ram_custom": [],
            "joule_builtin": [],
            "joule_custom": [],
        }

        builtin_scenarios = config[builtin]

        for scenario in builtin_scenarios:
            custom_builtin_path = f'custom_builtin/{builtin}.py'
            original_builtin_path = f'builtin/{builtin}.py'

            # cpu_original = []
            # cpu_custom = []
            # ram_original = []
            # ram_custom = []
            scenario_joule_builtin = []
            scenario_joule_custom = []

            for i in range(5):
                custom_joule_results = vjoule_handler.eval_python(
                    custom_builtin_path,
                    *scenario
                )
                original_joule_results = vjoule_handler.eval_python(
                    original_builtin_path,
                    *scenario
                )

                '''#FOR TESTS
                custom_joule_results = {
                    'CPU': 20,
                    'RAM': 22,
                    'total': 23,
                }

                original_joule_results = {
                    'CPU': 19,
                    'RAM': 18,
                    'total': 15,
                }'''

                # cpu_original.append(original_joule_results['CPU'])
                # cpu_custom.append(custom_joule_results['CPU'])
                # ram_original.append(original_joule_results['RAM'])
                # ram_custom.append(custom_joule_results['RAM'])
                scenario_joule_builtin.append(original_joule_results['total'])
                scenario_joule_custom.append(custom_joule_results['total'])

            # results['cpu_original'].append(cpu_original)
            # results['cpu_custom'].append(cpu_custom)
            # results['ram_original'].append(ram_original)
            # results['ram_custom'].append(ram_custom)
            results['joule_builtin'].append(scenario_joule_builtin)
            results['joule_custom'].append(scenario_joule_custom)

            results_path = f'output/{builtin}.csv'

            df = pd.DataFrame(results)
            df.to_csv(results_path, index=True)


if __name__ == '__main__':
    main()
