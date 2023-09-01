# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# mala zmiana - Fibbo:
if __name__ == '__main__':
    print_hi('PyCharm')
    x = 1
    y = 0
    for i in range(1,20):
        z = x + y
        y = x
        x = z
        print(z)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


