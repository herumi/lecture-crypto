---
marp: true
html: true
title: slides
paginate: true
math: mathjax
size: 16:9
style: |
  @import "themes/mytheme01.css";
---
<!--
headingDivider: 1
-->
<!--
_class: title
-->
# マイナンバーカード, BBS署名
<br>
光成滋生, 2025/10
<br>

# 概要
## 目的
- マイナンバーカードの仕組みと課題を理解する
-  SD-JWTやBBS署名などの選択開示署名の概念を理解する

# 目次
## 用語一覧
- 本人確認
- マイナンバーカード
- 選択的開示可能署名

# 本人確認ガイドライン
## 本人確認 ＝ 身元確認 ＋ 当人認証
- 身元確認 ＝ 登録する基本4情報などが正しいことを確認する
  - L3: 対面で公的身分証を元に確認
  - L2: 郵送などの非対面で公的身分証を元に確認
  - L1: 自己申告

- 当人確認 ＝ 登録された情報と、今回の情報を認証の3要素（生体・所持・知識）で照合
  - L3: 耐タンパ性ハードウェアを用いた複数の認証
  - L2: 3要素のうち複数用いる認証
  - L1: 3要素のうち1要素を用いる認証

- サービスレベルに応じてレベルは異なるが銀行などではL2+L2以上が多い
- 参考: [IPA「サービスに応じたデジタル本人確認ガイドラインの検討」](https://www.digital.go.jp/assets/contents/node/basic_page/field_ref_resources/093e09a7-2ffe-4a41-971a-5c0dcfd3c0b3/20220125_meeting_trust_dx_02.pdf)

# マイナンバーカード
## 公的個人認証サービス
- 署名用電子証明書
  - 「基本4情報（氏名・住所・生年月日・性別）＋個人の検証鍵」にCAが署名したもの
  - マイナンバーカードは証明書を耐タンパー性のハードウェアに格納
  - いろいろなシーンで使ってほしい by デジタル庁
  - 利用者証明用電子証明書には基本4情報は含まれない
## 利用時の手順
1. なんらかの文書に署名鍵で署名する（要 署名用電子証明書のパスワード）
2. 「文書 + 署名 + 署名用電子証明書」を相手に送る
3. 相手はCAの検証鍵で署名用電子証明書の正しさを確認
4. 署名用電子証明書に含まれる検証鍵で文書の正しさを確認
  ユーザの証明書が失効されていないかの検証も必要

# 署名の流れ
## 行政機関向け（左）と民間事業者向け（右）の違い
- ![width:600px](https://services.digital.go.jp/uploads/auth-and-sign-image-administration-02.png) ![width:600px](https://services.digital.go.jp/uploads/auth-and-sign-image-business-02.png)
## 電子証明書の扱い
- 署名の検証に必要な電子証明書は直接民間事業者には渡さない
- CRL（証明書失効リスト）はシリアル番号と失効日時のリスト

# 署名のシーケンス図
![bg right 78%](https://images.microcms-assets.io/assets/7c793323a46a46b7bb9a2ac7d0023301/cda6cc666aef4f22bb16394862d0fb81/%E3%82%B7%E3%83%BC%E3%82%B1%E3%83%B3%E3%82%B9%E5%9B%B3-%E7%BD%B2%E5%90%8D.png)
## 主な処理
- [10]でデータのハッシュ値に対して署名する
  - 署名用電子証明書の
  認証パス・有効期間の検証
  - 署名用電子証明書の有効性確認
  （行政機関のみ）
## 署名検証は行わない
- 署名対象データ・署名対象ハッシュ値・署名値の確認をしない
- 署名検証は自分（RPアプリ）でやる[17]
  - 実際にはPF（プラットフォーム）事業者に依頼する [JPKIサービス](https://www.digital.go.jp/policies/mynumber/private-business/jpki-introduction/)

# プライバシー
## 基本4情報は直接渡さない
- しかし代わりに絶対的な権限がデジタル認証アプリサーバーに集中する可能性
- 原理的には、いつ、だれが、どのサービスに何の情報を渡したのか把握できる
## [プライバシーポリシー](https://services.digital.go.jp/auth-and-sign/privacy-policy/)
- 保有する情報を利用目的以外には使わない・提供しない
- 「情報の全部または一部の処理を第三者に委託する」場合もある

# Apple Walletのマイナンバーカード
## カード代替電磁的記録（属性証明機能）
- マイナンバーカードに記録された基本4情報（氏名・住所・生年月日・性別）
  ＋その情報が正しいことを示す情報
  ＋送信者が本人であることを証明する情報
- 大多数のオンラインサービスでは十分な本人確認になる

## iPhoneの[Verify with Wallet API](https://developer.apple.com/wallet/get-started-with-verify-with-wallet/)
- Apple Walletに格納された個人情報を扱うAPI
- 2025年9月対応しているのはUSの一部の州と日本のみ
## 仕様
- ISO/IEC 18015-5: モバイル運転免許証の規定
- ISO/IEC 23220: モバイルデバイス上で動作するデジタル身分証の規定

# Apple Walletで確認できる項目
## 要求できる項目
- N歳（以上）であること
- ID写真
- 姓・名
- 住所
- 誕生日
- マイナンバー
- 性別
## 信頼性
- Appleとそのソフトウェアを信頼するしかない

# 選択的開示可能な署名
## 基本4情報（に限らないが）の一部のみを開示して確認できる暗号技術
- W3Cの[VC : Verifiable Credentials （検証可能な認証情報）](https://www.w3.org/TR/vc-data-model-2.0/)などで規格策定中
  - 大きく二種類の方法
    - ハッシュ関数ベースのもの (SD-JWT)
    - ペアリング暗号ベースのもの (BBS署名)
## メリットとデメリット

項目|SD-JWT|BBS署名
-|-|-
実装|容易|難しい
検証コスト|低い|大きい
*unlinkability* （後述）|弱い|強い

# SD-JWT
## 用語
- JOSE (JSON Object Signing and Encryption) : JSONを用いた署名と暗号化の規格
  - JSON + Base64URL
- JWS (JSON Web Signature) : 署名に関する規格
- JWE (JSON Web Encryption) : 暗号化に関する規格
- JWK (JSON Web Key) : 鍵に関する規格
- JWA (JSON Web Algorithms) : アルゴリズムに関する規格
- JWT (JSON Web Token) : クレーム（値）に関する規格
- [SD-JWT (Selective Disclosure for JWTs)](https://datatracker.ietf.org/doc/draft-ietf-oauth-selective-disclosure-jwt/)
  - JWTで選択的開示を実現するための規格
- CBOR (Concise Binary Object Representation) : JSONのバイナリ版
  - COSE (CBOR Object Signing and Encryption) : CBORを用いた署名と暗号化の規格

# SD-JWTのコアアイデア
## salt+ハッシュ関数を使う

クレーム|クレーム値|salt (128bit)|ハッシュ値(_sd)
-|-|-|-
姓|山田|1aef...|`H("山田", "1aef...")`
名|太郎|584a...|`H("太郎", "584a...")`
誕生日|2000/01/01|39ff...|`H("2000/01/01", "39ff...")`

- クレーム値全体を署名するのではなくハッシュ値全体に対して信頼できる機関が署名する
  - ハッシュ値だけ公開する
- 検証方法
  - 検証者はハッシュ値を含む署名を検証
  - 開示したいクレーム値に対してsaltとクレーム値を要求し, ハッシュ値が正しいことを確認
- saltが128bitあるのでsaltが非公開だとハッシュ値からクレーム値を求められない

# SD-JWTの暗号学的な欠点
## 署名は常に同じ
- いろんなサービスで同じSD-JWTを提示する
## saltの漏洩
- クレーム値のドメインが小さいとsaltが漏洩するとハッシュ値からクレーム値を計算できる
  - H(salt, クレーム値)=hash値となるクレーム値の総当たりが可能
  - 性別なら精々数パターン, 誕生日も365*100程度

# unlinkability （連結不可能性）とは
## あちこちのサービスで利用したときに追跡されないこと
- 検証のために相手に渡すデータがいつも同じだと追跡される
![w:500px](images/sd-jwt.drawio.svg)
- 3rd party cookieのようなもの
- プライバシーを保つにはunlinkabilityが重要

# BBS署名
## Boneh, Boyen, Shacham, "[Short Group Signatures](https://link.springer.com/chapter/10.1007/978-3-540-28628-8_3)", CRYPTO'04
- Revisiting BBS Signatures, EUROCRYPT'23
  - [draft-irtf-cfrg-bbs-signatures](https://datatracker.ietf.org/doc/draft-irtf-cfrg-bbs-signatures/)
## フロー
![bg right:45% width:700px](images/bbs-sequence.drawio.svg)
- CAが基本4情報等に対してBBS署名を発行
- ユーザは開示情報を決めて「証明prf」を生成
- 検証者は開示情報とprfをCAの検証鍵で検証
## SD-JWTに対する利点
- 同じ開示情報に対するprfでも毎回異なるのでunlinkabilityが高い

# BBS署名オリジナルのコアアイデア
## グループ署名
- メンバーが自身の身元を明かさずに署名する傘連判状みたいなの
- アルゴリズム
  - 発行者は $γ$ を生成しグループの鍵生成をした後 $γ$ を破棄する
  - グループの公開鍵 $gpk$ ($w=g_2^γ$を含む), 追跡用秘密鍵: $gmsk$
  - 各ユーザの秘密鍵 $gsk_i$ $(x_i,\frac{1}{γ+x_i}g_1)$
  - 署名: sign($gpk$, $gsk_i$, メッセージ $m$) から署名 $σ$ を作る
  - 検証: verify($gpk$, $m$, $σ$) で正しいか確認
  - 公開: open($gpk$, $gmsk$, $m$, $σ$) でメンバーの身元を明かす
## 応用
- 複数メッセージに対応し($\sum_i m_i h_i$)、その一部の秘匿をゼロ知識証明ZKPを使って実現

# BBS署名の実装デモ
## ブラウザで動作するデモ
- [github/herumi/bbs](https://github.com/herumi/misc/tree/main/bbs)
- C++/LLVMで実装したものをWasm用にコンパイルしてNode.jsモジュール化
  - TypeScriptで利用してブラウザで動かす
- 細かいデータフォーマットなどは仕様に従ってないプロトタイプ実装