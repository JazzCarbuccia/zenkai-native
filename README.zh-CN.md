# Zenkai Native

《龙珠斗士 Z》（Dragon Ball FighterZ）的 Apple Silicon 原生移植。English: [README](README.md).

Zenkai Native 让 DBFZ 的游戏代码在 Apple silicon 上原生运行——它不是模拟器，画面由 Metal 绘制。
本仓库**只有源码**：它用你自己导出的游戏文件和你自己主机里的密钥来构建游戏。仓库不包含、不下载
任何游戏数据、ROM、密钥或存档。

## 当前状态

- **Phase 0 已通过**：移植版可以从用户自己的文件构建并在 Apple silicon 上运行。
- **Mod 支持是实验性的**，不保证可用。
- 本仓库只支持《龙珠斗士 Z》一款游戏。

## 你需要准备

- **一台 Apple silicon Mac。** 构建需要 Xcode 及 macOS SDK（见 [BUILDING.zh-CN.md](BUILDING.zh-CN.md)）。
- **你自己的 DBFZ 游戏文件**（NSP）和**你自己主机导出的 `prod.keys`**。仓库不包含、不下载、不代查任何东西。

## 唯一的构建路径

本仓库只支持一种构建方式——直接用下面的脚本：

```bash
python3 scripts/build_ipa_from_nsp.py <你的 DBFZ NSP 目录> \
  -k <你的 prod.keys 路径> --platform mac-app
```

`--platform mac-app` 产出一个自包含、可双击运行的 DBFZ Mac App。依赖与选项见
[BUILDING.zh-CN.md](BUILDING.zh-CN.md)。本仓库没有启动器 App、没有发布包，也没有其他构建目标。

## 仓库结构

- `dm/` —— 原生引擎、宿主层与渲染器（vendored 快照）。
- `scripts/` —— 上面命令使用的 NSP 到 App 构建流水线。
- `docs/reference/` —— 引擎参考文档；`docs/development.md` —— 开发说明。
- `BASELINE_SOURCE.md` —— 代码来源。

## 来源与致谢

Zenkai Native 衍生自 **[LNPANDY/NX2Apple](https://github.com/LNPANDY/NX2Apple)**（MIT）和
**[seedds/nxnative](https://github.com/seedds/nxnative)**（MIT）。代码改写工具链、Horizon 宿主层和
NVN-on-Metal 来自这两个项目；本仓库把它们聚焦于《龙珠斗士 Z》。继承的历史见
[CHANGELOG.zh-CN.md](CHANGELOG.zh-CN.md) 和 [BASELINE_SOURCE.md](BASELINE_SOURCE.md)；许可证和版权
声明见 [LICENSE](LICENSE) 与 [NOTICE](NOTICE)。

## 参与贡献

报告问题和提交改动见 [CONTRIBUTING.zh-CN.md](CONTRIBUTING.zh-CN.md)。

## 法律声明

本作品与任天堂无关联、不受其赞助或认可。"Nintendo Switch" 与 "Dragon Ball FighterZ" 是各自
所有者的商标。你需自行遵守所在地关于个人备份的法律，且绝不分发游戏文件或密钥。软件按
[LICENSE](LICENSE) 中的许可证"按原样"提供，不作任何明示或暗示的保证。
