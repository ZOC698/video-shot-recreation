import os, cv2, math
from PIL import Image, ImageDraw, ImageFont

def calculate_grid_dims(n_frames):
    """Dynamically determine optimal cols and rows for any frame count from 6 to 100+"""
    if n_frames <= 6:
        return 3, 2
    elif n_frames <= 8:
        return 4, 2
    elif n_frames <= 12:
        return 4, 3
    elif n_frames <= 16:
        return 4, 4
    elif n_frames <= 24:
        return 6, 4
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
    shot_info schema:
    {
        "id": "01",
        "title": "SHOT 01 · 镜头标题",
        "desc": "镜头主要内容与视效描述",
        "frames": [0, 22, 45, ...], # Any count from 10 to 100+ frames!
        "labels": ["F000 | 00:00.0s 描述", ...],
        "cols": None, # If None, auto-calculated
        "rows": None, # If None, auto-calculated
        "accent": "#58a6ff"
    }
    """
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    
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
    draw.text((34, 13), f"{shot_info['title']}  —  {shot_info['desc']} (共{n_frames}帧采样)", fill="#ffffff", font=title_font)
    
    for idx, (f_idx, lbl) in enumerate(zip(shot_info["frames"], shot_info["labels"])):
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
        
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    canvas.save(output_path, quality=95)
    cap.release()
    print(f"Saved adaptive contact sheet ({n_frames} frames, {cols}x{rows}) to {output_path}")

if __name__ == "__main__":
    print("Adaptive helper script ready.")
