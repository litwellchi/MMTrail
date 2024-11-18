import open_clip
import torch
from PIL import Image
import argparse
import json
import cv2

def getImageFromVideo(clip_path):
    num_frames=3
    try:
        cap = cv2.VideoCapture(clip_path)
        frame_list = []
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        if frame_count <= num_frames:
            query_list = [0,0,0]
        else:
            query_list =  [0, frame_count // 2, frame_count - 1]
        for i in query_list:
            cap.set(cv2.CAP_PROP_POS_FRAMES, i)
            _, frame = cap.read()
            frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            frame_list.append(Image.fromarray(frame).convert("RGB"))
        return frame_list
    except:
        Exception(f"Failed to open video file {clip_path}.")
        return None

def run(input_json,output_json):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model, _, transform = open_clip.create_model_and_transforms(
    model_name="coca_ViT-L-14",
    pretrained="mscoco_finetuned_laion2B-s13B-b90k",
    device=device
    )

    with open(input_json,"r") as f:
        data = json.load(f)[:5]
    
    result_list = []
    for item in data:
        video_path = item["video_path"]
        frame_list = getImageFromVideo(video_path)
        frame_list = [transform(frame).unsqueeze(0) for frame in frame_list]
        frames = torch.cat(frame_list, dim=0)

        with torch.no_grad(), torch.cuda.amp.autocast():
            generated = model.generate(frames.to(device))

        result = [open_clip.decode(item).split("<end_of_text>")[0].replace("<start_of_text>", "") for item in generated]
        # print(result)
        item["coca_caption"] = result
        result_list.append(item)

    with open(args.output_json,"w") as f:
        json.dump(result_list,f,indent=4)
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_json', type=str)
    parser.add_argument('--output_json', type=str)
    args = parser.parse_args()

    run(args.input_json, args.output_json)