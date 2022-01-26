[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-f059dc9a6f8d3a56e377f745f24479a46679e63a5d9fe6f495e02850cd0d8118.svg)](https://classroom.github.com/online_ide?assignment_repo_id=6700079&assignment_repo_type=AssignmentRepo)

## Execução

  - python main.py

## Exemplos

```
{
  "method": "backward",
  "initialData": ["S"],
  "goal": "R",
  "rules": [
    ["P & Q", "R = SIM"],
    ["S",     "T = SIM"],
    ["T",     "P = SIM"],
    ["S",     "V = SIM"],
    ["V",     "Q = SIM"]
  ]
}


{
  "method": "backward",
  "initialData": [
    "I", "T", "U"
  ],
  "goal": "O",
  "rules": [
    ["P & Q", "O = SIM"],
    ["R & S", "P = SIM"],
    ["W & R", "P = SIM"],
    ["T & U", "Q = SIM"],
    ["V",     "S = SIM"],
    ["I",     "V = SIM"],
    ["I",     "R = SIM"],
    ["I",     "Q = SIM"]
  ]
}



{
  "method": "backward",
  "initialData": ["I", "V"],
  "goal": "O",
  "rules": [
    ["P & Q", "O = SIM"],
    ["W & R", "P = SIM"],
    ["R & S", "P = SIM"],
    ["I",     "R = SIM"],
    ["V",     "S = SIM"],
    ["V",     "Q = SIM"]
  ]
}



{
  "method": "forward",
  "initialData": ["S"],
  "goal": "R",
  "rules": [
    ["P & Q", "R = SIM"],
    ["S", "T = SIM"],
    ["T", "P = SIM"],
    ["S", "V = SIM"],
    ["V", "Q = SIM"]
  ]
}

```
