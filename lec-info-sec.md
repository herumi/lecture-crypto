---
marp: true
title: slides
theme: default
paginate: true
size: 16:9
style: |
  section {
    justify-content: flex-start;
    margin: 0px;
    background-color: white;
    padding: 0px;
    background: linear-gradient(180deg,#E7FFE7 10%, #008080 10%,#008080 10.5%, white 10.5%, white 100%);
    display: flex;
    font-family: Noto Sans JP;
  }
  code {
    font-family: 'BIZ UDGothic', monospace;
  }
  pre {
    font-family: inherit;
  }
  pre code {
    font-family: 'BIZ UDGothic', monospace;
  }
  section h1 {
    margin: 0px;
    padding-left: 10px;
    padding-top: 5px;
    padding-bottom: 3px;
    background-size: 15%;
    background-repeat: no-repeat;
    background-position: right 5px top 5px;
  }
  section.title {
    font-size: 200%;
    padding: 40px;
    background: linear-gradient(180deg,#E7FFE7 49%, #008080 49%,#008080 50%, white 50%, white 100%);
    text-align: center;
    justify-content: center;
  }
  section h2 {
    padding-left: 10px;
    padding-top: 0px;
    padding-bottom: 0px;
  }
  section h3 {
    padding-left: 30px;
    padding-top: 0px;
    padding-bottom: 0px;
  }
  section ul {
    margin: 0px;
  }
  section::after {
   font-size: 70%;
   content: attr(data-marpit-pagination) " / " attr(data-marpit-pagination-total);
  }
  table {
    margin-left: auto;
    margin-right: auto;
    table-layout: fixed;
    width: auto;
    display:table;
  }
  thead th {text-align: center !important;}
  thead tr {background: #eaeaea;}
  tbody tr:nth-child(2n+1) {text-align: center !important;background: #fff;}
  tbody tr:nth-child(2n) {text-align: center !important;background: #eeeeee;}
  section .emp { color: red; }
  section pre {
    margin: 0px;
  }
  em {
    color: red;
    font-style: normal;
  }
  img {
    display: inline;
    vertical-align: top;
  }
---
<!--
headingDivider: 1
-->
<!--
_class: title
-->
# 情報セキュリティ
<br>
光成滋生
<br>
2025/08/22

# 情報セキュリティとは
## ネットショッピングにおける望ましい状態
![bg right:33% width:300px](images/lec-info-sec.drawio.svg)
- 自分がどんな商品を買ったか他人に知られない
- 商品の値段や送付先が勝手に書き換えられない
- いつでも買い物ができる
## 情報セキュリティの三要素
- 機密性 (confidentiality)
  - 許可されてない人が情報にアクセスできないこと
- 完全性 (integrity)
  - 情報が改竄されたり消えたりせずに正確に存在すること
- 可用性 (availability)
  - 許可された人が必要なときに情報にアクセスできること

# 情報セキュリティと暗号技術
## JIS Q 27000
- 日本の産業の標準化のために定められた国家規格
- 日本産業標準調査会JISCが調査審議を行う
## 暗号技術との関係
- 情報セキュリティを守るには様々な技術が必要
  - そのうちの暗号・認証・署名・改竄検知・否認防止などの技術を総称して暗号技術という

**情報セキュリティの三要素と関連する暗号技術**
要件|求められる特性|暗号技術|
-|-|-|
機密性|データの秘匿|暗号化・認証|
完全性|データの正確さ|メッセージ認証符号・署名|
可用性|データへのアクセスしやすさ|秘密分散|

# 追加された要件
## 真正性 (authenticity)
- ユーザや、システムなどが本当にその人やものであり、偽物が紛れていないこと
  - 本当に当事者であることを確認する
## 責任追及性 (accountability)
- システムに対して誰が、いつ、何をしたのかを正確に記録して問題が起きたときに原因を追求できること
## 否認防止 (non-repudiation)
- なんらかの操作を後でなかったことにされないようにすること
## 信頼性 (reliability)
- システムが不具合無く正確に動作していること
