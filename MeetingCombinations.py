import itertools 


def get_meeting_couples(participants: list[str]):
    return itertools.combinations(participants, 2)


if __name__ == "__main__":
    no_of_participants = int(input("Enter the number of participants: "))
    participants = []
    print("Enter the names of participants (1 on each line): ")
    for _ in range(no_of_participants):
        participants.append(input())

    print(list(get_meeting_couples(participants)))
