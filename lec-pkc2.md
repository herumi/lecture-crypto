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
# 公開鍵暗号2<br>
TLS1.3, ビットコイン
<br>
光成滋生
<br>

# 目次
## 用語一覧

# TLS1.3 (Transport Layer Security)
## 通信を安全に暗号化するプロトコル
- 暗号化されていないHTTP（に限らない）を安全に通信できるようにする
- [RFC 8446](https://datatracker.ietf.org/doc/html/rfc8446), [RFC 8446bis](https://datatracker.ietf.org/doc/draft-ietf-tls-rfc8446bis/): 2025年9月現在draftが更新中
## 特徴
- 盗聴・改竄を防ぐ
- TLS1.2までに比べてハンドシェイクの効率化
- 暗号化アルゴリズムの整備
- 新しい鍵導出アルゴリズム
- 形式検証
- AEAD
- 前方秘匿性など

# TLS1.3のハンドシェイク
<!-- _class: image-right -->
![w:600px](images/lec-tls1.3.drawio.svg)
## 暗号化通信が始まるまでの流れ
- クライアントからサーバへ接続開始 ClientHello
  - KS :ECDH鍵共有情報, PSK: 事前鍵共有情報
- サーバからクライアントへ応答
  - ServerHello: ECDH完了
  - ECDH鍵共有完了でAEADによる暗号化通信開始
  - Certificate: サーバ証明書送信
  - CertificateVerify: 検証鍵でこれまでの通信に署名
  - Finished: 完了, 本来のデータを送信開始
- クライアント
  - Finished: 証明書と署名を検証し通信開始
- 重要: 公開鍵による暗号化は*行わない*
# 鍵導出アルゴリズム
## HKDF (HMAC-based Key Derivation Function)
- HMACを利用した鍵導出関数
- 短いシードから秘密鍵に利用できる安全な擬似乱数を生成
- HKDF-Extract
  - salt : 秘密ではないランダムな値, x : DH鍵共有などの結果
  - $prk = HMAC(salt, x)$
- HKDF-Expand
  - $prk$ と付加情報 info から複数の安全な擬似乱数を生成
    - $T_1=HMAC(prk, \texttt{""|info|1})$
    - $T_2=HMAC(prk, T_1\texttt{|info|1})$
    - $T_3=HMAC(prk, T_2\texttt{|info|1})$
- Derive-Secret
  - infoにヘッダ情報を付与してHKDF-Expandを呼び出す

# 鍵導出手順
## 詳細はRFC8446参照
![w:700px](images/lec-tls-kdf.png)