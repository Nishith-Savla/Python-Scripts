import pickle

filename = 'FACTORY.DAT'


def load_pickle_file():
    global filename
    with open(filename, 'rb') as file:
        return pickle.load(filename)


def create():
    global filename
    factory_id, name, workers, factory_type = input().split()
    loaded = load_pickle_file(filename)
    loaded.append(factory_id, name, workers, factory_type)
    with open(filename, 'wb') as outfile:
        file.write(pickle.dump(loaded, outfile))


def count(factory_type: str):
    loaded = load_pickle_file(filename)
    count = 0
    for _, _, _, f_type in loaded:
        if f_type == factory_type:
            count += 1
    return count


if __name__ == "__main__":
    main()
