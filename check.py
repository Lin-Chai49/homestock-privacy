#!/usr/bin/env python3
"""Lock the published HomeStock policy to the facts in index.html."""

import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent
PAGE = ROOT / "index.html"

REQUIRED = (
    "com.chailin.homestock",
    "HomeStockDB",
    "homestock-backup-",
    "android.permission.INTERNET",
    "allowBackup",
    "usesCleartextTraffic",
    "1.0.0",
    "versionCode 2",
    "临期提醒",
    "已过期提醒",
    "库存不足提醒",
    "购物清单更新",
    "每周报告",
    "月度总结",
    "免打扰时段",
    "不发送系统通知",
    "does not post a system notification",
    "不声明 <code>POST_NOTIFICATIONS</code>",
    "does not declare <code>POST_NOTIFICATIONS</code>",
    "清空全部数据",
    "保留类别、位置和设置",
    "keeps categories, locations, and settings",
    "家庭住址",
    "昵称",
    "盒马生鲜",
    "barcode",
    "imageUrl",
    "不打开相机",
    "does not open the camera",
    "不打开相册",
    "schema",
    "exportedAt",
    "dataExtractionRules",
    "com.chailin.homestock.fileprovider",
    "冰箱·冷藏",
    "同步自动补货",
    "家庭主妇/主夫",
    "将于过期前",
)

BANNED = (
    "AES-256",
    "v1.1",
    "设置 → 关于",
    "应用启动后的提示",
    "samincase0@gmail.com",
    "永远不会通过网络",
    "无年龄分级限制",
    "FOREGROUND_SERVICE",
)


def main():
    if not PAGE.is_file():
        print("missing index.html")
        return 1
    text = PAGE.read_text(encoding="utf-8")
    if "</html>" not in text.lower():
        print("unclosed html")
        return 1
    for phrase in REQUIRED:
        if phrase not in text:
            print("missing", phrase)
            return 1
    for phrase in BANNED:
        if phrase in text:
            print("banned", phrase)
            return 1
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for phrase in ("HomeStockDB", "com.chailin.homestock", "临期提醒", "不发送系统通知"):
        if phrase not in readme:
            print("readme drift", phrase)
            return 1
    print("ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
