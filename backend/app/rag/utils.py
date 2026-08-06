from itertools import islice


def chunks(data, size):

    iterator = iter(data)

    while True:

        batch = list(
            islice(iterator, size)
        )

        if not batch:
            break

        yield batch