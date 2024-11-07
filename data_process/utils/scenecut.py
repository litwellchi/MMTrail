import os
import json
import argparse
from tqdm import tqdm
from typing import List, Any, Union
from scenedetect import open_video, SceneManager
from scenedetect.detectors import ContentDetector
from scenedetect.video_splitter import split_video_ffmpeg
from scenedetect.frame_timecode import FrameTimecode


class MetadataDict:
    def __init__(self):
        self.metadata = {
            "basic": {
                "video_id": "",
                "video_path": "",
                "video_duration": 0.0,
                "video_resolution": [],
                "video_fps": 0.0,
                "clip_id": "",
                "clip_path": "",
                "clip_duration": 0.0,
                "clip_start_end_idx": [0, 0],
            },
            "transcript": {}
        }

    def set_basic_info(self, index: int, video_id: str, video_path: str, scenes: List[List[FrameTimecode]],
                       resolution: set, out_dir: str):
        scene = scenes[index]
        self.metadata["basic"]["video_id"] = video_id
        self.metadata["basic"]["video_path"] = os.path.join(os.path.basename(os.path.dirname(video_path)), os.path.basename(video_path))
        self.metadata["basic"]["video_duration"] = scenes[-1][1].get_seconds()
        self.metadata["basic"]["video_resolution"] = resolution
        self.metadata["basic"]["video_fps"] = scenes[0][0].get_framerate()
        self.metadata["basic"]["clip_id"] = f'{video_id}_{"%07d" % index}'
        self.metadata["basic"]["clip_path"] = f"{self.metadata['basic']['clip_id']}.mp4"
        self.metadata["basic"]["clip_duration"] = (scene[1] - scene[0]).get_seconds()
        self.metadata["basic"]["clip_start_end_idx"] = [scene[0].get_frames(), scene[1].get_frames()]

    def load_from_dict(self, metadata_dict: dict):
        if "basic" in metadata_dict:
            self._set_basic_info(**metadata_dict["basic"])
        if "transcript" in metadata_dict:
            try:
                self.set_transcript_info(metadata_dict["transcript"])
            except:
                self.set_transcript_info({})

    def _set_basic_info(self, video_id: str, video_path: str, video_duration: float,
                        video_resolution: List[int], video_fps: int, clip_id: str,
                        clip_path: str, clip_duration: float, clip_start_end_idx: List[int]):
        self.metadata["basic"]["video_id"] = video_id
        self.metadata["basic"]["video_path"] = video_path
        self.metadata["basic"]["video_duration"] = video_duration
        self.metadata["basic"]["video_resolution"] = video_resolution
        self.metadata["basic"]["video_fps"] = video_fps
        self.metadata["basic"]["clip_id"] = clip_id
        self.metadata["basic"]["clip_path"] = clip_path
        self.metadata["basic"]["clip_duration"] = clip_duration
        self.metadata["basic"]["clip_start_end_idx"] = clip_start_end_idx

    def set_transcript_info(self, transcript_info: dict):
        self.metadata["transcript"] = transcript_info

    def get_metadata(self):
        return self.metadata

    def get_value(self, section: str, key: str) -> Any:
        if section in self.metadata and key in self.metadata[section]:
            return self.metadata[section][key]
        else:
            return None

    def update_value(self, section: str, key: str, value: Union[str, int, float, List[Any], dict]) -> bool:
        if section in self.metadata and key in self.metadata[section]:
            self.metadata[section][key] = value
            return True
        else:
            return False

    def to_dict(self) -> dict:
        return self.metadata

def find_scenes(video_path, threshold=30.0):
    video = open_video(video_path)
    scene_manager = SceneManager()
    scene_manager.add_detector(ContentDetector(threshold=threshold))
    scene_manager.detect_scenes(video)
    return scene_manager.get_scene_list(start_in_scene=True), video.frame_size

def run(vid_dir, out_dir):
    threshold = 30.0    # Threshold for detecting scene cuts, the higher the value, the less cuts
    if not os.path.isabs(vid_dir):
        vid_dir = os.path.abspath(vid_dir)
    os.makedirs(out_dir, exist_ok=True)
    
    file_list = os.listdir(vid_dir)
    if len(file_list) == 0:
        return
    
    with open(os.path.join(out_dir, 'metadata.json'), 'a') as out_file:
        for vid_file in tqdm(file_list):
            try:
                if '.' in vid_file:
                    vid_name, vid_ext = vid_file.rsplit('.', 1)
                else:
                    continue
                if vid_ext in ['mp4', 'avi', 'mkv', 'mov', 'wmv', 'flv', 'webm', 'mpeg', 'mpg']:
                    vid_path = os.path.join(vid_dir, vid_file)
                    scenes, resolution = find_scenes(vid_path, threshold=threshold)
                    for index in range(len(scenes)):
                        metadata = MetadataDict()
                        metadata.set_basic_info(index, video_id=vid_name, video_path=vid_path, scenes=scenes,
                                                resolution=resolution, out_dir=out_dir)
                        out_file.write(json.dumps(metadata.to_dict()) + '\n')
                        split_video_ffmpeg(vid_path, [scenes[index]], out_dir, output_file_template="$VIDEO_NAME",
                                            video_name=f"{metadata.get_value('basic', 'clip_id')}.mp4")
            except Exception as e:
                print("An error occurred:", str(e))
                continue

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--vid_dir', type=str)
    parser.add_argument('--out_dir', type=str)
    args = parser.parse_args()

    run(args.vid_dir, args.out_dir)