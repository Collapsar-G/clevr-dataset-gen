import argparse
import json
import os

import ijson

parser = argparse.ArgumentParser()
# /questions/CLEVR_test_questions.json
# Inputs
parser.add_argument('--all_scene_paths', default='../data/CLEVR_v1.0/scenes',
                    help="JSON file containing questions information for all images " +
                         "from generate_questions.py")
parser.add_argument('--output_scene_file', default='../data/CLEVR_v1.0/CLEVR_train_scenes.json',
                    help="Directory containing JSON templates for captions")

if __name__ == "__main__":
    all_scenes = []
    args = parser.parse_args()
    paths = os.listdir(args.all_scene_paths)
    for scene_path in paths:
        # print(scene_path)
        with open(args.all_scene_paths + "/" + scene_path, 'r') as f:
            all_scenes.append(json.load(f))
    output = {
        'info':
            {"split": "train", "license": "Creative Commons Attribution (CC BY 4.0)", "version": "1.0",
             "date": "2/14/2017"},
        'scenes': all_scenes
    }
    with open(args.output_scene_file, 'w') as f:
        json.dump(output, f)
