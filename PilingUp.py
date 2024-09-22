def can_stack_cube(cube):
    left = 0
    right = len(cube) - 1
    last_cube = float('inf')
    while left <= right:
        if cube[left] >= cube[right]:
            select_cube = cube[left]
            left += 1
        else:
            select_cube = cube[right]
            right -= 1
            
        if select_cube > last_cube:
            return "No"
        last_cube = select_cube
    return "Yes"

n = int(input())
cube = list(map(int, input().split()))
print(can_stack_cube(cube))