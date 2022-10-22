def compact(lst):
        return [item for item in lst if item]

print(compact([0, 1, 2, '', [], False, (), None, 'All done']))