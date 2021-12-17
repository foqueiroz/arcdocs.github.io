import sys
import pandas as pd


def main(file_path):

    file = pd.read_csv(file_path, names=["host", "module_ver"])

    file["module"] = file.module_ver.apply(lambda x: x.split("/")[0])

    file["version"] = file.module_ver.apply(lambda x: x.split("/")[-1].strip())

    file.sort_values("module", inplace=True)

    for key, group in file.groupby("module"):

        # print(key, end="-")

        for idx, row in group.iterrows():
            print(
                f'{{"HPC":"{row.host}", "version":"{row.version}", "load_name": "{row.module_ver}" }};',
                end="",
            )
        print("")


if __name__ == "__main__":
    main(sys.argv[1])
