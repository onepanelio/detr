import os
import json
import argparse

def update_img_paths(args):
    # read json data
    with open(args.file_path, "r") as file:
        json_data = json.load(file)
        # update image path
        for img in json_data['images']:
            img['file_name'] = os.path.join(args.prefix, os.path.basename(img['file_name']))
        # write data back to file
        with open(args.file_path, "w") as file_out:
            json.dump(json_data, file_out)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--file_path', default="/mnt/data/datasets/annotations/instances_default.json")
    parser.add_argument('--prefix', default="/media/savan/Data/GitHub/detr/ddata")
    args = parser.parse_args()
    update_img_paths(args)
