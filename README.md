[![Requirements Status](https://requires.io/github/lancelote/stepic_python_in_action_eng/requirements.svg?branch=master)](https://requires.io/github/lancelote/stepic_python_in_action_eng/requirements/?branch=master)
[![Build Status](https://travis-ci.org/lancelote/stepic_python_in_action_eng.svg?branch=master)](https://travis-ci.org/lancelote/stepic_python_in_action_eng)

# stepic_python_in_action_eng

Code for [Stepic][1] course [Python in Action (eng)][2]

## Requirements

 - Python 3
 - Inside virtual environment: `pip install -r requirements.txt`

## Utils

Simple scripts to handle the project routine tasks

### Tests

 - `invoke tests` - uses (`pytest`)

### Syntax Validation

 - `invoke syntax` - uses (`pylint`)

### New Solution

 - `invoke new 135` will create solution and test file templates for s135

### Renaming

 - `invoke rename` will rename all solutions and test files (imports will be
   auto fixed), renaming logic defined in the `update_number` function inside
   [`utils.py`](utils/utils.py)

 [1]: https://stepic.org/
 [2]: https://stepic.org/course/Adaptive-Python-%CE%B2-568
