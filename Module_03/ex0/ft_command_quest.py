import sys


def command_interpreter() -> None:
    print("=== Command Quest ===")
    try:
        p_name = sys.argv[0]
        p_arguments_count = len(sys.argv)
        p_arguments_received = p_arguments_count - 1
        i = 1
        flag = 1
        if p_arguments_count == 1:
            print("No arguments provided!")
            flag = 0
        print(f"Program name: {p_name}")
        if flag == 1:
            print(f"Arguments received: {p_arguments_received}")
        while i < p_arguments_count:
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1
        print(f"Total arguments: {p_arguments_count}")
    except Exception:
        raise Exception("Something Went Wrong !")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    command_interpreter()
