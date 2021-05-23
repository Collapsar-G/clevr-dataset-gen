#!/usr/bin/env bash
start_idx=1
/home/sdu/gjf/blender-2.79/blender --background --python render_images.py -- --num_images 1000 --min_objects 4 --max_objects 4 --output_image_dir ../inc_output/images/ --output_scene_dir ../inc_output/scenes/ --output_scene_file ../inc_output/CLEVR_scenes${start_idx}.json --use_gpu 1 --start_idx ${start_idx}
