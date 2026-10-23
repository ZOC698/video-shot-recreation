import os
import cv2
import math
import json
import argparse
from PIL import Image, ImageDraw, ImageFont

def calculate_grid_dims(n_frames):
    """
    Dynamically determine optimal cols and rows for any frame count from 4 to 100+ frames.
    Follows Information Density Adaptive Principle (无上限原则).
    """
    if n_frames <= 4:
        return 2, 2
    elif n_frames <= 6:
        return 3, 2
    elif n_frames <= 8:
        return 4, 2
    elif n_frames <= 12:
        return 4, 3
    elif n_frames <= 16:
        return 4, 4
    elif n_frames <= 20:
        return 5, 4
    elif n_frames <= 24:
        return 6, 4
    elif n_frames <= 30:
        return 6, 5
    elif n_frames <= 36:
        return 6, 6
    elif n_frames <= 48:
        return 8, 6
    elif n_frames <= 64:
        return 8, 8
    elif n_frames <= 80:
        return 10, 8
    else:
        cols = 10
        rows = math.ceil(n_frames / cols)
        return cols, rows

def generate_contact_sheet(video_path, shot_info, output_path, thumb_w=390, thumb_h=164):
    """
    Generates a Codex-style contact sheet grid for a single shot.
    shot_info schema:
    {
        "id": "01",
        "title": "SHOT 01 · 极远景风暴建立",
        "desc": "雷云低垂与野兽派基地停机坪",
        "start_ms": 0,
        "end_ms": 2200,
        "frames": [0, 15, 30, 45, ...], # 4 to 100+ frames
        "labels": ["F000 | 00:00.0s 闪电劈落", ...],
        "cols": None, # Optional override
        "rows": None, # Optional override
        "accent": "#58a6ff" # GitHub Blue / Yellow / Red accent
    }
    """
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise IOError(f"Cannot open video file: {video_path}")
        
    fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    n_frames = len(shot_info["frames"])
    default_cols, default_rows = calculate_grid_dims(n_frames)
    cols = shot_info.get("cols") or default_cols
    rows = shot_info.get("rows") or default_rows
    accent = shot_info.get("accent", "#58a6ff")
    
    pad_x, pad_y = 10, 10
    header_h = 46
    bottom_pad = 12
    grid_w = cols * thumb_w + (cols + 1) * pad_x
    grid_h = header_h + rows * thumb_h + (rows + 1) * pad_y + bottom_pad
    
    canvas = Image.new("RGB", (grid_w, grid_h), color="#0d1117")
    draw = ImageDraw.Draw(canvas)
    
    try:
        font = ImageFont.truetype("msyh.ttc", 12)
        title_font = ImageFont.truetype("msyhbd.ttc", 15)
    except:
        font = ImageFont.load_default()
        title_font = font
        
    # Header bar
    draw.rectangle([(0, 0), (grid_w, header_h)], fill="#161b22")
    draw.line([(0, header_h), (grid_w, header_h)], fill="#30363d", width=1)
    draw.ellipse([(14, 16), (24, 26)], fill=accent)
    title_text = f"{shot_info.get('title', 'SHOT')} — {shot_info.get('desc', '')} (共 {n_frames} 帧密集采样)"
    draw.text((34, 13), title_text, fill="#ffffff", font=title_font)
    
    for idx, (f_idx, lbl) in enumerate(zip(shot_info["frames"], shot_info["labels"])):
        if f_idx >= total_frames:
            f_idx = total_frames - 1
            
        cap.set(cv2.CAP_PROP_POS_FRAMES, f_idx)
        ret, frame = cap.read()
        if not ret:
            continue
            
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        im = Image.fromarray(frame_rgb)
        im = im.resize((thumb_w, thumb_h), Image.Resampling.LANCZOS)
        
        im_draw = ImageDraw.Draw(im)
        badge_h = 24
        im_draw.rectangle([(0, thumb_h - badge_h), (thumb_w, thumb_h)], fill=(13, 17, 23))
        im_draw.line([(0, thumb_h - badge_h), (thumb_w, thumb_h - badge_h)], fill=accent, width=1)
        im_draw.text((8, thumb_h - badge_h + 4), lbl, fill="#e6edf3", font=font)
        
        c = idx % cols
        r = idx // cols
        x = pad_x + c * (thumb_w + pad_x)
        y = header_h + pad_y + r * (thumb_h + pad_y)
        
        draw.rectangle([(x-1, y-1), (x + thumb_w + 1, y + thumb_h + 1)], outline="#30363d", width=1)
        canvas.paste(im, (x, y))
        
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    canvas.save(output_path, quality=95)
    cap.release()
    print(f"[ContactSheet] Saved: {output_path} ({n_frames} frames, {cols}x{rows} grid)")
    return output_path

def build_promptdirector_payload(shots, video_meta=None, project_title="影视分镜拉片与复刻"):
    """
    Transforms dense shot breakdowns into PromptDirector native MCP schemas:
    - timeNotes (for timeline markers & review)
    - visualSetAnalyses (for contact sheet multi-frame group analysis)
    - videoAnalyses (for overall shot reverse-engineering)
    - save_material payload (for one-click library persistence)
    """
    time_notes = []
    visual_set_analyses = []
    video_analyses = []
    contact_files = []
    
    for shot in shots:
        shot_id = shot.get("id", "00")
        start_ms = shot.get("start_ms", 0)
        end_ms = shot.get("end_ms", 0)
        title = shot.get("title", f"SHOT {shot_id}")
        desc = shot.get("desc", "")
        six_d = shot.get("six_d", {})
        
        # 1. PromptDirector timeline note
        time_notes.append({
            "assetId": shot.get("asset_id", f"shot_{shot_id}"),
            "startMs": start_ms,
            "endMs": end_ms,
            "text": f"[{title}] {desc} | 镜头: {six_d.get('camera', '')} | 视效: {six_d.get('vfx', '')} | 力学: {six_d.get('action', '')}"
        })
        
        # 2. PromptDirector visualSetAnalyses (组图系统分析)
        visual_set_analyses.append({
            "assetIds": [shot.get("sheet_file", f"shot_{shot_id}_sheet.jpg")],
            "imageRoles": {
                f"frame_{idx:02d}": lbl.split("|")[-1].strip()
                for idx, lbl in enumerate(shot.get("labels", []))
            },
            "sharedVisualSystem": six_d.get("vfx", "高光比暗黑基调，等离子流体与体积光"),
            "differences": f"帧间物理形变：共采录 {len(shot.get('frames', []))} 帧，涵盖起始蓄势至爆发衰减微步",
            "continuity": six_d.get("action", "动量守恒与预备冲量传递"),
            "compositionRules": six_d.get("camera", "极远景/特写/轴线规则"),
            "reusablePrompt": shot.get("reusable_prompt", six_d.get("prompt", ""))
        })
        
        # 3. PromptDirector videoAnalyses
        video_analyses.append({
            "assetId": shot.get("asset_id", f"shot_{shot_id}"),
            "reconstructionPrompt": shot.get("reusable_prompt", ""),
            "tags": shot.get("tags", ["dense-shot", "action-dynamics", "impact-frame", "vfx-morphology"]),
            "uncertainties": shot.get("uncertainties", []),
            "analysisScope": "visual"
        })
        
        if "sheet_file" in shot:
            contact_files.append(os.path.abspath(shot["sheet_file"]))
            
    # 4. PromptDirector save_material payload
    save_material_payload = {
        "title": project_title,
        "kind": "creation",
        "creative": {
            "prompt": "影视分镜与动作动力学可执行提示词矩阵",
            "summary": f"基于自适应高密抽帧与 PromptDirector 协议完成的工业级逐镜头拉片全案，涵盖 {len(shots)} 组独立镜头接触网格与六维解析。",
            "notes": "符合总导演五大铁律：一个镜头一组、信息密度自适应抽帧、视效形态逐帧量化、严禁稀疏脑补。",
            "purpose": "影视级动作复刻、AI 视频分镜精准控制与角色特征移植",
            "plan": "将原片动力学与镜头调度移植至自研设定（如二头身咕嘎 Doro vs BSAA 重装机甲）"
        },
        "timeNotes": time_notes,
        "files": contact_files,
        "sourceFacts": {
            "tool": "video-shot-recreation-v3",
            "totalShots": len(shots),
            "videoMeta": video_meta or {}
        }
    }
    
    return {
        "timeNotes": time_notes,
        "visualSetAnalyses": visual_set_analyses,
        "videoAnalyses": video_analyses,
        "saveMaterialPayload": save_material_payload
    }

def main():
    parser = argparse.ArgumentParser(description="Video Shot Recreation v3.0 (Fused with PromptDirector)")
    parser.add_argument("--video", type=str, help="Path to input video file")
    parser.add_argument("--config", type=str, help="Path to shot configuration JSON file")
    parser.add_argument("--outdir", type=str, default="./output", help="Directory to save contact sheets and JSON")
    parser.add_argument("--export_pd", action="store_true", help="Export PromptDirector MCP compatible payload JSON")
    args = parser.parse_args()
    
    if not args.config:
        print("[Notice] No --config specified. Run with --help for usage details.")
        return
        
    with open(args.config, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    video_path = args.video or data.get("video_path")
    shots = data.get("shots", [])
    os.makedirs(args.outdir, exist_ok=True)
    
    for shot in shots:
        sheet_filename = f"shot_{shot['id']}_sheet.jpg"
        sheet_path = os.path.join(args.outdir, sheet_filename)
        shot["sheet_file"] = sheet_path
        if video_path and os.path.exists(video_path):
            generate_contact_sheet(video_path, shot, sheet_path)
            
    if args.export_pd:
        pd_data = build_promptdirector_payload(shots, video_meta=data.get("video_meta"), project_title=data.get("title", "分镜拉片结题案"))
        pd_out_path = os.path.join(args.outdir, "promptdirector_export.json")
        with open(pd_out_path, "w", encoding="utf-8") as pf:
            json.dump(pd_data, pf, ensure_ascii=False, indent=2)
        print(f"[PromptDirector] Exported native MCP payloads to: {pd_out_path}")

if __name__ == "__main__":
    main()
