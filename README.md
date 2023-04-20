# CV処理プログラム
rawデータを処理し、igoreで読み込み可能な`.itx`形式にファイルを変換

## 必要なライブラリ
- numpy
- pathlib
もしこれらのライブラリが入っていなかったら、以下のコマンドでダウンロードをお願いします.

```python
python -m pip install numpy
python -m pip install pathlib
```

## 使い方
- Data階層\
[data](data)内に含まれる階層ディレクトリに測定データを保存してください.\
(それ以外のディレクトリの構造ではエラーが起こります.)

```
.
└── Data
    ├── Cycle1
    │   └── CSVファイル
    ├── Cycle2
    │   └── CSVファイル
    ├── Cycle3
    │   └── CSVファイル
    └── Cyclen
        └── CSVファイル
```

- 引数設定
[main.py](main.py)では設定すべき引数は4つある.
```
mass_mc(float):合剤の質量
mass_sm(float):サンプルの質量
mass_ele(float):電極の質量
mass_gr(float):グラファイトの質量
```
これらの引数をコマンドで指定する. 4つの引数を上からarg1,arg2,arg3,arg4とした時、以下のコマンドで実行する.
```python
#arg1の値と書いてあるところには実際の値を入れてください.
python -m main.py -arg1 arg1の値 -arg2 arg2の値 -arg3 arg3の値 -arg4 arg4の値
```
コマンド実行後、data階層に`.txt`と`.itx`形式のファイルが追加されている.