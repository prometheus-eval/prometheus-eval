from datasets import load_dataset

if __name__ == "__main__":
    dataset = load_dataset("prometheus-eval/BiGGen-Bench")

    print(dataset)
