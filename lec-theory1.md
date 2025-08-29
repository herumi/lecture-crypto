---
marp: true
html: true
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
# 暗号理論の定式化
<br>
光成滋生
<br>
