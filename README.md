<h1>画像を文字にしてくれるましーーん</h1>
<p>※中2の頃にpythoの画像処理の練習として作ったものです。どうぞ温かい目で見てください。</p>
<p>画像のパスと作りたいテキストファイルの横幅の文字数を入力したら.txtファイルとして出力されるよ！</p>
<h2>～処理の流れ～</h2>
<ul>
  <li>1.全てのASCII半角文字を白地に出力して、そのマスが占める黒色の割合を求めてrecord.txtに記録する。</li>
  <li>2.画像を入力された横幅の比率にリサイズ。</li>
  <li>3.画像が入力されたらグレースケールにして、明るさ(黒さ)が最も近い文字を求める。</li>
  <li>4.それを1ピクセルごとに繰り返したら出来上がり。</li>
</ul>
<p>main_AA.pyを実行してね～</p>
