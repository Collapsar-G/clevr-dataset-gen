import argparse
import json
import os

import ijson

parser = argparse.ArgumentParser()
# /questions/CLEVR_test_questions.json
# Inputs
parser.add_argument('--input_questions_file', default='../data/CLEVR_v1.0/questions/CLEVR_train_questions.json',
                    help="JSON file containing questions information for all images " +
                         "from generate_questions.py")
parser.add_argument('--output_dir', default='../data/CLEVR_v1.0/captions',
                    help="Directory containing JSON templates for captions")


def question2caption(question, answer):
    cap = question
    try:
        cap = cap.replace("?", "")
    except:
        cap = cap
    if (answer == "yes") | (answer == True):
        cap = cap.replace(" ###", "")
    elif (answer == "no") | (answer == False):
        cap = cap.replace("###", "not")
    else:
        cap = cap.replace("###", str(answer))
    cap = cap + "."
    # print(question, answer)
    # print(cap)
    # print("$" * 50)

    return cap


if __name__ == "__main__":
    args = parser.parse_args()
    file = args.input_questions_file
    with open(file, 'r', encoding='utf-8') as f:
        print("loading data from ", file)
        # obj = list(ijson.items(f, 'questions.item'))
        obj = list(json.load(f)["questions"])
    print(len(obj))
    print(obj[0])
    captions = []
    caption = {}
    count = 0
    for item in obj:
        caption = {"image_index": item["image_index"], "caption_index": item["question_index"],
                   "image_filename": item["image_filename"],
                   "caption": question2caption(item["question"], item["answer"])}

        # except:
        #     caption["caption"] = None
        #     print(caption, item["question"], item["answer"])
        #     continue
        captions.append(caption)
        count += 1
        if count % 10000 == 0:
            print("生成" + str(count) + "条文本")
    # print(captions)

    f = args.input_questions_file
    output = {
        'captions': captions
    }
    with open(args.output_dir, 'w') as w:
        json.dump(output, w)
    print("Writing output to %s" % args.output_dir, "total captions " + str(count))
