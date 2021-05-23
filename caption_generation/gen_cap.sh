#!/usr/bin/env bash
split=train start_idx=30000
#python generate_questions.py --input_scene_file ../data/CLEVR_v1.0/scenes/CLEVR_${split}_scenes.json --output_questions_file ../data/CLEVR_v1.0/captions/CLEVR_${split}_pre_captions_${start_idx}.json --scene_start_idx ${start_idx} --num_scenes 10000 --templates_per_image 90 --instances_per_template 1

python caption_gen.py --input_questions_file ../data/CLEVR_v1.0/captions/CLEVR_${split}_pre_captions_${start_idx}.json --output_dir ../data/CLEVR_v1.0/captions/CLEVR_${split}_captons_${start_idx}.json