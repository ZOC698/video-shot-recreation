# 视频拉片与复刻 · Video Shot Recreation (v3.0 融合版)

[中文](README.md) | [日本語](README.ja.md) | [English](README.en.md)

工业级影视分析、自适应接触组图（10~100+帧）与 **[PromptDirector 提示词导演](https://github.com/wchao6891/PromptDirector)** 资产中枢深度融合版。

将实战拉片经验、**总导演五大核心军规**、**Codex 风格接触网格组图（Contact Sheets）**、**六维视听解构** 与 **PromptDirector 本地优先 MCP 协议**无缝打通，提供从“参考片采集/审片时间轴”到“高密拉片分析”再到“分镜移植与资产持久化回存”的工业级完整闭环。

---

## 核心升级（v3.0 融合版）

### 1. 深度融合 PromptDirector 资产管理与审片中枢
- **时间轴双向联动**：原生导出 PromptDirector 格式的 `timeNotes`（`{assetId, startMs, endMs, text}`），使拉片成果能够直接在浏览器播放器时间轴上作为毫秒级镜头标记高亮显示。
- **组图系统解构对接**：输出符合 PromptDirector 规范的 `visualSetAnalyses`（`sharedVisualSystem`, `differences`, `continuity`, `compositionRules`, `reusablePrompt`），与多帧网格完美绑定。
- **一键回存与 Skill 封装**：支持生成标准 `save_material` 载荷，可直接通过本机 MCP 将组图资产、结题报告与提示词矩阵存入本地资料库，并使用 `save_skill` 打包为可复用创作技能。
- **资料完整性原则**：客观画面事实与 AI 推断严格隔离，AI 逆推明确标记 `ai-suggestion`，原片与原始提示词受保护留存。

### 2. 贯彻总导演五大核心军规（用户原话无损定调）
1. **镜头意识与景别调度**：严禁全篇单调平视死镜头，精准识别并还原极远景（EWS）、仰俯角（Tilt Up/Down）、快推特写（Crash Zoom）与侧移跟拍（Tracking）。
2. **Codex 组图与六维框架**：强制采用网格接触图集中呈现镜头演变，每组严格归纳：**使用的镜头、视觉效果、完成剧情叙事、人物动作与力学、人物行为逻辑与心理、使用的拍摄手法与剪辑技法**。
3. **严禁稀疏抽帧与视觉脑补**：锁死关键战斗窗口，严格执行高密采样，绝不凭空脑补未发生的动作或位移。
4. **一个镜头一组，深挖形态演变与真实物理**：以物理剪辑切点（Cut Point）为法定边界；对复杂视效（如冲击波三态演化：紫金初核/引力拱门 $\rightarrow$ 贴地旋转金光涡流 $\rightarrow$ 半球巨穹顶与双马赫环）逐帧追踪形变全程；绝不脑补角色位移（如将身处爆心误判为冲出火雾）。
5. **信息密度自适应采样（无上限原则）**：网格不限定几帧。信息密度高则 24 帧、48 帧、100 帧均可；信息密度低则十几帧。唯一终极标准是**“保留全部原本信息，防止遗漏与错误”**。

---

## 双引擎工作流架构

```text
[PromptDirector 资产驾驶舱]
  ├── 20+ 平台图文/视频一键采集 (保留原始提示词与上下文)
  └── 时间轴审片 (I/O 键圈选区间, timeNotes 标记关键爆点)
        │
        ▼ 本机 Native MCP 协议调用 (read_workspace_content / control_workspace)
[Dense Shot Analysis 工业级拉片大脑]
  ├── 物理剪辑切点划分 (一个镜头一组)
  ├── 信息密度自适应抽帧 (爆点/冲击波无上限采样 10~100+ 帧)
  ├── Codex 风格暗黑网格合成 (generate_shot_sheets.py)
  ├── 六维视听解构与流体多阶段形变追踪
  └── 分镜移植与 Seedance 2.5 / Midjourney 提示词矩阵重构
        │
        ▼ 结构化数据导出与 MCP 双向回存 (save_material / submit_analysis_result)
[本地个人影视分镜案例库]
  ├── 毫秒级时间轴标记可跳回播放 (timeNotes)
  ├── 组图分析系统留存 (visualSetAnalyses)
  └── 沉淀为可跨 Agent 复用的标准创作技能 (save_skill)
```

---

## 目录结构

```text
video-shot-recreation/
├── SKILL.md            # 核心技能入口文档（含导演五大军规、融合协议与六步拉片流程）
├── README.md           # 项目介绍与使用指南
├── SOURCES.md          # 理论来源、开源工具与证据边界
└── scripts/
    ├── generate_shot_sheets.py      # 自适应接触网格组图合成与 PromptDirector MCP 数据导出器
    └── example_shot_config.json    # 标准镜头配置与六维分析模板样例
```

---

## 快速使用

### 1. 命令行一键生成接触网格与 PromptDirector 载荷
```bash
# 依据配置文件生成高密组图，并自动导出 PromptDirector MCP 专用 JSON
python scripts/generate_shot_sheets.py \
  --video "path/to/reference_video.mp4" \
  --config "scripts/example_shot_config.json" \
  --outdir "output/" \
  --export_pd
```

执行后将在 `output/` 目录生成：
- 各镜头暗黑风格 Contact Sheet 网格图像（`shot_01_sheet.jpg`, `shot_02_sheet.jpg`, ...）
- `promptdirector_export.json`：包含标准 `timeNotes`、`visualSetAnalyses`、`videoAnalyses` 和 `saveMaterialPayload`，可直接通过 MCP 回存或前端导入。

### 2. Python 模块级调用
```python
from scripts.generate_shot_sheets import generate_contact_sheet, build_promptdirector_payload

shot_info = {
    "id": "06",
    "title": "SHOT 06 · 核心冲击帧对拳",
    "desc": "原画级负片线稿轰面与等离子火球引爆",
    "frames": [384, 389, 394, 399, 404, 409],  # 支持 4 至 100+ 帧任意密度
    "labels": ["F384 | 00:12.8s 纯黑白负片线稿", ...],
    "accent": "#f85149"
}

# 1. 生成自适应暗黑接触组图
generate_contact_sheet("path/to/video.mp4", shot_info, "output/shot_06.jpg")

# 2. 导出 PromptDirector 结构包
pd_payload = build_promptdirector_payload([shot_info])
```

### 3. Agent 对话调用范例
```text
使用 $video-shot-recreation 对该片段进行融合版逐镜头拉片：
1. 锁定核心对决段落，严格执行一个镜头一组；
2. 高信息密度镜头无上限抽帧，生成 Codex 风格暗黑接触网格；
3. 每一帧给出毫秒级动作与视效描述，每组完成六维专业解构；
4. 追踪冲击波与气浪的完整流体演变；
5. 完成分镜移植与提示词矩阵，并导出兼容 PromptDirector MCP 的 timeNotes 与回存载荷。
```

---

## 安装与配置

### 本地 Skill 安装
将本仓库克隆至本地 Agent 技能目录：
```sh
# Claude Code / Codex 本地目录
git clone https://github.com/ZOC698/video-shot-recreation.git ~/.codex/skills/video-shot-recreation

# 或 Antigravity 全局目录
git clone https://github.com/ZOC698/video-shot-recreation.git ~/.gemini/config/skills/video-shot-recreation
```

### 依赖项
- Python 3.8+
- OpenCV (`pip install opencv-python`)
- Pillow (`pip install Pillow`)

---

## 协议与来源

- 融合工业级电影拉片规范、日系原画冲击帧理论与计算机视觉技术。
- MCP 协议与资产回存规范对齐 [PromptDirector](https://github.com/wchao6891/PromptDirector) 开源标准。
- 详细理论来源与证据边界参见 [SOURCES.md](SOURCES.md)。
