# Python List Methods

- **`append(item)` — adds one item to the end of the list.**

  `numbers = [1, 2]; numbers.append(3); print(numbers)  # Output: [1, 2, 3]`

- **`extend(iterable)` — adds all items from another iterable to the end of the list.**

  `numbers = [1, 2]; numbers.extend([3, 4]); print(numbers)  # Output: [1, 2, 3, 4]`

- **`pop(index)` — removes and returns the item at an index; without an index, it removes the last item.**

  `numbers = [1, 2, 3]; removed = numbers.pop(); print(numbers, removed)  # Output: [1, 2] 3`

- **`remove(item)` — removes the first matching item from the list.**

  `numbers = [1, 2, 2]; numbers.remove(2); print(numbers)  # Output: [1, 2]`

- **`sort()` — sorts the list in place.**

  `numbers = [3, 1, 2]; numbers.sort(); print(numbers)  # Output: [1, 2, 3]`

- **`reverse()` — reverses the list in place.**

  `numbers = [1, 2, 3]; numbers.reverse(); print(numbers)  # Output: [3, 2, 1]`

- **`insert(index, item)` — adds an item at a specific position.**

  `numbers = [1, 3]; numbers.insert(1, 2); print(numbers)  # Output: [1, 2, 3]`

- **`copy()` — returns a shallow copy of the list.**

  `numbers = [1, 2, 3]; copied = numbers.copy(); print(copied)  # Output: [1, 2, 3]`

- **`count(item)` — returns how many times an item appears in the list.**

  `numbers = [1, 2, 2, 3]; print(numbers.count(2))  # Output: 2`

- **`index(item)` — returns the index of the first matching item.**

  `numbers = [10, 20, 30]; print(numbers.index(20))  # Output: 1`

- **`clear()` — removes all items from the list.**

  `numbers = [1, 2, 3]; numbers.clear(); print(numbers)  # Output: []`
