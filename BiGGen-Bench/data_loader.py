import json
from pathlib import Path


class BiGGenBenchLoader:
    def __init__(self):
        self.dataset_path = Path(__file__).parent.parent / "tasks"
        self.data = {}  # Changed to a dictionary for hierarchical storage

    def load_data(self):
        for capability_path in self.dataset_path.iterdir():
            if capability_path.is_dir():
                capability_name = capability_path.name
                self.data[capability_name] = {}  # Initialize capability dictionary
                for task_path in capability_path.iterdir():
                    if task_path.is_dir():
                        task_name = task_path.name
                        self.data[capability_name][
                            task_name
                        ] = []  # Initialize task list
                        data_file = task_path / "data.json"
                        if data_file.exists():
                            with open(data_file, "r", encoding="utf-8") as file:
                                data_json = json.load(file)
                                for idx, instance in enumerate(data_json):
                                    unique_id = f"{capability_name}_{task_name}_{instance['instance_idx']}"
                                    instance_data = {"id": unique_id, **instance}
                                    self.data[capability_name][task_name].append(
                                        instance_data
                                    )

    def dump_data(self):
        print(json.dumps(self.data, indent=2))

    def query_data(self, capability_names=None, task_names=None):
        """
        Query the loaded data based on capability and task names.

        Parameters:
        - capability_names: A list of capability names to filter by.
        - task_names: A list of task names to filter by.

        Returns:
        - A dictionary of filtered data based on the provided criteria.
        """
        filtered_data = {}
        for capability_name, tasks in self.data.items():
            if capability_names is None or capability_name in capability_names:
                filtered_data[capability_name] = {}
                for task_name, instances in tasks.items():
                    if task_names is None or task_name in task_names:
                        filtered_data[capability_name][task_name] = instances

        # Removing empty capabilities from the final result
        filtered_data = {cap: tasks for cap, tasks in filtered_data.items() if tasks}

        return filtered_data


if __name__ == "__main__":
    # Example usage
    loader = BiGGenBenchLoader()
    loader.load_data()
    dataset_dict = loader.data
    # loader.dump_data()

    # Show the statistics of the dataset
    print("Statistics of the dataset:")

    for capability_name, tasks in dataset_dict.items():
        if capability_name == "vision":
            continue

        print(f"Capability: {capability_name}")
        for task_name, instances in tasks.items():
            print(f"    Task: {task_name} - {len(instances)} instances")
        print()
        print(f"Number of tasks in {capability_name}: {len(tasks)}")
        print(
            f"Number of instances in {capability_name}: {sum([len(instances) for instances in tasks.values()])}"
        )
        print()

    uid_set = set()

    for capability_name, tasks in dataset_dict.items():
        if capability_name == "vision":
            continue
        for task_name, instances in tasks.items():
            for instance in instances:
                uid_set.add(instance["id"])

    print(len(uid_set))
