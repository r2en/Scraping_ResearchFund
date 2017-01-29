###Scraping_Research_Fund

stage.1

1. URLから研究費の最新版を取得
2. twitterでつぶやく

![screen shot 2017-01-30 at 02 42 51](https://cloud.githubusercontent.com/assets/17031124/22406405/082b495a-e696-11e6-88ce-ae01bf60e511.png)

     -------------↑clear--------------

stage.2

1. URLから研究費の最新版を取得
2. 最新の研究費情報のURLを取得
3. twitterでつぶやく

stage.3

1. URLから研究費の最新版を取得
2. 最新の研究費情報のURLを取得
3. そこから全文情報を引き出す
4. 最新版をtwitterでつぶやく

stage.4

1. Cron で定期更新
2. 情報が更新された時のみ動く
3. URLから研究費の最新版を取得
4. 最新の研究費情報のURLを取得
5. そこから全文情報を引き出す
6. 最新版をSlackに流す