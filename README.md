# 悦家库存 HomeStock — 隐私政策

本仓库发布 **悦家库存（HomeStock）** 的隐私政策页，给 Google Play 的政策网址用。

线上页面：<https://lin-chai49.github.io/homestock-privacy/>

页面是根目录的 `index.html`。中文在前，同一网址下有完整英文。它描述的是应用 **1.0.0**（`versionCode` 2，包名 `com.chailin.homestock`）的实际行为，不是路线图。

```bash
python3 check.py
```

`check.py` 锁住包名、数据库名、导出文件名前缀、七个提醒开关，以及“不发送系统通知”“清空后保留类别、位置和设置”。旧文里的 AES-256、启动确认和“设置 → 关于”的政策日志不能再出现。GitHub Actions 工作流 `check` 在每次推送和拉取请求上跑同一条命令。

## 这页在说什么

开发者收不到用户输入的内容。应用没有账号。数据在本机 IndexedDB `HomeStockDB`（版本 1）的六个存储里：`items`、`categories`、`locations`、`consumptions`、`shoppingList`、`settings`。

引导页要求 2–20 个字符的昵称。设置里还可以保存家庭角色、家庭人数，以及最长 50 字的家庭住址。住址是手输文字，不是 GPS。应用不声明定位权限。

入库字段是名称、类别、品牌、规格、数量、单位、最低库存、购买日、到期日、金额、备注和存放位置。金额只进本机图表。记录里有空的 `barcode` 和 `imageUrl`。这一版的表单不填它们。应用不打开相机，不打开相册，也不扫码。

预置 8 个类别和 12 个存放位置。这一版的屏幕不能新增或删除它们。导入可以整表替换。药品类别只是库存分类，应用不做诊断。

购物清单上的建议去处是写死的标签：食品对应盒马生鲜，日用品对应京东超市，药品对应京东大药房，茶饮对应永辉超市。应用不访问这些商店。

七个开关——临期提醒、已过期提醒、库存不足提醒、购物清单更新、每周报告、月度总结、免打扰时段——保存在 `settings.notifications`。版本 1.0.0 不发送系统通知，不声明 `POST_NOTIFICATIONS`，首页和任何定时任务都不读这些开关。`quietHours` 写成 22:00–07:00，设置页不能改，也没有任务去用它。

设置 → 数据管理：

| 操作 | 行为 |
|---|---|
| 导出数据（JSON） | 内存里拼出 `schema=HomeStockDB` 的整库，含昵称和住址，下载为 `homestock-backup-YYYY-MM-DD-HHmm.json`。不上传。文件不加密。 |
| 导入备份 | schema 必须是 HomeStockDB。通过后清空六个存储再写入，类别、位置和设置一并被覆盖。 |
| 加载演示数据 | 在现有物品后面追加示例物品、消耗和几条购物清单，不先删除。 |
| 清空全部数据 | 两次确认后删除物品、消耗和购物清单。保留类别、位置和设置，昵称和住址还在。 |

清单只声明 `android.permission.INTERNET`，给 WebView 加载随包页面。`usesCleartextTraffic` 为 false。应用代码没有 `fetch`、XHR、WebSocket 或上报。`allowBackup` 和 `fullBackupContent` 为 false。`dataExtractionRules` 把 root、database、file、sharedpref、external 排除出云备份和换机传输。

工程里有一个不导出的 FileProvider，authority 是 `com.chailin.homestock.fileprovider`。这一版的屏幕不用它把文件交给别的应用。

卸载会清掉 WebView 里的 HomeStockDB，不会删掉已经保存到别处的 JSON。

随包库是 Vue 3、Vue Router、Pinia、idb、ECharts、dayjs、Capacitor 6。没有广告、统计、推送、崩溃收集或分享 SDK。

版本 1.0.0 没有加密备份，没有启动时的隐私弹窗，关于页也没有政策日志。本页和关于页都没有电子邮箱。上架后用 Play 商品页的反馈。著作权人是柴琳。

minSdk 24，targetSdk 35。

## English

The page matches HomeStock 1.0.0, package `com.chailin.homestock`. Records stay in on-device `HomeStockDB`. The manifest declares `android.permission.INTERNET` so the WebView can open the bundled page. The app source does not make a network request. The seven reminder switches are stored and the app does not post a system notification. It does not declare `POST_NOTIFICATIONS`.

Export writes `homestock-backup-YYYY-MM-DD-HHmm.json`, including the nickname and the optional address, and does not upload it. The file is not encrypted. Import replaces all six stores. Demo data is appended. Clear all deletes items, consumptions, and the shopping list, and keeps categories, locations, and settings.

`android:allowBackup` is false. Cloud backup and device transfer exclude the app data. The entry form does not open the camera or the photo library. `barcode` and `imageUrl` stay empty.

There is no email address on the page. Developer: 柴琳.
