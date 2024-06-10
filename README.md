# 🎞MMTrail: A Multimodal Trailer Video Dataset with Language and Music Descriptions

This is the offical Github repository of MMTrail-20M

[![arXiv](https://img.shields.io/badge/arXiv-2311.17963-b31b1b.svg)](https://github.com/litwellchi/MMTrail)
[![Project Page](https://img.shields.io/badge/Project-Website-green)](https://github.com/litwellchi/MMTrail)


<div align='center'>
<img src="examples/teaser.png" class="interpolation-image" alt="teaser." height="96%" width="96%" />
</div>

## TODO
- [ ] Testing Prompts
- [ ] Release MMTrail-3M metadata
- [ ] Release Processing code
- [ ] Release MMTrail-Test metadata

## Updates!!
* 【2024/06/10】 We build our github page

## Introduction
MMTrail is a large-scale multi-modality video-language dataset with over 20M trailer clips, featuring high-quality multimodal captions that integrate context, visual frames, and background music, aiming to enhance cross-modality studies and fine-grained multimodal-language model training.

## Download

 | Split           | Download | # Samples | Video Duration | Storage Space|
  |-----------------|----------|-----------------|-----------|----------------|
  | Training (20M)  | TODO (-) | 20M | 27.1 khrs | ~8.0 TB |
  | Training (3M)   | TODO (-)  | 3.2M | 12.2 khrs | ~1.6 TB |
  | Testing         | TODO (2.77 MB)  | 1,000      | 3.5 hrs  | 794 Mb |


  
## Metadata format
```
[
    {
        "basic": {
            "video_id": "-3r7ptfObEs",
            "video_path": "group_33/-3r7ptfObEs.mp4",
            "video_duration": 71.73333333333333,
            "video_resolution": [
                720,
                1280
            ],
            "video_fps": 30.0,
            "clip_id": "-3r7ptfObEs_0000000",
            "clip_path": "video_dataset_33/-3r7ptfObEs_0000000.mp4",
            "clip_duration": 7.033333333333333,
            "clip_start_end_idx": [
                0,
                211
            ],
            "imaging_quality": 36.83453941345215,
            "of_score": 12.92151,
            "aesthetic_score": [
                3.010026454925537,
                3.664743423461914,
                3.994750499725342
            ]
        },
        "camera": {
            "view_scale": "",
            "movement": "",
            "speed": ""
        },
        "misc": {
            "frame_caption": [
                "a person standing in a room with a laptop on their lap. ",
                "a black and blue background with the name of the series. ",
                "a black and white image of the words manga and comics. "
            ],
            "music_caption": [
                {
                    "text": "This is an indie rock music piece. There is a male vocalist singing melodically in the lead. The main tune is being played by the electric guitar while the bass guitar is playing in the background. The rhythm is provided by a simple acoustic drum beat. The atmosphere is easygoing. This piece could be used in the soundtrack of a teenage drama TV series as the opening theme.",
                    "time": "0:00-10:00"
                }
            ]
        },
        "scene": {
            "objects": [
                " Matheus Trindade",
                " de",
                " original",
                "Series",
                " Manga & Comics"
            ],
            "background": "Dark",
            "ocr_score": 0.07147466104497355,
            "caption": "The video is a series of original de Matheus Trindade comics, showcasing the artist's unique style and storytelling.",
            "polish_caption": "Original de Matheus Trindade comics showcase the artist's unique style and storytelling, featuring a series of vibrant and expressive illustrations that bring characters and scenes to life.",
            "merge_caption": "In this captivating video, Matheus Trindade's original comics come to life with vibrant and expressive illustrations, showcasing the artist's unique style and storytelling. Set against a dark background, the video features a series of dynamic and colorful images, including a person sitting in a room with a laptop, a black and blue background with the name of the series, and a black and white image of the words \"manga\" and \"comics.\" The indie rock music piece, featuring a male vocalist and simple acoustic drum beat, adds an easygoing atmosphere to the video, making it perfect for the opening theme of a teenage drama TV series."
        }
    }
]
```


## Notification
The publish version code is still under development. 
### Tutorials
**Validation.**
TODO

## Licience

## Cite MMtrail
```
TODO
```
## Thanks


```latex
```
