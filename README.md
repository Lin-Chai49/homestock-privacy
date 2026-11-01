# 悦家库存 HomeStock — 隐私政策

本仓库发布 **悦家库存（HomeStock）** 的隐私政策页，给 Google Play 的政策网址用。

线上页面：<https://lin-chai49.github.io/homestock-privacy/>

页面是根目录的 `index.html`。中文在前，同一网址下有完整英文。它描述的是应用 **1.0.0**（`versionCode` 2，包名 `com.chailin.homestock`）的实际行为。记录在本机数据库 `HomeStockDB`。临期提醒等开关只保存在本机，这一版不发送系统通知。

```bash
python3 check.py
```

`check.py` 锁住包名、数据库名、导出文件名前缀、七个提醒开关，以及“不发送系统通知”“清空后保留类别、位置和设置”。旧文里的 AES-256、启动确认和“设置 → 关于”的政策日志不能再出现。GitHub Actions 工作流 `check` 在每次推送和拉取请求上跑同一条命令。

## English

The page matches HomeStock 1.0.0, package `com.chailin.homestock`. Records stay in on-device `HomeStockDB`. The manifest declares `android.permission.INTERNET` so the WebView can open the bundled page. The app source does not make a network request. The seven reminder switches are stored and the app does not post a system notification. It does not declare `POST_NOTIFICATIONS`. The add-item screen can show “将于过期前 N 天自动通知”; no job sends that notice. Auto-buy runs only when the shopping screen’s 同步自动补货 button is pressed.

Export writes `homestock-backup-YYYY-MM-DD-HHmm.json`, including the nickname and the optional address, and does not upload it. The file is not encrypted. Import replaces all six stores. Demo data is appended. Clear all deletes items, consumptions, and the shopping list, and keeps categories, locations, and settings.

`android:allowBackup` is false. Cloud backup and device transfer exclude the app data. The entry form does not open the camera or the photo library. `barcode` and `imageUrl` stay empty.

There is no email address on the page. Developer: 柴琳.
