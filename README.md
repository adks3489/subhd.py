# subhd.py

subhd.com 字幕下載器。

這個工具除了能幫你自動從 [subhd.com](http://subhd.com/) 下載字幕以外，它還能夠：

- 自動解壓縮並找出最可能的檔案
- 將編碼轉換成 UTF-8 without DOM
- 自動轉換為 Unix style 的行尾字元
- 自動繁體 / 簡體轉換

## 修改聲明

這原來是 [Frank Tang](https://github.com/pa4373) 的專案，由於我在使用該專案的時候遇到了一些 bug，所以我 fork 了一份自己進行了一些修改。

## 安裝

由於原專案已佔用 `pip` 的同名位置，本專案修正只能手動使用 `setup.py` 安裝：

``` shell
$ git clone https://github.com/henry40408/subhd.py
$ cd subhd.py
$ python setup.py install
```

為了要能解壓縮 rar 格式的檔案，必須先安裝 `unrar`。

如果你是使用 [Homebrew](http://brew.sh/) 管理 Mac OS X 上的套件，可以透過以下指令安裝 `unrar`：

``` shell
$ brew install unrar
```

## 使用方法

``` shell
$ subhd.py -h
usage: subhd.py [-h] [-r] [-a] [-t TYPE] [-o OUTPUT] keyword [keyword ...]

Download subtitle from subhd.com, with support for Traditional Chinese /
 Simplified Chinese, encoding conversion

positional arguments:
  keyword               Specify source filename or keyword string

optional arguments:
  -h, --help            show this help message and exit
  -r, --raw             Treat keyword as raw string instead of filename
  -a, --auto            Download subtitle without prompting (best guess)
  -t TYPE, --type TYPE  Type of operation, either 'zhs' or 'zht'
  -o OUTPUT, --output   OUTPUT  Specify destination filename, default's prefix
                        is the same as filename

Copyright (C) 2015 Wei-Shao Tang (Frank Tang)

Web: https://github.com/pa4373/subhd.py

This is free software; see the source for copying conditions.
There is no warranty, not even for merchantability or fitness
for a particular purpose.
```

舉例來說，你能夠直接使用檔名搜索字幕：

``` shell
$ subhd.py Blade.Runner.1982.The.Final.Cut.BluRay.720p.DTS.2Audio.x264-CHD.mkv
1) Blade Runner (final Cut)(1982) | 銀翼殺手 (None)
2) Blade.Runner.1982.Final.Cut.BDRip.X264.iNT-TLF | 银翼杀手 导演最终剪辑版 (None)
3) Blade Runner | 银翼杀手 | 公元2020/叛狱追杀令 (None)
4) Blade Runner | 銀翼殺手 | 2020 (None)
5) Blade Runner | 银翼杀手 | （好沉闷，看不懂！） (None)
6) Dangerous Days: Making Blade Runner | 危险的日子：制作《银翼杀手》 (None)
7) Blade Runner | 銀翼殺手 | 2020 (None)
8) Blade Runner | 2020 | 银翼杀手 (None)
9) Blade Runner | 银翼杀手 (None)
10) Blade Runner | 银翼杀手 (None)
11) Blade Runner | 银翼杀手 (None)
12) Blade Runner | 银翼杀手 (None)
13) Blade Runner | 银翼杀手 (None)
14) Blade Runner | 銀翼殺手(國際院線版) (None)
15) 银翼杀手 | Blade Runner | 导演剪辑版 修复版 | 銀翼殺手 (None)
16) 银翼杀手 | Blade Runner (None)
17) 银翼杀手 | Blade Runner (None)
18) Blade.Runner | Blade.Runner.1982.Final.Cut.DVDRip.XviD-EPiC | 银翼杀手 (None)
19) [银翼杀手].Blade.Runner.1982.HD-DVDRip.x264.a720.AC3-C@SiLU | Blade Runner | 银翼杀手 (None)
20) 银翼杀手 | Blade Runner (None)
Select one subtitle to download: 2
```

此時，你的字幕以備自動轉換為 UTF-8 編碼，並且翻譯成繁體中文。若字幕為 srt 格式，也會重新整理字幕索引，這樣對於類似 Plex 的服務器應用非常方便。

若要讓程式自動選擇字幕下載，打開 `-a` 的旗標：

``` shell
$ subhd.py -a Blade.Runner.1982.The.Final.Cut.BluRay.720p.DTS.2Audio.x264-CHD.mkv
```

字幕也可以翻譯成簡體中文：

``` shell
$ subhd.py -t zhs Blade.Runner.1982.The.Final.Cut.BluRay.720p.DTS.2Audio.x264-CHD.mkv
```

亦可使用字串直接查詢：

``` 
$ subhd.py -r Blade\ Runner
```

## 貢獻

1. 複製這個版本庫。
2. 建立你自己的功能分支 `git checkout -b my-new-feature`。
3. 在你的分支上提交改變 `git commit -am 'Add some feature'`。
4. 推回你的遠端版本庫 `git push origin my-new-feature`。
5. 在這個專案發布 pull request。

## 授權

本程式以 GNU GPL v3 方式授權。

專案內未包含授權文件，請至 [https://www.gnu.org/licenses/gpl.txt](https://www.gnu.org/licenses/gpl.txt) 下載。