#!/bin/bash
#findコマンドで、このシェルスクリプトがあるディレクトリのファイルを検索して、最後が.outで終わるファイル全てに対してforループで処理をする、という意味
for file in `\find . -maxdepth 1 -type f -name '*.csv'`; do
    python3 ../.././CDc_csv2itx.py ${file}
done
