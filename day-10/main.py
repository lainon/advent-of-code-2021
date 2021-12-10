from collections import deque
import os.path


def part_one(file):
    file.seek(0)
    score = 0
    stacks = []
    for line in file:
        incomplete = True
        line = line.strip()
        stack = deque()
        for idx, char in enumerate(line):
            if char in ["(", "[", "{", "<"]:
                stack.appendleft(char)
            elif char == ')' and stack[0] != '(':
                score += 3
                incomplete = False
                break
            elif char == ']' and stack[0] != '[':
                score += 57
                incomplete = False
                break
            elif char == '}' and stack[0] != '{':
                score += 1197
                incomplete = False
                break
            elif char == '>' and stack[0] != '<':
                score += 25137
                incomplete = False
                break
            else:
                stack.popleft()
        if incomplete:
            stacks.append(stack)
    print(score)
    return stacks


def part_two(file):
    stacks = part_one(file)
    scores = []
    for stack in stacks:
        score = 0
        for char in stack:
            score *= 5
            if char == '(':
                score += 1
            elif char == '[':
                score += 2
            elif char == '{':
                score += 3
            elif char == '<':
                score += 4
        scores.append(score)
    scores.sort()
    print(scores[int(len(scores)/2)])


def main():
    try:
        with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as file:
            part_one(file)
            part_two(file)

    except IOError:
        print("File not found...")


if __name__ == "__main__":
    main()
