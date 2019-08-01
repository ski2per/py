import json
import yaml


outer_key = []

class Dict2Prop():
    def __init__(self, dic):
        self.dic = dic
        self.level = 0
        self.outer_keys = []
        self.track = {}

    def iterdict(self, d:dict):
        self.level += 1
        self.track[self.level] = self.outer_keys

        # print(outer_key)
        for k, v in d.items():
            self.outer_keys.append(k)
            if isinstance(v, dict):
                self.iterdict(v)
            else:
                print(k, v)
                # print(outer_key, v)
                # print(outer_key)
                # outer_key.clear()


if __name__ == "__main__":
    with open('application-dkxl.yml', 'r') as f:
        data = yaml.load(f, yaml.Loader)
        print(json.dumps(data))

       # print(json.dumps(data, indent=4))
       # print(data.keys())
       # iterdict(data)
    # with open('test.json', 'r') as f:
    #     data = json.load(f)

        # d2p = Dict2Prop(data)
        # d2p.iterdict(d2p.dic)
