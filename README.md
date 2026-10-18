# 视频拉片与复刻 · Video Shot Recreation (v2.0)

[中文](README.md) | [日本語](README.ja.md) | [English](README.en.md)

一个提供中文、日本語、English 文档的工业级影视分析与分镜复刻 Skill：融合总导演实战训诫、**Codex 风格接触网格组图（Contact Sheets）**、**信息密度自适应抽帧（10帧到100+帧）**、**一镜头一组精密拉片** 与 **六维视听解构**，服务于高精度动作复刻、角色替换与成片对比诊断。

默认使用用户的语言交付；指定提示词语言时遵从指定。

---

## 核心升级（v2.0）

基于实战拉片与导演级复刻经验，本版本正式确立了**总导演五大核心军规**：

1. **镜头意识与景别调度**：严禁单一平视死镜头，严格把控 EWS 建立、Tilt Up 仰摇、Crash Zoom 爆推与 Tracking 侧移。
2. **Codex 组图与六维框架**：强制采用网格接触图集中呈现镜头演变，每组严格归纳：**使用的镜头、视觉效果、完成剧情叙事、人物动作与力学、人物行为逻辑与心理、使用的拍摄手法与剪辑技法**。
3. **严禁稀疏抽帧与视觉脑补**：锁死关键战斗窗口，严格执行高密采样，绝不凭空脑补未发生的动作或位移。
4. **一个镜头一组，深挖形态演变与真实物理**：以物理剪辑切点（Cut Point）为法定边界；对复杂视效（如冲击波三态演化：紫金初核/引力拱门 $\rightarrow$ 贴地旋转金光涡流 $\rightarrow$ 半球巨穹顶与双马赫环）逐帧追踪形变全程；绝不脑补角色位移（如将身处爆心误判为冲出火雾）。
5. **信息密度自适应采样（无上限原则）**：网格不限定几帧。信息密度高则 24 帧、48 帧、100 帧均可；信息密度低则十几帧。唯一终极标准是**“保留全部原本信息，防止遗漏与错误”**。

---

## 能做什么

- **单镜头独立成组分析**：精准识别物理剪辑点，以 Shot 为单位独立拉片。
- **自适应 Codex 接触网格组图**：调用自动化脚本 `scripts/generate_shot_sheets.py`，生成包含毫秒时间码与动作微描述的暗黑风格网格。
- **冲击帧与流体形态追踪**：对日系原画级负片冲击帧（Impact Frame）、爆炸聚能与激波多阶段形变进行逐帧物理拆解。
- **六维专业总结与量化**：量化击打点、受力反馈、投射物重叠、时间窗口与攻防轮次。
- **分镜移植与复刻结题全案**：输出角色映射表、尺度反差萌力学、导演实操避坑法则，并生成直接可用于 Seedance 2.5 / Midjourney 的提示词矩阵（Prompt Matrix）。

---

## 目录结构

```text
video-shot-recreation/
├── SKILL.md            # 核心技能入口文档（含导演五大军规与四步拉片流程）
├── README.md           # 项目介绍与使用指南
├── SOURCES.md          # 理论来源、开源工具与证据边界
└── scripts/
    └── generate_shot_sheets.py  # 工业级自适应接触网格组图生成脚本（支持10-100+帧）
```

---

## 快速使用

### 1. 组图生成脚本使用
```python
from scripts.generate_shot_sheets import generate_contact_sheet

shot_info = {
    "id": "06",
    "title": "SHOT 06 · 核心冲击帧对拳",
    "desc": "原画级负片线稿轰面与等离子火球引爆",
    "frames": [384, 389, 394, 399, 404, 409],  # 支持任意帧数，自适应排版
    "labels": ["F384 | 00:12.8s 纯黑白负片线稿", ...],
    "accent": "#f85149"
}

generate_contact_sheet("path/to/video.mp4", shot_info, "output/shot_06.jpg")
```

### 2. 对话调用范例
```text
使用 $video-shot-recreation 对该片段前30秒进行逐镜头拉片：
严格执行一个镜头一组，信息密度高的镜头抽足帧数生成Codex组图，
每一帧下面写画面描述，每组做六维总结，最后提供分镜移植结题报告。
```

---

## 安装

将本仓库克隆至本地技能目录：
```sh
git clone https://github.com/ZOC698/video-shot-recreation.git ~/.codex/skills/video-shot-recreation
```
或放置于 Antigravity 全局目录 `~/.gemini/config/skills/video-shot-recreation` 即可生效。

---

## 来源与验证状态

融合工业级电影拉片规范、日系作画与美漫冲击帧视效理论、社区高燃打斗提示词方法与 OpenCV 计算机视觉技术。
详细参考见 [SOURCES.md](SOURCES.md)。
