def flatten_dict(input_dict, parent=None, output=None):
    if parent is None:
        parent = []
    if output is None:
        output = {}

    for key, value in input_dict.items():
        if isinstance(value, dict):
            flatten_dict(value, parent + [key], output)
        else:
            output.setdefault(parent[-1] if parent else None, []).append(value)

    return output

input_dict = {
    "abc": {
        "def": {
            "ghi": {
                "jkl": {
                    "mno": {
                        "pqr": {
                            "stu": {
                                "vwx": {
                                    "yz": "you are finally here !!!"
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

output_dict = flatten_dict(input_dict)
print(output_dict)



