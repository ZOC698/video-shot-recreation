# 来源、取舍与证据边界

[中文](SOURCES.md) | [日本語](SOURCES.ja.md) | [English](SOURCES.en.md)

查阅日期：2026-10-05。链接内容可变化；本文件记录借鉴范围，不认证第三方全部结论，也不代表与这些项目存在合作关系。

## 社区动作导演方法

[liyue-aigc/seedance-2-5-fight-director](https://github.com/liyue-aigc/seedance-2-5-fight-director)

重点阅读其 SKILL.md，以及 references 中的 core-engine、grammar-library、diagnose、fight-camera-library、seedance-adaptation 和 examples。

采用：把动作和对方反应写在一起；接触后给受力结果；群体在不同景深持续参与；相邻镜头延续位置与动量；将素材分工和成片故障分开诊断。

不照搬：固定动作频率上限、默认均势、所有群战密度单调增加、统一地形改变结局、固定长度就必须分段。参考片已经确定的故事、机位、超常速度与入口优先。

其 [examples.md](https://github.com/liyue-aigc/seedance-2-5-fight-director/blob/main/references/examples.md) 明示范例未进行实际生成或成功率测试。因此本项目将其视为社区编排方法，不能称为已证明的模型能力边界。本文为独立归纳，没有复制其完整脚本。

## 镜头表与画面规划

[StudioBinder：How to Make a Shot List](https://www.studiobinder.com/blog/how-to-make-a-shot-list/)

采用镜头表组织画面信息、以图片辅助沟通的工作思路。本项目另加“观察事实/估计/目标”的证据分层。镜头表是组织工具，不是模型参数，不要求使用其商业软件。

## 媒体时间与帧数据

[FFmpeg：ffprobe Documentation](https://ffmpeg.org/ffprobe.html)

使用其流、格式、帧和时间戳检查能力作为元数据依据。帧率、时长与帧数须实际读取；可变帧率不能只靠帧号除以标称帧率。工具能给元数据，不能替代镜头含义的视觉审阅。

## 自动切点的局限

[PySceneDetect：Detectors](https://www.scenedetect.com/docs/latest/api/detectors.html)

ContentDetector依据帧间颜色/亮度变化给出切点；AdaptiveDetector使用相邻变化的滚动比较，可缓解快速相机运动中的误检。采用其“候选检测”用途，切点仍需复核。默认阈值不是本 Skill 对所有影片的统一推荐值。

## 项目协作经验

来源为本项目创建前的创作协作：参考片分析、角色替换、成片节奏对比、光学关系修订和局部剪辑。只提炼一般方法，不公开附件、身份信息和本机路径。

- 区分源片事实、作者推测和新版创作目标。
- 明确敌人参与数与脉冲数量可能比抽象密度词更有用；已有用户正向反馈，未做受控验证。
- 原片中极短爆发不能机械套用写实动作耗时。
- 披风、眼睛等新造型必须替换旧约束。
- 镜面反射、背景折射、巨大尺度需要明确相机与几何关系。
- 本地视频处理保留原件，分析和剪辑的完成状态分别核验。

这些经验是可修订的工作假设与约定，不是任何平台的官方结论。报告发布时以实际完成的检查为准，文档检查不等于生成效果验证。
