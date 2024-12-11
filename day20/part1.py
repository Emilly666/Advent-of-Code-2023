from pathlib import Path
from collections import deque
from pprint import pprint

class Module:
    def __init__(self, name, type, outputs):
        self.name, self.type, self.outputs = name, type, outputs
        
        if type == '%':
            self.memory = 'off'
        else:
            self.memory = {}
    def __repr__(self):
        return self.name + '{type=' + self.type + ', outputs=[' + ', '.join(self.outputs) + '], memory=' + str(self.memory) + '}'

modules = {}
broadcast_targets = []

for line in open(Path(__file__).parent / 'input.txt', 'r').read().split('\n'):
    left, right = line.split(' -> ')
    outputs = right.split(', ')
    if left == 'broadcaster':
        broadcast_targets = outputs
    else:
        name = left[1:]
        modules[name] = Module(name, left[0], outputs)

for name, module in modules.items():
    for output in module.outputs:
        if output in modules and modules[output].type == '&':
            modules[output].memory[name] = 'lo'

lo, hi = 0, 0
for _ in range(1000):
    lo += 1
    q = deque([('broadcaster', x, 'lo') for x in broadcast_targets])

    while q:
        origin, target, pulse = q.popleft()
        if pulse == 'lo':
            lo += 1
        else:
            hi += 1
        
        if target not in modules:
            continue
        
        module = modules[target]
        if module.type == '%' and pulse == 'lo':
            module.memory = 'on' if module.memory == 'off' else 'off'
            out = 'hi' if module.memory == 'on' else 'lo'
            for x in module.outputs:
                q.append((module.name, x, out))
        elif module.type == '&':
            module.memory[origin] = pulse
            out = 'lo' if all(x == 'hi' for x in module.memory.values()) else 'hi'
            for x in module.outputs:
                q.append((module.name, x, out))


pprint(lo * hi)